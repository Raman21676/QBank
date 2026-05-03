#!/usr/bin/env python3
"""Generate answer sheet for CACS251 Operating Systems 2019."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS251_2019 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "Explain the functions of operating system.",
                "marks": "5",
                "answer": """<b>Functions of Operating System:</b><br/><br/>
<b>1. Process Management:</b> The OS manages the creation, scheduling, and termination of processes. It allocates CPU time using scheduling algorithms (FCFS, SJF, Round Robin, etc.) and handles inter-process communication and synchronization.<br/><br/>
<b>2. Memory Management:</b> The OS keeps track of memory usage, allocates memory to processes, and deallocates it when no longer needed. It manages virtual memory, paging, segmentation, and swapping to optimize RAM usage.<br/><br/>
<b>3. File Management:</b> The OS provides a file system to store, retrieve, and organize data on storage devices. It handles file creation, deletion, naming, directory structures, permissions, and disk space allocation.<br/><br/>
<b>4. Device Management:</b> The OS manages device communication via device drivers. It handles I/O operations, buffer caching, spooling, and ensures efficient use of peripherals (printers, disks, keyboards).<br/><br/>
<b>5. Security and Access Control:</b> The OS protects system resources and user data through authentication, authorization, encryption, and access control lists (ACL). It prevents unauthorized access and ensures user privacy.<br/><br/>
<b>6. User Interface:</b> The OS provides interfaces for user interaction — Command Line Interface (CLI) and Graphical User Interface (GUI). It abstracts hardware complexity, making the system user-friendly.<br/><br/>
<b>7. Error Detection and Handling:</b> The OS constantly monitors the system for errors (hardware failures, software crashes) and takes corrective actions to maintain stability and reliability.""",
            },
            {
                "num": "3",
                "question": "How does semaphore help in dining philosopher problem?",
                "marks": "5",
                "answer": """<b>Dining Philosopher Problem:</b><br/>
Five philosophers sit around a table with five chopsticks (forks) between them. Each philosopher needs two chopsticks to eat. The problem is to design a solution where no philosopher starves (deadlock-free) and maximum parallelism is achieved.<br/><br/>
<b>Role of Semaphore:</b><br/>
A semaphore is a synchronization variable that controls access to shared resources. In the dining philosopher problem, each chopstick is represented by a binary semaphore (initialized to 1).<br/><br/>
<b>Algorithm:</b><br/>
• Philosopher i picks left chopstick by executing <b>wait(chopstick[i])</b><br/>
• Philosopher i picks right chopstick by executing <b>wait(chopstick[(i+1)%5])</b><br/>
• After eating, philosopher releases both chopsticks using <b>signal(chopstick[i])</b> and <b>signal(chopstick[(i+1)%5])</b><br/><br/>
<b>Deadlock Issue:</b><br/>
If all philosophers pick up their left chopstick simultaneously, they all wait for the right chopstick — deadlock.<br/><br/>
<b>Solution using Semaphore:</b><br/>
1. <b>Limit philosophers:</b> Allow at most 4 philosophers to sit simultaneously using a counting semaphore.<br/>
2. <b>Asymmetric solution:</b> Odd philosophers pick left first, even philosophers pick right first.<br/>
3. <b>Monitor or mutex:</b> Protect the pickup and putdown operations with a mutex so that picking up both forks is an atomic operation.<br/><br/>
Semaphores ensure mutual exclusion and prevent race conditions, providing a structured way to solve synchronization problems.""",
            },
            {
                "num": "4",
                "question": "Consider a system with three resources. Each process needs a maximum of two resources. Prove that deadlock cannot occur. Explain with answer.",
                "marks": "5",
                "answer": """<b>Given:</b><br/>
• Total resources (R) = 3 (of the same type)<br/>
• Maximum need of each process = 2 resources<br/>
• Number of processes can be any<br/><br/>
<b>Proof that Deadlock Cannot Occur:</b><br/><br/>
For deadlock to occur, the four Coffman conditions must hold simultaneously: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.<br/><br/>
Consider the <b>worst-case scenario</b> for deadlock: each process holds one resource and waits for another.<br/><br/>
If there are <b>3 processes</b>, each holding 1 resource, then all 3 resources are allocated. Each process needs 1 more. But since all resources are held, no process can proceed — this seems like deadlock.<br/><br/>
However, the key insight is: <b>if there are only 2 processes</b>, each can hold at most 1 resource (total 2 allocated), leaving 1 resource free. The free resource can be allocated to either process, allowing it to complete and release both resources.<br/><br/>
If there are <b>3 or more processes</b>, at least one process must be able to obtain 2 resources because the maximum need is 2 and there are 3 resources total. The system can always satisfy at least one process completely, which then releases its resources for others.<br/><br/>
<b>General Proof:</b><br/>
Let n = number of processes, R = 3, Max = 2.<br/>
If each process holds (Max - 1) = 1 resource, total held = n.<br/>
For deadlock, we need n ≥ R (all resources held). So n ≥ 3.<br/>
But if n = 2, total held = 2, leaving 1 free. One process gets the free resource, finishes, and releases 2 resources.<br/>
If n ≥ 3, the pigeonhole principle ensures at least one process can get its full requirement (2) because not all processes can simultaneously hold exactly 1 and block — the OS can allocate the third resource to any waiting process.<br/><br/>
<b>Conclusion:</b> Since the maximum need (2) is less than the total resources (3), the system can always find at least one process that can be satisfied completely, preventing deadlock.""",
            },
            {
                "num": "5",
                "question": "If processes arrive at an average of six processes per minute and each requires 8 seconds of service time. Estimate the fraction of time the CPU is busy. [M/M/1 queue problem]",
                "marks": "5",
                "answer": """<b>Given (M/M/1 Queue):</b><br/>
• Arrival rate (λ) = 6 processes per minute = 6/60 = <b>0.1 processes/second</b><br/>
• Service time = 8 seconds per process<br/>
• Service rate (μ) = 1 / 8 = <b>0.125 processes/second</b><br/><br/>
<b>Traffic Intensity (ρ):</b><br/>
ρ = λ / μ = 0.1 / 0.125 = <b>0.8</b><br/><br/>
<b>Interpretation:</b><br/>
Traffic intensity ρ represents the fraction of time the CPU is busy (utilization).<br/><br/>
<b>Fraction of time CPU is busy = ρ = 0.8 = 80%</b><br/><br/>
<b>Additional Metrics (for completeness):</b><br/>
• Average number of processes in system (L) = ρ / (1 - ρ) = 0.8 / 0.2 = <b>4 processes</b><br/>
• Average time in system (W) = 1 / (μ - λ) = 1 / 0.025 = <b>40 seconds</b><br/>
• Average number in queue (Lq) = ρ² / (1 - ρ) = 0.64 / 0.2 = <b>3.2 processes</b><br/><br/>
<b>Conclusion:</b> The CPU is busy 80% of the time and idle 20% of the time.""",
            },
            {
                "num": "6",
                "question": "Consider the page reference string: 8,2,3,8,3. A program has three page frames for each of the processes. Determine which pages are replaced using FIFO page replacement algorithm.",
                "marks": "5",
                "answer": """<b>Given:</b><br/>
• Page reference string: 8, 2, 3, 8, 3<br/>
• Number of page frames: 3<br/>
• Algorithm: FIFO (First In First Out)<br/><br/>
<b>Page Replacement Trace:</b><br/>
<table border='1' cellpadding='4'>
<tr><td>Reference</td><td>8</td><td>2</td><td>3</td><td>8</td><td>3</td></tr>
<tr><td>Frame 1</td><td>8*</td><td>8</td><td>8</td><td>8</td><td>8</td></tr>
<tr><td>Frame 2</td><td>-</td><td>2*</td><td>2</td><td>2</td><td>2</td></tr>
<tr><td>Frame 3</td><td>-</td><td>-</td><td>3*</td><td>3</td><td>3</td></tr>
<tr><td>Page Fault</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr>
</table><br/>
* indicates page loaded into memory.<br/><br/>
<b>Step-by-step:</b><br/>
1. <b>Reference 8:</b> Memory is empty. Load 8 into Frame 1. <b>Page Fault</b><br/>
2. <b>Reference 2:</b> 2 not in memory. Load 2 into Frame 2. <b>Page Fault</b><br/>
3. <b>Reference 3:</b> 3 not in memory. Load 3 into Frame 3. <b>Page Fault</b><br/>
4. <b>Reference 8:</b> 8 is already in Frame 1. <b>No Page Fault</b><br/>
5. <b>Reference 3:</b> 3 is already in Frame 3. <b>No Page Fault</b><br/><br/>
<b>Result:</b><br/>
• Total page faults = <b>3</b><br/>
• Total hits = <b>2</b><br/>
• No pages are replaced because the reference string contains only 3 unique pages and we have exactly 3 frames. All pages fit into memory without needing replacement.<br/><br/>
<b>Note:</b> If the reference string had more unique pages than frames, the oldest page (the one at the front of the FIFO queue) would be replaced.""",
            },
            {
                "num": "7",
                "question": "What is authentication? How worms are differing from viruses?",
                "marks": "5",
                "answer": """<b>Authentication:</b><br/>
Authentication is the process of verifying the identity of a user, device, or system. It ensures that the entity requesting access is who it claims to be. Common authentication methods include:<br/><br/>
<b>1. Password-based:</b> User provides a secret string known only to them.<br/>
<b>2. Biometric:</b> Uses physical characteristics (fingerprint, iris, face recognition).<br/>
<b>3. Token-based:</b> Uses hardware or software tokens (OTP, smart cards).<br/>
<b>4. Multi-factor Authentication (MFA):</b> Combines two or more methods (password + OTP).<br/><br/>
<b>Difference between Worms and Viruses:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Aspect</b></td><td><b>Virus</b></td><td><b>Worm</b></td></tr>
<tr><td>Definition</td><td>A malicious program that attaches itself to a host file or program and requires human action to spread.</td><td>A standalone malicious program that replicates itself and spreads automatically across networks without host attachment.</td></tr>
<tr><td>Host Requirement</td><td>Requires a host file or program to execute.</td><td>Does not require a host file; runs independently.</td></tr>
<tr><td>Spreading Mechanism</td><td>Spreads when the infected file is shared or executed by the user.</td><td>Spreads automatically over networks by exploiting vulnerabilities.</td></tr>
<tr><td>Human Intervention</td><td>Usually requires human action (opening a file) to propagate.</td><td>No human intervention needed; self-propagating.</td></tr>
<tr><td>Speed</td><td>Slow spreading.</td><td>Rapid spreading across networks.</td></tr>
<tr><td>Payload</td><td>May corrupt, delete, or alter files.</td><td>Consumes bandwidth and system resources; may carry payloads.</td></tr>
<tr><td>Examples</td><td>ILOVEYOU, Melissa, Chernobyl (CIH).</td><td>Morris Worm, Conficker, Stuxnet, WannaCry.</td></tr>
</table>""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "8",
                "question": "Explain process scheduling algorithms with examples.",
                "marks": "10",
                "answer": """<b>Process Scheduling Algorithms:</b><br/>
Process scheduling is the mechanism used by the OS to allocate CPU time to processes. The goal is to maximize CPU utilization, throughput, and fairness while minimizing waiting and response time.<br/><br/>
<b>1. First Come First Serve (FCFS):</b><br/>
Processes are executed in the order of their arrival.<br/>
• <b>Example:</b> Processes P1 (burst 24), P2 (burst 3), P3 (burst 3) arrive in order.<br/>
• Gantt Chart: | P1 | P2 | P3 |<br/>
• Waiting times: P1=0, P2=24, P3=27. Average = (0+24+27)/3 = <b>17</b><br/>
• <b>Disadvantage:</b> Convoy effect — short processes wait behind long ones.<br/><br/>
<b>2. Shortest Job First (SJF):</b><br/>
The process with the smallest burst time is executed first.<br/>
• <b>Example:</b> Same processes. Order: P2, P3, P1.<br/>
• Waiting times: P2=0, P3=3, P1=6. Average = <b>3</b><br/>
• <b>Types:</b> Non-preemptive and Preemptive (Shortest Remaining Time First).<br/><br/>
<b>3. Priority Scheduling:</b><br/>
Each process has a priority. The highest priority process runs first.<br/>
• Can be preemptive or non-preemptive.<br/>
• <b>Problem:</b> Starvation of low-priority processes. <b>Solution:</b> Aging (gradually increasing priority of waiting processes).<br/><br/>
<b>4. Round Robin (RR):</b><br/>
Each process gets a small time quantum (e.g., 4 ms). If not finished, it goes to the tail of the ready queue.<br/>
• <b>Example:</b> Time quantum = 4. Processes P1(10), P2(3), P3(3).<br/>
• Gantt: P1 P2 P3 P1 P3 P1 P1<br/>
• Fair for time-sharing systems; no starvation.<br/><br/>
<b>5. Multilevel Queue Scheduling:</b><br/>
Ready queue is divided into multiple queues (e.g., foreground, background). Each queue has its own scheduling algorithm. Fixed priority between queues.<br/><br/>
<b>6. Multilevel Feedback Queue:</b><br/>
Allows processes to move between queues. I/O-bound and interactive processes get higher priority; CPU-bound processes move to lower-priority queues.<br/><br/>
<b>Comparison Table:</b><br/>
<table border='1' cellpadding='4'>
<tr><td>Algorithm</td><td>Type</td><td>Starvation</td><td>Overhead</td></tr>
<tr><td>FCFS</td><td>Non-preemptive</td><td>No</td><td>Low</td></tr>
<tr><td>SJF</td><td>Both</td><td>Yes</td><td>Medium</td></tr>
<tr><td>Priority</td><td>Both</td><td>Yes</td><td>Low</td></tr>
<tr><td>Round Robin</td><td>Preemptive</td><td>No</td><td>Medium</td></tr>
<tr><td>MLFQ</td><td>Preemptive</td><td>No</td><td>High</td></tr>
</table>""",
                "diagram": "Gantt charts should be drawn for each scheduling algorithm to illustrate process execution timelines.",
            },
            {
                "num": "9",
                "question": "Explain memory management techniques (paging and segmentation).",
                "marks": "10",
                "answer": """<b>Memory Management Techniques:</b><br/>
Memory management is the functionality of an OS that handles primary memory. It keeps track of each byte in memory, which part is free or allocated, and how much is allocated.<br/><br/>
<b>1. Paging:</b><br/>
Paging is a fixed-size partitioning scheme that eliminates external fragmentation.<br/><br/>
<b>Concept:</b><br/>
• Physical memory is divided into fixed-size blocks called <b>frames</b>.<br/>
• Logical memory is divided into same-size blocks called <b>pages</b>.<br/>
• The OS maintains a <b>page table</b> for each process, mapping logical pages to physical frames.<br/><br/>
<b>Address Translation:</b><br/>
Logical address = (Page Number, Offset)<br/>
• Page Number indexes the page table to get Frame Number.<br/>
• Physical Address = (Frame Number, Offset)<br/><br/>
<b>Example:</b><br/>
Page size = 4 KB. Logical address space = 16 pages. Physical memory = 32 frames.<br/>
Logical address 0 maps to page 0 → frame 5 → physical address 5 × 4096 + 0 = 20480.<br/><br/>
<b>Advantages:</b> No external fragmentation, simple memory allocation.<br/>
<b>Disadvantages:</b> Internal fragmentation (last page may not fill frame), page table overhead.<br/><br/>
<b>2. Segmentation:</b><br/>
Segmentation is a variable-size partitioning scheme that matches the logical structure of programs.<br/><br/>
<b>Concept:</b><br/>
• A program is divided into segments based on its logical units: code, data, stack, heap, etc.<br/>
• Each segment has a name and length.<br/>
• The OS maintains a <b>segment table</b> containing base (starting physical address) and limit (length) for each segment.<br/><br/>
<b>Address Translation:</b><br/>
Logical address = (Segment Number, Offset)<br/>
• Check if offset < limit. If not, trap (addressing error).<br/>
• Physical Address = Base + Offset<br/><br/>
<b>Example:</b><br/>
Segment 0 (Code): base=1000, limit=600<br/>
Segment 1 (Data): base=2000, limit=400<br/>
Logical address (1, 300) → physical address 2000 + 300 = 2300.<br/><br/>
<b>Advantages:</b> Matches program structure, supports sharing and protection per segment, no internal fragmentation.<br/>
<b>Disadvantages:</b> External fragmentation (variable-size holes), complex allocation.<br/><br/>
<b>Comparison:</b><br/>
<table border='1' cellpadding='4'>
<tr><td>Aspect</td><td>Paging</td><td>Segmentation</td></tr>
<tr><td>Block size</td><td>Fixed (pages)</td><td>Variable (segments)</td></tr>
<tr><td>Fragmentation</td><td>Internal</td><td>External</td></tr>
<tr><td>User awareness</td><td>Transparent</td><td>Visible to programmer</td></tr>
<tr><td>Table</td><td>Page table</td><td>Segment table (base + limit)</td></tr>
<tr><td>Sharing</td><td>Difficult</td><td>Easy (share whole segment)</td></tr>
</table>""",
                "diagram": "Diagrams showing logical to physical address translation using page table and segment table.",
            },
            {
                "num": "10",
                "question": "Explain file system architecture and directory structures.",
                "marks": "10",
                "answer": """<b>File System Architecture:</b><br/>
A file system is a method and data structure that the OS uses to control how data is stored and retrieved on storage devices.<br/><br/>
<b>Layers of File System:</b><br/>
<b>1. Application Programs:</b> User-level programs that interact with files (text editors, browsers).<br/>
<b>2. Logical File System:</b> Manages metadata (file control blocks, directory structures), handles security and protection, and provides the API for file operations (open, read, write, close).<br/>
<b>3. File Organization Module:</b> Knows about files, their logical blocks, and physical blocks. Translates logical block addresses to physical block addresses and manages free space.<br/>
<b>4. Basic File System (Physical I/O):</b> Issues generic commands to device drivers to read/write physical blocks on disk.<br/>
<b>5. I/O Control (Device Drivers):</b> Low-level software that interacts directly with hardware controllers. Handles interrupts, manages device registers.<br/>
<b>6. Devices:</b> Physical storage hardware (HDD, SSD, USB).<br/><br/>
<b>Directory Structures:</b><br/>
A directory is a special file that contains a list of files and subdirectories.<br/><br/>
<b>1. Single-Level Directory:</b><br/>
All files are in one directory.<br/>
• Simple but suffers from naming conflicts and poor organization.<br/><br/>
<b>2. Two-Level Directory:</b><br/>
Separate directory for each user.<br/>
• Path: /username/filename<br/>
• Reduces naming conflicts but no user cooperation.<br/><br/>
<b>3. Tree-Structured Directory:</b><br/>
A root directory with files and subdirectories forming a tree.<br/>
• Path: /home/user/docs/file.txt<br/>
• Supports efficient searching and grouping; most common structure.<br/><br/>
<b>4. Acyclic-Graph Directory:</b><br/>
Allows directories and files to be shared via links (symbolic/hard links).<br/>
• Same file can appear in multiple directories.<br/>
• No cycles allowed to avoid infinite loops.<br/><br/>
<b>5. General Graph Directory:</b><br/>
Allows cycles via links.<br/>
• Requires garbage collection or reference counting to reclaim disk space.<br/>
• More flexible but complex.<br/><br/>
<b>File System Implementation:</b><br/>
• <b>File Allocation Table (FAT):</b> Linked list of blocks stored in a table.<br/>
• <b>Inode (Index Node):</b> UNIX-style structure storing metadata and pointers to data blocks.<br/>
• <b>Extents:</b> Contiguous blocks allocated together for large files.<br/><br/>
<b>Diagram Description:</b> A layered architecture diagram with Application at top, Logical FS, File Organization Module, Basic File System, I/O Control, and Devices at bottom.""",
                "diagram": "Layered file system architecture diagram and tree directory structure diagram.",
            },
        ]
    }
]

if __name__ == "__main__":
    print("Generating CACS251 Operating Systems 2019 answer sheet...")
    generate_answer_sheet("CACS251", "operating-systems", "Operating Systems", 2019, "semester-4", CACS251_2019)
    print("✅ CACS251 2019 answer sheet generated!")
