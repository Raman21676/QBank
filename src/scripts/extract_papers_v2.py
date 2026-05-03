#!/usr/bin/env python3
"""Extract individual papers from compiled semester PDFs - v2 with better handling of mixed pages."""

import sys
import re
import os
from pypdf import PdfReader, PdfWriter

def extract_papers_v2(pdf_path, output_dir, subject_map):
    """
    Extract papers using a more robust method.
    subject_map: dict of {code: {year: (start_page_hint, expected_pages)}} or just process all found
    """
    reader = PdfReader(pdf_path)
    pages = list(reader.pages)
    
    # Analyze each page: what year and subject does it belong to?
    page_info = []
    for i, page in enumerate(pages):
        text = page.extract_text() or ""
        
        # Find year
        year_match = re.search(r'20(18|19|20|21|22|23|24)', text)
        year = year_match.group(0) if year_match else None
        
        # Find subject code
        code_match = re.search(r'Code\s*No:\s*CACS\s*(\d+)', text, re.IGNORECASE)
        if not code_match:
            code_match = re.search(r'CACS\s*(\d+)', text)
        code = f"CACS{code_match.group(1)}" if code_match else None
        
        # Find title
        title_match = re.search(r'Course Title:\s*([^\n]+)', text)
        title = title_match.group(1).strip() if title_match else None
        
        text_len = len(text.strip())
        is_header = bool(year and (code or title))
        
        page_info.append({
            'idx': i,
            'year': year,
            'code': code,
            'title': title,
            'text_len': text_len,
            'is_header': is_header,
            'text': text[:200]
        })
    
    # Print analysis
    print("=== Page Analysis ===")
    for p in page_info:
        header_mark = "[HDR]" if p['is_header'] else "     "
        print(f"Page {p['idx']+1}: {header_mark} Year={p['year']} Code={p['code']} Title={p['title'][:30] if p['title'] else '?'} len={p['text_len']}")
    
    # Group pages by subject/year using a sliding window approach
    # For each header page, take it and subsequent pages until we hit another header
    # of the SAME subject but different year, or a header of a DIFFERENT subject
    papers = {}
    
    # First pass: identify all header pages and their subjects
    headers = [p for p in page_info if p['is_header']]
    
    for i, hdr in enumerate(headers):
        start = hdr['idx']
        code = hdr['code']
        year = hdr['year']
        title = hdr['title']
        
        if not code or not year:
            continue
        
        key = (year, code)
        
        # Determine end: look for next header that is either:
        # 1. Different subject, OR
        # 2. Same subject but different year
        end = len(pages)
        for next_hdr in headers[i+1:]:
            next_code = next_hdr['code']
            next_year = next_hdr['year']
            if next_code and next_year:
                if next_code != code or (next_code == code and next_year != year):
                    end = next_hdr['idx']
                    break
        
        page_range = list(range(start, end))
        
        # Only keep if this is the first/best occurrence
        if key not in papers:
            papers[key] = {
                'year': year,
                'code': code,
                'title': title,
                'pages': page_range
            }
        else:
            # Compare text length
            existing_len = sum(page_info[j]['text_len'] for j in papers[key]['pages'])
            new_len = sum(page_info[j]['text_len'] for j in page_range)
            if new_len > existing_len:
                papers[key]['pages'] = page_range
                papers[key]['title'] = title
    
    # Save
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
        
        total_len = sum(page_info[j]['text_len'] for j in paper['pages'])
        saved.append(paper)
        print(f"Saved: {filename} ({len(paper['pages'])} pages, text_len={total_len})")
    
    return saved

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract_papers_v2.py <input_pdf> <output_dir>")
        sys.exit(1)
    
    extract_papers_v2(sys.argv[1], sys.argv[2], {})
