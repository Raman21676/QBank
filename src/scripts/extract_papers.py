#!/usr/bin/env python3
"""Extract individual papers from compiled semester PDFs."""

import sys
import re
import os
from pypdf import PdfReader, PdfWriter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def extract_papers(pdf_path, output_dir, faculty_slug="bca"):
    """Extract individual papers from a compiled PDF."""
    reader = PdfReader(pdf_path)
    pages = list(reader.pages)
    
    # Identify header pages
    headers = []
    for i, page in enumerate(pages):
        text = page.extract_text() or ""
        year_match = re.search(r'20(18|19|20|21|22|23|24)', text)
        code_match = re.search(r'CACS\s*(\d+)', text)
        title_match = re.search(r'Course Title:\s*([^\n]+)', text)
        
        if year_match and (code_match or title_match):
            year = year_match.group(0)
            code = f"CACS{code_match.group(1)}" if code_match else "UNKNOWN"
            title = title_match.group(1).strip() if title_match else "Unknown"
            headers.append({
                'page_idx': i,
                'year': year,
                'code': code,
                'title': title,
                'text_len': len(text.strip())
            })
    
    print(f"Found {len(headers)} header pages")
    for h in headers:
        print(f"  Page {h['page_idx']+1}: {h['code']} {h['title']} ({h['year']})")
    
    # Group pages into papers
    papers = {}
    for i, header in enumerate(headers):
        start = header['page_idx']
        end = headers[i+1]['page_idx'] if i+1 < len(headers) else len(pages)
        
        key = (header['year'], header['code'])
        if key not in papers:
            papers[key] = {
                'year': header['year'],
                'code': header['code'],
                'title': header['title'],
                'pages': list(range(start, end))
            }
        else:
            # Duplicate - keep the first one with more text
            existing_len = sum(len(pages[j].extract_text() or "") for j in papers[key]['pages'])
            new_len = sum(len(pages[j].extract_text() or "") for j in range(start, end))
            if new_len > existing_len:
                papers[key]['pages'] = list(range(start, end))
                papers[key]['title'] = header['title']
    
    # Save individual PDFs
    os.makedirs(output_dir, exist_ok=True)
    saved = []
    
    for key, paper in papers.items():
        writer = PdfWriter()
        for pidx in paper['pages']:
            writer.add_page(pages[pidx])
        
        filename = f"{paper['code']}-{paper['year']}.pdf"
        filepath = os.path.join(output_dir, filename)
        
        with open(filepath, 'wb') as f:
            writer.write(f)
        
        saved.append({
            'code': paper['code'],
            'year': paper['year'],
            'title': paper['title'],
            'pages': len(paper['pages']),
            'path': filepath
        })
        print(f"Saved: {filename} ({len(paper['pages'])} pages)")
    
    return saved

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_papers.py <input_pdf> <output_dir>")
        sys.exit(1)
    
    extract_papers(sys.argv[1], sys.argv[2])
