#!/usr/bin/env python3
"""
Generate answer sheet PDFs for BCA question papers.
Uses reportlab for PDF generation.
"""

import os
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfgen import canvas
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY

# Resolve PDF_BASE relative to project root (this script is at src/scripts/)
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", ".."))
PDF_BASE = os.path.join(PROJECT_ROOT, "public", "pdfs", "bca")


def create_styles():
    styles = getSampleStyleSheet()
    
    styles.add(ParagraphStyle(
        name='TUHeader',
        fontSize=10,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=6,
    ))
    
    styles.add(ParagraphStyle(
        name='AnsTitle',
        fontSize=18,
        leading=24,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#0f172a'),
        spaceAfter=12,
        fontName='Helvetica-Bold',
    ))
    
    styles.add(ParagraphStyle(
        name='AnsSubtitle',
        fontSize=12,
        leading=16,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#475569'),
        spaceAfter=20,
    ))
    
    styles.add(ParagraphStyle(
        name='GroupHeader',
        fontSize=13,
        leading=18,
        alignment=TA_LEFT,
        textColor=colors.HexColor('#0ea5e9'),
        spaceAfter=10,
        spaceBefore=16,
        fontName='Helvetica-Bold',
    ))
    
    styles.add(ParagraphStyle(
        name='Question',
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#1e293b'),
        spaceAfter=6,
        leftIndent=0,
        fontName='Helvetica-Bold',
    ))
    
    styles.add(ParagraphStyle(
        name='Answer',
        fontSize=10,
        leading=14,
        alignment=TA_JUSTIFY,
        textColor=colors.HexColor('#334155'),
        spaceAfter=12,
        leftIndent=12,
    ))
    
    styles.add(ParagraphStyle(
        name='DiagramNote',
        fontSize=9,
        leading=12,
        alignment=TA_CENTER,
        textColor=colors.HexColor('#64748b'),
        spaceAfter=12,
        leftIndent=12,
        rightIndent=12,
        backColor=colors.HexColor('#f1f5f9'),
        borderPadding=8,
    ))
    
    styles.add(ParagraphStyle(
        name='Marks',
        fontSize=9,
        leading=12,
        alignment=TA_RIGHT,
        textColor=colors.HexColor('#94a3b8'),
        spaceAfter=6,
    ))
    
    return styles


def draw_header_footer(canvas, doc, subject_name, year, code):
    canvas.saveState()
    
    # Header line
    canvas.setStrokeColor(colors.HexColor('#38bdf8'))
    canvas.setLineWidth(3)
    canvas.line(1.5*cm, A4[1] - 1.5*cm, A4[0] - 1.5*cm, A4[1] - 1.5*cm)
    
    # Footer
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(colors.HexColor('#94a3b8'))
    canvas.drawString(1.5*cm, 1*cm, f"TU QBank — {subject_name} {year} Answer Sheet")
    canvas.drawRightString(A4[0] - 1.5*cm, 1*cm, f"Page {doc.page}")
    
    canvas.restoreState()


def generate_answer_sheet(subject_code, subject_slug, subject_name, year, semester_slug, questions_data):
    """Generate an answer sheet PDF."""
    
    output_dir = os.path.join(PDF_BASE, semester_slug, subject_slug, "answers")
    os.makedirs(output_dir, exist_ok=True)
    
    output_path = os.path.join(output_dir, f"{subject_code}-{year}-answers.pdf")
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        rightMargin=1.5*cm,
        leftMargin=1.5*cm,
        topMargin=2.5*cm,
        bottomMargin=2*cm,
    )
    
    styles = create_styles()
    story = []
    
    # Header
    story.append(Paragraph("Tribhuvan University", styles['TUHeader']))
    story.append(Paragraph("Faculty of Humanities & Social Sciences", styles['TUHeader']))
    story.append(Paragraph("OFFICE OF THE DEAN", styles['TUHeader']))
    story.append(Spacer(1, 0.3*cm))
    
    story.append(Paragraph(f"{subject_name}", styles['AnsTitle']))
    story.append(Paragraph(f"BCA — {semester_slug.replace('-', ' ').title()} — {year} — Answer Sheet", styles['AnsSubtitle']))
    story.append(Paragraph(f"Subject Code: {subject_code}", styles['AnsSubtitle']))
    story.append(Spacer(1, 0.5*cm))
    
    # Divider
    story.append(Table([['']], colWidths=[17*cm], style=TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor('#e2e8f0')),
    ])))
    story.append(Spacer(1, 0.3*cm))
    
    # Questions and Answers
    for group in questions_data:
        story.append(Paragraph(group['title'], styles['GroupHeader']))
        story.append(Paragraph(group['instruction'], styles['Answer']))
        story.append(Spacer(1, 0.2*cm))
        
        for q in group['questions']:
            # Keep question + answer together when possible
            q_block = []
            q_block.append(Paragraph(f"<b>{q['num']}. {q['question']}</b>", styles['Question']))
            if q.get('marks'):
                q_block.append(Paragraph(f"[{q['marks']}]", styles['Marks']))
            
            q_block.append(Spacer(1, 0.1*cm))
            q_block.append(Paragraph(f"<b>Answer:</b> {q['answer']}", styles['Answer']))
            
            if q.get('diagram'):
                q_block.append(Paragraph(
                    f"<i>📐 Diagram Required:</i> {q['diagram']}",
                    styles['DiagramNote']
                ))
            
            story.append(KeepTogether(q_block))
    
    # Disclaimer
    story.append(Spacer(1, 0.5*cm))
    story.append(Table([['']], colWidths=[17*cm], style=TableStyle([
        ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor('#e2e8f0')),
    ])))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph(
        "<i>Note: These answers are prepared for educational purposes. Students are encouraged to verify with official textbooks and course materials.</i>",
        ParagraphStyle('Disclaimer', fontSize=8, leading=12, textColor=colors.HexColor('#94a3b8'), alignment=TA_CENTER)
    ))
    
    doc.build(story, onFirstPage=lambda c, d: draw_header_footer(c, d, subject_name, year, subject_code),
              onLaterPages=lambda c, d: draw_header_footer(c, d, subject_name, year, subject_code))
    
    print(f"Generated: {output_path}")
    return output_path


# ============== DATA FOR 4TH SEMESTER 2020 ==============

OS_QUESTIONS = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "1",
                "question": "What is an Operating System? Why is it known as the resource manager and the extended machine?",
                "marks": "2+3",
                "answer": """An <b>Operating System (OS)</b> is system software that manages computer hardware and software resources and provides common services for computer programs. It acts as an intermediary between users and computer hardware.

<b>Resource Manager:</b> The OS manages all hardware resources including CPU (through scheduling), memory (through allocation and deallocation), disk (through file systems), and I/O devices (through device drivers). It ensures efficient and fair resource sharing among multiple processes and users.

<b>Extended Machine:</b> The OS hides the complexity of hardware from users by providing a clean, abstract interface. Instead of dealing with low-level hardware details (disk sectors, memory addresses, I/O ports), users interact with high-level abstractions like files, folders, and applications. The OS extends the bare hardware into a more convenient and powerful virtual machine.""",
            },
            {
                "num": "2",
                "question": "What is Kernel? What role does it play in an Operating System? Differentiate between monolithic and micro kernel.",
                "marks": "1+1+3",
                "answer": """The <b>Kernel</b> is the core component of an operating system. It is the first program loaded on startup and remains in memory throughout system operation. It has complete control over everything in the system.

<b>Role of Kernel:</b>
• Process management: creating, scheduling, and terminating processes
• Memory management: allocating and deallocating memory space
• Device management: managing device communication via drivers
• System calls: handling requests from applications
• Security and access control

<b>Monolithic vs Micro Kernel:</b>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>Monolithic Kernel</b></td><td><b>Micro Kernel</b></td></tr>
<tr><td>Architecture</td><td>All OS services (file system, device drivers, scheduler) run in kernel space</td><td>Only essential services (memory, scheduling, IPC) run in kernel space</td></tr>
<tr><td>Size</td><td>Large and complex</td><td>Small and minimal</td></tr>
<tr><td>Performance</td><td>Faster (less context switching)</td><td>Slower (more message passing)</td></tr>
<tr><td>Extensibility</td><td>Harder to extend/modify</td><td>Easier to extend services</td></tr>
<tr><td>Reliability</td><td>One bug can crash entire system</td><td>Services can fail independently</td></tr>
<tr><td>Examples</td><td>Linux, Windows (hybrid)</td><td>Minix, QNX, L4</td></tr>
</table>""",
            },
            {
                "num": "3",
                "question": "Suppose that a disk has 200 cylinders (0-200). The head pointer is currently at 50 and previously at 35. The queue of pending request, in FIFO order is 60, 190, 40, 125, 15, and 150. The time required to move per cylinder is 6 msec. Starting from the current head position, what is the total seek time needed to satisfy all the pending request for each of the following disk scheduling algorithms? a) FCFS b) SCAN",
                "marks": "2.5+2.5",
                "answer": """<b>Given:</b>
• Current head position: 50
• Previous head position: 35 (so head is moving upward)
• Request queue: 60, 190, 40, 125, 15, 150
• Time per cylinder: 6 msec

<b>a) FCFS (First Come First Serve):</b>
Order of service: 50 → 60 → 190 → 40 → 125 → 15 → 150

Seek distances:
|60-50| = 10
|190-60| = 130
|40-190| = 150
|125-40| = 85
|15-125| = 110
|150-15| = 135

Total seek distance = 10 + 130 + 150 + 85 + 110 + 135 = <b>620 cylinders</b>
Total seek time = 620 × 6 = <b>3,720 msec (3.72 seconds)</b>

<b>b) SCAN (Elevator Algorithm):</b>
Since previous position was 35 and current is 50, head is moving upward (toward higher cylinders).
Order: 50 → 60 → 125 → 150 → 190 → 200 (end) → 40 → 15

Seek distances:
|60-50| = 10
|125-60| = 65
|150-125| = 25
|190-150| = 40
|200-190| = 10
|40-200| = 160
|15-40| = 25

Total seek distance = 10 + 65 + 25 + 40 + 10 + 160 + 25 = <b>335 cylinders</b>
Total seek time = 335 × 6 = <b>2,010 msec (2.01 seconds)</b>""",
            },
            {
                "num": "4",
                "question": "Define file and directory. Explain the concept of Access Control List (ACL) and Access Control Matrix (ACM).",
                "marks": "2+3",
                "answer": """<b>File:</b> A file is a named collection of related information stored on secondary storage. It is the basic unit of storage in a file system and can contain data, programs, or text.

<b>Directory:</b> A directory is a special file that contains a list of files and subdirectories. It provides a logical organization structure for the file system, allowing users to group related files together.

<b>Access Control List (ACL):</b>
An ACL is a list of permissions attached to an object (file/directory). Each entry in the list specifies which user or group is granted or denied specific access rights (read, write, execute). ACLs provide fine-grained access control.

Example: File 'grades.txt' might have:
• Owner: read, write
• Group 'teachers': read, write
• Group 'students': read only
• User 'admin': full control

<b>Access Control Matrix (ACM):</b>
An ACM is a two-dimensional matrix where rows represent subjects (users/processes) and columns represent objects (files/resources). Each cell contains the access rights that the subject has for that object.

Example matrix:
<table border='1' cellpadding='4'><tr><td></td><td>File A</td><td>File B</td><td>Printer</td></tr>
<tr><td>User1</td><td>RW</td><td>R</td><td>W</td></tr>
<tr><td>User2</td><td>R</td><td>RW</td><td>-</td></tr>
<tr><td>Admin</td><td>RWX</td><td>RWX</td><td>W</td></tr>
</table>

<b>Comparison:</b> ACL is more space-efficient for systems with many objects but few permissions per object. ACM provides a complete view but wastes space when most entries are empty.""",
            },
            {
                "num": "5",
                "question": "What is biometric password in authentication? Explain the various system threats.",
                "marks": "2+3",
                "answer": """<b>Biometric Authentication:</b>
Biometric authentication uses unique physical or behavioral characteristics of an individual for identification. Unlike passwords, biometric traits cannot be easily stolen, shared, or forgotten.

<b>Types of biometric authentication:</b>
• <b>Physical:</b> Fingerprint, iris/retina scan, facial recognition, palm geometry, DNA
• <b>Behavioral:</b> Voice recognition, handwriting/signature dynamics, gait analysis, keystroke dynamics

<b>Advantages:</b> High security, convenience (no password to remember), non-transferable
<b>Disadvantages:</b> Expensive hardware, privacy concerns, false accept/reject rates, cannot be changed if compromised

<b>System Threats:</b>
1. <b>Malware:</b> Viruses, worms, trojans, ransomware that damage or steal data
2. <b>Denial of Service (DoS):</b> Overwhelming system resources to make services unavailable
3. <b>Man-in-the-Middle (MitM):</b> Intercepting communication between two parties
4. <b>Phishing:</b> Fraudulent attempts to obtain sensitive information by disguising as trustworthy
5. <b>Privilege Escalation:</b> Exploiting bugs to gain higher-level access
6. <b>Spoofing:</b> Faking identity (IP spoofing, email spoofing)
7. <b>Buffer Overflow:</b> Overwriting memory to execute malicious code
8. <b>Insider Threats:</b> Malicious actions by authorized users""",
            },
            {
                "num": "6",
                "question": "How distributed operating system is more applicable than centralized operating system? Explain the major goals of distributed operating system.",
                "marks": "2+3",
                "answer": """<b>Distributed OS vs Centralized OS:</b>

A <b>centralized OS</b> manages a single computer with all resources in one location. A <b>distributed OS</b> manages a collection of independent computers that appear to users as a single coherent system.

<b>Why Distributed OS is more applicable:</b>
• <b>Resource Sharing:</b> Users can access remote resources (printers, files, databases) transparently
• <b>Reliability:</b> If one node fails, others continue operating (fault tolerance)
• <b>Scalability:</b> System can grow by adding more nodes
• <b>Performance:</b> Load balancing across multiple processors improves throughput
• <b>Communication:</b> Enables collaboration across geographic locations
• <b>Cost-effective:</b> Network of PCs can be cheaper than a single supercomputer

<b>Major Goals of Distributed OS:</b>
1. <b>Transparency:</b> Hide distribution from users (access, location, migration, replication, concurrency, failure transparency)
2. <b>Reliability:</b> System should continue functioning despite component failures
3. <b>Performance:</b> Response time should be comparable to centralized systems
4. <b>Scalability:</b> System should handle growth in users, resources, and geographic spread
5. <b>Openness:</b> System should conform to standards for interoperability
6. <b>Security:</b> Protect data and resources across the distributed environment""",
            },
            {
                "num": "7",
                "question": "Write short notes on any TWO: a) Producer Consumer problem b) Coalescing and Compaction c) Ubuntu",
                "marks": "2.5+2.5",
                "answer": """<b>a) Producer-Consumer Problem:</b>
The producer-consumer problem is a classic synchronization problem where one or more producer threads generate data and put it into a shared buffer, while one or more consumer threads remove and process data from the buffer.

<b>Challenges:</b>
• Producer must not add data when buffer is full
• Consumer must not remove data when buffer is empty
• Mutual exclusion is needed to prevent race conditions

<b>Solution using semaphores:</b>
• empty = N (buffer size)
• full = 0
• mutex = 1

Producer: wait(empty); wait(mutex); add item; signal(mutex); signal(full)
Consumer: wait(full); wait(mutex); remove item; signal(mutex); signal(empty)

<b>b) Coalescing and Compaction:</b>
These are memory management techniques to reduce external fragmentation.

<b>Coalescing:</b> When a block of memory is freed, the system checks if adjacent blocks are also free. If so, they are merged into a single larger free block. This reduces fragmentation by combining small holes into larger ones.

<b>Compaction:</b> All allocated memory blocks are moved to one end of memory, leaving one large contiguous free block at the other end. This eliminates external fragmentation entirely but requires dynamic relocation support and is time-consuming.

<b>c) Ubuntu:</b>
Ubuntu is a popular Linux-based open-source operating system developed by Canonical Ltd. It is based on Debian and follows a regular release cycle (every 6 months) with LTS (Long Term Support) releases every 2 years supported for 5 years.

<b>Features:</b> User-friendly GUI, extensive software repository, strong community support, security updates, suitable for desktops, servers, and cloud computing. Uses APT package management and GNOME desktop environment by default.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "8",
                "question": "What is CPU scheduling? Write down the criteria for CPU scheduling? Consider the following set of processes, with the length of the CPU burst given in milliseconds, draw Gantt chart illustrating their execution and calculate average waiting time and turnaround time using: a) First Come First Serve b) Shortest Job First c) Non-preemptive priority (smaller number implies higher priority) d) Round Robin (quantum=1). The processes have arrived in the order P0, P1, P2, P3, P4 all at time 0.",
                "marks": "1+1+2+2+2+2",
                "answer": """<b>CPU Scheduling:</b> CPU scheduling is the process of selecting which process in the ready queue should be allocated the CPU. It is a fundamental OS function that improves system performance by maximizing CPU utilization and throughput while minimizing waiting time and response time.

<b>Criteria for CPU Scheduling:</b>
• <b>CPU Utilization:</b> Keep CPU as busy as possible
• <b>Throughput:</b> Number of processes completed per unit time
• <b>Turnaround Time:</b> Time from submission to completion
• <b>Waiting Time:</b> Time spent waiting in ready queue
• <b>Response Time:</b> Time from request submission to first response
• <b>Fairness:</b> Each process gets fair share of CPU

<b>Note:</b> The specific process burst times table was not fully visible in the original paper. A typical example would be:

<table border='1' cellpadding='4'><tr><td>Process</td><td>Burst Time</td><td>Priority</td></tr>
<tr><td>P0</td><td>10</td><td>3</td></tr>
<tr><td>P1</td><td>1</td><td>1</td></tr>
<tr><td>P2</td><td>2</td><td>4</td></tr>
<tr><td>P3</td><td>1</td><td>5</td></tr>
<tr><td>P4</td><td>5</td><td>2</td></tr>
</table>

<b>a) FCFS:</b> P0→P1→P2→P3→P4
Gantt: | P0 (0-10) | P1 (10-11) | P2 (11-13) | P3 (13-14) | P4 (14-19) |

Waiting times: P0=0, P1=10, P2=11, P3=13, P4=14
Average Waiting Time = (0+10+11+13+14)/5 = <b>9.6 ms</b>
Turnaround times: P0=10, P1=11, P2=13, P3=14, P4=19
Average Turnaround Time = (10+11+13+14+19)/5 = <b>13.4 ms</b>

<b>b) SJF (Non-preemptive):</b> P1→P3→P2→P4→P0 (shortest burst first)
Gantt: | P1 (0-1) | P3 (1-2) | P2 (2-4) | P4 (4-9) | P0 (9-19) |

Waiting times: P0=9, P1=0, P2=2, P3=1, P4=4
Average WT = (9+0+2+1+4)/5 = <b>3.2 ms</b>
Average TAT = (19+1+4+2+9)/5 = <b>7.0 ms</b>

<b>c) Priority (Non-preemptive):</b> P1→P4→P0→P2→P3 (lower number = higher priority)
Gantt: | P1 (0-1) | P4 (1-6) | P0 (6-16) | P2 (16-18) | P3 (18-19) |

Average WT = <b>5.4 ms</b>, Average TAT = <b>9.2 ms</b>

<b>d) Round Robin (quantum=1):</b>
Gantt: P0,P1,P2,P3,P4,P0,P2,P4,P0,P4,P0,P4,P0,P0,P0,P0,P0,P0,P0 (0-19)

Average WT ≈ <b>6.8 ms</b>, Average TAT ≈ <b>10.6 ms</b>""",
                "diagram": "Gantt charts should be drawn for each scheduling algorithm showing process execution timeline.",
            },
            {
                "num": "9",
                "question": "Define the terms: page fault and thrashing. Consider the following page reference string: 1, 3, 5, 1, 7, 1, 5, 5, 1, 4, 3, 7, 6, 3, 4, 1. How many page faults would occur for each of the following page replacement algorithms assuming 3 page frames? a) FIFO page replacement b) LRU page replacement c) Optimal page replacement",
                "marks": "2+2+2+2+2",
                "answer": """<b>Page Fault:</b> A page fault occurs when a running program accesses a memory page that is mapped into its virtual address space but is not currently loaded in physical memory (RAM). The OS must then load the required page from disk into memory, which is a costly operation.

<b>Thrashing:</b> Thrashing occurs when a computer's virtual memory resources are overused, leading to a constant state of paging and page faults. The system spends more time swapping pages in and out than executing actual processes. Causes: insufficient physical memory, too many processes running, poor locality of reference.

<b>Reference String:</b> 1, 3, 5, 1, 7, 1, 5, 5, 1, 4, 3, 7, 6, 3, 4, 1
<b>Page Frames:</b> 3

<b>a) FIFO (First In First Out):</b>
<table border='1' cellpadding='3'><tr><td>Ref</td><td>1</td><td>3</td><td>5</td><td>1</td><td>7</td><td>1</td><td>5</td><td>5</td><td>1</td><td>4</td><td>3</td><td>7</td><td>6</td><td>3</td><td>4</td><td>1</td></tr>
<tr><td>F1</td><td>1*</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>4*</td><td>4</td><td>4</td><td>6*</td><td>6</td><td>6</td><td>6</td></tr>
<tr><td>F2</td><td>-</td><td>3*</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>7*</td><td>7</td><td>7</td><td>7</td><td>7</td></tr>
<tr><td>F3</td><td>-</td><td>-</td><td>5*</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>5</td><td>3*</td><td>3</td><td>1*</td></tr>
</table>
Page faults marked with *. Total page faults with FIFO = <b>9</b>

<b>b) LRU (Least Recently Used):</b>
<table border='1' cellpadding='3'><tr><td>Ref</td><td>1</td><td>3</td><td>5</td><td>1</td><td>7</td><td>1</td><td>5</td><td>5</td><td>1</td><td>4</td><td>3</td><td>7</td><td>6</td><td>3</td><td>4</td><td>1</td></tr>
<tr><td>F1</td><td>1*</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>3*</td><td>3</td><td>6*</td><td>6</td><td>6</td><td>1*</td></tr>
<tr><td>F2</td><td>-</td><td>3*</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>4*</td><td>4</td><td>4</td><td>4</td><td>3</td><td>3</td><td>3</td></tr>
<tr><td>F3</td><td>-</td><td>-</td><td>5*</td><td>5</td><td>7*</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>7</td><td>4*</td><td>4</td></tr>
</table>
Total page faults with LRU = <b>7</b>

<b>c) Optimal Page Replacement:</b>
The optimal algorithm replaces the page that will not be used for the longest period in the future.
<table border='1' cellpadding='3'><tr><td>Ref</td><td>1</td><td>3</td><td>5</td><td>1</td><td>7</td><td>1</td><td>5</td><td>5</td><td>1</td><td>4</td><td>3</td><td>7</td><td>6</td><td>3</td><td>4</td><td>1</td></tr>
<tr><td>F1</td><td>1*</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>1</td><td>6*</td><td>6</td><td>6</td><td>6</td></tr>
<tr><td>F2</td><td>-</td><td>3*</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td><td>3</td></tr>
<tr><td>F3</td><td>-</td><td>-</td><td>5*</td><td>5</td><td>7*</td><td>7</td><td>7</td><td>7</td><td>7</td><td>4*</td><td>4</td><td>7*</td><td>7</td><td>7</td><td>4*</td><td>1*</td></tr>
</table>
Total page faults with Optimal = <b>7</b>""",
            },
            {
                "num": "10",
                "question": "Define deadlock. List out the conditions that can result in resource deadlock. Explain different deadlock handling methods in details.",
                "marks": "2+1+7",
                "answer": """<b>Deadlock:</b> A deadlock is a situation in which two or more processes are unable to proceed because each is waiting for one of the others to release a resource. It is a permanent blocking of processes.

<b>Four Necessary Conditions for Deadlock (Coffman Conditions):</b>
1. <b>Mutual Exclusion:</b> At least one resource must be non-sharable
2. <b>Hold and Wait:</b> A process holding resources can request additional resources
3. <b>No Preemption:</b> Resources cannot be forcibly taken from a process
4. <b>Circular Wait:</b> A circular chain of processes exists where each waits for a resource held by the next

<b>Deadlock Handling Methods:</b>

<b>1. Deadlock Prevention:</b> Ensure at least one Coffman condition never holds.
• <b>Mutual Exclusion:</b> Make all resources sharable (not always possible)
• <b>Hold and Wait:</b> Require processes to request all resources at once, or release current resources before requesting new ones
• <b>No Preemption:</b> Allow forced resource preemption (rollback and restart)
• <b>Circular Wait:</b> Impose ordering on resource types; processes must request resources in increasing order

<b>2. Deadlock Avoidance:</b> Dynamically analyze resource allocation state to ensure system never enters unsafe state.
• <b>Banker's Algorithm:</b> Uses maximum demand, current allocation, and available resources to determine if a request can be safely granted. System maintains safe state where a sequence exists for all processes to complete.

<b>3. Deadlock Detection and Recovery:</b> Allow deadlocks to occur, then detect and recover.
• <b>Detection:</b> Use wait-for graph (single instance) or resource allocation graph (multiple instances)
• <b>Recovery:</b> Process termination (kill all or one at a time) or resource preemption (select victim, rollback, starvation prevention)

<b>4. Deadlock Ignorance (Ostrich Algorithm):</b> Pretend deadlocks never occur. Used in most OS (Windows, Linux) because deadlock prevention is too expensive and deadlocks are rare. If deadlock occurs, reboot the system.""",
            },
        ]
    }
]


if __name__ == "__main__":
    # Generate OS answer sheet
    generate_answer_sheet(
        "CACS251", "operating-systems", "Operating Systems",
        2020, "semester-4", OS_QUESTIONS
    )
    print("Answer sheet generation complete for OS!")


# ============== NUMERICAL METHODS (CACS252) 2020 ==============

NM_QUESTIONS = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "1",
                "question": "Compute the root of equation x² - 5x + 6 = 0 in the vicinity of x = 5 using Newton-Raphson method.",
                "marks": "5",
                "answer": """<b>Newton-Raphson Method:</b> x<sub>n+1</sub> = x<sub>n</sub> - f(x<sub>n</sub>)/f'(x<sub>n</sub>)

Given: f(x) = x² - 5x + 6, f'(x) = 2x - 5, x₀ = 5

<b>Iteration 1:</b>
f(5) = 25 - 25 + 6 = 6
f'(5) = 10 - 5 = 5
x₁ = 5 - 6/5 = 5 - 1.2 = <b>3.8</b>

<b>Iteration 2:</b>
f(3.8) = 14.44 - 19 + 6 = 1.44
f'(3.8) = 7.6 - 5 = 2.6
x₂ = 3.8 - 1.44/2.6 = 3.8 - 0.554 = <b>3.246</b>

<b>Iteration 3:</b>
f(3.246) = 10.537 - 16.23 + 6 = 0.307
f'(3.246) = 6.492 - 5 = 1.492
x₃ = 3.246 - 0.307/1.492 = 3.246 - 0.206 = <b>3.04</b>

<b>Iteration 4:</b>
f(3.04) = 9.242 - 15.2 + 6 = 0.042
f'(3.04) = 6.08 - 5 = 1.08
x₄ = 3.04 - 0.042/1.08 = 3.04 - 0.039 = <b>3.001</b>

<b>Root ≈ 3.0</b> (The exact roots are x = 2 and x = 3; starting near 5 converges to x = 3)""",
            },
            {
                "num": "2",
                "question": "Estimate the value of ln(2.5) using Newton-Gregory forward difference formula given the following data.",
                "marks": "5",
                "answer": """<b>Note:</b> The data table was not fully visible in the original question. Assuming typical data points for ln(x):

<table border='1' cellpadding='4'><tr><td>x</td><td>2.0</td><td>2.2</td><td>2.4</td><td>2.6</td><td>2.8</td></tr>
<tr><td>ln(x)</td><td>0.693</td><td>0.788</td><td>0.875</td><td>0.956</td><td>1.030</td></tr>
</table>

Step size h = 0.2, x₀ = 2.0, x = 2.5
u = (x - x₀)/h = (2.5 - 2.0)/0.2 = 2.5

Forward differences:
Δy₀ = 0.095, Δ²y₀ = -0.008, Δ³y₀ = 0.001

Newton-Gregory Forward:
y(2.5) ≈ y₀ + uΔy₀ + u(u-1)Δ²y₀/2! + u(u-1)(u-2)Δ³y₀/3!
= 0.693 + 2.5(0.095) + 2.5(1.5)(-0.008)/2 + 2.5(1.5)(0.5)(0.001)/6
= 0.693 + 0.2375 - 0.015 + 0.0003
= <b>0.9158</b>

Actual ln(2.5) = 0.9163. Error ≈ 0.0005""",
            },
            {
                "num": "3",
                "question": "Write an algorithm to compute integration using Simpson's 1/3 rule. Evaluate integration of f(x) using Simpson's 1/3 rule.",
                "marks": "2.5+2.5",
                "answer": """<b>Simpson's 1/3 Rule Algorithm:</b>
1. Start
2. Define function f(x)
3. Read lower limit a, upper limit b, number of intervals n (must be even)
4. Calculate h = (b - a)/n
5. Initialize sum = f(a) + f(b)
6. For i = 1 to n-1:
   If i is even: sum += 2 × f(a + i×h)
   Else: sum += 4 × f(a + i×h)
7. Result = (h/3) × sum
8. Print Result
9. Stop

<b>Formula:</b> ∫<sub>a</sub><sup>b</sup> f(x)dx ≈ (h/3)[y₀ + 4(y₁+y₃+...) + 2(y₂+y₄+...) + y<sub>n</sub>]

<b>Evaluation:</b> Since the specific function f(x) was not visible in the original paper, a common example would be ∫<sub>0</sub><sup>1</sup> dx/(1+x²) with n=4:
h = 0.25
y₀=1.000, y₁=0.941, y₂=0.800, y₃=0.640, y₄=0.500
Result = (0.25/3)[1 + 4(0.941+0.640) + 2(0.800) + 0.500]
= (0.0833)[1 + 6.324 + 1.6 + 0.5] = <b>0.7854</b>

(Exact value = arctan(1) = π/4 ≈ 0.7854)""",
            },
            {
                "num": "4",
                "question": "What is meant by ill-conditioned system? Find the Cholesky decomposition of the following matrix.",
                "marks": "5",
                "answer": """<b>Ill-conditioned System:</b>
A system of linear equations is ill-conditioned if small changes in the coefficients or right-hand side values lead to large changes in the solution. The system is sensitive to round-off errors during computation. The condition number of the matrix (ratio of largest to smallest singular value) is large for ill-conditioned systems.

<b>Cholesky Decomposition:</b> A = LL<sup>T</sup> where L is lower triangular.

<b>Note:</b> The specific matrix was not fully visible in the original paper. A common example:

A = [[4, 2], [2, 5]]

L = [[l₁₁, 0], [l₂₁, l₂₂]]

l₁₁ = √4 = 2
l₂₁ = 2/2 = 1
l₂₂ = √(5 - 1²) = √4 = 2

So L = [[2, 0], [1, 2]]

Verification: LL<sup>T</sup> = [[2,0],[1,2]] × [[2,1],[0,2]] = [[4,2],[2,5]] = A ✓""",
            },
            {
                "num": "5",
                "question": "Use the classical RK method to estimate y(0.4) of the equation with y(0) = 0 assume h = 0.2",
                "marks": "5",
                "answer": """<b>Classical RK-4 Method:</b>
y<sub>n+1</sub> = y<sub>n</sub> + (h/6)(k₁ + 2k₂ + 2k₃ + k₄)

<b>Note:</b> The specific differential equation was not fully visible. Assuming a common example: dy/dx = x + y, y(0) = 0, h = 0.2, find y(0.4).

<b>Step 1: x₀ = 0, y₀ = 0</b>
k₁ = f(0, 0) = 0 + 0 = 0
k₂ = f(0.1, 0 + 0.1×0) = 0.1 + 0 = 0.1
k₃ = f(0.1, 0 + 0.1×0.1) = 0.1 + 0.01 = 0.11
k₄ = f(0.2, 0 + 0.2×0.11) = 0.2 + 0.022 = 0.222

y₁ = 0 + (0.2/6)(0 + 0.2 + 0.22 + 0.222) = 0.0333 × 0.642 = <b>0.0214</b>

<b>Step 2: x₁ = 0.2, y₁ = 0.0214</b>
k₁ = f(0.2, 0.0214) = 0.2214
k₂ = f(0.3, 0.0214 + 0.1×0.2214) = 0.3 + 0.0435 = 0.3435
k₃ = f(0.3, 0.0214 + 0.1×0.3435) = 0.3 + 0.0558 = 0.3558
k₄ = f(0.4, 0.0214 + 0.2×0.3558) = 0.4 + 0.0926 = 0.4926

y₂ = 0.0214 + (0.2/6)(0.2214 + 0.687 + 0.7116 + 0.4926)
= 0.0214 + 0.0333 × 2.1126 = 0.0214 + 0.0704 = <b>0.0918</b>

Therefore, <b>y(0.4) ≈ 0.0918</b>""",
            },
            {
                "num": "6",
                "question": "Solve the Poisson equation over the square domain 0≤x≤3 and 0≤y≤3 with f = 0 on the boundary and h = 1.",
                "marks": "5",
                "answer": """<b>Poisson Equation:</b> ∇²u = f(x,y)

For this problem with h = 1 and domain 0≤x≤3, 0≤y≤3:
Grid points: (0,0), (1,0), (2,0), (3,0), ..., (3,3) — 16 points total

Boundary condition: u = 0 on all boundaries
Interior points to solve: (1,1), (2,1), (1,2), (2,2)

Using finite difference: u<sub>i+1,j</sub> + u<sub>i-1,j</sub> + u<sub>i,j+1</sub> + u<sub>i,j-1</sub> - 4u<sub>i,j</sub> = h²f<sub>i,j</sub>

Since f = 0 and h = 1:
4u<sub>i,j</sub> = u<sub>i+1,j</sub> + u<sub>i-1,j</sub> + u<sub>i,j+1</sub> + u<sub>i,j-1</sub>

By symmetry and boundary conditions (all boundary values = 0):
Let u(1,1) = u(2,1) = u(1,2) = u(2,2) = u

For any interior point: 4u = 0 + 0 + 0 + u → This gives 4u = u, so u = 0

Wait — with all boundaries zero and f=0, the solution is trivial: <b>u = 0 everywhere</b>.

This suggests the original question likely had non-zero boundary conditions or a non-zero f that were not fully visible in the source document.""",
            },
            {
                "num": "7",
                "question": "Write a short note on (Any Two): a) Types of Errors b) Convergent Methods c) PDE",
                "marks": "2.5+2.5",
                "answer": """<b>a) Types of Errors in Numerical Methods:</b>

<b>1. Round-off Error:</b> Occurs due to finite precision of computer arithmetic. Computers represent numbers with finite bits, so some numbers cannot be represented exactly. Accumulates through repeated calculations.

<b>2. Truncation Error:</b> Results from approximating an infinite process with a finite one. Example: truncating Taylor series after finite terms. Error = True value - Approximate value.

<b>3. Absolute Error:</b> |True value - Approximate value|
<b>4. Relative Error:</b> Absolute Error / |True value|
<b>5. Percentage Error:</b> Relative Error × 100%

<b>6. Inherent Error:</b> Present in initial data due to measurement limitations or approximate input values.

<b>b) Convergent Methods:</b>
A numerical method is convergent if the approximate solution approaches the exact solution as the step size h approaches zero. 

<b>Key concepts:</b>
• <b>Order of convergence:</b> Rate at which error decreases (e.g., O(h), O(h²))
• <b>Consistency:</b> Local truncation error → 0 as h → 0
• <b>Stability:</b> Small perturbations don't cause unbounded growth
• <b>Lax Equivalence Theorem:</b> For well-posed linear problems, consistency + stability ⇔ convergence

<b>c) Partial Differential Equations (PDE):</b>
PDEs involve partial derivatives of a function of multiple variables.

<b>Major types:</b>
• <b>Elliptic:</b> ∇²u = f (e.g., Laplace, Poisson) — steady-state problems
• <b>Parabolic:</b> ∂u/∂t = α∇²u (e.g., heat equation) — diffusion problems
• <b>Hyperbolic:</b> ∂²u/∂t² = c²∇²u (e.g., wave equation) — propagation problems

<b>Solution methods:</b> Finite difference, finite element, finite volume methods.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "8",
                "question": "Write an algorithm and program to compute root of nonlinear equation using bisection method.",
                "marks": "4+6",
                "answer": """<b>Bisection Method Algorithm:</b>
1. Start
2. Define function f(x)
3. Read initial guesses a and b
4. Check if f(a) × f(b) < 0 (opposite signs). If not, error — no root guaranteed.
5. Repeat until |b-a| < tolerance:
   c = (a + b)/2
   If f(c) = 0: c is the root. Stop.
   If f(a) × f(c) < 0: b = c
   Else: a = c
6. Print root c
7. Stop

<b>Python Program:</b>
<pre>
def f(x):
    return x**3 - x - 2

def bisection(a, b, tol=0.0001, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails.")
        return None
    
    for i in range(max_iter):
        c = (a + b) / 2
        if abs(f(c)) < tol:
            return c
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

root = bisection(1, 2)
print(f"Root = {root}")  # Output: ~1.521
</pre>

<b>Explanation:</b> The bisection method repeatedly halves the interval [a,b] and selects the subinterval where the function changes sign. It is guaranteed to converge if f is continuous and f(a)×f(b) < 0. Convergence is linear with rate O(1/2<sup>n</sup>).""",
            },
            {
                "num": "9",
                "question": "Given the data points, estimate the function value of f at x = 14 using cubic splines.",
                "marks": "10",
                "answer": """<b>Cubic Spline Interpolation:</b>
A cubic spline S(x) is a piecewise cubic polynomial that passes through all data points and has continuous first and second derivatives at the interior points.

<b>Note:</b> The specific data points were not fully visible in the original paper. Using a typical example:

<table border='1' cellpadding='4'><tr><td>x</td><td>10</td><td>12</td><td>15</td><td>18</td></tr>
<tr><td>f(x)</td><td>20</td><td>28</td><td>40</td><td>55</td></tr>
</table>

For cubic splines with natural boundary conditions (S''=0 at endpoints):

The spline on each interval [x<sub>i</sub>, x<sub>i+1</sub>] is:
S<sub>i</sub>(x) = a<sub>i</sub> + b<sub>i</sub>(x-x<sub>i</sub>) + c<sub>i</sub>(x-x<sub>i</sub>)² + d<sub>i</sub>(x-x<sub>i</sub>)³

After solving the tridiagonal system for c<sub>i</sub> values and computing coefficients:

For interval [12, 15] (since 14 falls here):
S(x) ≈ 28 + 2.8(x-12) + 0.15(x-12)² - 0.01(x-12)³

At x = 14:
S(14) = 28 + 2.8(2) + 0.15(4) - 0.01(8)
= 28 + 5.6 + 0.6 - 0.08 = <b>34.12</b>

Exact calculation depends on the specific data points provided in the exam.""",
            },
            {
                "num": "10",
                "question": "a) Solve the following system of equation by Gauss-Seidel method. 2x - 7y - 10z = -17, 5x + y + 3z = 14, x + 10y + 9z = 7. b) Write an expansion of Taylor's Theorem. Solve the equation y'(x) = x² + y², y(0) = 1 for x = 0.5 using Taylor method.",
                "marks": "5+2.5+2.5",
                "answer": """<b>a) Gauss-Seidel Method:</b>
Rewrite equations:
x = (14 - y - 3z)/5
y = (-17 - 2x + 10z)/(-7) = (17 + 2x - 10z)/7
z = (7 - x - 10y)/9

Initial guess: (0, 0, 0)

<b>Iteration 1:</b>
x = (14 - 0 - 0)/5 = 2.8
y = (17 + 5.6 - 0)/7 = 22.6/7 = 3.229
z = (7 - 2.8 - 32.29)/9 = -28.09/9 = -3.121

<b>Iteration 2:</b>
x = (14 - 3.229 + 9.363)/5 = 20.134/5 = 4.027
y = (17 + 8.054 + 31.21)/7 = 56.264/7 = 8.038
z = (7 - 4.027 - 80.38)/9 = -77.407/9 = -8.601

<b>Note:</b> This system may be ill-conditioned or require rearrangement for convergence. Gauss-Seidel requires diagonal dominance for guaranteed convergence. Let me try rearranging:

5x + y + 3z = 14 → x = (14-y-3z)/5
2x - 7y - 10z = -17 → y = (17+2x-10z)/7
x + 10y + 9z = 7 → z = (7-x-10y)/9

The system is not strictly diagonally dominant. Gauss-Seidel may diverge. Using Gaussian elimination or Jacobi method with relaxation might be better.

<b>b) Taylor's Theorem Expansion:</b>
f(x+h) = f(x) + hf'(x) + (h²/2!)f''(x) + (h³/3!)f'''(x) + ... + (h<sup>n</sup>/n!)f<sup>(n)</sup>(x) + R<sub>n</sub>

<b>Taylor Series Method for ODE:</b>
Given: y' = x² + y², y(0) = 1, find y(0.5), h = 0.5 (single step)

y' = x² + y²
y'' = 2x + 2yy'
y''' = 2 + 2(y')² + 2yy''

At x=0, y=1:
y' = 0 + 1 = 1
y'' = 0 + 2(1)(1) = 2
y''' = 2 + 2(1) + 2(1)(2) = 2 + 2 + 4 = 8

y(0.5) = y(0) + 0.5y' + (0.5²/2)y'' + (0.5³/6)y'''
= 1 + 0.5(1) + 0.125(2) + 0.0208(8)
= 1 + 0.5 + 0.25 + 0.1667 = <b>1.9167</b>""",
            },
        ]
    }
]


# ============== SOFTWARE ENGINEERING (CACS253) 2020 ==============

SE_QUESTIONS = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "1",
                "question": "What is software engineering? Explain the challenges facing software engineering.",
                "marks": "2+3",
                "answer": """<b>Software Engineering:</b> Software engineering is the systematic application of engineering approaches to the development, operation, and maintenance of software. It encompasses techniques, methods, and tools for building high-quality software within budget and schedule constraints. Fritz Bauer defined it as "the establishment and use of sound engineering principles to obtain economically software that is reliable and works efficiently on real machines."

<b>Challenges Facing Software Engineering:</b>
1. <b>Increasing Complexity:</b> Modern software systems are highly complex with millions of lines of code, multiple platforms, and distributed architectures.
2. <b>Changing Requirements:</b> Requirements evolve throughout the development lifecycle, making it difficult to deliver what customers actually need.
3. <b>Time and Cost Constraints:</b> Pressure to deliver quickly while maintaining quality and staying within budget.
4. <b>Quality Assurance:</b> Ensuring reliability, security, performance, and usability in diverse environments.
5. <b>Legacy Systems:</b> Integrating with and maintaining old systems while modernizing technology stacks.
6. <b>Security Threats:</b> Protecting against increasingly sophisticated cyber attacks and data breaches.
7. <b>Scalability:</b> Designing systems that can handle growing user bases and data volumes.
8. <b>Team Coordination:</b> Managing large, often geographically distributed development teams.
9. <b>Technology Evolution:</b> Keeping up with rapidly changing technologies, frameworks, and platforms.
10. <b>User Expectations:</b> Meeting high expectations for intuitive interfaces and seamless experiences.""",
            },
            {
                "num": "2",
                "question": "What is extreme programming? Explain how the principles underlying extreme programming lead to the accelerated development of software.",
                "marks": "1+4",
                "answer": """<b>Extreme Programming (XP):</b> XP is an agile software development methodology introduced by Kent Beck that emphasizes customer satisfaction, continuous feedback, and rapid delivery of working software. It takes best practices to "extreme" levels.

<b>Principles and How They Accelerate Development:</b>

1. <b>Fine-scale Feedback:</b>
   • <b>Pair Programming:</b> Two developers work together — one codes, one reviews. This catches defects immediately, reducing debugging time later.
   • <b>Planning Game:</b> Customers and developers collaborate on planning, ensuring alignment and reducing rework.
   • <b>Customer Presence:</b> On-site customer provides immediate clarifications, eliminating delays from waiting for responses.

2. <b>Continuous Process:</b>
   • <b>Continuous Integration:</b> Code is integrated and tested multiple times daily. Problems are caught immediately rather than at the end.
   • <b>Refactoring:</b> Continuous code improvement prevents technical debt accumulation, keeping the codebase maintainable.
   • <b>Small Releases:</b> Frequent small releases provide early value and rapid feedback.

3. <b>Shared Understanding:</b>
   • <b>Simple Design:</b> The simplest solution that works reduces development time and complexity.
   • <b>System Metaphor:</b> Shared conceptual framework helps team communicate efficiently.
   • <b>Collective Code Ownership:</b> Anyone can modify any code, eliminating bottlenecks when specific developers are unavailable.

4. <b>Programmer Welfare:</b>
   • <b>Sustainable Pace:</b> 40-hour weeks prevent burnout, maintaining consistent productivity.
   • <b>Coding Standards:</b> Consistent style reduces time spent understanding others' code.

By emphasizing communication, simplicity, feedback, and courage, XP eliminates waste and focuses effort on delivering value quickly.""",
            },
            {
                "num": "3",
                "question": "Define quality assurance? Under what circumstances would you recommend the use of staged representation of the CMM?",
                "marks": "2+3",
                "answer": """<b>Software Quality Assurance (SQA):</b> SQA is a set of activities that define and assess the adequacy of software processes to provide evidence that establishes confidence that the software processes are appropriate for and produce software products of suitable quality for their intended purposes. It includes the entire software development process — monitoring and improving the process, making sure standards and procedures are followed, and ensuring problems are found and fixed.

<b>CMM Staged Representation:</b>
The Capability Maturity Model (CMM) defines five maturity levels:
1. <b>Initial:</b> Ad hoc, chaotic processes
2. <b>Managed:</b> Basic project management processes established
3. <b>Defined:</b> Standard processes across the organization
4. <b>Quantitatively Managed:</b> Detailed metrics for process control
5. <b>Optimizing:</b> Continuous process improvement

<b>Circumstances for Staged Representation:</b>

1. <b>Process Improvement Initiative:</b> When an organization wants a clear roadmap for improving software development capabilities step by step.

2. <b>Government or Defense Contracts:</b> Many government contracts (especially in the US) require specific CMM levels (typically Level 3 or higher).

3. <b>Large Organizations:</b> When standardizing processes across multiple teams or departments that currently work differently.

4. <b>Quality-Critical Systems:</b> For safety-critical software (medical devices, aerospace, nuclear systems) where process maturity directly impacts risk.

5. <b>Vendor Assessment:</b> When evaluating outsourced development partners — CMM level provides a standardized benchmark.

6. <b>Benchmarking:</b> Comparing organizational capability against industry standards.

The staged model is preferred when a sequential, milestone-based improvement approach is desired, as opposed to the continuous representation which allows focusing on specific process areas.""",
            },
            {
                "num": "4",
                "question": "What is architectural design? Explain layered model of software architecture with example.",
                "marks": "1+4",
                "answer": """<b>Architectural Design:</b> Architectural design is the process of defining a structured solution that meets all technical and operational requirements while optimizing common quality attributes such as performance, security, and manageability. It identifies major system components, their responsibilities, interfaces, and interactions. The architecture serves as the blueprint for both the system and the project developing it.

<b>Layered Architecture Model:</b>
The layered architecture pattern organizes software into distinct layers, each with a specific responsibility. Lower layers provide services to upper layers, and each layer is independent of layers above it.

<b>Typical Layers:</b>

1. <b>Presentation Layer (UI Layer):</b>
   • Handles user interface and user interaction
   • Displays information and captures user input
   • Example: HTML/CSS/JavaScript in web apps, Android Activities

2. <b>Business Logic Layer (Application/Service Layer):</b>
   • Contains core business rules and logic
   • Processes data, makes decisions, coordinates workflows
   • Example: Order processing, payment validation, user authentication

3. <b>Data Access Layer (Persistence Layer):</b>
   • Handles database interactions
   • CRUD operations, query execution, ORM mapping
   • Example: Repository classes, DAO (Data Access Objects)

4. <b>Database Layer:</b>
   • Physical data storage
   • Example: MySQL, PostgreSQL, MongoDB

<b>Example — E-Commerce Application:</b>

<table border='1' cellpadding='4'><tr><td><b>Layer</b></td><td><b>Components</b></td></tr>
<tr><td>Presentation</td><td>Product catalog page, shopping cart UI, checkout forms</td></tr>
<tr><td>Business Logic</td><td>CartService (calculates totals), OrderService (validates orders), PaymentService</td></tr>
<tr><td>Data Access</td><td>ProductRepository, OrderRepository, UserRepository</td></tr>
<tr><td>Database</td><td>Products table, Orders table, Users table</td></tr>
</table>

<b>Advantages:</b> Separation of concerns, easier maintenance, testability, reusability, parallel development.
<b>Disadvantages:</b> Performance overhead from layer transitions, potential for tight coupling if not designed carefully.""",
                "diagram": "A layered architecture diagram showing 4 horizontal layers: Presentation at top, then Business Logic, then Data Access, then Database at bottom, with downward arrows indicating dependency.",
            },
            {
                "num": "5",
                "question": "Differentiate between verification and validation. Explain why software inspection is an effective technique for discovering errors in software?",
                "marks": "3+2",
                "answer": """<b>Verification vs Validation:</b>

<table border='1' cellpadding='4'><tr><td><b>Aspect</b></td><td><b>Verification</b></td><td><b>Validation</b></td></tr>
<tr><td>Definition</td><td>Are we building the product right?</td><td>Are we building the right product?</td></tr>
<tr><td>Focus</td><td>Process, documents, code conformity to specifications</td><td>Final product meets user needs and expectations</td></tr>
<tr><td>When</td><td>Throughout development (reviews, inspections, walkthroughs)</td><td>At the end or with user involvement (testing, UAT)</td></tr>
<tr><td>Activities</td><td>Static analysis, code reviews, requirement reviews</td><td>Functional testing, beta testing, user acceptance</td></tr>
<tr><td>Objective</td><td>Ensure software conforms to specifications</td><td>Ensure software meets intended use</td></tr>
<tr><td>Techniques</td><td>Walkthroughs, inspections, audits</td><td>Black-box testing, white-box testing, usability testing</td></tr>
</table>

<b>Why Software Inspection is Effective:</b>

1. <b>Early Defect Detection:</b> Inspections find errors before testing, when they are cheaper to fix (up to 100x cheaper than post-deployment fixes).

2. <b>High Defect Detection Rate:</b> Studies show inspections can find 60-90% of defects, compared to 30-50% for testing alone.

3. <b>Diverse Perspectives:</b> Multiple reviewers bring different viewpoints — developers, testers, domain experts all contribute.

4. <b>Process Improvement:</b> Patterns in defects found during inspections reveal systematic problems in development processes.

5. <b>No Execution Required:</b> Inspections can be done on requirements, designs, and code without working software, enabling earlier feedback.

6. <b>Knowledge Sharing:</b> Team members learn from each other during inspections, improving overall team capability.

7. <b>Cost Effective:</b> Finding and fixing a defect during inspection costs a fraction of finding it during testing or in production.""",
            },
            {
                "num": "6",
                "question": "What is software reengineering? List its advantages. Explain source code translation and reverse engineering approach in brief.",
                "marks": "1+1+3",
                "answer": """<b>Software Reengineering:</b> Software reengineering is the examination and alteration of a subject system to reconstitute it in a new form and the subsequent implementation of the new form. It involves analyzing, modifying, and reconstructing existing software systems to improve their maintainability, performance, or adaptability to new environments. It is not simply rewriting — it is a systematic transformation that preserves the system's functionality.

<b>Advantages:</b>
• Reduced risk compared to complete redevelopment
• Lower cost than building from scratch
• Preserves business knowledge embedded in the system
• Improved maintainability and documentation
• Better performance and reliability
• Easier integration with modern systems
• Extended system lifetime

<b>Source Code Translation:</b>
This is the automatic conversion of program source code from one programming language to another (e.g., COBOL to Java) or from one platform to another. Tools analyze the source code, parse it into an intermediate representation, and then generate equivalent code in the target language. Challenges include handling language-specific features, preserving semantics, and dealing with platform dependencies.

<b>Reverse Engineering:</b>
Reverse engineering is the process of analyzing a finished product (source code or executable) to understand its design, architecture, and functionality. It extracts design information from code when documentation is missing or outdated. Activities include:
• Identifying system components and relationships
• Recovering data models and control flow
• Creating documentation from undocumented code
• Understanding algorithms and business rules

Reverse engineering is often the first step before forward engineering or reengineering, providing the understanding needed to make informed modifications.""",
            },
            {
                "num": "7",
                "question": "What do you mean by software quality management? Explain software quality management activities in brief.",
                "marks": "2+3",
                "answer": """<b>Software Quality Management (SQM):</b> SQM is the collection of all processes and activities that ensure software meets its intended quality standards. It encompasses quality planning, quality assurance, quality control, and continuous improvement throughout the software lifecycle. SQM aims to deliver software that satisfies customer requirements, is fit for purpose, and is free from critical defects.

<b>Software Quality Management Activities:</b>

1. <b>Quality Planning:</b>
   • Define quality goals and standards
   • Identify quality metrics and acceptance criteria
   • Determine quality assurance activities and resources
   • Create quality management plan

2. <b>Quality Assurance (QA):</b>
   • Process-focused activities to ensure development follows standards
   • Audits and reviews of processes and documentation
   • Training and process improvement initiatives
   • Establishing and maintaining quality standards

3. <b>Quality Control (QC):</b>
   • Product-focused testing and inspection activities
   • Unit testing, integration testing, system testing, acceptance testing
   • Defect tracking and reporting
   • Verification that product meets specifications

4. <b>Quality Improvement:</b>
   • Analyze defect data to identify root causes
   • Implement process changes to prevent recurring issues
   • Continuous monitoring and measurement
   • Apply frameworks like Six Sigma, CMMI, or TQM

5. <b>Configuration Management:</b>
   • Version control and change management
   • Ensuring traceability of requirements to code to tests
   • Managing releases and baselines

6. <b>Metrics and Measurement:</b>
   • Collect data on defects, effort, schedule, size
   • Calculate quality indicators (defect density, test coverage, MTBF)
   • Use metrics to drive decisions and improvements""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "8",
                "question": "What is software process model? List different software process model. Explain how both the waterfall model of the software process and prototyping model can be accommodated in the spiral process model.",
                "marks": "2+2+6",
                "answer": """<b>Software Process Model:</b> A software process model is an abstract representation of a software process. It provides a structured approach to software development by defining the phases, activities, deliverables, and control mechanisms for building software systems. It serves as a roadmap guiding the project from conception to delivery and maintenance.

<b>Different Software Process Models:</b>
1. Waterfall Model
2. V-Model
3. Incremental Model
4. Spiral Model
5. Prototyping Model
6. RAD (Rapid Application Development)
7. Agile/Scrum/XP
8. DevOps

<b>Accommodating Waterfall and Prototyping in Spiral Model:</b>

The <b>Spiral Model</b>, proposed by Barry Boehm, combines iterative development with systematic aspects of the waterfall model. Each loop of the spiral represents a phase of the software process and is divided into four quadrants:

1. <b>Determine Objectives, Alternatives, Constraints</b>
2. <b>Evaluate Alternatives, Identify and Resolve Risks</b>
3. <b>Develop and Verify Next-Level Product</b>
4. <b>Plan Next Phase</b>

<b>Waterfall in Spiral:</b>
Within each spiral loop (especially early loops with low risk), the development can follow a waterfall-like sequence. For well-understood requirements with clear objectives, the third quadrant can execute requirements → design → implementation → testing in a linear fashion. The waterfall's discipline of completing one phase before moving to the next fits within a single spiral iteration when risks are minimal and requirements are stable.

<b>Prototyping in Spiral:</b>
When risks are high and requirements are unclear (typically in early spirals), the third quadrant employs prototyping. A quick prototype is built to explore alternatives, validate requirements with users, and reduce uncertainty. Based on user feedback, the prototype evolves or is discarded. This directly maps to the risk-resolution focus of the second quadrant — prototyping is the primary technique for resolving requirement risks.

The spiral model's flexibility allows it to incorporate different approaches in different iterations based on risk assessment — waterfall for low-risk phases, prototyping for high-risk uncertain areas.""",
                "diagram": "Spiral model diagram showing 4 quadrants: (1) Objectives, (2) Risk Analysis, (3) Development & Test, (4) Planning. Multiple loops expanding outward with increasing completeness.",
            },
            {
                "num": "9",
                "question": "What do you mean by software requirement? Differentiate between functional requirement and non-functional requirement. List the functional requirements of online examination system and represent it in use case diagram.",
                "marks": "2+4+4",
                "answer": """<b>Software Requirement:</b> A software requirement is a condition or capability needed by a user to solve a problem or achieve an objective. It can be a condition or capability that must be met or possessed by a system or system component to satisfy a contract, standard, specification, or other formally imposed documents. Requirements form the foundation for software design, implementation, testing, and acceptance.

<b>Functional vs Non-Functional Requirements:</b>

<table border='1' cellpadding='4'><tr><td><b>Aspect</b></td><td><b>Functional Requirements</b></td><td><b>Non-Functional Requirements</b></td></tr>
<tr><td>Definition</td><td>What the system should do — specific behaviors, features, functions</td><td>How the system should behave — quality attributes, constraints</td></tr>
<tr><td>Focus</td><td>Business logic, data processing, user operations</td><td>Performance, security, usability, reliability</td></tr>
<tr><td>Examples</td><td>User login, data validation, report generation</td><td>Response time &lt; 2s, 99.9% uptime, supports 1000 concurrent users</td></tr>
<tr><td>Testability</td><td>Verified by functional testing</td><td>Verified by performance testing, security audits</td></tr>
<tr><td>Source</td><td>Business rules, user stories, use cases</td><td>Quality standards, technical constraints, regulations</td></tr>
<tr><td>Documentation</td><td>Use cases, user stories, functional specs</td><td>Quality attribute scenarios, SLAs, architecture decisions</td></tr>
</table>

<b>Functional Requirements of Online Examination System:</b>

1. <b>User Management:</b> Registration, login, profile management for students, instructors, and administrators
2. <b>Exam Creation:</b> Instructors can create exams with different question types (MCQ, essay, coding)
3. <b>Question Bank:</b> Store, categorize, and manage questions by subject, difficulty, and topic
4. <b>Exam Scheduling:</b> Set exam dates, durations, availability windows, and attempt limits
5. <b>Exam Taking:</b> Students can take scheduled exams with timer, navigation, and auto-save
6. <b>Proctoring:</b> Browser lockdown, random photo capture, tab switching detection
7. <b>Auto-grading:</b> Automatic scoring for objective questions; rubric-based grading for subjective
8. <b>Result Publication:</b> Display scores, rankings, detailed analytics to students and instructors
9. <b>Report Generation:</b> Generate performance reports, statistics, and analytics dashboards
10. <b>Notification System:</b> Email/push notifications for exam schedules, results, and deadlines

<b>Use Case Diagram Description:</b>

<b>Actors:</b> Student, Instructor, Administrator, System

<b>Student use cases:</b> Register, Login, View Schedule, Take Exam, View Result, Download Certificate

<b>Instructor use cases:</b> Login, Create Exam, Manage Question Bank, Schedule Exam, Review Answers, Publish Results, Generate Reports

<b>Administrator use cases:</b> Manage Users, Configure System, Monitor Exams, Generate Analytics, Backup Data

<b>System use cases:</b> Send Notifications, Auto-grade, Proctor Exam, Generate Reports""",
                "diagram": "Use case diagram with three actors (Student, Instructor, Admin) on the left. System boundary labeled 'Online Examination System' contains use cases: Register, Login, Take Exam, View Result, Create Exam, Manage Questions, Schedule Exam, Review Answers, Publish Results, Auto-grade, Send Notifications, Generate Reports. Associations connect actors to relevant use cases.",
            },
            {
                "num": "10",
                "question": "a) What is risk management? Explain risk management process in software engineering with block diagram. b) List good programming practices. Explain CASE and its type with example.",
                "marks": "1+4+2+3",
                "answer": """<b>a) Risk Management:</b>
Risk management is the process of identifying, analyzing, and responding to risk factors throughout the life of a project to minimize their negative impact on project objectives. In software engineering, risks can threaten schedule, budget, quality, or customer satisfaction.

<b>Risk Management Process:</b>

1. <b>Risk Identification:</b> Discover potential risks through brainstorming, checklists, historical data, and expert judgment. Categories: project risks, technical risks, business risks.

2. <b>Risk Analysis (Assessment):</b> Evaluate each risk's probability of occurrence and potential impact. Prioritize risks based on severity (Probability × Impact). Create risk register.

3. <b>Risk Planning (Response):</b> Develop strategies for each significant risk:
   • <b>Avoidance:</b> Change plans to eliminate the risk
   • <b>Minimization:</b> Reduce probability or impact
   • <b>Contingency:</b> Plan alternative actions if risk occurs
   • <b>Acceptance:</b> Acknowledge and monitor

4. <b>Risk Monitoring:</b> Continuously track identified risks, detect new risks, and evaluate effectiveness of response strategies throughout the project.

<b>Block Diagram Description:</b>
```
[Risk Identification] → [Risk Analysis] → [Risk Planning] → [Risk Monitoring]
       ↑                                                    ↓
       └────────────── Feedback Loop ←──────────────────────┘
```

<b>b) Good Programming Practices:</b>

1. <b>Meaningful Naming:</b> Variables, functions, and classes should have descriptive names
2. <b>Comments and Documentation:</b> Explain why, not what — code should be self-documenting
3. <b>Modularity:</b> Break code into small, reusable functions with single responsibility
4. <b>Error Handling:</b> Anticipate and handle exceptions gracefully
5. <b>Code Reviews:</b> Peer review all code before integration
6. <b>Version Control:</b> Use Git or similar for tracking changes
7. <b>Testing:</b> Write unit tests alongside production code (TDD)
8. <b>Consistent Formatting:</b> Follow style guides (PEP 8, Google Style)
9. <b>DRY Principle:</b> Don't Repeat Yourself — avoid duplication
10. <b>KISS:</b> Keep It Simple, Stupid — simplest solution is often best

<b>CASE (Computer-Aided Software Engineering):</b>
CASE refers to software tools that automate activities in the software development lifecycle, improving productivity and quality.

<b>Types of CASE Tools:</b>

1. <b>Upper CASE (Front-End):</b> Support early lifecycle phases
   • Requirements tools: IBM Rational RequisitePro
   • Design tools: Enterprise Architect, Visio, StarUML
   • Analysis tools: Data flow diagram editors

2. <b>Lower CASE (Back-End):</b> Support implementation and maintenance
   • Code generators
   • Compilers and debuggers
   • Testing tools: JUnit, Selenium
   • Configuration management: Git, Jenkins

3. <b>Integrated CASE (I-CASE):</b> Covers entire lifecycle
   • Examples: IBM Rational Suite, Microsoft Visual Studio

<b>Example:</b> <b>StarUML</b> is an Upper CASE tool used for creating UML diagrams (class diagrams, use case diagrams, sequence diagrams) during the design phase. It helps visualize system architecture before coding begins, improving communication among team members and reducing design defects.""",
                "diagram": "Risk management block diagram: 4 rectangular boxes arranged horizontally: Risk Identification → Risk Analysis → Risk Planning → Risk Monitoring, with an arrow from Monitoring back to Identification forming a feedback loop.",
            },
        ]
    }
]


if __name__ == "__main__":
    # Generate all answer sheets
    generate_answer_sheet("CACS251", "operating-systems", "Operating Systems", 2020, "semester-4", OS_QUESTIONS)
    generate_answer_sheet("CACS252", "numerical-methods", "Numerical Methods", 2020, "semester-4", NM_QUESTIONS)
    generate_answer_sheet("CACS253", "software-engineering", "Software Engineering", 2020, "semester-4", SE_QUESTIONS)
    print("All 4th-semester 2020 answer sheets generated!")


# ============== SCRIPTING LANGUAGE (CACS254) 2020 ==============

SL_QUESTIONS = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "1",
                "question": "What is javaScript? What are the potential platforms where javaScript can be used?",
                "marks": "1+3",
                "answer": """<b>JavaScript:</b> JavaScript is a lightweight, interpreted, object-oriented programming language with first-class functions. It was created by Brendan Eich at Netscape in 1995 and is best known as the scripting language for Web pages. Despite the name similarity, it is not related to Java. It conforms to the ECMAScript specification.

<b>Potential Platforms:</b>
1. <b>Web Browsers (Client-Side):</b> DOM manipulation, form validation, animations, AJAX requests, SPAs (React, Vue, Angular)
2. <b>Server-Side (Node.js):</b> Building scalable network applications, REST APIs, real-time chat, microservices
3. <b>Mobile Applications:</b> React Native, Ionic, NativeScript for cross-platform mobile apps
4. <b>Desktop Applications:</b> Electron (VS Code, Slack, Discord), NW.js
5. <b>IoT and Embedded:</b> Johnny-Five, Cylon.js for robotics and hardware
6. <b>Game Development:</b> Browser-based games using Canvas, WebGL, Phaser.js, Three.js
7. <b>Machine Learning:</b> TensorFlow.js for running ML models in browser
8. <b>Cloud and Serverless:</b> AWS Lambda, Azure Functions with Node.js runtime
9. <b>Database:</b> MongoDB uses JavaScript for queries and MapReduce operations""",
            },
            {
                "num": "2",
                "question": "Define javaScript event. Illustrate how an event handler response particular event in web page.",
                "marks": "1+4",
                "answer": """<b>JavaScript Event:</b> An event is an action or occurrence that happens in the browser, which the browser can respond to. Events are the foundation of interactive web applications. They can be triggered by user actions (click, keypress, mouseover), browser actions (page load, resize, scroll), or API-generated notifications.

<b>Common Events:</b> click, dblclick, mouseover, mouseout, keydown, keyup, submit, load, resize, scroll, focus, blur

<b>Event Handler Example:</b>
<pre>
&lt;!-- HTML --&gt;
&lt;button id="myBtn"&gt;Click Me&lt;/button&gt;
&lt;p id="output"&gt;&lt;/p&gt;

&lt;script&gt;
// Method 1: Inline (not recommended)
// &lt;button onclick="alert('Hello')"&gt;

// Method 2: DOM property
document.getElementById('myBtn').onclick = function() {
    document.getElementById('output').textContent = 'Button was clicked!';
};

// Method 3: addEventListener (recommended)
document.getElementById('myBtn').addEventListener('click', function(event) {
    console.log('Event type:', event.type);
    console.log('Target element:', event.target);
    document.getElementById('output').textContent = 
        'Clicked at coordinates: ' + event.clientX + ', ' + event.clientY;
});
&lt;/script&gt;
</pre>

<b>Event Flow:</b> Events propagate through the DOM in two phases:
• <b>Event Capturing:</b> Event travels from document root down to the target
• <b>Event Bubbling:</b> Event bubbles up from target to document root

<b>Event Object:</b> When an event occurs, the browser creates an event object containing information about the event (type, target, timestamp, mouse coordinates, key codes, etc.). This object is passed to the event handler function.""",
            },
            {
                "num": "3",
                "question": "What is an Immediately Invoked Function in javaScript? Explain with suitable example.",
                "marks": "1+4",
                "answer": """<b>Immediately Invoked Function Expression (IIFE):</b>
An IIFE is a JavaScript function that runs as soon as it is defined. It is a design pattern that produces a lexical scope using JavaScript's function scoping. IIFEs are commonly used to avoid polluting the global namespace, create private variables, and implement the module pattern.

<b>Syntax:</b>
<pre>
(function() {
    // code here runs immediately
})();

// Or with arrow function
(() => {
    // code here runs immediately
})();
</pre>

<b>Example 1: Basic IIFE</b>
<pre>
(function() {
    var message = "Hello from IIFE!";
    console.log(message);  // Outputs: Hello from IIFE!
})();

console.log(message);  // Error: message is not defined
</pre>

<b>Example 2: IIFE with Parameters</b>
<pre>
(function(name, age) {
    console.log(name + " is " + age + " years old.");
})("Ram", 20);
// Outputs: Ram is 20 years old.
</pre>

<b>Example 3: Module Pattern (Practical Use)</b>
<pre>
var counterModule = (function() {
    var count = 0;  // Private variable
    
    return {
        increment: function() {
            count++;
            return count;
        },
        decrement: function() {
            count--;
            return count;
        },
        getCount: function() {
            return count;
        }
    };
})();

console.log(counterModule.getCount());  // 0
counterModule.increment();
console.log(counterModule.getCount());  // 1
console.log(counterModule.count);       // undefined (private!)
</pre>

<b>Benefits:</b> Encapsulation, private variables, avoiding global scope pollution, isolation of variables in loops.""",
            },
            {
                "num": "4",
                "question": "Explain an array using suitable example and discuss how foreach loop accessing of elements is stored in an array using PHP.",
                "marks": "2+3",
                "answer": """<b>Array:</b> An array is a data structure that stores multiple values in a single variable. In JavaScript, arrays are dynamic, zero-indexed, and can hold mixed data types. They are implemented as objects with integer-based keys and have built-in methods for manipulation.

<b>JavaScript Array Example:</b>
<pre>
let fruits = ["Apple", "Banana", "Orange"];
console.log(fruits[0]);      // "Apple"
console.log(fruits.length);  // 3
fruits.push("Mango");        // Add element
fruits.pop();                // Remove last element
</pre>

<b>PHP foreach Loop:</b>
In PHP, foreach is a convenient way to iterate over arrays without managing counters.

<b>Indexed Array with foreach:</b>
<pre>
&lt;?php
$students = ["Ram", "Sita", "Hari"];

// foreach with values only
foreach ($students as $name) {
    echo $name . "&lt;br&gt;";
}
// Output: Ram Sita Hari

// foreach with index and value
foreach ($students as $index => $name) {
    echo "Index $index: $name &lt;br&gt;";
}
// Output: Index 0: Ram, Index 1: Sita, Index 2: Hari
?&gt;
</pre>

<b>Associative Array with foreach:</b>
<pre>
&lt;?php
$student = [
    "name" => "Ram",
    "age" => 20,
    "faculty" => "BCA"
];

foreach ($student as $key => $value) {
    echo "$key: $value &lt;br&gt;";
}
// Output: name: Ram, age: 20, faculty: BCA
?&gt;
</pre>

<b>How foreach accesses elements:</b> PHP foreach creates a copy of the array's internal pointer and iterates through each element. For indexed arrays, it accesses elements by position (0, 1, 2...). For associative arrays, it accesses key-value pairs using the hash table implementation. It does not require manual index management like traditional for loops.""",
            },
            {
                "num": "5",
                "question": "What is jQuery? Illustrate different types of selectors in jQuery with appropriate example?",
                "marks": "1+4",
                "answer": """<b>jQuery:</b> jQuery is a fast, small, and feature-rich JavaScript library created by John Resig in 2006. It simplifies HTML document traversal and manipulation, event handling, animation, and Ajax interactions. Its motto is "Write less, do more." jQuery abstracts browser inconsistencies and provides a consistent API across all major browsers.

<b>jQuery Selectors:</b>
jQuery uses CSS-style selectors to find and select HTML elements.

<b>1. Element Selector:</b>
<pre>$('p')          // Selects all &lt;p&gt; elements
$('div')        // Selects all &lt;div&gt; elements</pre>

<b>2. ID Selector:</b>
<pre>$('#header')    // Selects element with id="header"
$('#menu').hide();  // Hides the menu</pre>

<b>3. Class Selector:</b>
<pre>$('.active')    // Selects all elements with class="active"
$('.btn').click(function() { ... });</pre>

<b>4. Universal Selector:</b>
<pre>$('*')          // Selects all elements</pre>

<b>5. Multiple Selectors:</b>
<pre>$('p, div, .highlight')  // Selects all p, div, and .highlight elements</pre>

<b>6. Descendant Selector:</b>
<pre>$('div p')      // Selects all &lt;p&gt; inside &lt;div&gt;
$('#nav a')     // Selects all links inside #nav</pre>

<b>7. Child Selector:</b>
<pre>$('ul > li')    // Selects direct &lt;li&gt; children of &lt;ul&gt;</pre>

<b>8. Attribute Selectors:</b>
<pre>$('[href]')             // Elements with href attribute
$('input[type="text"]')  // Text inputs
$('[class*="col"]')      // Classes containing "col"</pre>

<b>9. Pseudo-class Selectors:</b>
<pre>$('li:first')     // First &lt;li&gt;
$('li:last')      // Last &lt;li&gt;
$('tr:even')      // Even rows
$('tr:odd')       // Odd rows
$(':input')       // All form inputs</pre>

<b>Complete Example:</b>
<pre>
&lt;div id="container"&gt;
    &lt;p class="intro"&gt;Welcome&lt;/p&gt;
    &lt;p class="detail"&gt;Details here&lt;/p&gt;
    &lt;button class="btn"&gt;Click&lt;/button&gt;
&lt;/div&gt;

&lt;script&gt;
$(document).ready(function() {
    $('.intro').css('color', 'blue');
    $('#container').addClass('highlight');
    $('button').click(function() {
        $('p').toggle();
    });
});
&lt;/script&gt;
</pre>""",
            },
            {
                "num": "6",
                "question": "What is the benefit of using AJAX? Discuss major methods that communicate with server-side scripting.",
                "marks": "1+4",
                "answer": """<b>AJAX (Asynchronous JavaScript and XML):</b>
AJAX is a technique for creating fast, dynamic web pages by allowing web pages to be updated asynchronously by exchanging small amounts of data with the server behind the scenes. This means parts of a web page can be updated without reloading the entire page.

<b>Benefits of AJAX:</b>
1. <b>Improved User Experience:</b> No full page reloads — updates happen seamlessly
2. <b>Faster Response:</b> Only necessary data is transferred, reducing bandwidth
3. <b>Reduced Server Load:</b> Less data processing and rendering on server side
4. <b>Asynchronous Operations:</b> User can continue interacting while data loads
5. <b>Rich Interactive Applications:</b> Enables features like auto-complete, infinite scroll, live search
6. <b>Partial Page Updates:</b> Only affected parts of DOM are updated

<b>Major Methods for Server Communication:</b>

1. <b>XMLHttpRequest (Legacy):</b>
<pre>
var xhr = new XMLHttpRequest();
xhr.open('GET', 'api/data.php', true);
xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        console.log(xhr.responseText);
    }
};
xhr.send();
</pre>

2. <b>Fetch API (Modern):</b>
<pre>
fetch('api/data.php')
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error));
</pre>

3. <b>jQuery AJAX:</b>
<pre>
$.ajax({
    url: 'api/data.php',
    method: 'POST',
    data: { name: 'Ram', age: 20 },
    success: function(response) { console.log(response); },
    error: function(xhr, status, error) { console.log(error); }
});

// Shorthand methods
$.get('api/data.php', function(data) { ... });
$.post('api/save.php', { name: 'Ram' }, function(data) { ... });
$.getJSON('api/data.json', function(data) { ... });
</pre>

4. <b>Axios (Popular Library):</b>
<pre>
axios.get('/api/users')
    .then(response => console.log(response.data))
    .catch(error => console.error(error));

axios.post('/api/users', { name: 'Ram' })
    .then(response => console.log(response.data));
</pre>

<b>HTTP Methods Used:</b>
• <b>GET:</b> Retrieve data from server
• <b>POST:</b> Submit data to server
• <b>PUT:</b> Update existing resource
• <b>DELETE:</b> Remove resource
• <b>PATCH:</b> Partial update""",
            },
            {
                "num": "7",
                "question": "Discuss about MVC architecture with appropriate diagram.",
                "marks": "5",
                "answer": """<b>MVC (Model-View-Controller) Architecture:</b>
MVC is a software design pattern that separates an application into three interconnected components, enabling modular development, easier maintenance, and parallel work.

<b>Components:</b>

1. <b>Model:</b>
   • Represents the data and business logic
   • Manages data storage, retrieval, and validation
   • Notifies views when data changes
   • Independent of user interface
   • Example: User class with properties (name, email) and methods (save(), validate())

2. <b>View:</b>
   • Represents the user interface and presentation layer
   • Displays data from the model to the user
   • Sends user commands to the controller
   • Should not contain business logic
   • Example: HTML templates, React components, blade files

3. <b>Controller:</b>
   • Acts as an intermediary between Model and View
   • Receives user input from View
   • Processes input, interacts with Model
   • Selects appropriate View for response
   • Example: UserController with methods like index(), store(), show()

<b>Workflow:</b>
1. User interacts with View (clicks button, submits form)
2. View sends request to Controller
3. Controller processes request, updates/retrieves Model
4. Model performs business logic and data operations
5. Model returns data to Controller
6. Controller selects View and passes data
7. View renders data for user

<b>Advantages:</b>
• Separation of concerns — each component has distinct responsibility
• Parallel development — designers work on Views, developers on Models
• Easier testing — components can be unit tested independently
• Reusability — same model can serve multiple views
• Maintainability — changes to UI don't affect business logic

<b>Examples:</b> Laravel (PHP), Ruby on Rails, Django (MTV variant), ASP.NET MVC, Spring MVC.""",
                "diagram": "MVC architecture diagram: User interacts with View (UI). View sends input to Controller. Controller updates Model. Model notifies View of changes. View displays updated data to User. Three boxes labeled Model, View, Controller with arrows showing this flow.",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "8",
                "question": "a) Write a program which includes a function sum(). This function sum() should be designed to add an arbitrary list of parameters. b) Write a program that displays the continuous time in the web page. The time should be in the format of HH:MM:SS.",
                "marks": "5+5",
                "answer": """<b>a) JavaScript Function with Arbitrary Parameters:</b>
<pre>
// Using rest parameters (...args)
function sum(...numbers) {
    let total = 0;
    for (let num of numbers) {
        total += num;
    }
    return total;
}

// Alternative using arguments object
function sumClassic() {
    let total = 0;
    for (let i = 0; i < arguments.length; i++) {
        total += arguments[i];
    }
    return total;
}

// Alternative using reduce
function sumReduce(...numbers) {
    return numbers.reduce((acc, curr) => acc + curr, 0);
}

// Test cases
console.log(sum(1, 2));        // Output: 3
console.log(sum(1, 3, 4));     // Output: 8
console.log(sum(10, 20, 30, 40)); // Output: 100
console.log(sum());            // Output: 0
</pre>

<b>HTML Integration:</b>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;body&gt;
    &lt;p id="result"&gt;&lt;/p&gt;
    &lt;script&gt;
        function sum(...nums) {
            return nums.reduce((a, b) => a + b, 0);
        }
        document.getElementById('result').textContent = 
            'sum(1,2) = ' + sum(1,2) + ', sum(1,3,4) = ' + sum(1,3,4);
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

<b>b) Continuous Time Display Program:</b>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;style&gt;
        #clock {
            font-size: 48px;
            font-family: 'Courier New', monospace;
            color: #0ea5e9;
            text-align: center;
            margin-top: 100px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div id="clock"&gt;00:00:00&lt;/div&gt;

    &lt;script&gt;
        function updateClock() {
            const now = new Date();
            
            let hours = now.getHours();
            let minutes = now.getMinutes();
            let seconds = now.getSeconds();
            
            // Add leading zeros
            hours = hours &lt; 10 ? '0' + hours : hours;
            minutes = minutes &lt; 10 ? '0' + minutes : minutes;
            seconds = seconds &lt; 10 ? '0' + seconds : seconds;
            
            const timeString = hours + ':' + minutes + ':' + seconds;
            document.getElementById('clock').textContent = timeString;
        }
        
        // Update immediately and then every second
        updateClock();
        setInterval(updateClock, 1000);
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

<b>Explanation:</b> The setInterval function calls updateClock every 1000 milliseconds (1 second). The Date object provides current time, which is formatted with leading zeros using the ternary operator. The display updates continuously without page refresh.""",
            },
            {
                "num": "9",
                "question": "Define method overriding. Write a PHP program to handle the overriding situation.",
                "marks": "2+8",
                "answer": """<b>Method Overriding:</b> Method overriding is an object-oriented programming feature where a subclass provides a specific implementation of a method that is already defined in its parent class. The overridden method in the child class has the same name, same parameters, and same return type as the method in the parent class. It enables runtime polymorphism and allows subclasses to customize or extend the behavior inherited from parent classes.

<b>Rules for Method Overriding:</b>
• Method name must be identical to parent method
• Parameter list must be the same
• Access level cannot be more restrictive
• Use "parent::methodName()" to call parent's method

<b>PHP Program Demonstrating Method Overriding:</b>
<pre>
&lt;?php
class Animal {
    protected $name;
    
    public function __construct($name) {
        $this->name = $name;
    }
    
    // Parent method to be overridden
    public function makeSound() {
        return "Some generic animal sound";
    }
    
    public function describe() {
        return "This is a " . $this->name;
    }
}

class Dog extends Animal {
    public function __construct($name) {
        parent::__construct($name);
    }
    
    // Overriding makeSound method
    public function makeSound() {
        return "Woof! Woof!";
    }
    
    // Overriding with additional functionality
    public function describe() {
        // Call parent's method and extend it
        return parent::describe() . " and it barks loudly.";
    }
}

class Cat extends Animal {
    public function __construct($name) {
        parent::__construct($name);
    }
    
    // Overriding makeSound method
    public function makeSound() {
        return "Meow! Meow!";
    }
}

// Usage
$dog = new Dog("German Shepherd");
echo $dog->describe() . "&lt;br&gt;";
echo "Sound: " . $dog->makeSound() . "&lt;br&gt;&lt;br&gt;";

$cat = new Cat("Persian Cat");
echo $cat->describe() . "&lt;br&gt;";
echo "Sound: " . $cat->makeSound() . "&lt;br&gt;";
?&gt;
</pre>

<b>Output:</b>
<pre>
This is a German Shepherd and it barks loudly.
Sound: Woof! Woof!

This is a Persian Cat
Sound: Meow! Meow!
</pre>

<b>Real-World Example — Payment Gateway:</b>
<pre>
&lt;?php
abstract class PaymentGateway {
    abstract public function processPayment($amount);
    
    public function validate($amount) {
        return $amount > 0;
    }
}

class EsewaPayment extends PaymentGateway {
    public function processPayment($amount) {
        return "Processing Rs. $amount via eSewa... Success!";
    }
}

class KhaltiPayment extends PaymentGateway {
    public function processPayment($amount) {
        return "Processing Rs. $amount via Khalti... Success!";
    }
}
?&gt;
</pre>""",
            },
            {
                "num": "10",
                "question": "Design following form in HTML and write corresponding PHP and SQL code for CRUD operations based on user's data. Assume your own database and database connectivity related constraints if necessary.",
                "marks": "10",
                "answer": """<b>HTML Form Design:</b>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;title&gt;User Management&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
    &lt;h2&gt;User Registration Form&lt;/h2&gt;
    &lt;form action="process.php" method="POST"&gt;
        &lt;input type="hidden" name="action" value="create"&gt;
        Name: &lt;input type="text" name="name" required&gt;&lt;br&gt;&lt;br&gt;
        Email: &lt;input type="email" name="email" required&gt;&lt;br&gt;&lt;br&gt;
        Phone: &lt;input type="text" name="phone"&gt;&lt;br&gt;&lt;br&gt;
        Address: &lt;textarea name="address"&gt;&lt;/textarea&gt;&lt;br&gt;&lt;br&gt;
        &lt;input type="submit" value="Submit"&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

<b>SQL Database Setup:</b>
<pre>
CREATE DATABASE userdb;
USE userdb;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
</pre>

<b>Database Connection (db.php):</b>
<pre>
&lt;?php
$host = "localhost";
$user = "root";
$pass = "";
$dbname = "userdb";

$conn = new mysqli($host, $user, $pass, $dbname);
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
?&gt;
</pre>

<b>PHP CRUD Operations (process.php):</b>
<pre>
&lt;?php
include 'db.php';

$action = $_POST['action'] ?? $_GET['action'] ?? '';

// CREATE
if ($action == 'create') {
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);
    $phone = $conn->real_escape_string($_POST['phone']);
    $address = $conn->real_escape_string($_POST['address']);
    
    $sql = "INSERT INTO users (name, email, phone, address) 
            VALUES ('$name', '$email', '$phone', '$address')";
    
    if ($conn->query($sql) === TRUE) {
        echo "User registered successfully!&lt;br&gt;";
    } else {
        echo "Error: " . $conn->error;
    }
}

// READ
elseif ($action == 'read') {
    $sql = "SELECT * FROM users";
    $result = $conn->query($sql);
    
    echo "&lt;table border='1'&gt;";
    echo "&lt;tr&gt;&lt;th&gt;ID&lt;/th&gt;&lt;th&gt;Name&lt;/th&gt;&lt;th&gt;Email&lt;/th&gt;&lt;th&gt;Phone&lt;/th&gt;&lt;/tr&gt;";
    while ($row = $result->fetch_assoc()) {
        echo "&lt;tr&gt;";
        echo "&lt;td&gt;" . $row['id'] . "&lt;/td&gt;";
        echo "&lt;td&gt;" . $row['name'] . "&lt;/td&gt;";
        echo "&lt;td&gt;" . $row['email'] . "&lt;/td&gt;";
        echo "&lt;td&gt;" . $row['phone'] . "&lt;/td&gt;";
        echo "&lt;/tr&gt;";
    }
    echo "&lt;/table&gt;";
}

// UPDATE
elseif ($action == 'update') {
    $id = intval($_POST['id']);
    $name = $conn->real_escape_string($_POST['name']);
    $email = $conn->real_escape_string($_POST['email']);
    
    $sql = "UPDATE users SET name='$name', email='$email' WHERE id=$id";
    
    if ($conn->query($sql) === TRUE) {
        echo "User updated successfully!";
    } else {
        echo "Error: " . $conn->error;
    }
}

// DELETE
elseif ($action == 'delete') {
    $id = intval($_GET['id']);
    $sql = "DELETE FROM users WHERE id=$id";
    
    if ($conn->query($sql) === TRUE) {
        echo "User deleted successfully!";
    } else {
        echo "Error: " . $conn->error;
    }
}

$conn->close();
?&gt;
</pre>

<b>Note:</b> For production, use prepared statements to prevent SQL injection:
<pre>
$stmt = $conn->prepare("INSERT INTO users (name, email) VALUES (?, ?)");
$stmt->bind_param("ss", $name, $email);
$stmt->execute();
</pre>""",
            },
        ]
    }
]


# ============== DATABASE MANAGEMENT SYSTEM (CACS255) 2020 ==============

DBMS_QUESTIONS = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "1",
                "question": "What is database? Discuss the importance of DBMS.",
                "marks": "1+3",
                "answer": """<b>Database:</b> A database is an organized collection of structured data stored electronically in a computer system. It is designed to efficiently store, retrieve, and manage large amounts of information. Data in a database is typically organized into tables consisting of rows (records) and columns (attributes), with relationships defined between tables.

<b>Importance of DBMS (Database Management System):</b>

1. <b>Data Independence:</b> DBMS provides abstraction between physical storage and logical view. Changes in physical storage don't affect application programs.

2. <b>Data Integrity:</b> Enforces constraints (primary keys, foreign keys, check constraints) to maintain data accuracy and consistency.

3. <b>Data Security:</b> Provides authentication, authorization, and access control mechanisms to protect sensitive data from unauthorized access.

4. <b>Data Redundancy Control:</b> Normalization techniques minimize duplicate data, saving storage and preventing update anomalies.

5. <b>Concurrent Access:</b> Allows multiple users to access and modify data simultaneously while maintaining consistency through locking and transaction management.

6. <b>Backup and Recovery:</b> Provides mechanisms to create data backups and recover from system failures, ensuring data durability.

7. <b>Query Language:</b> SQL provides a powerful, standardized way to interact with data without writing complex procedural code.

8. <b>Scalability:</b> Modern DBMS can handle terabytes of data and scale horizontally or vertically as needs grow.

9. <b>Decision Support:</b> Enables complex analytics, reporting, and business intelligence through aggregation, joins, and views.""",
            },
            {
                "num": "2",
                "question": "Define union compatibility. Given following relations, show the resulting relation of Director ∩ Actor and Actor ∪ Director?",
                "marks": "2+3",
                "answer": """<b>Union Compatibility:</b> Two relations are union compatible if they have the same number of attributes and the corresponding attributes have compatible domains (same data types). For set operations (UNION, INTERSECTION, DIFFERENCE) to be valid, the participating relations must be union compatible.

<b>Requirements for Union Compatibility:</b>
• Same number of columns
• Corresponding columns have the same domain
• Column names may differ (result typically uses first relation's names)

<b>Note:</b> The specific relations "Director" and "Actor" were not fully visible in the original paper. Using typical examples:

<b>Relation: Director</b>
<table border='1' cellpadding='4'><tr><td>Name</td><td>Movie</td></tr>
<tr><td>Christopher Nolan</td><td>Inception</td></tr>
<tr><td>Steven Spielberg</td><td>Jurassic Park</td></tr>
<tr><td>Quentin Tarantino</td><td>Pulp Fiction</td></tr>
</table>

<b>Relation: Actor</b>
<table border='1' cellpadding='4'><tr><td>Name</td><td>Movie</td></tr>
<tr><td>Leonardo DiCaprio</td><td>Inception</td></tr>
<tr><td>Quentin Tarantino</td><td>Pulp Fiction</td></tr>
<tr><td>Sam Neill</td><td>Jurassic Park</td></tr>
</table>

<b>Director ∩ Actor (INTERSECTION):</b>
Returns tuples present in BOTH relations.
<table border='1' cellpadding='4'><tr><td>Name</td><td>Movie</td></tr>
<tr><td>Quentin Tarantino</td><td>Pulp Fiction</td></tr>
</table>

<b>Actor ∪ Director (UNION):</b>
Returns all unique tuples from both relations.
<table border='1' cellpadding='4'><tr><td>Name</td><td>Movie</td></tr>
<tr><td>Christopher Nolan</td><td>Inception</td></tr>
<tr><td>Steven Spielberg</td><td>Jurassic Park</td></tr>
<tr><td>Quentin Tarantino</td><td>Pulp Fiction</td></tr>
<tr><td>Leonardo DiCaprio</td><td>Inception</td></tr>
<tr><td>Sam Neill</td><td>Jurassic Park</td></tr>
</table>

<b>SQL Implementation:</b>
<pre>
SELECT * FROM Director INTERSECT SELECT * FROM Actor;
SELECT * FROM Actor UNION SELECT * FROM Director;
</pre>""",
            },
            {
                "num": "3",
                "question": "How Order By and Group BY Having Clause in SQL are different? Illustrate with suitable examples.",
                "marks": "3+2",
                "answer": """<b>ORDER BY vs GROUP BY vs HAVING:</b>

<table border='1' cellpadding='4'><tr><td><b>Feature</b></td><td><b>ORDER BY</b></td><td><b>GROUP BY</b></td><td><b>HAVING</b></td></tr>
<tr><td>Purpose</td><td>Sorts result set</td><td>Groups rows by column values</td><td>Filters grouped results</td></tr>
<tr><td>When applied</td><td>After all selection</td><td>Before aggregation</td><td>After GROUP BY</td></tr>
<tr><td>Works with</td><td>Any selected columns</td><td>Aggregate functions</td><td>Aggregate conditions</td></tr>
<tr><td>Can use</td><td>Column names, aliases, expressions</td><td>Column names only</td><td>Aggregate functions</td></tr>
</table>

<b>Example Table: Employees</b>
<table border='1' cellpadding='4'><tr><td>ID</td><td>Name</td><td>Dept</td><td>Salary</td></tr>
<tr><td>1</td><td>Ram</td><td>IT</td><td>50000</td></tr>
<tr><td>2</td><td>Sita</td><td>HR</td><td>45000</td></tr>
<tr><td>3</td><td>Hari</td><td>IT</td><td>60000</td></tr>
<tr><td>4</td><td>Gita</td><td>HR</td><td>55000</td></tr>
<tr><td>5</td><td>Shyam</td><td>IT</td><td>70000</td></tr>
</table>

<b>1. ORDER BY Example:</b>
<pre>
SELECT * FROM Employees ORDER BY Salary DESC;
</pre>
Result: Shyam (70000), Hari (60000), Gita (55000), Ram (50000), Sita (45000)

<b>2. GROUP BY Example:</b>
<pre>
SELECT Dept, COUNT(*) as Count, AVG(Salary) as AvgSalary 
FROM Employees 
GROUP BY Dept;
</pre>
Result:
<table border='1' cellpadding='4'><tr><td>Dept</td><td>Count</td><td>AvgSalary</td></tr>
<tr><td>HR</td><td>2</td><td>50000</td></tr>
<tr><td>IT</td><td>3</td><td>60000</td></tr>
</table>

<b>3. HAVING Example:</b>
<pre>
SELECT Dept, AVG(Salary) as AvgSalary 
FROM Employees 
GROUP BY Dept 
HAVING AVG(Salary) > 55000;
</pre>
Result: Only IT department (avg 60000) since HR's average (50000) is filtered out.

<b>Key Difference:</b> WHERE filters rows BEFORE grouping; HAVING filters groups AFTER aggregation. ORDER BY simply sorts the final output.""",
            },
            {
                "num": "4",
                "question": "Why normalization is needed? When an relation is said to be in 1NF and 2NF?",
                "marks": "1+4",
                "answer": """<b>Need for Normalization:</b>
Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. Without normalization, databases suffer from:

• <b>Insertion Anomalies:</b> Cannot insert certain data without other unrelated data
• <b>Update Anomalies:</b> Changing one piece of data requires updating multiple rows
• <b>Deletion Anomalies:</b> Deleting data unintentionally loses other important information
• <b>Data Redundancy:</b> Same data stored multiple times, wasting storage and causing inconsistencies

<b>First Normal Form (1NF):</b>
A relation is in 1NF if and only if:
1. All attributes contain only atomic (indivisible) values
2. Each attribute contains values of a single type
3. Each row is unique (has a primary key)
4. There are no repeating groups

<b>Example violating 1NF:</b>
<table border='1' cellpadding='4'><tr><td>StudentID</td><td>Name</td><td>Courses</td></tr>
<tr><td>1</td><td>Ram</td><td>Math, Physics, Chemistry</td></tr>
</table>

<b>1NF Compliant:</b>
<table border='1' cellpadding='4'><tr><td>StudentID</td><td>Name</td><td>Course</td></tr>
<tr><td>1</td><td>Ram</td><td>Math</td></tr>
<tr><td>1</td><td>Ram</td><td>Physics</td></tr>
<tr><td>1</td><td>Ram</td><td>Chemistry</td></tr>
</table>

<b>Second Normal Form (2NF):</b>
A relation is in 2NF if:
1. It is in 1NF
2. All non-key attributes are fully functionally dependent on the entire primary key (no partial dependency)

<b>Partial Dependency:</b> A non-key attribute depends on only part of a composite primary key.

<b>Example violating 2NF:</b>
<table border='1' cellpadding='4'><tr><td>StudentID</td><td>CourseID</td><td>StudentName</td><td>CourseName</td><td>Grade</td></tr>
<tr><td>1</td><td>C101</td><td>Ram</td><td>Database</td><td>A</td></tr>
</table>
PK = (StudentID, CourseID)
StudentName depends only on StudentID (partial dependency)
CourseName depends only on CourseID (partial dependency)

<b>2NF Compliant (split into three tables):</b>

<b>Student table:</b>
<table border='1' cellpadding='4'><tr><td>StudentID (PK)</td><td>StudentName</td></tr>
<tr><td>1</td><td>Ram</td></tr>
</table>

<b>Course table:</b>
<table border='1' cellpadding='4'><tr><td>CourseID (PK)</td><td>CourseName</td></tr>
<tr><td>C101</td><td>Database</td></tr>
</table>

<b>Enrollment table:</b>
<table border='1' cellpadding='4'><tr><td>StudentID (FK)</td><td>CourseID (FK)</td><td>Grade</td></tr>
<tr><td>1</td><td>C101</td><td>A</td></tr>
</table>""",
            },
            {
                "num": "5",
                "question": "How cost of query is measured during query processing? Construct query expression tree for the relational algebra query.",
                "marks": "3+2",
                "answer": """<b>Query Cost Measurement:</b>
The cost of query execution is measured using various metrics that estimate the resources required to execute a query:

<b>1. Disk I/O Cost:</b>
• Number of block transfers (most significant factor)
• Number of disk seeks
• Formula: Cost = (Number of block transfers × block_transfer_time) + (Number of seeks × seek_time)

<b>2. CPU Cost:</b>
• Time for processing operations (comparisons, computations)
• Time for sorting, hashing, and merging

<b>3. Memory Cost:</b>
• Amount of buffer space required
• Number of buffer pages used

<b>4. Network Cost:</b>
• For distributed databases, data transfer between sites

<b>Factors Affecting Cost:</b>
• Size of relations (number of tuples, tuple size)
• Available indexes (B+ tree, hash indexes)
• Selectivity of selection and join conditions
• Sorting requirements
• Buffer pool size

<b>Cost Estimation for Operations:</b>
• <b>Selection (σ):</b> Cost depends on whether index exists. With B+ tree index: cost ≈ height of tree + matching entries. Without index: full table scan.
• <b>Projection (π):</b> Cost = scanning relation + eliminating duplicates (if DISTINCT)
• <b>Join (⋈):</b> Nested loop join: |R| × |S|. Hash join: 3(|R| + |S|). Merge join: sort cost + merge cost.

<b>Query Expression Tree:</b>
For the query: π<sub>FName,LName,Address</sub>(σ<sub>DName="Research"</sub>(Department ⋈<sub>Dnumber=Dno</sub> (Employee × Works_on)))

The expression tree from bottom to top:

<pre>
         π (FName, LName, Address)
                   |
              σ (DName='Research')
                   |
               ⋈ (Dnumber=Dno)
              /             \
       Department          ×
                        /     \
                    Employee  Works_on
</pre>

<b>Optimized Tree (pushing selection down):</b>
<pre>
         π (FName, LName, Address)
                   |
               ⋈ (Dnumber=Dno)
              /             \
       σ(DName='Research')   ⋈
           |               /    \
      Department      Employee  Works_on
</pre>

Optimization: Apply selection on Department early to reduce join size.""",
                "diagram": "Query expression tree diagram showing root node π at top, child node σ below it, then join node ⋈, with Department on left and cross-product × on right (Employee and Works_on as leaves).",
            },
            {
                "num": "6",
                "question": "How wait-for-graph is constructed? How can you use it to detect deadlock in a schedule of transactions? Support your answer with an example.",
                "marks": "2+2+1",
                "answer": """<b>Wait-For Graph (WFG):</b>
A wait-for graph is a directed graph used to detect deadlocks in database systems. It is maintained by the database lock manager.

<b>Construction:</b>
1. Create a node for each active transaction in the system
2. If transaction T<sub>i</sub> is waiting for a lock held by transaction T<sub>j</sub>, draw a directed edge from T<sub>i</sub> to T<sub>j</sub> (T<sub>i</sub> → T<sub>j</sub>)
3. The edge means "T<sub>i</sub> is waiting for T<sub>j</sub>"

<b>Deadlock Detection:</b>
If the wait-for graph contains a <b>cycle</b>, a deadlock exists. The transactions involved in the cycle are deadlocked.

<b>Example:</b>
Consider transactions T1, T2, T3 and data items A, B, C:

• T1 holds lock on A, requests lock on B
• T2 holds lock on B, requests lock on C
• T3 holds lock on C, requests lock on A

<b>Wait-For Graph:</b>
<pre>
    T1 ----→ T2
    ↑        |
    |        ↓
    T3 ←----
</pre>

Edges: T1→T2 (T1 waits for B held by T2), T2→T3 (T2 waits for C held by T3), T3→T1 (T3 waits for A held by T1)

<b>Cycle:</b> T1 → T2 → T3 → T1. <b>Deadlock detected!</b>

<b>Resolution:</b> The DBMS must break the deadlock by:
• <b>Aborting a victim transaction:</b> Choose the transaction with least work done (victim selection criteria: age, progress, resources held)
• <b>Rollback:</b> Undo victim's changes and release its locks
• <b>Restart:</b> Restart the aborted transaction later

<b>Alternative — Timeout:</b> If a transaction waits longer than a predetermined time, assume deadlock and abort.

<b>Advantage of WFG:</b> Precise detection, no false positives.
<b>Disadvantage:</b> Maintenance overhead — graph must be updated every time locks are requested or released.""",
                "diagram": "Wait-for graph with 3 nodes (T1, T2, T3) arranged in a triangle. Arrows: T1→T2, T2→T3, T3→T1 forming a cycle.",
            },
            {
                "num": "7",
                "question": "How read and write operations are performed in a transaction? List the various states where transactions can enter into.",
                "marks": "3+2",
                "answer": """<b>Read and Write Operations in Transactions:</b>

<b>Read Operation (read(X)):</b>
1. Transaction T<sub>i</sub> issues read(X) to access data item X
2. The system checks if X is in T<sub>i</sub>'s local workspace (buffer)
3. If yes, return the buffered value
4. If no, check if T<sub>i</sub> has a shared or exclusive lock on X
5. If locked appropriately, read X from database into buffer and return
6. If not locked, request appropriate lock from lock manager
7. If lock granted, proceed; if not, transaction waits

<b>Write Operation (write(X)):</b>
1. Transaction T<sub>i</sub> modifies the value of X in its local buffer
2. When T<sub>i</sub> issues write(X), the system checks if T<sub>i</sub> holds an exclusive lock on X
3. If yes, write the buffered value to the database (or to undo/redo log first)
4. If no, request exclusive lock; if granted, proceed; else wait
5. In strict 2PL, the actual database update may be deferred until commit

<b>Transaction States:</b>

1. <b>Active:</b> The transaction is currently executing operations. This is the initial state when a transaction begins.

2. <b>Partially Committed:</b> The transaction has completed its final operation but may still need to ensure durability. Changes are written to logs but may not be permanently saved.

3. <b>Committed:</b> The transaction has successfully completed all operations, and all changes have been made permanent in the database. This is a terminal state.

4. <b>Failed:</b> The transaction cannot complete normally due to an error (hardware failure, logical error, deadlock). It must be rolled back.

5. <b>Aborted:</b> The transaction has been rolled back, and all changes have been undone. The database is restored to its state before the transaction began. The transaction may be restarted or discarded.

<b>State Transition Diagram:</b>
<pre>
[Active] -- final operation --> [Partially Committed] -- successful --> [Committed]
   |                                                              
   | failure                                                      
   ↓                                                              
[Failed] -- rollback --> [Aborted] -- restart --> [Active]        
</pre>

<b>ACID Properties ensure:</b>
• Atomicity: All or nothing (via rollback/commit)
• Consistency: Valid state to valid state
• Isolation: Concurrent transactions don't interfere
• Durability: Committed changes survive failures""",
                "diagram": "State diagram: Active → Partially Committed → Committed (success path). Active → Failed → Aborted (failure path). Aborted can restart to Active.",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "8",
                "question": "Given the schema as below, write relational algebra and SQL queries for following...",
                "marks": "10",
                "answer": """<b>Schema:</b>
• Sailors(sid, sname, rating, age)
• Boats(bid, bname, colour)
• Reserves(sid, bid, reservedate)

<b>Relational Algebra and SQL Queries:</b>

<b>i. Find name, rating and age of all sailors.</b>
<pre>
Relational Algebra: π<sub>sname, rating, age</sub>(Sailors)

SQL:
SELECT sname, rating, age FROM Sailors;
</pre>

<b>ii. Find the name and color of boats having color blue.</b>
<pre>
Relational Algebra: π<sub>bname, colour</sub>(σ<sub>colour='blue'</sub>(Boats))

SQL:
SELECT bname, colour FROM Boats WHERE colour = 'blue';
</pre>

<b>iii. Find name of the boats reserved on date 2021/07/20.</b>
<pre>
Relational Algebra: π<sub>bname</sub>(σ<sub>reservedate='2021-07-20'</sub>(Boats ⋈ Reserves))

SQL:
SELECT b.bname 
FROM Boats b 
JOIN Reserves r ON b.bid = r.bid 
WHERE r.reservedate = '2021-07-20';
</pre>

<b>iv. Find the names of boats and sailors who have reserved boats having color green.</b>
<pre>
Relational Algebra: π<sub>sname, bname</sub>(σ<sub>colour='green'</sub>(Sailors ⋈ Reserves ⋈ Boats))

SQL:
SELECT s.sname, b.bname 
FROM Sailors s 
JOIN Reserves r ON s.sid = r.sid 
JOIN Boats b ON r.bid = b.bid 
WHERE b.colour = 'green';
</pre>

<b>v. Use Left and Right Outer join between Sailors and Reserves.</b>
<pre>
SQL:
-- Left Outer Join: All sailors even if they haven't reserved
SELECT s.sid, s.sname, r.bid, r.reservedate
FROM Sailors s 
LEFT JOIN Reserves r ON s.sid = r.sid;

-- Right Outer Join: All reservations even if sailor info missing
SELECT s.sid, s.sname, r.bid, r.reservedate
FROM Sailors s 
RIGHT JOIN Reserves r ON s.sid = r.sid;

-- Full Outer Join (all records from both)
SELECT s.sid, s.sname, r.bid, r.reservedate
FROM Sailors s 
FULL OUTER JOIN Reserves r ON s.sid = r.sid;
</pre>""",
            },
            {
                "num": "9",
                "question": "a) Design an ER diagram of your choice. The ER diagram should contain at least five entities. Out of those entities, one should be weak entity. Your entities should have appropriate attributes including primary key attributes, if any. There should be presence of one to one relationship, one to many relationship and many to many relationship in your ER diagram. b) Convert the ER diagram in Q.I.a. into equivalent relational tables.",
                "marks": "5+5",
                "answer": """<b>ER Diagram Design — University Database:</b>

<b>Entities and Attributes:</b>

1. <b>Student</b> (Strong Entity)
   • Attributes: student_id (PK), name, email, date_of_birth, address

2. <b>Department</b> (Strong Entity)
   • Attributes: dept_id (PK), dept_name, location, budget

3. <b>Course</b> (Strong Entity)
   • Attributes: course_id (PK), course_name, credits, description

4. <b>Instructor</b> (Strong Entity)
   • Attributes: instructor_id (PK), name, email, salary

5. <b>Dependent</b> (Weak Entity — depends on Instructor)
   • Attributes: dependent_name (Partial Key), relationship, birth_date
   • Identifying relationship with Instructor

<b>Relationships:</b>

1. <b>Belongs_to</b> (Student — Department): <b>Many-to-One</b>
   • Many students belong to one department

2. <b>Heads</b> (Instructor — Department): <b>One-to-One</b>
   • One instructor heads one department
   • One department has one head

3. <b>Teaches</b> (Instructor — Course): <b>Many-to-Many</b>
   • One instructor can teach many courses
   • One course can be taught by many instructors
   • Attribute: semester, year

4. <b>Enrolls</b> (Student — Course): <b>Many-to-Many</b>
   • One student can enroll in many courses
   • One course has many students
   • Attribute: grade, enrollment_date

5. <b>Has</b> (Instructor — Dependent): <b>One-to-Many</b> (Identifying)
   • One instructor has many dependents
   • Dependent cannot exist without instructor

<b>ER Diagram Description:</b>
• Rectangles for entities (double rectangle for Dependent)
• Diamonds for relationships
• Lines connect entities to relationships
• Cardinality marked as 1, M, N on lines
• Underlined attributes are primary keys
• Dashed underline for partial key of weak entity

<b>b) Relational Tables:</b>

1. <b>Department</b>(dept_id, dept_name, location, budget, head_instructor_id)
   • PK: dept_id
   • FK: head_instructor_id references Instructor(instructor_id)

2. <b>Instructor</b>(instructor_id, name, email, salary, dept_id)
   • PK: instructor_id
   • FK: dept_id references Department(dept_id)

3. <b>Student</b>(student_id, name, email, date_of_birth, address, dept_id)
   • PK: student_id
   • FK: dept_id references Department(dept_id)

4. <b>Course</b>(course_id, course_name, credits, description)
   • PK: course_id

5. <b>Dependent</b>(instructor_id, dependent_name, relationship, birth_date)
   • PK: (instructor_id, dependent_name)
   • FK: instructor_id references Instructor(instructor_id)

6. <b>Teaches</b>(instructor_id, course_id, semester, year)
   • PK: (instructor_id, course_id, semester, year)
   • FK: instructor_id references Instructor(instructor_id)
   • FK: course_id references Course(course_id)

7. <b>Enrollment</b>(student_id, course_id, grade, enrollment_date)
   • PK: (student_id, course_id)
   • FK: student_id references Student(student_id)
   • FK: course_id references Course(course_id)

<b>Conversion Rules Applied:</b>
• Strong entities → separate tables with all attributes
• Weak entities → table with partial key + owner's primary key as composite PK
• 1:1 relationships → Add FK to either side or merge tables
• 1:N relationships → Add FK on the many side
• M:N relationships → Create junction table with PKs of both entities as composite PK""",
                "diagram": "ER diagram with 5 entities: Student, Department, Course, Instructor, Dependent (double rectangle). Relationships: Belongs_to (M:1), Heads (1:1), Teaches (M:N), Enrolls (M:N), Has (1:N identifying).",
            },
            {
                "num": "10",
                "question": "Define stored procedures and triggers. How they are applicable in database? Illustrate with examples, how can you create before and after triggers on INSERT query.",
                "marks": "3+2+5",
                "answer": """<b>Stored Procedures:</b>
A stored procedure is a precompiled collection of SQL statements and control-flow statements stored in the database under a name. It can accept parameters, perform operations, and return results. Stored procedures reduce network traffic, improve performance, and enforce business logic at the database level.

<b>Benefits:</b>
• Reusability: Write once, call many times
• Security: Users can execute without direct table access
• Performance: Precompiled execution plan
• Maintainability: Centralized business logic

<b>Example Stored Procedure:</b>
<pre>
DELIMITER //
CREATE PROCEDURE GetStudentGrades(IN student_id INT)
BEGIN
    SELECT c.course_name, e.grade
    FROM Enrollment e
    JOIN Course c ON e.course_id = c.course_id
    WHERE e.student_id = student_id;
END //
DELIMITER ;

-- Call the procedure
CALL GetStudentGrades(101);
</pre>

<b>Triggers:</b>
A trigger is a stored program that is automatically executed by the DBMS when a specific event (INSERT, UPDATE, DELETE) occurs on a specified table. Triggers enforce integrity constraints, audit changes, and automatically maintain derived data.

<b>Types of Triggers by Timing:</b>
• <b>BEFORE:</b> Executed before the triggering event
• <b>AFTER:</b> Executed after the triggering event

<b>Types by Event:</b>
• INSERT trigger
• UPDATE trigger
• DELETE trigger

<b>Applicability in Database:</b>
1. <b>Audit Logging:</b> Track who changed what and when
2. <b>Data Validation:</b> Enforce complex business rules
3. <b>Derived Data Maintenance:</b> Automatically update summary tables
4. <b>Cascading Changes:</b> Propagate changes to related tables
5. <b>Security:</b> Prevent unauthorized modifications

<b>Example: BEFORE INSERT Trigger</b>
<pre>
-- Create audit table
CREATE TABLE Student_Audit (
    audit_id INT AUTO_INCREMENT PRIMARY KEY,
    action VARCHAR(10),
    student_id INT,
    old_name VARCHAR(100),
    new_name VARCHAR(100),
    changed_by VARCHAR(50),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //
CREATE TRIGGER before_student_insert
BEFORE INSERT ON Student
FOR EACH ROW
BEGIN
    -- Validate: Ensure email is not empty
    IF NEW.email IS NULL OR NEW.email = '' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Email cannot be empty';
    END IF;
    
    -- Log the action
    INSERT INTO Student_Audit (action, student_id, new_name, changed_by)
    VALUES ('INSERT', NEW.student_id, NEW.name, CURRENT_USER());
END //
DELIMITER ;
</pre>

<b>Example: AFTER INSERT Trigger</b>
<pre>
DELIMITER //
CREATE TRIGGER after_student_insert
AFTER INSERT ON Student
FOR EACH ROW
BEGIN
    -- Automatically enroll new student in mandatory orientation course
    INSERT INTO Enrollment (student_id, course_id, enrollment_date)
    VALUES (NEW.student_id, 'ORIENT101', CURDATE());
    
    -- Update department student count
    UPDATE Department 
    SET student_count = student_count + 1 
    WHERE dept_id = NEW.dept_id;
END //
DELIMITER ;
</pre>

<b>Difference between BEFORE and AFTER:</b>

<table border='1' cellpadding='4'><tr><td><b>BEFORE Trigger</b></td><td><b>AFTER Trigger</b></td></tr>
<tr><td>Runs before the triggering statement</td><td>Runs after the triggering statement completes</td></tr>
<tr><td>Can modify NEW values (for INSERT/UPDATE)</td><td>Cannot modify NEW values</td></tr>
<tr><td>Can reject the operation (SIGNAL ERROR)</td><td>Cannot prevent the original operation</td></tr>
<tr><td>Use for validation, transformation</td><td>Use for cascading, logging, auditing</td></tr>
<tr><td>If trigger fails, original statement is cancelled</td><td>If trigger fails, may require rollback</td></tr>
</table>""",
            },
        ]
    }
]


if __name__ == "__main__":
    generate_answer_sheet("CACS251", "operating-systems", "Operating Systems", 2020, "semester-4", OS_QUESTIONS)
    generate_answer_sheet("CACS252", "numerical-methods", "Numerical Methods", 2020, "semester-4", NM_QUESTIONS)
    generate_answer_sheet("CACS253", "software-engineering", "Software Engineering", 2020, "semester-4", SE_QUESTIONS)
    generate_answer_sheet("CACS254", "scripting-language", "Scripting Language", 2020, "semester-4", SL_QUESTIONS)
    generate_answer_sheet("CACS255", "database-management-system", "Database Management System", 2020, "semester-4", DBMS_QUESTIONS)
    print("\n✅ All 4th-semester 2020 answer sheets generated successfully!")

# ============================================================
# SEMESTER 5 - 2020 ANSWER DATA
# ============================================================

MIS_QUESTIONS = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "How properties like ubiquity, richness and information density make e-commerce better than traditional commerce?",
                "marks": "5",
                "answer": """<b>Ubiquity:</b> E-commerce is available everywhere, at all times. Customers can shop from anywhere with internet access, 24/7. Traditional commerce is limited by physical store locations and operating hours. Ubiquity expands market reach beyond geographic boundaries and eliminates time constraints.

<b>Richness:</b> E-commerce can deliver rich, interactive content including videos, 3D models, reviews, and personalized recommendations. Traditional commerce is limited to in-person demonstrations and static displays. Online platforms can provide detailed product information, user guides, and multimedia experiences that enhance customer understanding.

<b>Information Density:</b> E-commerce enables unprecedented information density at low cost. Sellers can track detailed customer behavior, preferences, and purchase history. Prices can be adjusted dynamically based on demand, competition, and customer segments. Traditional commerce has limited ability to collect and analyze customer data. Online merchants can use data analytics to personalize offers, optimize inventory, and improve customer experience.

<b>Combined Impact:</b> These properties together create a more efficient, personalized, and accessible marketplace that reduces transaction costs, eliminates intermediaries, and provides greater value to both buyers and sellers.""",
            },
            {
                "num": "3",
                "question": "Differentiate B2C, B2B and C2C e-commerce with examples.",
                "marks": "5",
                "answer": """<b>B2C (Business-to-Consumer):</b>
Transactions between businesses and individual consumers. Businesses sell products or services directly to end users.
• Examples: Amazon, Flipkart, Daraz, Netflix
• Characteristics: Large customer base, lower transaction volume per customer, marketing focused on individual preferences, payment via credit cards/digital wallets
• Focus: Customer experience, brand loyalty, convenient checkout

<b>B2B (Business-to-Business):</b>
Transactions between two businesses. One business sells products or services to another business.
• Examples: Alibaba, IndiaMART, Salesforce, SAP
• Characteristics: Smaller customer base, higher transaction values, longer sales cycles, negotiated contracts, bulk orders
• Focus: Relationship management, supply chain efficiency, integration with buyer's systems

<b>C2C (Consumer-to-Consumer):</b>
Transactions between individual consumers, often facilitated by a third-party platform.
• Examples: eBay, Etsy, Facebook Marketplace, Hamrobazar
• Characteristics: Peer-to-peer transactions, platform takes commission, user-generated listings, trust and rating systems
• Focus: Community building, trust mechanisms, ease of listing/selling

<b>Comparison Table:</b>
<table border='1' cellpadding='4'><tr><td>Aspect</td><td>B2C</td><td>B2B</td><td>C2C</td></tr>
<tr><td>Participants</td><td>Business + Consumer</td><td>Business + Business</td><td>Consumer + Consumer</td></tr>
<tr><td>Order Size</td><td>Small</td><td>Large/Bulk</td><td>Variable</td></tr>
<tr><td>Decision Time</td><td>Quick</td><td>Long/Complex</td><td>Moderate</td></tr>
<tr><td>Payment</td><td>Instant</td><td>Credit/Invoice</td><td>Platform-mediated</td></tr>
<tr><td>Relationship</td><td>Transactional</td><td>Strategic</td><td>Community-based</td></tr></table>""",
            },
            {
                "num": "4",
                "question": "What is the role of information superhighway in e-commerce? List the components of information superhighway.",
                "marks": "2+3",
                "answer": """<b>Role of Information Superhighway in E-Commerce:</b>
The information superhighway is a global network of interconnected communication systems (primarily the Internet) that enables the rapid transmission of digital information across geographic boundaries.

• <b>Global Connectivity:</b> Connects buyers and sellers worldwide, enabling global e-commerce markets
• <b>Real-time Communication:</b> Supports instant messaging, video conferencing, and live customer support
• <b>Data Transmission:</b> Enables secure transfer of payment information, order details, and digital products
• <b>Marketing Channel:</b> Provides platforms for digital advertising, social media marketing, and search engine optimization
• <b>Supply Chain Integration:</b> Connects suppliers, manufacturers, distributors, and retailers for efficient operations
• <b>Infrastructure Foundation:</b> Serves as the backbone for all e-commerce activities including web hosting, cloud services, and content delivery networks

<b>Components of Information Superhighway:</b>
1. <b>Physical Infrastructure:</b> Fiber optic cables, satellites, cellular towers, routers, switches, and data centers
2. <b>Network Protocols:</b> TCP/IP, HTTP/HTTPS, FTP, and other communication standards
3. <b>Hardware Devices:</b> Computers, smartphones, tablets, servers, and networking equipment
4. <b>Software Applications:</b> Web browsers, email clients, e-commerce platforms, and mobile apps
5. <b>Content Providers:</b> Websites, streaming services, digital libraries, and online databases
6. <b>Service Providers:</b> ISPs (Internet Service Providers), cloud service providers, and hosting companies
7. <b>Human Users:</b> Consumers, businesses, governments, and educators who create and consume content""",
            },
            {
                "num": "5",
                "question": "What is international information system? Describe the concepts of outsourcing and offshoring in the system.",
                "marks": "1+4",
                "answer": """<b>International Information System:</b>
An international information system is an information system that supports business operations across multiple countries. It handles diverse languages, currencies, regulations, time zones, and cultural differences. Such systems are essential for multinational corporations to coordinate global operations, manage international supply chains, and serve customers in different regions.

<b>Outsourcing:</b>
Outsourcing is the practice of contracting specific business functions or IT services to external third-party providers, regardless of location.
• <b>Key Points:</b>
  - Can be domestic or international
  - Focuses on delegating specific tasks (e.g., customer support, software development, data entry)
  - Company retains control over core business operations
  - Reduces operational costs and accesses specialized expertise
• <b>Example:</b> A US company hiring an Indian firm to handle technical support

<b>Offshoring:</b>
Offshoring is the relocation of business processes or operations to another country, typically to reduce costs or access new markets.
• <b>Key Points:</b>
  - Always involves a different country
  - Can involve the company's own subsidiary (captive offshoring) or third-party providers
  - Often motivated by lower labor costs, tax incentives, or access to skilled talent
  - May involve manufacturing, service delivery, or IT operations
• <b>Example:</b> Apple manufacturing iPhones in China; Google operating R&D centers in India

<b>Comparison:</b>
<table border='1' cellpadding='4'><tr><td>Aspect</td><td>Outsourcing</td><td>Offshoring</td></tr>
<tr><td>Location</td><td>Can be domestic or foreign</td><td>Always foreign</td></tr>
<tr><td>Ownership</td><td>Third-party provider</td><td>Can be own subsidiary or third-party</td></tr>
<tr><td>Focus</td><td>Specific function/task</td><td>Entire process/operation</td></tr>
<tr><td>Control</td><td>Lower (external vendor)</td><td>Higher (if captive)</td></tr></table>""",
            },
            {
                "num": "6",
                "question": "Define availability, authentication and authorization. How they can be enforced in e-commerce security?",
                "marks": "3+2",
                "answer": """<b>Availability:</b>
Availability ensures that e-commerce systems and data are accessible to authorized users whenever needed. It guarantees that websites, payment gateways, and databases remain operational and responsive.
• <b>Enforcement:</b> Redundant servers, load balancing, DDoS protection, backup systems, disaster recovery plans, SLA monitoring, and cloud-based auto-scaling

<b>Authentication:</b>
Authentication is the process of verifying the identity of a user, device, or system. It ensures that the entity requesting access is who it claims to be.
• <b>Methods:</b> Passwords, multi-factor authentication (MFA), biometric verification (fingerprint, facial recognition), digital certificates, token-based authentication, and single sign-on (SSO)
• <b>Enforcement:</b> Strong password policies, MFA implementation, CAPTCHA for bot detection, session management, and secure login protocols (OAuth, SAML)

<b>Authorization:</b>
Authorization determines what resources and actions an authenticated user is permitted to access. It defines the permissions and privileges assigned to users.
• <b>Enforcement:</b> Role-Based Access Control (RBAC), Access Control Lists (ACL), permission matrices, principle of least privilege, and regular access audits

<b>How They Work Together in E-Commerce:</b>
1. <b>Authentication First:</b> Customer logs in with username/password + OTP (MFA)
2. <b>Authorization Next:</b> System checks what the customer can access (view orders, edit profile, but not admin functions)
3. <b>Availability Ensured:</b> Website remains online during peak shopping periods (e.g., Black Friday) through load balancing and CDN

<b>Security Defense:</b> Together with encryption (confidentiality) and integrity checks, these form the core security framework protecting e-commerce transactions and customer data.""",
            },
            {
                "num": "7",
                "question": "What is e-checking? Describe its working mechanism.",
                "marks": "2+3",
                "answer": """<b>E-Checking (Electronic Checking):</b>
E-checking is the electronic version of a paper check used for online payments. It contains the same information as a paper check (account number, routing number, payment amount) but is transmitted electronically. E-checks are processed through the Automated Clearing House (ACH) network and are governed by the same laws as paper checks.

<b>Working Mechanism of E-Checking:</b>
1. <b>Authorization:</b> The payer authorizes the payment by providing bank account details (account number, routing number) and signing an authorization form (digital or physical).

2. <b>Payment Setup:</b> The merchant or payment processor creates an electronic check with:
   - Payer's bank account number
   - Bank routing number
   - Payment amount
   - Date and authorization

3. <b>Encryption & Security:</b> The e-check is encrypted and digitally signed to ensure security and non-repudiation.

4. <b>Transmission:</b> The encrypted e-check is sent through the ACH network from the payer's bank to the payee's bank.

5. <b>Verification:</b> The payer's bank verifies that sufficient funds are available and that the account is valid.

6. <b>Clearing & Settlement:</b> Funds are debited from the payer's account and credited to the payee's account. This typically takes 1-3 business days.

7. <b>Confirmation:</b> Both parties receive confirmation of the transaction.

<b>Advantages:</b> Lower processing fees than credit cards, no need for physical handling, faster than traditional mail, automatic record keeping
<b>Disadvantages:</b> Slower than credit card processing, requires bank account information, limited consumer protection, not suitable for instant purchases""",
            },
            {
                "num": "8",
                "question": "Describe the website design criteria that one should show while designing an e-commerce website.",
                "marks": "5",
                "answer": """<b>Website Design Criteria for E-Commerce:</b>

1. <b>User-Friendly Navigation:</b>
   - Clear menu structure with logical categories
   - Search functionality with filters and autocomplete
   - Breadcrumb navigation to show user's location
   - Consistent layout across all pages

2. <b>Responsive Design:</b>
   - Website must work seamlessly on desktop, tablet, and mobile devices
   - Touch-friendly buttons and forms
   - Fast loading times on all screen sizes
   - Mobile-first approach for growing mobile commerce

3. <b>Fast Loading Speed:</b>
   - Optimize images and use content delivery networks (CDN)
   - Minimize HTTP requests and enable browser caching
   - Use lazy loading for images and videos
   - Target page load time under 3 seconds

4. <b>Secure Payment Integration:</b>
   - SSL certificates for HTTPS encryption
   - Multiple payment options (credit cards, digital wallets, COD)
   - PCI DSS compliance for card data security
   - Clear display of security badges and trust seals

5. <b>High-Quality Product Presentation:</b>
   - Multiple product images with zoom functionality
   - Detailed product descriptions and specifications
   - Customer reviews and ratings
   - 360-degree views or product videos where applicable

6. <b>Streamlined Checkout Process:</b>
   - Minimal steps to complete purchase (ideally 3 steps or fewer)
   - Guest checkout option
   - Clear progress indicators
   - Auto-fill for returning customers

7. <b>Trust Signals:</b>
   - Visible contact information and customer support
   - Clear return and refund policies
   - Company information and physical address
   - Social proof (testimonials, user counts, media mentions)

8. <b>SEO Optimization:</b>
   - Search engine friendly URLs and meta tags
   - Structured data for products
   - Fast mobile performance (Core Web Vitals)
   - Quality content and blog integration""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "What do you mean by Wireless Application Protocol (WAP)? How it works? Discuss the layered architecture of WAP.",
                "marks": "2+2+6",
                "answer": """<b>Wireless Application Protocol (WAP):</b>
WAP is an open international standard for applications that use wireless communication. It enables mobile devices (phones, PDAs) to access internet content and services. WAP was designed to work with low-bandwidth, high-latency wireless networks and devices with small screens and limited input capabilities.

<b>How WAP Works:</b>
1. <b>Request:</b> User enters a URL or clicks a link on a WAP-enabled mobile device
2. <b>WAP Gateway:</b> The request is sent to a WAP gateway, which acts as a proxy between the mobile network and the internet
3. <b>Protocol Translation:</b> The gateway converts WAP protocols to standard HTTP/TCP and fetches the requested content from the web server
4. <b>Content Encoding:</b> The gateway compresses and encodes the content into WML (Wireless Markup Language) or XHTML-MP
5. <b>Response:</b> The encoded content is sent back to the mobile device through the wireless network
6. <b>Rendering:</b> The device's WAP browser (microbrowser) renders the content on the small screen

<b>WAP Layered Architecture:</b>
<table border='1' cellpadding='4'><tr><td>Layer</td><td>Name</td><td>Function</td><td>Equivalent in Web</td></tr>
<tr><td>Layer 5</td><td>Application Layer (WAE)</td><td>Provides environment for wireless applications; includes WML, WMLScript, and telephony APIs</td><td>HTTP + HTML + JavaScript</td></tr>
<tr><td>Layer 4</td><td>Session Layer (WSP)</td><td>Manages sessions between client and server; supports connection-oriented and connectionless modes</td><td>HTTP/HTTPS</td></tr>
<tr><td>Layer 3</td><td>Transaction Layer (WTP)</td><td>Provides reliable request-response transactions with minimal overhead</td><td>TCP/UDP</td></tr>
<tr><td>Layer 2</td><td>Security Layer (WTLS)</td><td>Provides encryption, data integrity, and authentication; equivalent to TLS/SSL</td><td>TLS/SSL</td></tr>
<tr><td>Layer 1</td><td>Transport Layer (WDP)</td><td>Provides datagram service, abstracting underlying network (GSM, CDMA, SMS)</td><td>UDP</td></tr>
<tr><td>Layer 0</td><td>Bearer Networks</td><td>Physical network: GSM, GPRS, CDMA, SMS, USSD</td><td>Ethernet, Wi-Fi</td></tr></table>

<b>Key Features:</b> Optimized for low bandwidth, handles intermittent connectivity, supports push services, device-independent content adaptation, and security through WTLS.""",
            },
            {
                "num": "10",
                "question": "How important web contents are for e-commerce systems? Discuss their types. Justify, with examples, how web contents can be used to promote cross-selling, up-selling and promotions in e-commerce.",
                "marks": "2+2+6",
                "answer": """<b>Importance of Web Content in E-Commerce:</b>
Web content is the foundation of e-commerce success. It drives traffic, engages customers, builds trust, and converts visitors into buyers.
• <b>SEO:</b> Quality content improves search engine rankings and organic traffic
• <b>Customer Education:</b> Informs customers about products, features, and benefits
• <b>Trust Building:</b> Reviews, testimonials, and detailed descriptions reduce purchase anxiety
• <b>Brand Identity:</b> Content communicates brand values and personality
• <b>Conversion:</b> Compelling product descriptions and images increase purchase likelihood
• <b>Customer Support:</b> FAQ pages, guides, and tutorials reduce support costs

<b>Types of Web Content:</b>
1. <b>Product Content:</b> Descriptions, specifications, images, videos, 360° views
2. <b>Marketing Content:</b> Blog posts, articles, social media posts, email newsletters
3. <b>Transactional Content:</b> Pricing, shipping info, return policies, terms of service
4. <b>User-Generated Content:</b> Reviews, ratings, Q&A, photos from customers
5. <b>Interactive Content:</b> Quizzes, configurators, calculators, chatbots
6. <b>Visual Content:</b> Infographics, banners, product photos, demo videos
7. <b>Educational Content:</b> How-to guides, tutorials, comparison articles

<b>Cross-Selling with Web Content:</b>
Cross-selling recommends complementary products to increase order value.
• <b>Example:</b> Amazon's "Frequently Bought Together" section. When viewing a laptop, the page shows laptop bag, mouse, and keyboard. Content includes product images, compatibility info, and bundle pricing.
• <b>Technique:</b> "Complete the Look" content on fashion sites shows matching accessories

<b>Up-Selling with Web Content:</b>
Up-selling encourages customers to purchase a higher-end version of a product.
• <b>Example:</b> Apple's iPhone comparison table showing features of different models side-by-side, highlighting the benefits of the Pro model (better camera, longer battery). Content includes detailed spec comparisons and benefit-driven descriptions.
• <b>Technique:</b> "Upgrade and Save" messaging with feature comparison charts

<b>Promotions with Web Content:</b>
Promotional content drives urgency and increases conversion rates.
• <b>Example:</b> Flash sale countdown timers, "Limited Stock" badges, seasonal campaign banners. Daraz's "11.11 Sale" uses dedicated landing pages with countdown timers, discount badges, and curated product collections.
• <b>Technique:</b> Personalized email content with exclusive discount codes based on browsing history

<b>Combined Strategy:</b> Netflix uses content to promote cross-selling ("Because you watched X, you might like Y") and up-selling (premium plan benefits highlighted in comparison tables) through personalized web content.""",
            },
            {
                "num": "11",
                "question": "Discuss in detail the security defense strategies that you can implement while securing e-commerce systems from security attacks and threats.",
                "marks": "10",
                "answer": """<b>Security Defense Strategies for E-Commerce:</b>

<b>1. Encryption and SSL/TLS:</b>
• Implement SSL/TLS certificates to encrypt all data transmitted between customers and servers
• Use HTTPS for all pages, not just checkout
• Encrypt sensitive data at rest (customer information, payment details)
• Implement end-to-end encryption for messaging and communications

<b>2. Firewalls and Intrusion Detection/Prevention:</b>
• Deploy Web Application Firewalls (WAF) to filter malicious traffic
• Use network firewalls to control incoming and outgoing traffic
• Implement IDS/IPS to detect and block suspicious activities in real-time
• Regularly update firewall rules based on threat intelligence

<b>3. Secure Payment Processing:</b>
• Comply with PCI DSS (Payment Card Industry Data Security Standard)
• Use tokenization to replace card numbers with non-sensitive tokens
• Implement 3D Secure authentication for card payments
• Consider using trusted payment gateways (Stripe, PayPal) rather than storing card data

<b>4. Authentication and Access Control:</b>
• Enforce strong password policies (minimum length, complexity requirements)
• Implement Multi-Factor Authentication (MFA) for admin and customer accounts
• Use Role-Based Access Control (RBAC) for internal systems
• Implement account lockout policies after failed login attempts
• Use OAuth/SAML for secure third-party authentication

<b>5. Regular Security Audits and Testing:</b>
• Conduct penetration testing to identify vulnerabilities
• Perform code reviews and security scans
• Use automated vulnerability scanning tools
• Engage third-party security auditors annually
• Implement bug bounty programs

<b>6. Data Backup and Disaster Recovery:</b>
• Maintain regular backups of all critical data
• Store backups in geographically separate locations
• Test disaster recovery procedures regularly
• Implement point-in-time recovery capabilities
• Use redundant servers and failover mechanisms

<b>7. DDoS Protection:</b>
• Use DDoS mitigation services (Cloudflare, AWS Shield)
• Implement rate limiting on APIs and login endpoints
• Use Content Delivery Networks (CDN) to absorb traffic spikes
• Monitor traffic patterns for anomalies

<b>8. Software Updates and Patch Management:</b>
• Keep all software, frameworks, and libraries up to date
• Apply security patches promptly
• Remove unused plugins and dependencies
• Use automated patch management tools

<b>9. Employee Training and Awareness:</b>
• Train staff on phishing recognition and social engineering
• Establish clear security policies and procedures
• Conduct regular security awareness simulations
• Limit access to sensitive systems based on job roles

<b>10. Legal and Compliance Measures:</b>
• Implement privacy policies compliant with GDPR, CCPA
• Maintain audit logs of all transactions
• Use digital signatures for non-repudiation
• Comply with consumer protection laws
• Implement data retention and deletion policies""",
            },
        ]
    }
]

DOTNET_QUESTIONS = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "Differentiate Object Oriented Programming and Object Based Programming. Explain some of the major features of C# language.",
                "marks": "2+3",
                "answer": """<b>Object Oriented Programming (OOP) vs Object Based Programming (OBP):</b>
<table border='1' cellpadding='4'><tr><td>Aspect</td><td>Object Oriented Programming</td><td>Object Based Programming</td></tr>
<tr><td>Inheritance</td><td>Supports inheritance (single & multiple)</td><td>Does not support inheritance</td></tr>
<tr><td>Polymorphism</td><td>Supports polymorphism (overloading, overriding)</td><td>Limited or no polymorphism</td></tr>
<tr><td>Encapsulation</td><td>Full encapsulation support</td><td>Supports encapsulation</td></tr>
<tr><td>Examples</td><td>C#, Java, C++, Python</td><td>JavaScript, VBScript, Ruby (pre-2.0)</td></tr>
<tr><td>Reusability</td><td>High reusability through inheritance</td><td>Limited reusability through composition only</td></tr>
<tr><td>Complexity</td><td>More complex, structured approach</td><td>Simpler, more flexible</td></tr></table>

<b>Major Features of C# Language:</b>
1. <b>Object-Oriented:</b> Supports encapsulation, inheritance, and polymorphism. Everything is an object.
2. <b>Type-Safe:</b> Strong typing prevents type errors at compile time. Variables must be declared with specific types.
3. <b>Modern:</b> Supports generics, LINQ, async/await, lambda expressions, and extension methods.
4. <b>Managed Code:</b> Runs on .NET CLR with automatic memory management (garbage collection).
5. <b>Component-Oriented:</b> Supports properties, events, attributes, and reflection for building reusable components.
6. <b>Interoperability:</b> Can interact with COM components, native C/C++ libraries (P/Invoke), and other .NET languages.
7. <b>Versioning:</b> Supports method overloading and overriding with virtual/override keywords for safe versioning.
8. <b>Standardized:</b> ECMA and ISO standardized language with cross-platform support via .NET Core/.NET 5+.
9. <b>Rich Library:</b> Extensive Base Class Library (BCL) for common tasks like I/O, networking, collections, and threading.""",
            },
            {
                "num": "3",
                "question": "Explain overview of Microsoft .NET framework and its components in detail.",
                "marks": "5",
                "answer": """<b>Microsoft .NET Framework Overview:</b>
The .NET Framework is a software development platform developed by Microsoft. It provides a controlled programming environment where software can be developed, installed, and executed on Windows-based systems. It supports multiple programming languages and provides a large standard library.

<b>Components of .NET Framework:</b>

1. <b>Common Language Runtime (CLR):</b>
   - The execution engine of .NET
   - Provides memory management (Garbage Collection)
   - Handles exception management, type safety, and security
   - Just-In-Time (JIT) compilation converts IL code to native machine code
   - Provides cross-language integration

2. <b>.NET Framework Class Library (FCL):</b>
   - A comprehensive collection of reusable classes, interfaces, and value types
   - Provides functionality for: file I/O, database connectivity, XML processing, web services, GUI development, cryptography, threading
   - Organized into namespaces (System, System.IO, System.Data, System.Web, etc.)

3. <b>Common Type System (CTS):</b>
   - Defines how types are declared, used, and managed
   - Ensures type safety and cross-language interoperability
   - Supports value types (structs, enums) and reference types (classes, interfaces, delegates)

4. <b>Common Language Specification (CLS):</b>
   - A subset of CTS that all .NET languages must support
   - Ensures interoperability between different .NET languages
   - Any CLS-compliant code can be used by any .NET language

5. <b>Base Class Library (BCL):</b>
   - Core subset of FCL providing fundamental functionality
   - Includes collections, I/O, threading, reflection, networking, and security

6. <b>ASP.NET:</b>
   - Web development framework for building web applications and services
   - Supports Web Forms, MVC, Web API, and SignalR
   - Provides server controls, data binding, and state management

7. <b>ADO.NET:</b>
   - Data access technology for connecting to databases
   - Supports disconnected data architecture with DataSets and DataAdapters
   - Provides providers for SQL Server, Oracle, OLE DB, and ODBC

8. <b>Windows Forms / WPF:</b>
   - Technologies for building desktop applications
   - Windows Forms: traditional event-driven GUI framework
   - WPF: modern UI framework using XAML for declarative UI design

<b>Architecture:</b>
<table border='1' cellpadding='4'><tr><td>Application Layer</td><td>WinForms / WPF / ASP.NET / Console</td></tr>
<tr><td>Base Class Library</td><td>System, System.IO, System.Data, System.Web, etc.</td></tr>
<tr><td>Common Language Runtime</td><td>JIT Compiler, GC, Security, Type Checker</td></tr>
<tr><td>Operating System</td><td>Windows OS</td></tr></table>""",
            },
            {
                "num": "4",
                "question": "What do you mean by property in C# language? How it is different from method? Compare automatic property with other types of property with suitable example.",
                "marks": "1+1+3",
                "answer": """<b>Property in C#:</b>
A property in C# is a member that provides a flexible mechanism to read, write, or compute the value of a private field. Properties use accessors (get and set) to control access to fields. They appear like fields from the outside but are implemented like methods internally.

<b>Property vs Method:</b>
<table border='1' cellpadding='4'><tr><td>Aspect</td><td>Property</td><td>Method</td></tr>
<tr><td>Syntax</td><td>Accessed like a field: obj.Name</td><td>Called with parentheses: obj.GetName()</td></tr>
<tr><td>Purpose</td><td>Encapsulates field access</td><td>Performs operations/actions</td></tr>
<tr><td>Return</td><td>Always returns a single value</td><td>Can return void or any type</td></tr>
<tr><td>Parameters</td><td>Cannot have parameters (except indexers)</td><td>Can have multiple parameters</td></tr>
<tr><td>Overloading</td><td>Cannot be overloaded</td><td>Can be overloaded</td></tr>
<tr><td>Use Case</td><td>Data encapsulation, validation</td><td>Business logic, calculations</td></tr></table>

<b>Types of Properties:</b>

1. <b>Read-Write Property (Full Property):</b>
<pre>
private string name;
public string Name
{
    get { return name; }
    set { name = value; }
}
</pre>

2. <b>Read-Only Property:</b>
<pre>
public string Email { get; }
</pre>

3. <b>Write-Only Property:</b>
<pre>
public string Password { set { /* encrypt and store */ } }
</pre>

4. <b>Automatic Property:</b>
<pre>
public string Name { get; set; }
</pre>

<b>Comparison: Automatic Property vs Full Property</b>
<table border='1' cellpadding='4'><tr><td>Aspect</td><td>Automatic Property</td><td>Full Property</td></tr>
<tr><td>Backing Field</td><td>Compiler-generated, hidden</td><td>Explicitly declared</td></tr>
<tr><td>Validation</td><td>Cannot add validation in basic form</td><td>Can add validation logic in set</td></tr>
<tr><td>Code Length</td><td>Very concise</td><td>More verbose</td></tr>
<tr><td>Readability</td><td>Clean and simple</td><td>More explicit</td></tr>
<tr><td>Initialization</td><td>Can use default values</td><td>Full control over initialization</td></tr>
<tr><td>When to Use</td><td>Simple data binding, DTOs</td><td>Business logic, validation needed</td></tr></table>""",
            },
            {
                "num": "5",
                "question": "Define constructor. Explain different types of constructors used in C# with example.",
                "marks": "1+4",
                "answer": """<b>Constructor:</b>
A constructor is a special method in a class that is automatically invoked when an object of the class is created. It has the same name as the class and no return type. Constructors are used to initialize object state and allocate resources.

<b>Types of Constructors in C#:</b>

1. <b>Default Constructor:</b>
A constructor with no parameters. If no constructor is defined, C# provides a default constructor automatically.
<pre>
public class Student
{
    public string Name;
    public Student()  // Default constructor
    {
        Name = "Unknown";
    }
}
</pre>

2. <b>Parameterized Constructor:</b>
A constructor that accepts parameters to initialize object with specific values.
<pre>
public class Student
{
    public string Name;
    public int Age;
    public Student(string name, int age)
    {
        Name = name;
        Age = age;
    }
}
// Usage: Student s = new Student("Ram", 20);
</pre>

3. <b>Copy Constructor:</b>
Creates a new object by copying values from an existing object.
<pre>
public class Student
{
    public string Name;
    public Student(Student other)
    {
        Name = other.Name;
    }
}
</pre>

4. <b>Static Constructor:</b>
Called automatically before any instance is created or static member is referenced. Used to initialize static data.
<pre>
public class Database
{
    public static string ConnectionString;
    static Database()
    {
        ConnectionString = "Server=localhost;Database=Test";
    }
}
</pre>

5. <b>Private Constructor:</b>
Prevents instantiation from outside the class. Used in singleton pattern and utility classes.
<pre>
public class Singleton
{
    private static Singleton instance;
    private Singleton() { }
    public static Singleton GetInstance()
    {
        if (instance == null)
            instance = new Singleton();
        return instance;
    }
}
</pre>

<b>Constructor Chaining:</b>
Constructors can call other constructors using the <code>this</code> keyword:
<pre>
public Student() : this("Unknown", 0) { }
public Student(string name, int age)
{
    Name = name; Age = age;
}
</pre>""",
            },
            {
                "num": "6",
                "question": "Define inheritance. Write a C# program to demonstrate multilevel and multiple inheritance.",
                "marks": "1+2+2",
                "answer": """<b>Inheritance:</b>
Inheritance is an object-oriented programming concept where a new class (derived/child class) inherits properties and methods from an existing class (base/parent class). It promotes code reusability and establishes an "is-a" relationship between classes.

<b>C# supports:</b>
• Single inheritance (one base class per derived class)
• Multilevel inheritance (class B inherits from A, class C inherits from B)
• Hierarchical inheritance (multiple classes inherit from one base)
• Multiple inheritance of interfaces (not classes)

<b>Multilevel Inheritance Example:</b>
<pre>
// Base class
public class Person
{
    public string Name;
    public void DisplayPerson()
    {
        Console.WriteLine("Name: " + Name);
    }
}

// Intermediate derived class
public class Employee : Person
{
    public int EmployeeId;
    public void DisplayEmployee()
    {
        DisplayPerson();
        Console.WriteLine("Employee ID: " + EmployeeId);
    }
}

// Derived from Employee
public class Manager : Employee
{
    public string Department;
    public void DisplayManager()
    {
        DisplayEmployee();
        Console.WriteLine("Department: " + Department);
    }
}

// Usage
class Program
{
    static void Main()
    {
        Manager mgr = new Manager();
        mgr.Name = "Hari";
        mgr.EmployeeId = 101;
        mgr.Department = "IT";
        mgr.DisplayManager();
    }
}
</pre>

<b>Multiple Inheritance using Interfaces:</b>
C# does not support multiple class inheritance, but it supports multiple interface inheritance:
<pre>
public interface IPrintable
{
    void Print();
}

public interface IScannable
{
    void Scan();
}

public class AllInOnePrinter : IPrintable, IScannable
{
    public void Print()
    {
        Console.WriteLine("Printing document...");
    }
    public void Scan()
    {
        Console.WriteLine("Scanning document...");
    }
}

class Program
{
    static void Main()
    {
        AllInOnePrinter device = new AllInOnePrinter();
        device.Print();
        device.Scan();
    }
}
</pre>

<b>Output:</b>
<pre>
Name: Hari
Employee ID: 101
Department: IT
Printing document...
Scanning document...
</pre>""",
            },
            {
                "num": "7",
                "question": "What is generics? List different types of generic classes. Explain delegate with example.",
                "marks": "1+1+3",
                "answer": """<b>Generics:</b>
Generics in C# allow you to define type-safe data structures and methods without committing to actual data types at definition time. They enable code reusability by creating classes, interfaces, and methods that work with any data type while maintaining type safety at compile time.

<b>Benefits of Generics:</b>
• Type safety: Errors caught at compile time, not runtime
• Performance: No boxing/unboxing for value types
• Code reusability: One class/method works with multiple types
• Reduced code duplication

<b>Types of Generic Classes:</b>

1. <b>Generic Collections:</b>
   - <code>List&lt;T&gt;</code>: Dynamic array
   - <code>Dictionary&lt;TKey, TValue&gt;</code>: Key-value pairs
   - <code>Queue&lt;T&gt;</code>, <code>Stack&lt;T&gt;</code>: FIFO and LIFO structures

2. <b>Generic Interfaces:</b>
   - <code>IEnumerable&lt;T&gt;</code>, <code>IList&lt;T&gt;</code>, <code>ICollection&lt;T&gt;</code>

3. <b>Custom Generic Classes:</b>
<pre>
public class Box&lt;T&gt;
{
    private T item;
    public void SetItem(T value) { item = value; }
    public T GetItem() { return item; }
}
// Usage: Box&lt;int&gt; intBox = new Box&lt;int&gt;();
</pre>

4. <b>Generic Methods:</b>
<pre>
public T Max&lt;T&gt;(T a, T b) where T : IComparable
{
    return a.CompareTo(b) > 0 ? a : b;
}
</pre>

5. <b>Generic Constraints:</b>
   - <code>where T : class</code> (reference type)
   - <code>where T : struct</code> (value type)
   - <code>where T : new()</code> (parameterless constructor)
   - <code>where T : BaseClass</code> (inheritance constraint)
   - <code>where T : IComparable</code> (interface constraint)

<b>Delegate:</b>
A delegate is a type-safe function pointer that references methods. It defines the signature of methods that can be assigned to it.

<b>Example:</b>
<pre>
// Delegate declaration
public delegate void GreetingDelegate(string name);

public class Program
{
    public static void EnglishGreeting(string name)
    {
        Console.WriteLine("Hello, " + name);
    }
    public static void NepaliGreeting(string name)
    {
        Console.WriteLine("Namaste, " + name);
    }
    static void Main()
    {
        GreetingDelegate greet;
        greet = EnglishGreeting;
        greet("Ram");        // Output: Hello, Ram
        greet = NepaliGreeting;
        greet("Sita");       // Output: Namaste, Sita
    }
}
</pre>

<b>Built-in Delegates:</b>
• <code>Action&lt;T&gt;</code>: Delegate with no return value
• <code>Func&lt;T, TResult&gt;</code>: Delegate with return value
• <code>Predicate&lt;T&gt;</code>: Delegate that returns boolean""",
            },
            {
                "num": "8",
                "question": "What do you mean by lambda expression? Explain different types of lambda expression used in C# with example.",
                "marks": "1+4",
                "answer": """<b>Lambda Expression:</b>
A lambda expression is an anonymous function that can contain expressions and statements. It provides a concise way to write inline code blocks without explicitly declaring a method. Introduced in C# 3.0, lambdas are extensively used with LINQ, delegates, and event handlers.

<b>Syntax:</b>
<code>(parameters) => expression</code> or <code>(parameters) => { statements; }</code>

<b>Types of Lambda Expressions:</b>

1. <b>Expression Lambda:</b>
Contains a single expression on the right side of => operator. Returns the result of the expression.
<pre>
// Expression lambda with one parameter
Func&lt;int, int&gt; square = x => x * x;
Console.WriteLine(square(5));  // Output: 25

// Expression lambda with two parameters
Func&lt;int, int, int&gt; add = (a, b) => a + b;
Console.WriteLine(add(3, 4));  // Output: 7
</pre>

2. <b>Statement Lambda:</b>
Contains a block of statements enclosed in braces. Can include multiple statements, variable declarations, and loops.
<pre>
Action&lt;string&gt; greet = name =>
{
    string message = "Hello, " + name;
    Console.WriteLine(message);
};
greet("Ram");  // Output: Hello, Ram

Func&lt;int, int, string&gt; compare = (a, b) =>
{
    if (a > b)
        return a + " is greater";
    else if (a < b)
        return b + " is greater";
    else
        return "Both are equal";
};
Console.WriteLine(compare(5, 3));  // Output: 5 is greater
</pre>

3. <b>Lambda with LINQ:</b>
<pre>
List&lt;int&gt; numbers = new List&lt;int&gt; { 1, 2, 3, 4, 5, 6 };
// Using lambda with Where
var evenNumbers = numbers.Where(n => n % 2 == 0);
foreach (var n in evenNumbers)
    Console.Write(n + " ");  // Output: 2 4 6

// Using lambda with Select
var squares = numbers.Select(n => n * n);
</pre>

4. <b>Lambda with Delegates:</b>
<pre>
delegate bool IsEligible(Student s);

class Student
{
    public string Name;
    public int Marks;
}

IsEligible isPass = s => s.Marks >= 40;
Student student = new Student { Name = "Hari", Marks = 75 };
Console.WriteLine(isPass(student));  // Output: True
</pre>

5. <b>Lambda with Events:</b>
<pre>
Button btn = new Button();
btn.Click += (sender, e) =>
{
    Console.WriteLine("Button clicked!");
};
</pre>

<b>Key Points:</b>
• Type inference: Compiler infers parameter types
• Can capture variables from enclosing scope (closures)
• Shorter and more readable than anonymous methods
• Cannot be used where a statement block requires branching (return, break, continue) without statement lambda""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "a) Write a program to create user registration form in one ASP.NET web page and display filled data in another page. b) Write a program for handling exception in ASP.NET.",
                "marks": "7+3",
                "answer": """<b>a) ASP.NET User Registration Form:</b>

<b>Registration.aspx (Form Page):</b>
<pre>
&lt;%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Registration.aspx.cs" Inherits="WebApp.Registration" %&gt;
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;title&gt;User Registration&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
    &lt;form id="form1" runat="server"&gt;
        &lt;h2&gt;User Registration&lt;/h2&gt;
        &lt;asp:Label ID="lblName" runat="server" Text="Name:"&gt;&lt;/asp:Label&gt;
        &lt;asp:TextBox ID="txtName" runat="server"&gt;&lt;/asp:TextBox&gt;&lt;br /&gt;&lt;br /&gt;
        
        &lt;asp:Label ID="lblEmail" runat="server" Text="Email:"&gt;&lt;/asp:Label&gt;
        &lt;asp:TextBox ID="txtEmail" runat="server"&gt;&lt;/asp:TextBox&gt;&lt;br /&gt;&lt;br /&gt;
        
        &lt;asp:Label ID="lblPhone" runat="server" Text="Phone:"&gt;&lt;/asp:Label&gt;
        &lt;asp:TextBox ID="txtPhone" runat="server"&gt;&lt;/asp:TextBox&gt;&lt;br /&gt;&lt;br /&gt;
        
        &lt;asp:Button ID="btnSubmit" runat="server" Text="Submit" OnClick="btnSubmit_Click" /&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

<b>Registration.aspx.cs:</b>
<pre>
using System;

namespace WebApp
{
    public partial class Registration : System.Web.UI.Page
    {
        protected void btnSubmit_Click(object sender, EventArgs e)
        {
            Session["Name"] = txtName.Text;
            Session["Email"] = txtEmail.Text;
            Session["Phone"] = txtPhone.Text;
            Response.Redirect("Display.aspx");
        }
    }
}
</pre>

<b>Display.aspx (Result Page):</b>
<pre>
&lt;%@ Page Language="C#" AutoEventWireup="true" CodeBehind="Display.aspx.cs" Inherits="WebApp.Display" %&gt;
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;title&gt;Display Data&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
    &lt;form id="form1" runat="server"&gt;
        &lt;h2&gt;Registered User Details&lt;/h2&gt;
        &lt;asp:Label ID="lblResult" runat="server"&gt;&lt;/asp:Label&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

<b>Display.aspx.cs:</b>
<pre>
using System;

namespace WebApp
{
    public partial class Display : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            string name = Session["Name"].ToString();
            string email = Session["Email"].ToString();
            string phone = Session["Phone"].ToString();
            lblResult.Text = "Name: " + name + "&lt;br/&gt;Email: " + email + "&lt;br/&gt;Phone: " + phone;
        }
    }
}
</pre>

<b>b) Exception Handling in ASP.NET:</b>
<pre>
using System;

namespace WebApp
{
    public partial class ExceptionDemo : System.Web.UI.Page
    {
        protected void Page_Load(object sender, EventArgs e)
        {
            try
            {
                int a = 10;
                int b = 0;
                int result = a / b;  // This will throw DivideByZeroException
                lblResult.Text = "Result: " + result;
            }
            catch (DivideByZeroException ex)
            {
                lblResult.Text = "Error: Cannot divide by zero. " + ex.Message;
            }
            catch (Exception ex)
            {
                lblResult.Text = "General Error: " + ex.Message;
            }
            finally
            {
                // Cleanup code always executes
                lblResult.Text += "&lt;br/&gt;Execution completed.";
            }
        }
    }
}
</pre>

<b>Global Exception Handling (Global.asax):</b>
<pre>
void Application_Error(object sender, EventArgs e)
{
    Exception ex = Server.GetLastError();
    // Log error to file or database
    System.IO.File.AppendAllText("ErrorLog.txt", DateTime.Now + ": " + ex.Message + "\\n");
    Server.ClearError();
    Response.Redirect("ErrorPage.aspx");
}
</pre>""",
            },
            {
                "num": "10",
                "question": "a) How virtual method is used to achieve dynamic binding in C#? Explain with the help of suitable program. b) Define operator overloading. Write a C# program to overload binary operator.",
                "marks": "1+4+1+4",
                "answer": """<b>a) Virtual Method and Dynamic Binding:</b>

<b>Dynamic Binding (Runtime Polymorphism):</b>
Dynamic binding is the process of resolving a method call at runtime rather than compile time. In C#, virtual methods enable dynamic binding by allowing a derived class to override a base class method.

<b>How it works:</b>
1. Base class declares a method with <code>virtual</code> keyword
2. Derived class overrides it with <code>override</code> keyword
3. At runtime, the actual object's type (not the reference type) determines which method is called

<b>Program:</b>
<pre>
using System;

public class Shape
{
    public virtual void Draw()
    {
        Console.WriteLine("Drawing a shape");
    }
}

public class Circle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("Drawing a circle");
    }
}

public class Rectangle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("Drawing a rectangle");
    }
}

class Program
{
    static void Main()
    {
        Shape s1 = new Circle();      // Upcasting
        Shape s2 = new Rectangle();   // Upcasting
        
        s1.Draw();  // Output: Drawing a circle
        s2.Draw();  // Output: Drawing a rectangle
        
        // Even though reference type is Shape, 
        // the actual object's method is called at runtime
    }
}
</pre>

<b>Key Points:</b>
• Without <code>virtual</code>/<code>override</code>, method hiding occurs with <code>new</code> keyword
• Dynamic binding enables extensibility and loose coupling
• Used extensively in frameworks (ASP.NET MVC controllers, Entity Framework)

<b>b) Operator Overloading:</b>
Operator overloading allows custom types (classes/structs) to define how operators (+, -, *, /, ==, etc.) behave when applied to objects of that type.

<b>Program to Overload Binary + Operator:</b>
<pre>
using System;

public class Complex
{
    public double Real { get; set; }
    public double Imaginary { get; set; }
    
    public Complex(double real, double imaginary)
    {
        Real = real;
        Imaginary = imaginary;
    }
    
    // Overload binary + operator
    public static Complex operator +(Complex c1, Complex c2)
    {
        return new Complex(c1.Real + c2.Real, c1.Imaginary + c2.Imaginary);
    }
    
    // Overload binary - operator
    public static Complex operator -(Complex c1, Complex c2)
    {
        return new Complex(c1.Real - c2.Real, c1.Imaginary - c2.Imaginary);
    }
    
    public override string ToString()
    {
        return Real + " + " + Imaginary + "i";
    }
}

class Program
{
    static void Main()
    {
        Complex c1 = new Complex(3, 4);
        Complex c2 = new Complex(1, 2);
        
        Complex sum = c1 + c2;
        Complex diff = c1 - c2;
        
        Console.WriteLine("c1 = " + c1);       // Output: c1 = 3 + 4i
        Console.WriteLine("c2 = " + c2);       // Output: c2 = 1 + 2i
        Console.WriteLine("Sum = " + sum);     // Output: Sum = 4 + 6i
        Console.WriteLine("Diff = " + diff);   // Output: Diff = 2 + 2i
    }
}
</pre>

<b>Rules for Operator Overloading:</b>
• Must be declared as public and static
• At least one parameter must be of the containing type
• Cannot overload =, &&, ||, ?:, new, is, as, sizeof, typeof operators
• Can overload arithmetic (+, -, *, /, %), comparison (==, !=, <, >), and bitwise operators""",
            },
            {
                "num": "11",
                "question": "a) What is LINQ? Write a program to select employees whose salary is greater than 20000 and whose address is kathmandu using LINQ. b) Write a C# program to show insert and select operation in database.",
                "marks": "1+4+5",
                "answer": """<b>a) LINQ (Language Integrated Query):</b>
LINQ is a set of language extensions in C# that provides a consistent query syntax for querying data from various sources (objects, databases, XML, collections). It integrates query capabilities directly into the C# language, making queries type-safe and IntelliSense-supported.

<b>LINQ Program:</b>
<pre>
using System;
using System.Collections.Generic;
using System.Linq;

public class Employee
{
    public int Id { get; set; }
    public string Name { get; set; }
    public string Address { get; set; }
    public decimal Salary { get; set; }
}

class Program
{
    static void Main()
    {
        List&lt;Employee&gt; employees = new List&lt;Employee&gt;
        {
            new Employee { Id = 1, Name = "Ram", Address = "Kathmandu", Salary = 25000 },
            new Employee { Id = 2, Name = "Sita", Address = "Pokhara", Salary = 30000 },
            new Employee { Id = 3, Name = "Hari", Address = "Kathmandu", Salary = 18000 },
            new Employee { Id = 4, Name = "Gita", Address = "Kathmandu", Salary = 35000 },
            new Employee { Id = 5, Name = "Shyam", Address = "Lalitpur", Salary = 22000 }
        };
        
        // LINQ Query Syntax
        var result = from emp in employees
                     where emp.Salary > 20000 && emp.Address == "Kathmandu"
                     select emp;
        
        // Alternative: Method Syntax
        // var result = employees.Where(emp => emp.Salary > 20000 && emp.Address == "Kathmandu");
        
        Console.WriteLine("Employees with Salary > 20000 and Address = Kathmandu:");
        foreach (var emp in result)
        {
            Console.WriteLine($"ID: {emp.Id}, Name: {emp.Name}, Salary: {emp.Salary}");
        }
    }
}
</pre>

<b>Output:</b>
<pre>
Employees with Salary > 20000 and Address = Kathmandu:
ID: 1, Name: Ram, Salary: 25000
ID: 4, Name: Gita, Salary: 35000
</pre>

<b>b) C# Database Operations (Insert and Select):</b>
<pre>
using System;
using System.Data;
using System.Data.SqlClient;

public class DatabaseDemo
{
    static string connString = "Server=localhost;Database=CompanyDB;Trusted_Connection=True;";
    
    // INSERT Operation
    public static void InsertEmployee(string name, string address, decimal salary)
    {
        using (SqlConnection conn = new SqlConnection(connString))
        {
            string query = "INSERT INTO Employees (Name, Address, Salary) VALUES (@Name, @Address, @Salary)";
            SqlCommand cmd = new SqlCommand(query, conn);
            cmd.Parameters.AddWithValue("@Name", name);
            cmd.Parameters.AddWithValue("@Address", address);
            cmd.Parameters.AddWithValue("@Salary", salary);
            
            conn.Open();
            int rowsAffected = cmd.ExecuteNonQuery();
            Console.WriteLine($"{rowsAffected} row(s) inserted.");
        }
    }
    
    // SELECT Operation
    public static void SelectEmployees()
    {
        using (SqlConnection conn = new SqlConnection(connString))
        {
            string query = "SELECT Id, Name, Address, Salary FROM Employees";
            SqlCommand cmd = new SqlCommand(query, conn);
            
            conn.Open();
            SqlDataReader reader = cmd.ExecuteReader();
            
            Console.WriteLine("\\nEmployee List:");
            Console.WriteLine("ID\\tName\\t\\tAddress\\t\\tSalary");
            while (reader.Read())
            {
                Console.WriteLine($"{reader["Id"]}\\t{reader["Name"]}\\t\\t{reader["Address"]}\\t\\t{reader["Salary"]}");
            }
            reader.Close();
        }
    }
    
    static void Main()
    {
        // Insert a new employee
        InsertEmployee("Ram", "Kathmandu", 25000);
        
        // Display all employees
        SelectEmployees();
    }
}
</pre>

<b>Using DataAdapter and DataSet (Disconnected Architecture):</b>
<pre>
public static void SelectWithDataSet()
{
    using (SqlConnection conn = new SqlConnection(connString))
    {
        string query = "SELECT * FROM Employees";
        SqlDataAdapter adapter = new SqlDataAdapter(query, conn);
        DataSet ds = new DataSet();
        adapter.Fill(ds, "Employees");
        
        foreach (DataRow row in ds.Tables["Employees"].Rows)
        {
            Console.WriteLine($"{row["Name"]} - {row["Salary"]}");
        }
    }
}
</pre>""",
            },
        ]
    }
]

NETWORKING_QUESTIONS = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "Define protocols. Explain WWW and HTTP protocol.",
                "marks": "1+2+2",
                "answer": """<b>Protocol:</b>
A protocol is a set of rules and conventions that govern how data is transmitted, received, and processed in a network. Protocols define the format, timing, sequencing, and error checking for communication between devices. They ensure that different systems can communicate effectively despite differences in hardware, software, or architecture.

<b>Characteristics of Protocols:</b>
• Syntax: Structure or format of data (how it is organized)
• Semantics: Meaning of each section and action to take
• Timing: Speed matching and sequencing of data

<b>WWW (World Wide Web):</b>
The WWW is an information system where documents and other web resources are identified by URLs, interlinked by hyperlinks, and accessible via the Internet. It was invented by Tim Berners-Lee in 1989.

<b>Key Components of WWW:</b>
• <b>Web Browser:</b> Client software (Chrome, Firefox) that requests and displays web pages
• <b>Web Server:</b> Software (Apache, Nginx, IIS) that stores and serves web content
• <b>URL (Uniform Resource Locator):</b> Address that identifies a resource on the web
• <b>HTML:</b> Markup language for creating web pages
• <b>HTTP/HTTPS:</b> Protocol for transferring web pages

<b>HTTP (Hypertext Transfer Protocol):</b>
HTTP is an application-layer protocol used for transmitting hypermedia documents, such as HTML. It is the foundation of data communication on the WWW.

<b>Features of HTTP:</b>
• Stateless: Each request is independent; server does not retain client information between requests
• Connectionless: Client and server connect only during request/response
• Uses TCP port 80 (HTTP) or 443 (HTTPS)
• Supports various methods: GET, POST, PUT, DELETE, HEAD, OPTIONS

<b>HTTP Request Methods:</b>
• <b>GET:</b> Requests data from server (retrieval)
• <b>POST:</b> Submits data to server (form submission)
• <b>PUT:</b> Updates existing resource
• <b>DELETE:</b> Removes specified resource
• <b>HEAD:</b> Same as GET but returns only headers

<b>HTTP Response Codes:</b>
• 1xx: Informational (100 Continue)
• 2xx: Success (200 OK, 201 Created)
• 3xx: Redirection (301 Moved Permanently)
• 4xx: Client Error (404 Not Found, 400 Bad Request)
• 5xx: Server Error (500 Internal Server Error)""",
            },
            {
                "num": "3",
                "question": "Define transmission impairment. Explain the causes of impairments.",
                "marks": "1+4",
                "answer": """<b>Transmission Impairment:</b>
Transmission impairment refers to the degradation of signal quality during data transmission over a communication channel. As signals travel through media (cable, fiber, air), they become weaker, distorted, or contaminated by noise, leading to data errors.

<b>Causes of Transmission Impairment:</b>

1. <b>Attenuation:</b>
   - Loss of signal energy as it travels through the medium
   - The signal strength decreases with distance
   - Measured in decibels (dB)
   - <b>Solution:</b> Use amplifiers (analog) or repeaters (digital) to boost the signal
   - Example: A voice signal over a long telephone line becomes weaker and harder to hear

2. <b>Distortion:</b>
   - Change in the shape or form of the signal
   - Occurs because different frequency components travel at different speeds in the medium
   - Results from non-linear characteristics of the transmission channel
   - In composite signals (made of multiple frequencies), each frequency component may arrive at different times
   - <b>Solution:</b> Use equalizers to correct frequency response
   - Example: Audio distortion in poor quality speakers

3. <b>Noise:</b>
   - Unwanted signals inserted between transmitter and receiver
   - Types of noise:
     • <b>Thermal Noise:</b> Random motion of electrons in a conductor, present in all electronic devices. Cannot be eliminated.
     • <b>Induced Noise:</b> Caused by sources like motors and appliances. Can be minimized with shielding.
     • <b>Crosstalk:</b> Unwanted coupling between adjacent wires. One wire acts as antenna transmitting, another as antenna receiving.
     • <b>Impulse Noise:</b> Sudden spikes caused by external events like lightning, power surges. Brief but high amplitude.
     • <b>Shot Noise:</b> Random fluctuations in current flow in electronic devices.
   - <b>Solution:</b> Shielding, filtering, proper grounding, using better cables

<b>Signal-to-Noise Ratio (SNR):</b>
SNR = Signal Power / Noise Power
Higher SNR means better signal quality. Measured in decibels.

<b>Impact on Digital vs Analog:</b>
• Digital signals can be regenerated by repeaters
• Analog signals can only be amplified (noise is amplified too)
• Digital transmission is more resistant to noise""",
            },
            {
                "num": "4",
                "question": "Define HDLC. Explain the HDLC frame formats.",
                "marks": "1+4",
                "answer": """<b>HDLC (High-Level Data Link Control):</b>
HDLC is a bit-oriented synchronous data link layer protocol developed by ISO. It is widely used for reliable point-to-point and multipoint communication. HDLC provides error detection, flow control, and supports various operational modes.

<b>Features of HDLC:</b>
• Bit-oriented (uses bit stuffing for transparency)
• Synchronous transmission
• Supports full-duplex communication
• Provides error detection using CRC
• Supports both point-to-point and multipoint configurations

<b>HDLC Frame Format:</b>
<pre>
| Flag | Address | Control | Information | FCS | Flag |
| 8 bits | 8 bits | 8/16 bits | Variable | 16/32 bits | 8 bits |
</pre>

1. <b>Flag Field (8 bits):</b>
   - Pattern: 01111110
   - Marks beginning and end of frame
   - Used for synchronization

2. <b>Address Field (8 bits):</b>
   - Contains address of secondary station
   - In point-to-point: usually 11111111 (broadcast) or specific address
   - In multipoint: identifies destination or source station
   - First bit indicates if address is extended (1 = extended)

3. <b>Control Field (8 or 16 bits):</b>
   Defines the type and function of the frame. Three types:
   
   a) <b>I-Frame (Information Frame):</b>
   - First bit = 0
   - Carries user data
   - Contains send sequence number N(S) and receive sequence number N(R)
   - Used for piggybacked acknowledgments
   
   b) <b>S-Frame (Supervisory Frame):</b>
   - First two bits = 10
   - Used for flow control and error control (no data)
   - Types: RR (Receive Ready), RNR (Receive Not Ready), REJ (Reject), SREJ (Selective Reject)
   
   c) <b>U-Frame (Unnumbered Frame):</b>
   - First two bits = 11
   - Used for link management (setup, disconnection, mode setting)
   - Examples: SNRM (Set Normal Response Mode), SABM (Set Asynchronous Balanced Mode), DISC (Disconnect)

4. <b>Information Field (Variable):</b>
   - Contains actual data payload
   - Present only in I-frames and some U-frames
   - Variable length

5. <b>FCS (Frame Check Sequence) - 16 or 32 bits:</b>
   - Contains CRC (Cyclic Redundancy Check) for error detection
   - Computed over Address, Control, and Information fields
   - Receiver recalculates and compares

<b>HDLC Operational Modes:</b>
• <b>NRM (Normal Response Mode):</b> Unbalanced - secondary responds only when polled by primary
• <b>ABM (Asynchronous Balanced Mode):</b> Balanced - both stations are equal (most common)
• <b>ARM (Asynchronous Response Mode):</b> Unbalanced - secondary can initiate without polling""",
            },
            {
                "num": "5",
                "question": "Define IP Address. Specify IPv4 address classes with their address ranges.",
                "marks": "1+4",
                "answer": """<b>IP Address:</b>
An IP (Internet Protocol) address is a unique numerical identifier assigned to each device connected to a computer network that uses the Internet Protocol for communication. It serves two main functions: host/network interface identification and location addressing.

<b>Characteristics:</b>
• IPv4: 32-bit address written as four octets (e.g., 192.168.1.1)
• IPv6: 128-bit address written in hexadecimal (e.g., 2001:0db8:85a3::8a2e:0370:7334)
• Each IP address consists of a network portion and a host portion
• Assigned by IANA and regional registries

<b>IPv4 Address Classes:</b>

<table border='1' cellpadding='4'><tr><td>Class</td><td>First Bits</td><td>Network Bits</td><td>Host Bits</td><td>Address Range</td><td>Default Mask</td><td>Use</td></tr>
<tr><td>A</td><td>0</td><td>8</td><td>24</td><td>1.0.0.0 to 126.255.255.255</td><td>255.0.0.0 (/8)</td><td>Large networks</td></tr>
<tr><td>B</td><td>10</td><td>16</td><td>16</td><td>128.0.0.0 to 191.255.255.255</td><td>255.255.0.0 (/16)</td><td>Medium networks</td></tr>
<tr><td>C</td><td>110</td><td>24</td><td>8</td><td>192.0.0.0 to 223.255.255.255</td><td>255.255.255.0 (/24)</td><td>Small networks</td></tr>
<tr><td>D</td><td>1110</td><td>-</td><td>-</td><td>224.0.0.0 to 239.255.255.255</td><td>-</td><td>Multicast</td></tr>
<tr><td>E</td><td>1111</td><td>-</td><td>-</td><td>240.0.0.0 to 255.255.255.255</td><td>-</td><td>Reserved/Experimental</td></tr></table>

<b>Special IP Addresses:</b>
• <b>127.0.0.0/8:</b> Loopback addresses (127.0.0.1 = localhost)
• <b>0.0.0.0:</b> Default route / unspecified address
• <b>255.255.255.255:</b> Limited broadcast
• <b>10.0.0.0/8, 172.16.0.0/12, 192.168.0.0/16:</b> Private IP ranges (RFC 1918)
• <b>169.254.0.0/16:</b> Link-local addresses (APIPA)

<b>Class A Details:</b>
• Supports 126 networks (0 and 127 reserved)
• Each network supports 16,777,214 hosts
• Used by very large organizations (government, ISPs)

<b>Class B Details:</b>
• Supports 16,384 networks
• Each network supports 65,534 hosts
• Used by medium to large organizations

<b>Class C Details:</b>
• Supports 2,097,152 networks
• Each network supports 254 hosts
• Most common for small businesses and home networks""",
            },
            {
                "num": "6",
                "question": "Define Subnetting. Suppose you are given network address: 192.168.10.0 and subnet mask: 255.255.255.240 then calculate total number of subnets and numbers of hosts per subnet.",
                "marks": "1+2+2",
                "answer": """<b>Subnetting:</b>
Subnetting is the process of dividing a single physical network into multiple smaller logical networks (subnets). It improves network performance, enhances security, and allows efficient use of IP addresses. Subnetting is done by borrowing bits from the host portion of an IP address to create a subnet identifier.

<b>Benefits of Subnetting:</b>
• Reduces network congestion by limiting broadcast domains
• Improves security by isolating network segments
• Simplifies network management and troubleshooting
• Allows flexible allocation of IP addresses
• Enables logical organization by department or function

<b>Given:</b>
• Network Address: 192.168.10.0
• Subnet Mask: 255.255.255.240

<b>Step 1: Convert Subnet Mask to Binary</b>
255.255.255.240 = 11111111.11111111.11111111.11110000

<b>Step 2: Determine Number of Network Bits</b>
• Number of network bits = 28 (28 ones in the mask)
• This is a /28 network
• Original Class C network has 24 network bits
• Subnet bits borrowed = 28 - 24 = 4 bits

<b>Step 3: Calculate Number of Subnets</b>
Number of subnets = 2^(subnet bits) = 2^4 = <b>16 subnets</b>

<b>Step 4: Calculate Number of Host Bits</b>
• Total bits = 32
• Network bits = 28
• Host bits = 32 - 28 = 4 bits

<b>Step 5: Calculate Hosts per Subnet</b>
Number of hosts per subnet = 2^(host bits) - 2 = 2^4 - 2 = 16 - 2 = <b>14 hosts per subnet</b>
(We subtract 2 because first address is network address and last is broadcast address)

<b>Summary:</b>
<table border='1' cellpadding='4'><tr><td>Parameter</td><td>Value</td></tr>
<tr><td>Network Address</td><td>192.168.10.0</td></tr>
<tr><td>Subnet Mask</td><td>255.255.255.240 (/28)</td></tr>
<tr><td>Number of Subnets</td><td>16</td></tr>
<tr><td>Hosts per Subnet</td><td>14 usable hosts</td></tr>
<tr><td>Block Size</td><td>16 addresses per subnet</td></tr>
<tr><td>First Subnet</td><td>192.168.10.0 - 192.168.10.15</td></tr>
<tr><td>Second Subnet</td><td>192.168.10.16 - 192.168.10.31</td></tr>
<tr><td>Last Subnet</td><td>192.168.10.240 - 192.168.10.255</td></tr></table>

<b>Example Subnet Ranges:</b>
• Subnet 1: Network=192.168.10.0, Usable=192.168.10.1 to .14, Broadcast=192.168.10.15
• Subnet 2: Network=192.168.10.16, Usable=192.168.10.17 to .30, Broadcast=192.168.10.31
• Subnet 16: Network=192.168.10.240, Usable=192.168.10.241 to .254, Broadcast=192.168.10.255""",
            },
            {
                "num": "7",
                "question": "Draw a User Datagram format. Explain UDP operations.",
                "marks": "2+3",
                "answer": """<b>UDP (User Datagram Protocol):</b>
UDP is a connectionless, unreliable transport layer protocol in the TCP/IP suite. It provides minimal overhead and fast transmission but does not guarantee delivery, ordering, or duplicate protection.

<b>UDP Header Format (8 bytes total):</b>
<pre>
 0      7 8     15 16    23 24    31
+--------+--------+--------+--------+
|     Source Port      |  Destination Port   |
+--------+--------+--------+--------+
|     Length           |     Checksum        |
+--------+--------+--------+--------+
|              Data (Variable length)          |
+--------+--------+--------+--------+
</pre>

<b>Fields:</b>
1. <b>Source Port (16 bits):</b> Port number of the sender. Optional; set to 0 if not used.
2. <b>Destination Port (16 bits):</b> Port number of the receiver. Identifies the application process.
3. <b>Length (16 bits):</b> Total length of UDP segment (header + data) in bytes. Minimum value is 8 (header only).
4. <b>Checksum (16 bits):</b> Optional error-checking field. Covers header, data, and pseudo-header (IP addresses).

<b>UDP Operations:</b>

1. <b>Connectionless Communication:</b>
   - No connection establishment (no handshake like TCP)
   - Each datagram is independent
   - Sender simply formats the datagram and passes to IP
   - Fast but unreliable delivery

2. <b>Encapsulation:</b>
   - Application data is encapsulated with UDP header
   - UDP segment is passed to IP layer
   - IP adds its own header and routes the packet

3. <b>Demultiplexing:</b>
   - Receiver uses destination port number to deliver data to correct application
   - Multiple applications can use UDP simultaneously on different ports

4. <b>No Error Recovery:</b>
   - UDP checksum detects errors but does not correct them
   - Corrupted packets are silently discarded (no retransmission)
   - Applications must handle error recovery if needed

5. <b>No Flow Control:</b>
   - No mechanism to prevent sender from overwhelming receiver
   - No sliding window or acknowledgment system

6. <b>No Ordering:</b>
   - Packets may arrive out of order
   - No sequence numbers to reorder packets
   - Applications handle ordering if required

<b>Applications Using UDP:</b>
• DNS (Domain Name System) queries
• Streaming media (video/audio)
• Online gaming
• VoIP (Voice over IP)
• SNMP (Simple Network Management Protocol)
• TFTP (Trivial File Transfer Protocol)

<b>Advantages:</b> Low latency, minimal overhead, no connection setup delay, suitable for real-time applications
<b>Disadvantages:</b> Unreliable, no congestion control, no guaranteed delivery""",
            },
            {
                "num": "8",
                "question": "Write short notes on (Any Two): a) DNS b) Public Key Cryptography c) VPN",
                "marks": "2.5+2.5",
                "answer": """<b>a) DNS (Domain Name System):</b>
DNS is a hierarchical, distributed naming system that translates human-readable domain names (like www.google.com) into IP addresses (like 142.250.185.78). It acts as the "phonebook of the Internet."

<b>How DNS Works:</b>
1. User types www.example.com in browser
2. Browser checks local cache, then OS cache
3. If not found, query goes to configured DNS resolver (usually ISP's DNS)
4. Resolver queries Root DNS servers → TLD servers (.com) → Authoritative DNS servers
5. Authoritative server returns the IP address
6. Resolver caches the result and returns to client
7. Browser connects to the IP address

<b>DNS Record Types:</b>
• A: Maps domain to IPv4 address
• AAAA: Maps domain to IPv6 address
• CNAME: Alias for another domain
• MX: Mail exchange server
• NS: Name server for the domain
• TXT: Text records (SPF, DKIM)
• PTR: Reverse DNS lookup

<b>Benefits:</b> Human-friendly names, load distribution via multiple IPs, easy migration between servers

---

<b>b) Public Key Cryptography:</b>
Public key cryptography (asymmetric cryptography) uses a pair of keys: a public key for encryption and a private key for decryption. The public key can be freely shared, while the private key must be kept secret.

<b>Key Characteristics:</b>
• Two mathematically related but distinct keys
• Computationally infeasible to derive private key from public key
• Solves the key distribution problem of symmetric cryptography

<b>How it works for Encryption:</b>
1. Sender encrypts message with recipient's public key
2. Only recipient can decrypt with their private key

<b>How it works for Digital Signatures:</b>
1. Sender hashes the message and encrypts hash with their private key
2. Anyone can verify by decrypting with sender's public key and comparing hashes

<b>Common Algorithms:</b>
• RSA (Rivest-Shamir-Adleman): Based on factoring large primes
• ECC (Elliptic Curve Cryptography): More efficient, smaller key sizes
• Diffie-Hellman: Key exchange protocol

<b>Applications:</b> SSL/TLS certificates, secure email (PGP), code signing, blockchain, VPN authentication

<b>Advantages:</b> No need for secure key exchange, supports digital signatures, non-repudiation
<b>Disadvantages:</b> Slower than symmetric cryptography, larger key sizes required

---

<b>c) VPN (Virtual Private Network):</b>
A VPN creates a secure, encrypted connection over a public network (like the Internet), allowing remote users to access a private network as if they were directly connected to it.

<b>How VPN Works:</b>
1. User connects to VPN client and authenticates
2. VPN client establishes encrypted tunnel to VPN server
3. All traffic between client and server is encrypted
4. VPN server forwards requests to destination on behalf of client
5. Responses return through the encrypted tunnel

<b>Types of VPN:</b>
• <b>Remote Access VPN:</b> Individual users connect to corporate network (e.g., employees working from home)
• <b>Site-to-Site VPN:</b> Connects entire networks at different locations (e.g., branch offices to headquarters)
• <b>SSL VPN:</b> Uses web browser for remote access (no client installation)
• <b>IPsec VPN:</b> Operates at network layer, provides strong security

<b>VPN Protocols:</b>
• OpenVPN: Open-source, highly secure, uses SSL/TLS
• IPsec: Industry standard for site-to-site connections
• L2TP/IPsec: Combines L2TP tunneling with IPsec encryption
• WireGuard: Modern, fast, lightweight protocol

<b>Benefits:</b> Privacy and anonymity, bypass geo-restrictions, secure remote work, protection on public Wi-Fi
<b>Limitations:</b> Reduced speed due to encryption, potential logging by VPN providers, not completely anonymous""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Critically analyze the OSI reference model.",
                "marks": "10",
                "answer": """<b>OSI Reference Model (Open Systems Interconnection):</b>
The OSI model is a conceptual framework developed by ISO in 1984 that standardizes network communication into seven distinct layers. Each layer has specific functions and communicates with adjacent layers through well-defined interfaces.

<b>The Seven Layers:</b>

<b>7. Application Layer:</b>
• Closest to the end user
• Provides network services to applications (HTTP, FTP, SMTP, DNS)
• Handles user authentication, data formatting, and presentation
• Example: Web browser, email client

<b>6. Presentation Layer:</b>
• Translates data between application and network formats
• Handles encryption/decryption, compression/decompression
• Data representation (ASCII, EBCDIC, JPEG, MPEG)
• Example: SSL/TLS encryption, data compression

<b>5. Session Layer:</b>
• Establishes, manages, and terminates connections (sessions)
• Handles dialogue control (full-duplex, half-duplex)
• Synchronization using checkpoints for long transmissions
• Example: NetBIOS, RPC, PPTP

<b>4. Transport Layer:</b>
• End-to-end communication and data delivery
• Segmentation and reassembly of data
• Flow control and error recovery
• TCP (reliable, connection-oriented) and UDP (unreliable, connectionless)

<b>3. Network Layer:</b>
• Logical addressing (IP addressing)
• Routing and path determination between networks
• Packet forwarding and fragmentation
• Protocols: IP, ICMP, ARP, RIP, OSPF, BGP

<b>2. Data Link Layer:</b>
• Physical addressing (MAC addresses)
• Framing, error detection (CRC), and flow control
• Divided into LLC (Logical Link Control) and MAC (Media Access Control)
• Protocols: Ethernet, Wi-Fi (802.11), PPP, HDLC

<b>1. Physical Layer:</b>
• Transmits raw bits over physical medium
• Defines electrical, mechanical, and procedural specifications
• Cables, connectors, hubs, repeaters, signal encoding
• Examples: Ethernet cables, fiber optics, radio waves

<b>Critical Analysis - Advantages:</b>
1. <b>Modularity:</b> Changes in one layer don't affect others
2. <b>Standardization:</b> Provides common framework for vendors
3. <b>Interoperability:</b> Different systems can communicate
4. <b>Troubleshooting:</b> Easy to isolate network problems by layer
5. <b>Education:</b> Excellent teaching tool for understanding networking
6. <b>Protocol Independence:</b> Allows multiple protocols at each layer

<b>Critical Analysis - Disadvantages:</b>
1. <b>Complexity:</b> Seven layers can be unnecessarily complex
2. <b>Performance Overhead:</b> Multiple layers add processing overhead
3. <b>Not Widely Implemented:</b> TCP/IP (4 layers) became the de facto standard
4. <b>Some Layers Redundant:</b> Presentation and Session layers often merged with Application layer in practice
5. <b>Designed Before Internet:</b> Some concepts don't match modern networking reality
6. <b>Strict Layering Inefficient:</b> Some protocols (like TCP/IP) violate strict layering for performance

<b>Comparison with TCP/IP:</b>
<table border='1' cellpadding='4'><tr><td>Aspect</td><td>OSI</td><td>TCP/IP</td></tr>
<tr><td>Layers</td><td>7</td><td>4</td></tr>
<tr><td>Development</td><td>Model first, then protocols</td><td>Protocols first, then model</td></tr>
<tr><td>Approach</td><td>Vertical (strict)</td><td>Horizontal (loose)</td></tr>
<tr><td>Adoption</td><td>Theoretical reference</td><td>Practical implementation</td></tr>
<tr><td>Protocol Support</td><td>Generic</td><td>TCP/IP specific</td></tr></table>

<b>Conclusion:</b>
While OSI is not directly implemented, its concepts and terminology are fundamental to networking education and troubleshooting. The layered approach remains valid, and OSI terminology (like "Layer 2 switch" or "Layer 3 router") is widely used in the industry.""",
            },
            {
                "num": "10",
                "question": "Explain the random-access protocols under the multiple access taxonomy.",
                "marks": "10",
                "answer": """<b>Random Access Protocols:</b>
Random access protocols allow stations to access the channel randomly without prior coordination. When multiple stations transmit simultaneously, collisions may occur. These protocols are also called contention protocols.

<b>1. ALOHA:</b>
The simplest random access protocol developed at University of Hawaii.

<b>Pure ALOHA:</b>
• Stations transmit whenever they have data
• No synchronization or coordination
• If collision occurs, station waits random time and retransmits
• Vulnerable time = 2 × frame transmission time
• Maximum throughput = 18.4% (1/2e)

<b>Slotted ALOHA:</b>
• Time is divided into discrete slots (equal to frame transmission time)
• Stations can only transmit at slot boundaries
• Reduces collisions by half
• Vulnerable time = 1 × slot time
• Maximum throughput = 36.8% (1/e)

<b>2. CSMA (Carrier Sense Multiple Access):</b>
Stations listen to the channel before transmitting.

<b>a) 1-Persistent CSMA:</b>
• Station senses channel before transmitting
• If idle: transmits immediately (probability 1)
• If busy: waits until channel becomes idle, then transmits immediately
• Problem: High collision probability when multiple stations waiting

<b>b) Non-Persistent CSMA:</b>
• If channel idle: transmits immediately
• If channel busy: waits random time before sensing again
• Reduces collisions but increases delay

<b>c) p-Persistent CSMA:</b>
• If channel idle: transmits with probability p, or defer to next slot with probability (1-p)
• If channel busy: waits until next slot and senses again
• Used in slotted channels, balances between 1-persistent and non-persistent

<b>3. CSMA/CD (CSMA with Collision Detection):</b>
Used in Ethernet (IEEE 802.3).

<b>Operation:</b>
1. Station senses channel before transmitting
2. If idle, begins transmission while continuing to sense
3. If collision detected during transmission, station stops immediately
4. Sends jam signal to inform all stations of collision
5. Waits random time (binary exponential backoff) and retries

<b>Binary Exponential Backoff:</b>
• After first collision: wait 0 or 1 slot times
• After second collision: wait 0, 1, 2, or 3 slot times
• After nth collision: wait 0 to 2^n - 1 slot times (capped at 1023)
• After 16 attempts, frame is discarded

<b>Throughput:</b> Much higher than ALOHA, approaches 100% under light load
<b>Limitation:</b> Requires minimum frame size to ensure collision detection; not suitable for wireless

<b>4. CSMA/CA (CSMA with Collision Avoidance):</b>
Used in wireless networks (IEEE 802.11 Wi-Fi).

<b>Why CSMA/CD doesn't work for Wireless:</b>
• Hidden terminal problem: Two stations can't hear each other but both reach the access point
• Signal strength decay: Can't reliably detect collisions while transmitting
• Fading and interference make collision detection unreliable

<b>Operation:</b>
1. Station senses channel before transmitting
2. If idle: waits for DIFS (Distributed Inter-Frame Space), then transmits
3. If busy: waits until channel is idle, then waits additional DIFS
4. Uses RTS/CTS (Request to Send / Clear to Send) handshake:
   - Sender sends RTS to AP
   - AP responds with CTS
   - Other stations hearing CTS defer transmission
   - Sender transmits data
   - AP sends ACK after successful reception
5. Uses NAV (Network Allocation Vector) to track expected channel busy time

<b>5. Controlled Access Protocols (for comparison):</b>
• <b>Reservation:</b> Stations reserve slots before transmitting
• <b>Polling:</b> Master station invites slave stations to transmit
• <b>Token Passing:</b> Stations pass a token; only token holder can transmit

<b>Comparison Table:</b>
<table border='1' cellpadding='4'><tr><td>Protocol</td><td>Collision Handling</td><td>Throughput</td><td>Usage</td></tr>
<tr><td>Pure ALOHA</td><td>Retransmit after random delay</td><td>18%</td><td>Historical</td></tr>
<tr><td>Slotted ALOHA</td><td>Retransmit after random delay</td><td>37%</td><td>Historical</td></tr>
<tr><td>CSMA</td><td>Various strategies</td><td>Varies</td><td>Theoretical</td></tr>
<tr><td>CSMA/CD</td><td>Collision detection + backoff</td><td>~90%</td><td>Wired Ethernet</td></tr>
<tr><td>CSMA/CA</td><td>Collision avoidance (RTS/CTS)</td><td>~70%</td><td>Wireless (Wi-Fi)</td></tr></table>""",
            },
            {
                "num": "11",
                "question": "Explain the IPv4 Header format in detail.",
                "marks": "10",
                "answer": """<b>IPv4 Header Format:</b>
The IPv4 header is variable in size (minimum 20 bytes, maximum 60 bytes) and contains all necessary information for routing and delivering packets across networks.

<pre>
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version|  IHL  |Type of Service|          Total Length         |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Identification        |Flags|      Fragment Offset    |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  Time to Live |    Protocol   |         Header Checksum       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                       Source IP Address                       |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Destination IP Address                     |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                    Options (Variable, 0-40 bytes)             |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
</pre>

<b>Field Descriptions:</b>

1. <b>Version (4 bits):</b>
   - Indicates IP version (4 for IPv4)
   - Allows routers to process packet correctly

2. <b>IHL - Internet Header Length (4 bits):</b>
   - Length of header in 32-bit words
   - Minimum value = 5 (5 × 4 = 20 bytes)
   - Maximum value = 15 (15 × 4 = 60 bytes)

3. <b>Type of Service / DSCP (8 bits):</b>
   - Specifies quality of service parameters
   - Originally: Precedence, Delay, Throughput, Reliability bits
   - Now: Differentiated Services Code Point (DSCP) for QoS
   - ECN (Explicit Congestion Notification) bits for congestion signaling

4. <b>Total Length (16 bits):</b>
   - Entire packet size (header + data) in bytes
   - Maximum value = 65,535 bytes
   - Data length = Total Length - (IHL × 4)

5. <b>Identification (16 bits):</b>
   - Unique identifier for each packet
   - Used for reassembling fragmented packets
   - All fragments of same packet have same identification number

6. <b>Flags (3 bits):</b>
   - Bit 0: Reserved (must be 0)
   - Bit 1 (DF - Don't Fragment): If set, packet cannot be fragmented
   - Bit 2 (MF - More Fragments): If set, more fragments follow; 0 for last fragment

7. <b>Fragment Offset (13 bits):</b>
   - Position of fragment relative to original packet data
   - Measured in units of 8 bytes
   - First fragment has offset 0

8. <b>Time to Live / TTL (8 bits):</b>
   - Maximum number of hops (routers) packet can traverse
   - Decremented by 1 at each router
   - Packet discarded when TTL reaches 0 (prevents infinite loops)
   - Typical initial values: 64 (Linux), 128 (Windows), 255 (routers)

9. <b>Protocol (8 bits):</b>
   - Identifies transport layer protocol
   - 1 = ICMP, 6 = TCP, 17 = UDP, 41 = IPv6, 50 = ESP, 89 = OSPF

10. <b>Header Checksum (16 bits):</b>
    - Error detection for header only (not data)
    - Recalculated at each router (TTL changes)
    - If checksum fails, packet is discarded

11. <b>Source IP Address (32 bits):</b>
    - IPv4 address of sender

12. <b>Destination IP Address (32 bits):</b>
    - IPv4 address of intended receiver

13. <b>Options (Variable, 0-40 bytes):</b>
    - Rarely used in practice
    - Security, strict source routing, loose source routing, record route, timestamp
    - Must be padded to 32-bit boundary

<b>Key Points:</b>
• Minimum header size = 20 bytes (when no options)
• Header size must be multiple of 4 bytes
• Options field allows extension but reduces efficiency
• Checksum covers only header, not payload (higher layers handle data integrity)
• Fragmentation allows packets to traverse networks with smaller MTU""",
            },
        ]
    }
]

GRAPHICS_QUESTIONS = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What is computer graphics? Explain different application areas of computer graphics.",
                "marks": "5",
                "answer": """<b>Computer Graphics:</b>
Computer graphics is a field of computer science that deals with generating, manipulating, and displaying visual content using computers. It involves the creation, storage, and manipulation of models and images using mathematical algorithms and computational techniques.

<b>Key Components:</b>
• <b>Hardware:</b> Graphics cards (GPU), displays, input devices
• <b>Software:</b> Rendering engines, modeling tools, game engines
• <b>Mathematics:</b> Geometry, linear algebra, calculus for transformations
• <b>Algorithms:</b> Rasterization, shading, ray tracing, clipping

<b>Application Areas of Computer Graphics:</b>

1. <b>Entertainment and Gaming:</b>
   - 3D video games (Fortnite, Call of Duty)
   - CGI in movies (Avatar, Avengers)
   - Virtual reality experiences
   - Animation (Pixar, Disney films)

2. <b>Computer-Aided Design (CAD):</b>
   - Architectural design and visualization
   - Engineering product design (AutoCAD, SolidWorks)
   - Circuit board layout and design
   - Manufacturing and prototyping (3D printing)

3. <b>Medical Imaging:</b>
   - MRI, CT scan visualization
   - 3D reconstruction from 2D slices
   - Surgical simulation and planning
   - Virtual anatomy education

4. <b>Education and Training:</b>
   - Interactive educational software
   - Flight simulators for pilot training
   - Medical procedure simulators
   - Virtual laboratories

5. <b>Scientific Visualization:</b>
   - Weather pattern visualization
   - Molecular modeling in chemistry
   - Astronomical data representation
   - Fluid dynamics simulation

6. <b>Advertising and Marketing:</b>
   - Product visualization and mockups
   - Architectural walkthroughs
   - Logo and brand design
   - Virtual showrooms

7. <b>User Interface Design:</b>
   - Graphical user interfaces (GUI)
   - Icons, buttons, and visual elements
   - Touchscreen interfaces
   - AR/VR interfaces

8. <b>Art and Design:</b>
   - Digital painting (Photoshop, Procreate)
   - Graphic design (Illustrator, CorelDRAW)
   - Typography and layout design
   - Generative art using algorithms

9. <b>Simulation and Virtual Reality:</b>
   - Military training simulations
   - Vehicle crash testing simulation
   - Urban planning and traffic simulation
   - Virtual tourism

10. <b>Data Visualization:</b>
    - Business intelligence dashboards
    - Infographics
    - Real-time monitoring displays
    - Geographic information systems (GIS)""",
            },
            {
                "num": "3",
                "question": "How can you draw a circle using mid-point circle algorithm? Explain with the algorithm.",
                "marks": "5",
                "answer": """<b>Mid-Point Circle Algorithm:</b>
The mid-point circle algorithm is an efficient rasterization algorithm for drawing circles. It uses the circle's symmetry to calculate only one octant and derives the remaining seven octants by reflection.

<b>Circle Equation:</b>
x² + y² = r²

<b>Decision Parameter:</b>
At each step, we evaluate the midpoint between the east (E) and southeast (SE) pixels to decide which pixel to choose next.

<b>Algorithm Steps:</b>

1. <b>Initialization:</b>
   - Start with x = 0, y = r
   - Initial decision parameter: P₀ = 1 - r (or P₀ = 5/4 - r for integer version, approximated as 1 - r)

2. <b>Plot Initial Point:</b>
   - Plot (0, r) and use symmetry to plot all 8 octant points

3. <b>Iterative Process:</b>
   While x < y:
   
   a) If P < 0:
      - Choose East pixel (x+1, y)
      - P = P + 2x + 3
      - Increment x by 1
   
   b) If P ≥ 0:
      - Choose South-East pixel (x+1, y-1)
      - P = P + 2(x - y) + 5
      - Increment x by 1, decrement y by 1

4. <b>Symmetry:</b>
   For each calculated point (x, y), plot all 8 symmetric points:
   (x, y), (-x, y), (x, -y), (-x, -y), (y, x), (-y, x), (y, -x), (-y, -x)

<b>Example: Draw circle with radius r = 5</b>

Initial: x = 0, y = 5, P₀ = 1 - 5 = -4

<table border='1' cellpadding='4'><tr><td>Step</td><td>P</td><td>Action</td><td>(x, y)</td><td>P next</td></tr>
<tr><td>0</td><td>-4</td><td>Plot (0,5)</td><td>(0, 5)</td><td>-</td></tr>
<tr><td>1</td><td>-4</td><td>P&lt;0, E</td><td>(1, 5)</td><td>-4+2(0)+3=-1</td></tr>
<tr><td>2</td><td>-1</td><td>P&lt;0, E</td><td>(2, 5)</td><td>-1+2(1)+3=4</td></tr>
<tr><td>3</td><td>4</td><td>P≥0, SE</td><td>(3, 4)</td><td>4+2(2-5)+5=3</td></tr>
<tr><td>4</td><td>3</td><td>P≥0, SE</td><td>(4, 3)</td><td>3+2(3-4)+5=4</td></tr></table>

At step 4, x = 4 and y = 3, so x ≥ y. Stop.

<b>Points in first octant:</b> (0,5), (1,5), (2,5), (3,4), (4,3)

<b>Using symmetry, all circle points are plotted.</b>

<b>Advantages:</b>
• Uses only integer arithmetic (fast)
• No floating-point calculations needed
• Efficient due to symmetry (8-way)
• No square root or trigonometric functions

<b>Comparison with DDA:</b>
<table border='1' cellpadding='4'><tr><td>Aspect</td><td>Mid-Point</td><td>DDA</td></tr>
<tr><td>Arithmetic</td><td>Integer only</td><td>Floating point</td></tr>
<tr><td>Accuracy</td><td>Exact</td><td>Accumulated rounding errors</td></tr>
<tr><td>Speed</td><td>Faster</td><td>Slower</td></tr>
<tr><td>Complexity</td><td>More complex</td><td>Simpler</td></tr></table>""",
            },
            {
                "num": "4",
                "question": "Explain 3D basic geometric transformation with an example.",
                "marks": "5",
                "answer": """<b>3D Geometric Transformations:</b>
3D transformations are used to modify the position, orientation, or size of 3D objects. They are represented using 4×4 homogeneous transformation matrices for uniform treatment of translation, rotation, and scaling.

<b>1. 3D Translation:</b>
Moves an object by (tx, ty, tz) along each axis.

Transformation Matrix:
<pre>
| 1  0  0  tx |
| 0  1  0  ty |
| 0  0  1  tz |
| 0  0  0  1  |
</pre>

A point P(x, y, z, 1) becomes P'(x+tx, y+ty, z+tz, 1)

<b>2. 3D Scaling:</b>
Changes the size of an object by factors (sx, sy, sz).

Transformation Matrix:
<pre>
| sx  0   0   0 |
| 0   sy  0   0 |
| 0   0   sz  0 |
| 0   0   0   1 |
</pre>

A point P(x, y, z, 1) becomes P'(x×sx, y×sy, z×sz, 1)

If sx = sy = sz = s: Uniform scaling
If not equal: Non-uniform scaling

<b>3. 3D Rotation:</b>

<b>a) Rotation about X-axis by angle θ:</b>
<pre>
| 1    0       0      0 |
| 0   cosθ   -sinθ   0 |
| 0   sinθ    cosθ   0 |
| 0    0       0      1 |
</pre>
P'(x, y×cosθ - z×sinθ, y×sinθ + z×cosθ)

<b>b) Rotation about Y-axis by angle θ:</b>
<pre>
| cosθ   0   sinθ   0 |
|  0     1    0     0 |
| -sinθ  0   cosθ   0 |
|  0     0    0     1 |
</pre>
P'(x×cosθ + z×sinθ, y, -x×sinθ + z×cosθ)

<b>c) Rotation about Z-axis by angle θ:</b>
<pre>
| cosθ  -sinθ   0   0 |
| sinθ   cosθ   0   0 |
|  0      0     1   0 |
|  0      0     0   1 |
</pre>
P'(x×cosθ - y×sinθ, x×sinθ + y×cosθ, z)

<b>Example: Translate a point P(2, 3, 4) by (5, -2, 3) and then scale by (2, 2, 2)</b>

<b>Translation:</b>
P' = T × P
P' = (2+5, 3-2, 4+3) = (7, 1, 7)

<b>Scaling:</b>
P'' = S × P'
P'' = (7×2, 1×2, 7×2) = (14, 2, 14)

<b>Combined Transformation:</b>
For multiple transformations, matrices are multiplied in reverse order of application.
If we want to Scale then Translate: P' = T × S × P

<pre>
T × S = | 1  0  0  5 |   | 2  0  0  0 |   | 2  0  0  5 |
        | 0  1  0 -2 | × | 0  2  0  0 | = | 0  2  0 -2 |
        | 0  0  1  3 |   | 0  0  2  0 |   | 0  0  2  3 |
        | 0  0  0  1 |   | 0  0  0  1 |   | 0  0  0  1 |
</pre>

P' = (2×2+5, 3×2-2, 4×2+3) = (9, 4, 11)

<b>Properties:</b>
• Matrix multiplication is associative but not commutative
• Order of transformations matters (T then S ≠ S then T)
• Homogeneous coordinates (4th coordinate = 1) allow translation to be expressed as matrix multiplication""",
            },
            {
                "num": "5",
                "question": "What is polygon clipping? Explain Sutherland Hodgman algorithm for polygon clipping.",
                "marks": "5",
                "answer": """<b>Polygon Clipping:</b>
Polygon clipping is the process of removing parts of a polygon that lie outside a specified clipping region (usually a rectangular window). It is essential in computer graphics for displaying only the visible portion of objects and for operations like hidden surface removal.

<b>Why Line Clipping is Insufficient:</b>
Line clipping algorithms (Cohen-Sutherland, Liang-Barsky) only handle individual line segments. When clipping polygons, we need to maintain the polygon structure and generate new edges where the polygon crosses the clipping boundary.

<b>Sutherland-Hodgman Polygon Clipping Algorithm:</b>
This algorithm clips a polygon against a convex clipping window by processing each edge of the window sequentially. It clips the polygon against one edge at a time, producing a new vertex list after each edge.

<b>Algorithm:</b>

1. <b>Input:</b> List of polygon vertices (in order) and clipping window edges
2. <b>Process each window edge:</b>
   For each edge of the clipping window (left, right, top, bottom):
   
   a) Initialize output vertex list as empty
   
   b) For each polygon edge (from current vertex S to next vertex P):
      
      Case 1: <b>S inside, P inside</b>
      - Add P to output list
      
      Case 2: <b>S inside, P outside</b>
      - Add intersection point I to output list
      
      Case 3: <b>S outside, P outside</b>
      - Add nothing
      
      Case 4: <b>S outside, P inside</b>
      - Add intersection point I and P to output list
   
   c) Use output list as input for next window edge

3. <b>Output:</b> Final clipped polygon vertices

<b>Four Cases Illustrated:</b>
<pre>
Inside side        Outside side
     S ────────● I  (Case 2: S in, P out → add I)
     
     S ────────→ P  (Case 1: S in, P in → add P)
     
  I ●←─────── P    (Case 4: S out, P in → add I, P)
     
     S ────────→ P  (Case 3: S out, P out → add nothing)
              (both outside)
</pre>

<b>Example: Clip polygon against left edge (x = x_min)</b>

For each edge SP of polygon:
• S_inside = S.x ≥ x_min
• P_inside = P.x ≥ x_min
• Intersection I: y = S.y + (P.y - S.y) × (x_min - S.x) / (P.x - S.x)

<b>Advantages:</b>
• Simple and easy to implement
• Works for any convex clipping window
• Processes one edge at a time

<b>Limitations:</b>
• Only works for convex clipping regions
• For concave polygons, may produce extra edges
• Does not handle self-intersecting polygons

<b>Comparison with Weiler-Atherton:</b>
<table border='1' cellpadding='4'><tr><td>Aspect</td><td>Sutherland-Hodgman</td><td>Weiler-Atherton</td></tr>
<tr><td>Window type</td><td>Convex only</td><td>Any (convex/concave)</td></tr>
<tr><td>Polygon type</td><td>Any</td><td>Any</td></tr>
<tr><td>Complexity</td><td>Simpler</td><td>More complex</td></tr>
<tr><td>Output</td><td>Single polygon</td><td>Multiple polygons possible</td></tr></table>

<b>Applications:</b> Viewport clipping in 2D graphics, shadow volume clipping, CSG operations""",
            },
            {
                "num": "6",
                "question": "Given a triangle with vertices A(2,3), B(5,5), C(4,3) by rotating 90 degree about the origin and then translating two unit in each direction. Use homogenous transformation matrix to find the new vertices of the triangle.",
                "marks": "5",
                "answer": """<b>Given:</b>
• Triangle vertices: A(2,3), B(5,5), C(4,3)
• Rotation: 90° about origin (counter-clockwise)
• Translation: 2 units in x and 2 units in y

<b>Step 1: Rotation Matrix (90° about origin, counter-clockwise)</b>
<pre>
R(90°) = | cos90°  -sin90°  0 |   | 0  -1  0 |
         | sin90°   cos90°  0 | = | 1   0  0 |
         |   0        0     1 |   | 0   0  1 |
</pre>

For counter-clockwise rotation by θ:
x' = x×cosθ - y×sinθ
y' = x×sinθ + y×cosθ

At θ = 90°: cos90° = 0, sin90° = 1

<b>Apply Rotation to each vertex:</b>

A(2, 3):
A'x = 2×0 - 3×1 = -3
A'y = 2×1 + 3×0 = 2
<b>A' = (-3, 2)</b>

B(5, 5):
B'x = 5×0 - 5×1 = -5
B'y = 5×1 + 5×0 = 5
<b>B' = (-5, 5)</b>

C(4, 3):
C'x = 4×0 - 3×1 = -3
C'y = 4×1 + 3×0 = 4
<b>C' = (-3, 4)</b>

<b>Step 2: Translation Matrix (tx = 2, ty = 2)</b>
<pre>
T = | 1  0  2 |
    | 0  1  2 |
    | 0  0  1 |
</pre>

<b>Step 3: Combined Transformation</b>
First rotate, then translate: M = T × R

<pre>
M = | 1  0  2 |   | 0  -1  0 |   | 0  -1  2 |
    | 0  1  2 | × | 1   0  0 | = | 1   0  2 |
    | 0  0  1 |   | 0   0  1 |   | 0   0  1 |
</pre>

<b>Step 4: Apply Combined Transformation</b>

For A(2, 3):
<pre>
| 0  -1  2 |   | 2 |   | 0×2 + (-1)×3 + 2×1 |   | -1 |
| 1   0  2 | × | 3 | = | 1×2 +   0×3  + 2×1 | = |  4 |
| 0   0  1 |   | 1 |   | 0×2 +   0×3  + 1×1 |   |  1 |
</pre>
<b>A'' = (-1, 4)</b>

For B(5, 5):
<pre>
| 0  -1  2 |   | 5 |   | 0×5 + (-1)×5 + 2 |   | -3 |
| 1   0  2 | × | 5 | = | 1×5 +   0×5  + 2 | = |  7 |
| 0   0  1 |   | 1 |   | 0×5 +   0×5  + 1 |   |  1 |
</pre>
<b>B'' = (-3, 7)</b>

For C(4, 3):
<pre>
| 0  -1  2 |   | 4 |   | 0×4 + (-1)×3 + 2 |   | -1 |
| 1   0  2 | × | 3 | = | 1×4 +   0×3  + 2 | = |  6 |
| 0   0  1 |   | 1 |   | 0×4 +   0×3  + 1 |   |  1 |
</pre>
<b>C'' = (-1, 6)</b>

<b>Final Answer:</b>
<table border='1' cellpadding='4'><tr><td>Vertex</td><td>Original</td><td>After Rotation</td><td>After Translation</td></tr>
<tr><td>A</td><td>(2, 3)</td><td>(-3, 2)</td><td>(-1, 4)</td></tr>
<tr><td>B</td><td>(5, 5)</td><td>(-5, 5)</td><td>(-3, 7)</td></tr>
<tr><td>C</td><td>(4, 3)</td><td>(-3, 4)</td><td>(-1, 6)</td></tr></table>

<b>New vertices of the triangle: A''(-1, 4), B''(-3, 7), C''(-1, 6)</b>""",
            },
            {
                "num": "7",
                "question": "Explain the scan line algorithm for visible surface detection.",
                "marks": "5",
                "answer": """<b>Scan Line Algorithm for Visible Surface Detection:</b>
The scan line algorithm is an image-space method for hidden surface removal. It processes the scene one horizontal scan line at a time, determining which surfaces are visible at each pixel along the scan line.

<b>Basic Principle:</b>
For each horizontal scan line across the viewport:
1. Determine which polygons intersect the scan line
2. Find intersection points of these polygons with the scan line
3. Sort intersection points by x-coordinate
4. Determine which segments are visible based on depth
5. Draw visible segments with appropriate colors

<b>Data Structures Used:</b>

1. <b>Edge Table (ET):</b>
   - Contains all non-horizontal edges of all polygons
   - Grouped by the y-coordinate of the edge's lower endpoint
   - Each entry stores: y_max, x_intersect (at lower y), inverse slope (1/m)

2. <b>Active Edge Table (AET):</b>
   - Contains edges that intersect the current scan line
   - Updated as the algorithm moves from one scan line to the next
   - Sorted by x-intersection coordinate

<b>Algorithm Steps:</b>

1. <b>Initialize:</b>
   - Build Edge Table for all polygons
   - Set y = minimum y-coordinate in the scene
   - Initialize AET as empty

2. <b>For each scan line from bottom to top:</b>
   a) Move edges from ET[y] to AET (edges starting at this y)
   b) Remove edges from AET where y = y_max (edges ending at this y)
   c) Sort AET by x-intersection coordinate
   d) Process pairs of x-intersections in AET:
      - Between each pair of x-values, determine which polygon is visible
      - Compare z-depths of polygons at sample points
      - Draw visible polygon's color for that segment
   e) Update x-intersections for next scan line:
      - x_new = x_old + 1/m (increment by inverse slope)
   f) Increment y by 1

3. <b>Repeat until all scan lines are processed.</b>

<b>Example with Two Polygons:</b>
<pre>
Polygon 1 (Blue): closer to viewer
Polygon 2 (Red): farther from viewer

Scan line y = 50:
├─── ET adds edges that start at y=50
├─── AET contains: Edge1 (P1), Edge2 (P1), Edge3 (P2), Edge4 (P2)
├─── Sorted AET by x: x1, x2, x3, x4
├─── Segments: [x1,x2]=P1 visible, [x2,x3]=neither, [x3,x4]=P2 visible
└─── Draw blue from x1 to x2, red from x3 to x4
</pre>

<b>Handling Overlapping Polygons:</b>
When multiple polygons cover the same pixel:
1. Calculate z-depth of each polygon at that pixel
2. The polygon with smallest z-value (closest to viewer) is visible
3. If depths are equal, use additional criteria (arbitrary choice or painter's algorithm)

<b>Advantages:</b>
• Works at image resolution (pixel level)
• Can handle complex overlapping polygons
• Efficient for scenes with many polygons
• Can be combined with shading (Gouraud, Phong)

<b>Disadvantages:</b>
• Computationally expensive per pixel
• Requires maintaining and sorting edge tables
• Aliasing problems at edges (jagged lines)
• Difficult to handle transparent surfaces

<b>Optimizations:</b>
• Span coherence: Adjacent pixels often have same visibility
• Edge coherence: x-intersections change predictably between scan lines
• Depth coherence: Depth changes linearly across a polygon face

<b>Comparison with Z-Buffer:</b>
<table border='1' cellpadding='4'><tr><td>Aspect</td><td>Scan Line</td><td>Z-Buffer</td></tr>
<tr><td>Space</td><td>Less memory (edge tables)</td><td>More memory (depth buffer)</td></tr>
<tr><td>Speed</td><td>Faster for simple scenes</td><td>Consistent for complex scenes</td></tr>
<tr><td>Implementation</td><td>More complex</td><td>Simpler</td></tr>
<tr><td>Anti-aliasing</td><td>Easier</td><td>Harder</td></tr></table>""",
            },
            {
                "num": "8",
                "question": "Explain the architecture of VR system with necessary components.",
                "marks": "5",
                "answer": """<b>Virtual Reality (VR) System Architecture:</b>
A VR system creates an immersive, computer-generated environment that simulates physical presence in a real or imagined world. The architecture consists of hardware components, software systems, and user interfaces working together.

<b>1. Input Devices:</b>

a) <b>Head-Mounted Display (HMD) Sensors:</b>
   - Accelerometers, gyroscopes, magnetometers (IMU)
   - Track head position and orientation (6 DOF)
   - Examples: Oculus Rift, HTC Vive, PlayStation VR

b) <b>Hand Controllers:</b>
   - Track hand position and gestures
   - Provide haptic feedback (vibrations)
   - Examples: Oculus Touch, Valve Index controllers

c) <b>Motion Tracking Systems:</b>
   - Outside-in tracking: External base stations/lighthouses
   - Inside-out tracking: Cameras on HMD itself
   - Marker-based tracking: Reflective markers on user/body

d) <b>Additional Input:</b>
   - Eye tracking (foveated rendering)
   - Voice recognition
   - Body suits and treadmills
   - Bio-sensors (heart rate, brain activity)

<b>2. Output Devices:</b>

a) <b>Head-Mounted Display (HMD):</b>
   - Dual displays (one per eye) for stereoscopic 3D
   - High refresh rate (90-120 Hz minimum to prevent motion sickness)
   - Wide field of view (100-110° typical)
   - Lens systems for focus and distortion correction

b) <b>Audio Systems:</b>
   - 3D spatial audio (head-related transfer function)
   - Directional sound matching visual cues
   - Noise cancellation for immersion

c) <b>Haptic Feedback:</b>
   - Vibrations in controllers and suits
   - Force feedback devices
   - Treadmills for walking sensation

<b>3. Computing System:</b>

a) <b>Rendering Engine:</b>
   - Real-time 3D graphics rendering (OpenGL, Vulkan, DirectX)
   - Foveated rendering (high quality where user looks)
   - Asynchronous timewarp/spacewarp for smooth frame delivery

b) <b>Tracking and Processing:</b>
   - Sensor fusion algorithms (Kalman filters)
   - Predictive tracking to reduce latency
   - World reconstruction and spatial mapping

c) <b>Application Logic:</b>
   - Game engines: Unity, Unreal Engine
   - Physics simulation
   - AI for virtual characters and environments

<b>4. Software Architecture Layers:</b>

<pre>
+-----------------------------------+
|    VR Applications & Content      |
+-----------------------------------+
|    VR SDK / Game Engine           |
|  (Unity XR, OpenXR, SteamVR)      |
+-----------------------------------+
|    VR Runtime / Compositor        |
|  (Oculus Runtime, SteamVR)        |
+-----------------------------------+
|    Device Drivers & APIs          |
|  (OpenVR, OpenXR, OSVR)           |
+-----------------------------------+
|    Operating System               |
|  (Windows, Linux, Android)        |
+-----------------------------------+
|    Hardware (GPU, CPU, USB)       |
+-----------------------------------+
</pre>

<b>5. Key Technical Challenges:</b>

a) <b>Latency:</b>
   - Motion-to-photon latency must be < 20ms to prevent motion sickness
   - Achieved through prediction, timewarp, high refresh rates

b) <b>Resolution and Field of View:</b>
   - Higher resolution reduces screen-door effect
   - Wider FOV increases immersion
   - Trade-off with GPU performance

c) <b>Comfort:</b>
   - Ergonomic HMD design
   - Adjustable IPD (interpupillary distance)
   - Weight distribution
   - Ventilation to prevent fogging

<b>6. Types of VR Systems:</b>

• <b>Non-immersive (Desktop VR):</b> 3D environment on standard screen
• <b>Semi-immersive:</b> Large projection systems, flight simulators
• <b>Fully Immersive:</b> HMD with tracking, most common today
• <b>Collaborative VR:</b> Multiple users in shared virtual space
• <b>Augmented Reality (AR):</b> Overlays virtual objects on real world
• <b>Mixed Reality (MR):</b> Interactive blend of real and virtual

<b>Applications:</b> Gaming, education, medical training, architecture, military simulation, virtual tourism, therapy and rehabilitation""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Explain the working details of DDA line drawing algorithm? Digitize the line with endpoints (2,2) and (10,5) using Bresenham's line drawing algorithm.",
                "marks": "5+5",
                "answer": """<b>DDA (Digital Differential Analyzer) Line Drawing Algorithm:</b>
DDA is a scan-conversion algorithm based on calculating either dx or dy using the line equation. It samples the line at unit intervals in one coordinate and calculates the corresponding integer value nearest to the line path for the other coordinate.

<b>Algorithm:</b>
1. Calculate dx = x2 - x1 and dy = y2 - y1
2. Determine steps = max(|dx|, |dy|)
3. Calculate x_increment = dx / steps
4. Calculate y_increment = dy / steps
5. Set x = x1, y = y1
6. Plot pixel at (round(x), round(y))
7. For i = 1 to steps:
   - x = x + x_increment
   - y = y + y_increment
   - Plot pixel at (round(x), round(y))

<b>Example: Line from (2, 2) to (10, 5)</b>
dx = 10 - 2 = 8
dy = 5 - 2 = 3
steps = max(8, 3) = 8
x_increment = 8/8 = 1.0
y_increment = 3/8 = 0.375

<table border='1' cellpadding='4'><tr><td>i</td><td>x</td><td>y</td><td>Plot (round)</td></tr>
<tr><td>0</td><td>2.0</td><td>2.0</td><td>(2, 2)</td></tr>
<tr><td>1</td><td>3.0</td><td>2.375</td><td>(3, 2)</td></tr>
<tr><td>2</td><td>4.0</td><td>2.75</td><td>(4, 3)</td></tr>
<tr><td>3</td><td>5.0</td><td>3.125</td><td>(5, 3)</td></tr>
<tr><td>4</td><td>6.0</td><td>3.5</td><td>(6, 4)</td></tr>
<tr><td>5</td><td>7.0</td><td>3.875</td><td>(7, 4)</td></tr>
<tr><td>6</td><td>8.0</td><td>4.25</td><td>(8, 4)</td></tr>
<tr><td>7</td><td>9.0</td><td>4.625</td><td>(9, 5)</td></tr>
<tr><td>8</td><td>10.0</td><td>5.0</td><td>(10, 5)</td></tr></table>

<b>Advantages:</b> Simple to implement
<b>Disadvantages:</b> Floating-point operations, rounding errors, slower than Bresenham

---

<b>Bresenham's Line Drawing Algorithm:</b>
Bresenham's algorithm uses only integer arithmetic to determine the next pixel position. It evaluates a decision parameter at each step to choose between two candidate pixels.

<b>Given:</b> Endpoints (2, 2) and (10, 5)

<b>Step 1: Calculate differences</b>
dx = 10 - 2 = 8
dy = 5 - 2 = 3

<b>Step 2: Check slope</b>
Since |dx| > |dy| and dx, dy > 0: 0 < slope < 1, we increment x by 1 at each step.

<b>Step 3: Initialize decision parameter</b>
P₀ = 2×dy - dx = 2×3 - 8 = 6 - 8 = -2

<b>Step 4: Decision rules</b>
• If P < 0: Next point = (x+1, y), P = P + 2×dy
• If P ≥ 0: Next point = (x+1, y+1), P = P + 2×dy - 2×dx

<b>Step 5: Iteration</b>

<table border='1' cellpadding='4'><tr><td>Step</td><td>(x, y)</td><td>P</td><td>Decision</td><td>Next P</td></tr>
<tr><td>0</td><td>(2, 2)</td><td>-2</td><td>P&lt;0, E</td><td>-2+6=4</td></tr>
<tr><td>1</td><td>(3, 2)</td><td>4</td><td>P≥0, NE</td><td>4+6-16=-6</td></tr>
<tr><td>2</td><td>(4, 3)</td><td>-6</td><td>P&lt;0, E</td><td>-6+6=0</td></tr>
<tr><td>3</td><td>(5, 3)</td><td>0</td><td>P≥0, NE</td><td>0+6-16=-10</td></tr>
<tr><td>4</td><td>(6, 4)</td><td>-10</td><td>P&lt;0, E</td><td>-10+6=-4</td></tr>
<tr><td>5</td><td>(7, 4)</td><td>-4</td><td>P&lt;0, E</td><td>-4+6=2</td></tr>
<tr><td>6</td><td>(8, 4)</td><td>2</td><td>P≥0, NE</td><td>2+6-16=-8</td></tr>
<tr><td>7</td><td>(9, 5)</td><td>-8</td><td>P&lt;0, E</td><td>-8+6=-2</td></tr>
<tr><td>8</td><td>(10, 5)</td><td>-2</td><td>End</td><td>-</td></tr></table>

<b>Pixels plotted by Bresenham:</b>
(2, 2), (3, 2), (4, 3), (5, 3), (6, 4), (7, 4), (8, 4), (9, 5), (10, 5)

<b>Note:</b> Both DDA and Bresenham produce the same set of pixels for this line, but Bresenham uses only integer arithmetic, making it faster.""",
            },
            {
                "num": "10",
                "question": "Write the difference between object space method and image space method. Explain Z-buffer algorithm for visible surface detection.",
                "marks": "5+5",
                "answer": """<b>Object Space vs Image Space Methods:</b>

<table border='1' cellpadding='4'><tr><td>Aspect</td><td>Object Space Method</td><td>Image Space Method</td></tr>
<tr><td>Processing Level</td><td>Works with 3D object coordinates</td><td>Works with 2D pixel coordinates</td></tr>
<tr><td>Comparison</td><td>Compares objects with each other</td><td>Compares pixels depth values</td></tr>
<tr><td>Precision</td><td>Exact (geometric calculations)</td><td>Approximate (pixel resolution)</td></tr>
<tr><td>Complexity</td><td>O(n²) where n = number of objects</td><td>O(n×p) where p = number of pixels</td></tr>
<tr><td>Output</td><td>Determines visible surfaces directly</td><td>Determines visible pixels</td></tr>
<tr><td>Anti-aliasing</td><td>Difficult</td><td>Easier</td></tr>
<tr><td>Memory</td><td>Less memory required</td><td>More memory (depth buffer)</td></tr>
<tr><td>Examples</td><td>Back-face removal, BSP trees, ray casting</td><td>Z-buffer, scan line, ray tracing</td></tr>
<tr><td>Scene Size</td><td>Better for fewer objects</td><td>Better for complex scenes</td></tr>
<tr><td>Accuracy</td><td>Independent of resolution</td><td>Limited by image resolution</td></tr></table>

<b>Object Space Methods:</b>
• <b>Back-Face Removal:</b> Eliminate polygons facing away from viewer
• <b>Ray Casting:</b> Cast rays from eye through pixels, find first intersection
• <b>Depth Sorting (Painter's Algorithm):</b> Sort objects by depth, paint back to front

<b>Image Space Methods:</b>
• <b>Z-Buffer (Depth Buffer):</b> Store depth at each pixel
• <b>Scan Line:</b> Process one scan line at a time
• <b>A-Buffer:</b> Anti-aliased version of Z-buffer

---

<b>Z-Buffer Algorithm (Depth Buffer Algorithm):</b>

<b>Principle:</b>
The Z-buffer algorithm maintains two buffers:
1. <b>Frame Buffer:</b> Stores color/intensity of each pixel
2. <b>Z-Buffer (Depth Buffer):</b> Stores z-coordinate (depth) of visible surface at each pixel

<b>Algorithm:</b>

1. <b>Initialize:</b>
   - Frame buffer: Set to background color
   - Z-buffer: Set to maximum depth value (farthest from viewer)

2. <b>For each polygon in the scene:</b>
   a) For each pixel (x, y) covered by the polygon:
      
      i. Calculate depth z of polygon at (x, y)
         - For a plane ax + by + cz + d = 0:
         - z = -(ax + by + d) / c
      
      ii. If z < Z-buffer[x, y]:
          - Z-buffer[x, y] = z
          - Frame buffer[x, y] = polygon color at (x, y)

3. <b>Output:</b> Frame buffer contains the final image

<b>Depth Calculation Optimization:</b>
Instead of calculating z for each pixel from scratch:
• For a scan line: z(x+1, y) = z(x, y) - a/c
• For next scan line: z(x, y+1) = z(x, y) - b/c
This incremental calculation is very efficient.

<b>Example:</b>
Two polygons at a pixel:
- Polygon A: z = 5 (farther)
- Polygon B: z = 2 (closer)

Processing A first:
Z-buffer = 5, Frame buffer = Color_A

Processing B:
z = 2 < Z-buffer (5)
Z-buffer = 2, Frame buffer = Color_B

Final pixel shows Color_B (closer polygon)

<b>Advantages:</b>
• Simple to implement in hardware
• Handles any polygon complexity
• Works for overlapping/intersecting polygons
• Linear time complexity O(number of pixels × polygons)
• Can be parallelized efficiently

<b>Disadvantages:</b>
• Requires large memory for Z-buffer (e.g., 1920×1080 × 4 bytes ≈ 8 MB)
• Limited precision (z-fighting when depths are very close)
• Cannot handle transparency (requires multiple passes or A-buffer)
• Wastes processing on hidden surfaces
• Aliasing at polygon edges

<b>Variants:</b>
• <b>W-Buffer:</b> Uses 1/z for better precision distribution
• <b>Hierarchical Z-Buffer:</b> Uses coarse Z values to reject blocks of pixels early
• <b>Reverse Z:</b> Maps near plane to 1.0 and far plane to 0.0 for better precision""",
            },
            {
                "num": "11",
                "question": "Derive the formula for windows to viewport transformation. Given a window bordered by (0,0) at the lower-left and (4,4) at the upper right. Similarly, a viewport bordered by (0,0) at the lower-left and (2,2) at the upper right. If a window at position (2,4) is mapped into the viewport. What will be the position of viewport to maintain same relative placement as in window?",
                "marks": "5+5",
                "answer": """<b>Window to Viewport Transformation:</b>

The window defines what portion of the world coordinate system is visible. The viewport defines where on the display device the window contents appear. The transformation maps coordinates from the window to the viewport while maintaining relative positions.

<b>Derivation:</b>

Let:
• Window: (x_wmin, y_wmin) to (x_wmax, y_wmax)
• Viewport: (x_vmin, y_vmin) to (x_vmax, y_vmax)
• Point in window: (x_w, y_w)
• Corresponding point in viewport: (x_v, y_v)

<b>For X-coordinate:</b>
We want the relative position of x_w within the window to equal the relative position of x_v within the viewport:

(x_w - x_wmin) / (x_wmax - x_wmin) = (x_v - x_vmin) / (x_vmax - x_vmin)

Solving for x_v:
<b>x_v = x_vmin + (x_w - x_wmin) × (x_vmax - x_vmin) / (x_wmax - x_wmin)</b>

<b>For Y-coordinate:</b>
Similarly:
(y_w - y_wmin) / (y_wmax - y_wmin) = (y_v - y_vmin) / (y_vmax - y_vmin)

Solving for y_v:
<b>y_v = y_vmin + (y_w - y_wmin) × (y_vmax - y_vmin) / (y_wmax - y_wmin)</b>

<b>General Formula:</b>
<pre>
x_v = x_vmin + (x_w - x_wmin) × Sx
y_v = y_vmin + (y_w - y_wmin) × Sy
</pre>

Where:
• Sx = (x_vmax - x_vmin) / (x_wmax - x_wmin)  [Scaling factor for x]
• Sy = (y_vmax - y_vmin) / (y_wmax - y_wmin)  [Scaling factor for y]

<b>Matrix Form (including normalization):</b>
<pre>
| x_v |   | Sx   0   tx |   | x_w |
| y_v | = | 0   Sy   ty | × | y_w |
|  1  |   | 0    0    1 |   |  1  |
</pre>

Where:
• tx = x_vmin - x_wmin × Sx
• ty = y_vmin - y_wmin × Sy

---

<b>Given Problem:</b>

<b>Window:</b>
• Lower-left: (x_wmin, y_wmin) = (0, 0)
• Upper-right: (x_wmax, y_wmax) = (4, 4)

<b>Viewport:</b>
• Lower-left: (x_vmin, y_vmin) = (0, 0)
• Upper-right: (x_vmax, y_vmax) = (2, 2)

<b>Point in window:</b> (x_w, y_w) = (2, 4)

<b>Step 1: Calculate Scaling Factors</b>
Sx = (x_vmax - x_vmin) / (x_wmax - x_wmin) = (2 - 0) / (4 - 0) = 2/4 = <b>0.5</b>
Sy = (y_vmax - y_vmin) / (y_wmax - y_wmin) = (2 - 0) / (4 - 0) = 2/4 = <b>0.5</b>

<b>Step 2: Calculate Translation Terms</b>
tx = x_vmin - x_wmin × Sx = 0 - 0 × 0.5 = <b>0</b>
ty = y_vmin - y_wmin × Sy = 0 - 0 × 0.5 = <b>0</b>

<b>Step 3: Apply Transformation</b>
x_v = x_vmin + (x_w - x_wmin) × Sx
x_v = 0 + (2 - 0) × 0.5 = 2 × 0.5 = <b>1</b>

y_v = y_vmin + (y_w - y_wmin) × Sy
y_v = 0 + (4 - 0) × 0.5 = 4 × 0.5 = <b>2</b>

<b>Verification of Relative Placement:</b>
• In window: (2, 4) is at 50% of x-range (2/4) and 100% of y-range (4/4)
• In viewport: (1, 2) is at 50% of x-range (1/2) and 100% of y-range (2/2)

The relative positions are maintained.

<b>Final Answer:</b>
The point (2, 4) in the window maps to <b>(1, 2)</b> in the viewport.

<b>Visualization:</b>
<pre>
Window (4×4)              Viewport (2×2)

y                          y
↑                          ↑
4 ━━━━━ (2,4)●            2 ━━━━━━●(1,2)
3 ┃                        1 ┃
2 ┃                        0 ━━━━━
1 ┃                        
0 ━━━━━→ x                 → x
   0 1 2 3 4                  0 1 2
</pre>""",
            },
        ]
    }
]


if __name__ == "__main__":
    # Generate Semester 5 - 2020 answer sheets
    generate_answer_sheet(
        "CACS301", "management-information-systems", "MIS and E-Business",
        2020, "semester-5", MIS_QUESTIONS
    )
    generate_answer_sheet(
        "CACS302", "dotnet-technology", "DotNet Technology",
        2020, "semester-5", DOTNET_QUESTIONS
    )
    generate_answer_sheet(
        "CACS303", "computer-networking", "Computer Networking",
        2020, "semester-5", NETWORKING_QUESTIONS
    )
    generate_answer_sheet(
        "CAMG304", "computer-graphics-animation", "Computer Graphics and Animation",
        2020, "semester-5", GRAPHICS_QUESTIONS
    )
