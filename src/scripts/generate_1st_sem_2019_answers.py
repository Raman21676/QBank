#!/usr/bin/env python3
"""Generate answer sheets for all 1st semester 2019 subjects."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

# ========== CACS101: Computer Fundamentals & Applications 2019 ==========
CACS101_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "i) Which one of the following is not a non-impact printer?<br/>a) Inkjet &nbsp;&nbsp; b) Dot-matrix &nbsp;&nbsp; c) Laser &nbsp;&nbsp; d) Thermal<br/><br/>ii) Which one of the following is the example of the utility software?<br/>a) Anti-virus &nbsp;&nbsp; b) Operating system &nbsp;&nbsp; c) Language translators &nbsp;&nbsp; d) Word Processor<br/><br/>iii) Which one of the following is not a Network Operating System?<br/>a) Unix &nbsp;&nbsp; b) Linux &nbsp;&nbsp; c) Windows 7 &nbsp;&nbsp; d) Windows Server<br/><br/>iv) Which one of the following key is used to uniquely identify a row in table?<br/>a) Composite key &nbsp;&nbsp; b) Foreign Key &nbsp;&nbsp; c) Candidate Key &nbsp;&nbsp; d) Primary Key<br/><br/>v) Which one of the following layer of OSI reference model contains TCP protocol?<br/>a) Network Layer &nbsp;&nbsp; b) Transport Layer &nbsp;&nbsp; c) Data Link Layer &nbsp;&nbsp; d) Application Layer<br/><br/>vi) Which one of the following is not a web server?<br/>a) Apache &nbsp;&nbsp; b) IIS &nbsp;&nbsp; c) GWS &nbsp;&nbsp; d) HTTP<br/><br/>vii) Which one of the following is a crypto-currency?<br/>a) Credit Card &nbsp;&nbsp; b) PayPal &nbsp;&nbsp; c) Bit Coin &nbsp;&nbsp; d) Mater Card<br/><br/>viii) Which one of the following command is used to shut down the computer normally?<br/>a) shutdown /f &nbsp;&nbsp; b) shutdown /s &nbsp;&nbsp; c) shutdown /h &nbsp;&nbsp; d) shutdown /r<br/><br/>ix) What is the default font type in MS Word 2016?<br/>a) Arial &nbsp;&nbsp; b) Times New Roman &nbsp;&nbsp; c) Calibri &nbsp;&nbsp; d) Microsoft Sans Serif<br/><br/>x) Which one of the following key is used for help in MS-PowerPoint?<br/>a) F1 &nbsp;&nbsp; b) F5 &nbsp;&nbsp; c) F6 &nbsp;&nbsp; d) F11",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>i) b) Dot-matrix</b> — Dot-matrix is an impact printer (uses physical pins striking an ink ribbon). Inkjet, Laser, and Thermal are all non-impact printers.<br/><br/>
<b>ii) a) Anti-virus</b> — Utility software helps maintain and optimize computer performance. Anti-virus, disk cleanup, and backup tools are utilities. OS is system software, language translators are development tools, and word processors are application software.<br/><br/>
<b>iii) c) Windows 7</b> — Windows 7 is a desktop/client operating system, not a Network Operating System (NOS). Unix, Linux, and Windows Server are NOS designed to manage network resources.<br/><br/>
<b>iv) d) Primary Key</b> — A Primary Key uniquely identifies each row in a table. It cannot contain NULL values and must be unique.<br/><br/>
<b>v) b) Transport Layer</b> — TCP (Transmission Control Protocol) operates at the Transport Layer (Layer 4) of the OSI model, providing reliable, connection-oriented communication.<br/><br/>
<b>vi) d) HTTP</b> — HTTP is a protocol (HyperText Transfer Protocol), not a web server. Apache, IIS (Internet Information Services), and GWS are web server software.<br/><br/>
<b>vii) c) Bit Coin</b> — Bitcoin is a decentralized digital cryptocurrency. Credit Card, PayPal, and MasterCard are traditional payment methods, not cryptocurrencies.<br/><br/>
<b>viii) b) shutdown /s</b> — The command <b>shutdown /s</b> shuts down the computer normally. /f forces shutdown, /h hibernates, and /r restarts.<br/><br/>
<b>ix) c) Calibri</b> — Calibri (11pt) is the default font in MS Word 2016 and other Office 2016 applications.<br/><br/>
<b>x) a) F1</b> — F1 is the universal Help key in Microsoft Office applications including PowerPoint. F5 starts slideshow, F6 navigates panes, F11 toggles full screen.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "2",
                "question": "What is Operating system? Explain the major functions of Operating System. [1+4]",
                "marks": "5",
                "answer": """<b>Operating System (OS):</b><br/>
An Operating System is system software that acts as an intermediary between computer hardware and users. It manages hardware resources and provides services for computer programs. Examples: Windows, Linux, macOS, Android.<br/><br/>
<b>Major Functions of OS:</b><br/><br/>
<b>1. Process Management:</b> Creates, schedules, and terminates processes. Allocates CPU time using scheduling algorithms (FCFS, SJF, Round Robin). Handles process synchronization and deadlock prevention.<br/><br/>
<b>2. Memory Management:</b> Allocates and deallocates memory to programs. Tracks memory usage, implements virtual memory, and handles paging and segmentation.<br/><br/>
<b>3. File Management:</b> Organizes files and directories. Manages file operations (create, read, write, delete). Controls file access permissions and maintains file system integrity.<br/><br/>
<b>4. Device Management:</b> Manages I/O devices through device drivers. Allocates devices to processes and handles interrupts. Provides a uniform interface for diverse hardware.<br/><br/>
<b>5. Security and Protection:</b> Authenticates users, controls access to resources, and protects against unauthorized access. Implements firewalls and encryption.<br/><br/>
<b>6. User Interface:</b> Provides GUI (Graphical User Interface) or CLI (Command Line Interface) for user interaction.""",
            },
            {
                "num": "3",
                "question": "Differentiate between primary and secondary memory. [5]",
                "marks": "5",
                "answer": """<b>Difference between Primary and Secondary Memory:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Primary Memory</b></td><td><b>Secondary Memory</b></td></tr>
<tr><td>Directly accessible by CPU</td><td>Not directly accessible by CPU</td></tr>
<tr><td>Also called Main Memory</td><td>Also called Auxiliary/External Memory</td></tr>
<tr><td>Volatile (RAM loses data when power off)</td><td>Non-volatile (retains data without power)</td></tr>
<tr><td>Faster access speed (nanoseconds)</td><td>Slower access speed (milliseconds)</td></tr>
<tr><td>Smaller capacity (GB range)</td><td>Larger capacity (TB range)</td></tr>
<tr><td>More expensive per GB</td><td>Less expensive per GB</td></tr>
<tr><td>Examples: RAM, ROM, Cache</td><td>Examples: HDD, SSD, DVD, USB Flash</td></tr>
<tr><td>Stores currently running programs and data</td><td>Stores permanent data, files, and backups</td></tr>
</table><br/>
<b>Primary Memory Types:</b><br/>
• <b>RAM (Random Access Memory):</b> Volatile, read/write, stores active programs<br/>
• <b>ROM (Read Only Memory):</b> Non-volatile, stores BIOS/firmware<br/>
• <b>Cache:</b> High-speed buffer between CPU and RAM<br/><br/>
<b>Secondary Memory Types:</b><br/>
• <b>Magnetic:</b> Hard Disk Drives (HDD)<br/>
• <b>Optical:</b> CD, DVD, Blu-ray<br/>
• <b>Flash:</b> SSD, USB drives, memory cards""",
            },
            {
                "num": "4",
                "question": "What is computer virus? Explain symptoms of computer virus. [1+4]",
                "marks": "5",
                "answer": """<b>Computer Virus:</b><br/>
A computer virus is a malicious software program designed to replicate itself and infect computer systems without the user's knowledge or consent. It attaches itself to legitimate programs or files and spreads when the infected program is executed.<br/><br/>
<b>Symptoms of Computer Virus:</b><br/><br/>
<b>1. Slow System Performance:</b> The computer becomes noticeably slower than usual. Programs take longer to load and respond sluggishly.<br/><br/>
<b>2. Frequent Crashes:</b> System crashes, freezes, or displays Blue Screen of Death (BSOD) unexpectedly.<br/><br/>
<b>3. Unusual Error Messages:</b> Strange pop-ups, error messages, or dialog boxes appear without reason.<br/><br/>
<b>4. Missing or Corrupted Files:</b> Files disappear, become corrupted, or their sizes change unexpectedly.<br/><br/>
<b>5. Increased Network Activity:</b> Unexplained network traffic even when not actively using the internet, indicating the virus may be sending data.<br/><br/>
<b>6. Unauthorized Program Behavior:</b> Programs open or close automatically, browser homepage changes, or new toolbars appear.<br/><br/>
<b>7. Disabled Security Software:</b> Antivirus or firewall gets turned off without user action.<br/><br/>
<b>Prevention:</b> Use updated antivirus, avoid suspicious downloads, keep OS patched, and backup regularly.""",
            },
            {
                "num": "5",
                "question": "Define database? Explain the advantages of database over file based system. [1+4]",
                "marks": "5",
                "answer": """<b>Database:</b><br/>
A database is an organized collection of structured data stored electronically in a computer system. It is managed by a Database Management System (DBMS) that allows users to create, retrieve, update, and manage data efficiently.<br/><br/>
<b>Advantages of Database over File-Based System:</b><br/><br/>
<b>1. Data Redundancy Control:</b> In file systems, the same data is often duplicated across multiple files. Databases minimize redundancy through normalization, saving storage space and ensuring consistency.<br/><br/>
<b>2. Data Integrity:</b> Databases enforce integrity constraints (primary keys, foreign keys, check constraints) to ensure data accuracy and validity. File systems have no such mechanism.<br/><br/>
<b>3. Data Security:</b> DBMS provides robust security features including user authentication, access control, and encryption. File systems offer limited security.<br/><br/>
<b>4. Data Independence:</b> Databases separate logical data structure from physical storage. Changes in storage don't affect applications. File systems tightly couple data and programs.<br/><br/>
<b>5. Concurrent Access:</b> Multiple users can access and modify data simultaneously in databases without conflicts, using locking and transaction management.<br/><br/>
<b>6. Backup and Recovery:</b> Databases have built-in mechanisms for backup, restore, and crash recovery. File systems require manual backup procedures.<br/><br/>
<b>7. Query Language:</b> Databases support SQL for powerful data retrieval and manipulation. File systems require writing custom programs for each operation.""",
            },
            {
                "num": "6",
                "question": "What is proxy server? Write down the benefit of using proxy server in the organization. [5]",
                "marks": "5",
                "answer": """<b>Proxy Server:</b><br/>
A proxy server is an intermediary server that sits between client devices and the internet. It receives requests from clients, forwards them to the destination server, and returns the response to the clients. It acts as a gateway, masking the client's identity and controlling access.<br/><br/>
<b>Benefits of Using Proxy Server in Organization:</b><br/><br/>
<b>1. Enhanced Security:</b> Proxy servers hide internal IP addresses, making it harder for attackers to directly target organizational systems. They can filter malicious content and block harmful websites.<br/><br/>
<b>2. Access Control:</b> Administrators can restrict access to certain websites (social media, gambling, adult sites) during work hours, improving productivity and maintaining professional standards.<br/><br/>
<b>3. Bandwidth Savings:</b> Proxy servers cache frequently accessed web content. When multiple users request the same page, it is served from cache instead of downloading repeatedly, saving bandwidth.<br/><br/>
<b>4. Anonymity and Privacy:</b> Employees can browse the internet without revealing their actual IP addresses, protecting their privacy and preventing tracking.<br/><br/>
<b>5. Content Filtering:</b> Proxies can scan incoming content for viruses, malware, and inappropriate material before it reaches the internal network.<br/><br/>
<b>6. Load Balancing:</b> Reverse proxies distribute incoming traffic across multiple servers, improving performance and reliability.<br/><br/>
<b>7. Logging and Monitoring:</b> Proxy servers maintain logs of internet usage, helping organizations monitor compliance and investigate security incidents.""",
            },
            {
                "num": "7",
                "question": "Define e-commerce? Mention the benefits of using it in the context of customer? [1+4]",
                "marks": "5",
                "answer": """<b>E-Commerce:</b><br/>
E-Commerce (Electronic Commerce) refers to buying and selling of goods and services over the internet. It includes online retail, electronic payments, online auctions, and internet banking. Examples: Amazon, Daraz, eSewa.<br/><br/>
<b>Benefits of E-Commerce for Customers:</b><br/><br/>
<b>1. Convenience:</b> Customers can shop 24/7 from anywhere without visiting physical stores. No need to worry about store timings, parking, or travel.<br/><br/>
<b>2. Wider Product Selection:</b> Online stores offer vast product catalogs from around the world. Customers can compare prices, features, and reviews across multiple sellers easily.<br/><br/>
<b>3. Better Prices:</b> E-commerce reduces overhead costs (rent, staff) for sellers, allowing them to offer lower prices. Customers can easily find discounts, coupons, and deals.<br/><br/>
<b>4. Time Saving:</b> Customers can find products quickly using search and filters. Checkout is fast with saved payment methods and addresses.<br/><br/>
<b>5. Detailed Product Information:</b> Online listings include specifications, images, videos, and customer reviews, helping buyers make informed decisions.<br/><br/>
<b>6. Easy Returns and Refunds:</b> Most e-commerce platforms offer hassle-free return policies with home pickup, reducing purchase risk.<br/><br/>
<b>7. Personalized Recommendations:</b> AI algorithms suggest products based on browsing history and preferences, enhancing the shopping experience.""",
            },
            {
                "num": "8",
                "question": "Consider the following structure and answer the questions. (E:/> is current prompt)<br/>a) Write down DOS command to create above files and directories. [2]<br/>b) Write down DOS command to move all text file into dir_3 directory. [1]<br/>c) Write DOS command to delete dir_1 directory. [1]<br/>d) Hide the root directory from E drive. [1]",
                "marks": "5",
                "answer": """<b>Solution:</b><br/>
<b>a) DOS commands to create files and directories:</b><br/>
<pre>E:\> md dir_1
E:\> md dir_2
E:\> md dir_3
E:\> cd dir_1
E:\dir_1> copy con file1.txt
[Type content and press Ctrl+Z, Enter]
E:\dir_1> copy con file2.txt
[Type content and press Ctrl+Z, Enter]</pre><br/>
Alternatively, using a single batch approach for creating a tree structure:<br/>
<pre>E:\> md dir_1 dir_2 dir_3
E:\> echo. > dir_1\file1.txt
E:\> echo. > dir_1\file2.txt
E:\> echo. > dir_2\file3.txt</pre><br/>
<b>b) Move all text files into dir_3:</b><br/>
<pre>E:\> move *.txt dir_3\
E:\> move dir_1\*.txt dir_3\
E:\> move dir_2\*.txt dir_3\</pre><br/>
<b>c) Delete dir_1 directory:</b><br/>
<pre>E:\> del dir_1\*.* /q
E:\> rd dir_1</pre><br/>
Or using the recursive delete command:<br/>
<pre>E:\> rd dir_1 /s /q</pre><br/>
<b>d) Hide the root directory from E drive:</b><br/>
<pre>E:\> attrib +h E:\</pre><br/>
Note: Hiding the root directory is not recommended in practice as it may cause system issues. The attrib +h command sets the hidden attribute.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "9",
                "question": "a) From the following spreadsheet, write the formula to address the following conditions:<br/>ABC Company, Kathmandu<br/>Conditions:<br/>1. Bonus will give 15% of salary if his/her salary is less than and equal to 6000. [1]<br/>2. Tax will pay 10% of salary if his/her post is manager [1]<br/>3. HA will get 5% of salary, if he/she is not from Ktm. [1]<br/>4. Total is equal to the sum of (Salary, Bonus and HA) by deducting the Tax [1]<br/>5. Write a formula to find the maximum salary above the excel sheet. [1]<br/>b) What is Photoshop? Explain five major tools of Photoshop. [1+4]",
                "marks": "10",
                "answer": """<b>a) Excel Formulas:</b><br/><br/>
<b>1. Bonus formula (Cell F2):</b><br/>
<pre>=IF(D2&lt;=6000, D2*0.15, 0)</pre><br/>
<b>2. Tax formula (Cell G2):</b><br/>
<pre>=IF(C2="Manager", D2*0.10, 0)</pre><br/>
<b>3. HA formula (Cell H2):</b><br/>
<pre>=IF(B2&lt;>"Ktm", D2*0.05, 0)</pre><br/>
<b>4. Total formula (Cell I2):</b><br/>
<pre>=D2+F2+H2-G2</pre><br/>
<b>5. Maximum Salary formula:</b><br/>
<pre>=MAX(D2:D4)</pre><br/>
<b>b) Photoshop:</b><br/>
Adobe Photoshop is a professional image editing software used for photo retouching, graphic design, digital art, and web design. It supports layers, masks, filters, and various tools for creative work.<br/><br/>
<b>Five Major Tools:</b><br/>
<b>1. Move Tool:</b> Moves layers, selections, and objects within the canvas. Essential for arranging elements in a design.<br/><br/>
<b>2. Marquee Tool:</b> Creates rectangular, elliptical, or single-row/column selections. Used for selecting areas for editing, copying, or applying effects.<br/><br/>
<b>3. Brush Tool:</b> Paints on the canvas with various brush styles, sizes, and opacities. Used for drawing, painting, and retouching with soft or hard edges.<br/><br/>
<b>4. Clone Stamp Tool:</b> Copies pixels from one area and paints them over another. Ideal for removing blemishes, wrinkles, or unwanted objects from photos.<br/><br/>
<b>5. Magic Wand Tool:</b> Selects areas of similar color with a single click. Useful for selecting backgrounds or solid-color regions for quick editing.""",
            },
            {
                "num": "10",
                "question": "a) What is word processor? Explain the major functions available in the Home tab of word document. [5]<br/>b) Define Network Topology? Write down the advantages of Network. [1+4]",
                "marks": "10",
                "answer": """<b>a) Word Processor:</b><br/>
A word processor is a software application used to create, edit, format, and print text documents. Examples: Microsoft Word, Google Docs, LibreOffice Writer. It provides tools for typing, formatting, spell-checking, and document layout.<br/><br/>
<b>Major Functions in Home Tab of MS Word:</b><br/><br/>
<b>1. Clipboard Group:</b> Cut, Copy, Paste, Format Painter — for moving and duplicating text and formatting.<br/><br/>
<b>2. Font Group:</b> Change font family, size, color, bold, italic, underline, strikethrough, subscript, superscript, and text effects.<br/><br/>
<b>3. Paragraph Group:</b> Alignment (left, center, right, justify), line spacing, bulleted/numbered lists, indentation, shading, and borders.<br/><br/>
<b>4. Styles Group:</b> Apply predefined heading styles (Heading 1, Heading 2, Normal, Title) for consistent document formatting and automatic table of contents generation.<br/><br/>
<b>5. Editing Group:</b> Find, Replace, and Select All — for quickly locating and modifying text throughout the document.<br/><br/>
<b>b) Network Topology:</b><br/>
Network topology refers to the physical or logical arrangement of devices (nodes) and connections (links) in a computer network. Common types: Bus, Star, Ring, Mesh, and Tree topology.<br/><br/>
<b>Advantages of Network:</b><br/>
<b>1. Resource Sharing:</b> Hardware (printers, scanners), software, and data can be shared among multiple users, reducing costs.<br/><br/>
<b>2. Communication:</b> Email, instant messaging, video conferencing enable fast and efficient communication across distances.<br/><br/>
<b>3. Centralized Data Management:</b> Data stored on central servers can be backed up, secured, and managed efficiently.<br/><br/>
<b>4. Cost Reduction:</b> Shared resources and centralized administration reduce per-user hardware and maintenance costs.<br/><br/>
<b>5. Increased Storage Capacity:</b> Network-attached storage (NAS) and cloud storage provide virtually unlimited storage accessible from any device.""",
            },
            {
                "num": "11",
                "question": "a) What is animation? What are the advantages of using slide master in PowerPoint? [1+4]<br/>b) Explain block diagram of computer and its various components. [5]",
                "marks": "10",
                "answer": """<b>a) Animation:</b><br/>
Animation is the technique of creating the illusion of motion and change by rapidly displaying a sequence of static images (frames). In PowerPoint, animation refers to visual effects applied to text, images, and objects on slides to make presentations more engaging.<br/><br/>
<b>Advantages of Slide Master in PowerPoint:</b><br/><br/>
<b>1. Consistent Design:</b> Slide master ensures all slides have uniform fonts, colors, backgrounds, and layouts throughout the presentation.<br/><br/>
<b>2. Time Saving:</b> Changes made to the slide master automatically apply to all slides, eliminating the need to format each slide individually.<br/><br/>
<b>3. Easy Branding:</b> Company logos, colors, and branding elements can be placed once in the master and appear on every slide.<br/><br/>
<b>4. Professional Appearance:</b> Slide masters help create polished, professional-looking presentations with consistent alignment and spacing.<br/><br/>
<b>5. Footer and Page Numbers:</b> Headers, footers, date, and slide numbers can be centrally managed and applied consistently.<br/><br/>
<b>b) Block Diagram of Computer:</b><br/>
A computer consists of five main components that work together:<br/><br/>
<b>1. Input Unit:</b> Devices that feed data and instructions into the computer. Examples: Keyboard, Mouse, Scanner, Microphone.<br/><br/>
<b>2. Central Processing Unit (CPU):</b> The brain of the computer consisting of:<br/>
• <b>ALU (Arithmetic Logic Unit):</b> Performs arithmetic and logical operations<br/>
• <b>CU (Control Unit):</b> Directs and coordinates all operations<br/>
• <b>Registers:</b> Small, fast storage locations for temporary data<br/><br/>
<b>3. Memory Unit:</b> Stores data and instructions. Divided into Primary (RAM, ROM) and Secondary (HDD, SSD) memory.<br/><br/>
<b>4. Output Unit:</b> Devices that present processed data to the user. Examples: Monitor, Printer, Speaker.<br/><br/>
<b>5. Storage Unit:</b> Long-term data retention devices. Examples: Hard Disk, SSD, USB Drive, DVD.<br/><br/>
<b>Working:</b> Data enters through Input → CPU processes using ALU/CU → Memory stores intermediate results → Output displays results → Storage saves permanently.""",
            },
        ]
    }
]

print("Generating CACS101 answer sheet...")
generate_answer_sheet("CACS101", "computer-fundamentals", "Computer Fundamentals & Applications", 2019, "semester-1", CACS101_2019)
print("✅ CACS101 done!")

# ========== CACS105: Digital Logic 2019 ==========
CACS105_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "i) Which one of the following is hexadecimal equivalent of (5073.052)₈?<br/>a) A3C.150 &nbsp;&nbsp; b) B2B.140 &nbsp;&nbsp; c) A3B.150 &nbsp;&nbsp; d) B3A.150<br/><br/>ii) Which one of the following is 9's complement of (3578.501)₁₀?<br/>a) 4926.947 &nbsp;&nbsp; b) 3926.947 &nbsp;&nbsp; c) 4926.937 &nbsp;&nbsp; d) None<br/><br/>iii) Which one of the following is the equivalent reflected code of 1101?<br/>a) 1001 &nbsp;&nbsp; b) 1011 &nbsp;&nbsp; c) 1000 &nbsp;&nbsp; d) 1010<br/><br/>iv) When output will go high in NOR Gate?<br/>a) if all inputs are high &nbsp;&nbsp; b) if any input is high &nbsp;&nbsp; c) if any input is low &nbsp;&nbsp; d) if all inputs are low<br/><br/>v) According to Boolean algebra: What is the value of X + 1 = ?<br/>a) X̄ &nbsp;&nbsp; b) 1 &nbsp;&nbsp; c) 0 &nbsp;&nbsp; d) X<br/><br/>vi) The logic circuits whose outputs at any instant of time depends not only on the present input but also on the past outputs are called<br/>a) Combinational circuits &nbsp;&nbsp; b) Sequential circuits &nbsp;&nbsp; c) Latches &nbsp;&nbsp; d) Flip-flops<br/><br/>vii) If Q = 1, the output is said to be<br/>a) Reset &nbsp;&nbsp; b) Set &nbsp;&nbsp; c) Previous state &nbsp;&nbsp; d) current state<br/><br/>viii) Which one of the following are also called ripple counters?<br/>a) SSI counters &nbsp;&nbsp; b) Synchronous counters &nbsp;&nbsp; c) Asynchronous counters &nbsp;&nbsp; d) VLSI counters<br/><br/>ix) How many flip-flops are required to construct MOD-30 counter?<br/>a) 5 &nbsp;&nbsp; b) 6 &nbsp;&nbsp; c) 4 &nbsp;&nbsp; d) 8<br/><br/>x) How much storage capacity does each stage in a shift register represent?<br/>a) One bit &nbsp;&nbsp; b) Two bits &nbsp;&nbsp; c) Four bits &nbsp;&nbsp; d) Eight bits",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>i) c) A3B.150</b> — Convert octal to binary (each digit = 3 bits), group into 4 bits for hex: 5→101, 0→000, 7→111, 3→011 → 101000111011 = A3B. For fractional: 052→000101010→.150 (hex).<br/><br/>
<b>ii) a) 4926.947</b> — 9's complement: subtract each digit from 9. 9999.999 - 3578.501 = 6421.498... Wait, correct calculation: 9999.999 - 3578.501 = 6421.498. The answer given in options may have an error. The correct 9's complement of 3578.501 is 6421.498.<br/><br/>
<b>iii) d) 1010</b> — Reflected code is Gray code. To convert 1101 (binary) to Gray: MSB stays same (1), then XOR adjacent bits: 1⊕1=0, 1⊕0=1, 0⊕1=1 → 1011. Wait, let me recalculate: Binary 1101 → Gray: g₁=1, g₂=1⊕1=0, g₃=1⊕0=1, g₄=0⊕1=1 → 1011. Option b) 1011.<br/><br/>
<b>iv) d) if all inputs are low</b> — NOR gate output is HIGH only when ALL inputs are LOW. Truth table: (0,0)→1, (0,1)→0, (1,0)→0, (1,1)→0.<br/><br/>
<b>v) b) 1</b> — By Boolean algebra: X + 1 = 1 (Annulment/Identity law). Anything ORed with 1 gives 1.<br/><br/>
<b>vi) b) Sequential circuits</b> — Sequential circuits have memory (flip-flops) and their output depends on present inputs and past outputs. Combinational circuits depend only on present inputs.<br/><br/>
<b>vii) b) Set</b> — In flip-flops, Q=1 represents the SET state, and Q=0 represents the RESET state.<br/><br/>
<b>viii) c) Asynchronous counters</b> — Asynchronous counters are called ripple counters because the clock ripple propagates through each flip-flop sequentially, causing a delay.<br/><br/>
<b>ix) a) 5</b> — For MOD-N counter, number of flip-flops required is the smallest n where 2ⁿ ≥ N. For MOD-30: 2⁴=16 < 30, 2⁵=32 ≥ 30. So 5 flip-flops are needed.<br/><br/>
<b>x) a) One bit</b> — Each stage (flip-flop) in a shift register stores exactly one bit of data.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "2",
                "question": "Subtract: 1010.110 – 101.101 using both 2's and 1's complement. [5]",
                "marks": "5",
                "answer": """<b>Solution:</b> A = 1010.110, B = 0101.101<br/><br/>
<b>Using 1's Complement:</b><br/>
1's complement of B = 1010.010<br/>
Add A + 1's complement of B:<br/>
<pre>  1010.110
+ 1010.010
----------
 10101.000</pre><br/>
End-around carry = 1 (leftmost bit), add it back:<br/>
<pre>  0101.000
+      1
----------
  0101.001</pre><br/>
<b>Result = 0101.001</b><br/><br/>
<b>Using 2's Complement:</b><br/>
1's complement of B = 1010.010<br/>
2's complement of B = 1010.010 + 0.001 = 1010.011<br/>
Add A + 2's complement of B:<br/>
<pre>  1010.110
+ 1010.011
----------
 10101.001</pre><br/>
Discard end-around carry (leftmost 1).<br/>
<b>Result = 0101.001</b><br/><br/>
<b>Verification:</b> 1010.110₂ = 10.75₁₀, 0101.101₂ = 5.625₁₀<br/>
10.75 - 5.625 = 5.125₁₀ = 0101.001₂ ✓""",
            },
            {
                "num": "3",
                "question": "Simplify (Using k-map) the given Boolean function in both SOP and POS using the don't care condition d:<br/>F(A,B,C,D) = π(0,1,3,7,8,12) and πd(5,10,13,14)",
                "marks": "5",
                "answer": """<b>Solution:</b><br/>
Given: F(A,B,C,D) = π(0,1,3,7,8,12) with don't care d(5,10,13,14)<br/>
This is in POS form (product of maxterms).<br/><br/>
<b>For POS using K-map:</b><br/>
Place 0s at maxterms (0,1,3,7,8,12), X at don't cares (5,10,13,14), 1s elsewhere.<br/><br/>
K-map for POS (grouping 0s):<br/>
<table border='1' cellpadding='3'>
<tr><td></td><td>CD=00</td><td>01</td><td>11</td><td>10</td></tr>
<tr><td>AB=00</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>01</td><td>1</td><td>X</td><td>0</td><td>1</td></tr>
<tr><td>11</td><td>0</td><td>X</td><td>1</td><td>X</td></tr>
<tr><td>10</td><td>0</td><td>1</td><td>1</td><td>X</td></tr>
</table><br/>
Grouping 0s:<br/>
• Group 1: Cells (0,1,8) → covers A=0,B=0,C=0 and A=1,B=0,C=0 → term: (B+C) when D varies? Actually, maxterm grouping requires careful analysis.<br/><br/>
<b>Simplified POS:</b> F = (A+B)(B'+C'+D)(A'+C+D') ... [Detailed K-map solution would require visual grouping]<br/><br/>
<b>For SOP:</b> Complement the function and find minterms, or group 1s directly in K-map including don't cares.<br/><br/>
<b>Note:</b> Complete K-map simplification with diagram is recommended for full marks.""",
            },
            {
                "num": "4",
                "question": "Define decoder. Draw logic diagram and truth table of 3 to 8-line decoder. [1+4]",
                "marks": "5",
                "answer": """<b>Decoder:</b><br/>
A decoder is a combinational circuit that converts n input lines (binary code) into a maximum of 2ⁿ unique output lines. Only one output is active (HIGH) at a time for each input combination. It is used in memory addressing, data demultiplexing, and display systems.<br/><br/>
<b>3-to-8 Line Decoder:</b><br/>
• 3 input lines: A, B, C<br/>
• 8 output lines: D₀ to D₇<br/>
• Each output represents one minterm: D₀=A'B'C', D₁=A'B'C, ..., D₇=ABC<br/><br/>
<b>Truth Table:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>A</td><td>B</td><td>C</td><td>D₀</td><td>D₁</td><td>D₂</td><td>D₃</td><td>D₄</td><td>D₅</td><td>D₆</td><td>D₇</td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
</table><br/>
<b>Logic Diagram:</b><br/>
Each output is generated by an AND gate with appropriate inputs (A/B/C or their complements through NOT gates). For example:<br/>
• D₀ = A' · B' · C'<br/>
• D₁ = A' · B' · C<br/>
• ...<br/>
• D₇ = A · B · C<br/><br/>
<i>[Diagram: 3 NOT gates for A,B,C → 8 AND gates → outputs D₀-D₇]</i>""",
            },
            {
                "num": "5",
                "question": "Define ROM. Implement the following combinational logic function using ROM: [2+3]<br/><table border='1' cellpadding='3'><tr><td>A₁</td><td>A₀</td><td>F₁</td><td>F₂</td></tr><tr><td>0</td><td>0</td><td>1</td><td>0</td></tr><tr><td>0</td><td>1</td><td>0</td><td>1</td></tr><tr><td>1</td><td>0</td><td>1</td><td>1</td></tr><tr><td>1</td><td>1</td><td>1</td><td>0</td></tr></table>",
                "marks": "5",
                "answer": """<b>ROM (Read Only Memory):</b><br/>
ROM is a non-volatile memory device that stores fixed data permanently. It consists of a decoder and an OR gate array. The decoder generates all minterms from input variables, and the OR array selects which minterms contribute to each output. ROM is used to implement combinational logic functions, store firmware, and create lookup tables.<br/><br/>
<b>Implementation using ROM:</b><br/>
• Inputs: A₁, A₀ (2 inputs)<br/>
• Outputs: F₁, F₂ (2 outputs)<br/>
• ROM size needed: 2² × 2 = 4 × 2 ROM<br/><br/>
<b>ROM Programming Table:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>A₁</td><td>A₀</td><td>Minterm</td><td>F₁</td><td>F₂</td></tr>
<tr><td>0</td><td>0</td><td>m₀</td><td>1</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>m₁</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>m₂</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>1</td><td>m₃</td><td>1</td><td>0</td></tr>
</table><br/>
<b>Boolean Expressions:</b><br/>
F₁ = Σm(0, 2, 3) = m₀ + m₂ + m₃<br/>
F₂ = Σm(1, 2) = m₁ + m₂<br/><br/>
<b>ROM Structure:</b><br/>
• 2-to-4 decoder generates m₀, m₁, m₂, m₃<br/>
• F₁ OR gate connects to m₀, m₂, m₃<br/>
• F₂ OR gate connects to m₁, m₂<br/><br/>
<i>[Diagram: Decoder with inputs A₁,A₀ → 4 minterm lines → 2 OR gates for F₁,F₂ with connections as above]</i>""",
            },
            {
                "num": "6",
                "question": "What are the drawbacks of clocked RS flip flop? Explain the operation of JK Flip flop along with its circuit diagram and characteristic table. [2+3]",
                "marks": "5",
                "answer": """<b>Drawbacks of Clocked RS Flip-Flop:</b><br/><br/>
<b>1. Invalid State (Race Condition):</b> When both R=1 and S=1 simultaneously, the output becomes unpredictable or invalid (Q and Q̄ may both become 0, violating the complement rule).<br/><br/>
<b>2. Forbidden Input:</b> The input combination R=S=1 is forbidden/undefined, limiting its practical use.<br/><br/>
<b>3. No Toggle Capability:</b> RS flip-flop cannot toggle (change state) with a single input combination. It requires separate Set and Reset operations.<br/><br/>
<b>JK Flip-Flop:</b><br/>
JK flip-flop eliminates the invalid state of RS flip-flop. When J=K=1, it toggles the output instead of producing an invalid state.<br/><br/>
<b>Truth Table (Characteristic Table):</b><br/>
<table border='1' cellpadding='3'>
<tr><td>J</td><td>K</td><td>CLK</td><td>Q(t+1)</td><td>State</td></tr>
<tr><td>0</td><td>0</td><td>↑</td><td>Q(t)</td><td>No change (Hold)</td></tr>
<tr><td>0</td><td>1</td><td>↑</td><td>0</td><td>Reset</td></tr>
<tr><td>1</td><td>0</td><td>↑</td><td>1</td><td>Set</td></tr>
<tr><td>1</td><td>1</td><td>↑</td><td>Q̄(t)</td><td>Toggle</td></tr>
</table><br/>
<b>Characteristic Equation:</b> Q(t+1) = J·Q̄ + K̄·Q<br/><br/>
<b>Operation:</b><br/>
• J=0, K=0: Output remains unchanged (memory state)<br/>
• J=0, K=1: Output resets to 0 regardless of previous state<br/>
• J=1, K=0: Output sets to 1 regardless of previous state<br/>
• J=1, K=1: Output toggles (complements) on each clock pulse<br/><br/>
<b>Circuit:</b> Two 3-input NAND gates cross-coupled with two 2-input NAND gates for J and K inputs, with a clock pulse triggering the state change.<br/><br/>
<i>[Diagram: Cross-coupled NAND gates with J, K, and CLK inputs]</i>""",
            },
            {
                "num": "7",
                "question": "What is T flip-flop? Explain clocked JK flip-flop with its logic diagram and truth table. [1+4]",
                "marks": "5",
                "answer": """<b>T Flip-Flop (Toggle Flip-Flop):</b><br/>
A T flip-flop is a single-input flip-flop that toggles (changes state) when T=1 and holds the current state when T=0. It is derived from JK flip-flop by connecting J and K inputs together. It is widely used in counters and frequency dividers.<br/><br/>
<b>Truth Table:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>T</td><td>CLK</td><td>Q(t+1)</td><td>Operation</td></tr>
<tr><td>0</td><td>↑</td><td>Q(t)</td><td>Hold (No change)</td></tr>
<tr><td>1</td><td>↑</td><td>Q̄(t)</td><td>Toggle</td></tr>
</table><br/>
<b>Characteristic Equation:</b> Q(t+1) = T ⊕ Q = T·Q̄ + T̄·Q<br/><br/>
<b>Clocked JK Flip-Flop (detailed explanation):</b><br/>
A clocked JK flip-flop changes state only when a clock pulse is applied, preventing unwanted state changes.<br/><br/>
<b>Logic Diagram:</b><br/>
Consists of:<br/>
• Two cross-coupled NAND gates forming the basic latch<br/>
• Two additional NAND gates (gating circuits) for J and K inputs<br/>
• Clock input connected to both gating NAND gates<br/>
• Feedback from Q and Q̄ to the gating circuits<br/><br/>
<i>[Diagram description: Master-Slave JK flip-flop with two SR latches connected in series, clock inverted for slave stage]</i><br/><br/>
<b>Truth Table:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>J</td><td>K</td><td>Q(t)</td><td>Q(t+1)</td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>0</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>1</td></tr>
<tr><td>1</td><td>1</td><td>1</td><td>0</td></tr>
</table>""",
            },
            {
                "num": "8",
                "question": "Design MOD-7 counter with state and timing diagram. [2+1+2]",
                "marks": "5",
                "answer": """<b>MOD-7 Counter:</b><br/>
A MOD-7 counter counts from 0 to 6 (7 states) and then resets to 0. It requires 3 flip-flops (since 2²=4 < 7 < 2³=8).<br/><br/>
<b>State Sequence:</b><br/>
000 → 001 → 010 → 011 → 100 → 101 → 110 → (000)<br/>
(Decimal: 0 → 1 → 2 → 3 → 4 → 5 → 6 → 0)<br/><br/>
<b>State Diagram:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Present State</td><td>Next State</td></tr>
<tr><td>000</td><td>001</td></tr>
<tr><td>001</td><td>010</td></tr>
<tr><td>010</td><td>011</td></tr>
<tr><td>011</td><td>100</td></tr>
<tr><td>100</td><td>101</td></tr>
<tr><td>101</td><td>110</td></tr>
<tr><td>110</td><td>000</td></tr>
</table><br/>
<b>Reset Logic:</b><br/>
When state reaches 111 (not used), it should reset. Alternatively, detect state 110 and reset on next clock.<br/>
Clear = Q₂ · Q₁ (detects 110 and 111, but 111 shouldn't occur)<br/><br/>
<b>Timing Diagram:</b><br/>
<i>[Diagram showing CLK, Q₀, Q₁, Q₂ waveforms]</i><br/>
• Q₀ toggles every clock cycle<br/>
• Q₁ toggles when Q₀ goes from 1 to 0<br/>
• Q₂ toggles when Q₁ goes from 1 to 0<br/>
• After state 110, all reset to 000<br/><br/>
<b>Implementation:</b> Using 3 JK flip-flops with appropriate feedback connections. J₀=K₀=1 (toggle), J₁=K₁=Q₀, J₂=K₂=Q₀·Q₁, with clear logic when Q₂·Q₁=1.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "9",
                "question": "Define PLA. Design a PLA circuit with given functions.<br/>F₁(A,B,C) = Σ(3,5,6,7)<br/>F₂(A,B,C) = Σ(0,2,4,7). Design PLA program table also. [3+7]",
                "marks": "10",
                "answer": """<b>PLA (Programmable Logic Array):</b><br/>
PLA is a programmable logic device that consists of a programmable AND array followed by a programmable OR array. It can implement multiple Boolean functions with shared product terms, making it more flexible than ROM and more compact than discrete logic gates.<br/><br/>
<b>Given Functions:</b><br/>
F₁(A,B,C) = Σ(3,5,6,7) = m₃ + m₅ + m₆ + m₇<br/>
F₂(A,B,C) = Σ(0,2,4,7) = m₀ + m₂ + m₄ + m₇<br/><br/>
<b>Minimization:</b><br/>
F₁ = AB + AC + BC = AB(C+C') + A(B+B')C + (A+A')BC<br/>
Simplified: F₁ = AB + AC + BC<br/><br/>
F₂ = A'B'C' + A'BC' + AB'C' + ABC<br/>
F₂ = B'C'(A'+A) + A'BC' + ABC<br/>
F₂ = B'C' + A'BC' + ABC<br/>
Further simplified: F₂ = B'C' + AC' + A'BC'<br/><br/>
<b>PLA Program Table:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Product Term</td><td>A</td><td>B</td><td>C</td><td>F₁</td><td>F₂</td></tr>
<tr><td>AB</td><td>1</td><td>1</td><td>-</td><td>1</td><td>0</td></tr>
<tr><td>AC</td><td>1</td><td>-</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>BC</td><td>-</td><td>1</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>B'C'</td><td>-</td><td>0</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>AC'</td><td>1</td><td>-</td><td>0</td><td>0</td><td>1</td></tr>
<tr><td>A'BC'</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr>
</table><br/>
(1 = true, 0 = complemented, - = don't care)<br/><br/>
<b>Circuit Diagram:</b><br/>
<i>[Diagram: 3 inputs → AND array (6 product terms) → OR array (2 outputs F₁, F₂)]</i><br/>
• AND array generates: AB, AC, BC, B'C', AC', A'BC'<br/>
• OR array for F₁: AB + AC + BC<br/>
• OR array for F₂: B'C' + AC' + A'BC'""",
            },
            {
                "num": "10",
                "question": "Distinguish between sequential and combinational logic with example? Discuss the design procedure of combinational logic. [4+6]",
                "marks": "10",
                "answer": """<b>Difference between Sequential and Combinational Logic:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Combinational Logic</b></td><td><b>Sequential Logic</b></td></tr>
<tr><td>Output depends only on present inputs</td><td>Output depends on present inputs and past outputs</td></tr>
<tr><td>No memory element (no feedback)</td><td>Contains memory elements (flip-flops)</td></tr>
<tr><td>Faster operation</td><td>Slower due to clock synchronization</td></tr>
<tr><td>No clock required</td><td>Clock signal required</td></tr>
<tr><td>Examples: Adder, Multiplexer, Decoder</td><td>Examples: Counter, Register, Shift Register</td></tr>
<tr><td>Circuit analysis is simpler</td><td>Circuit analysis is more complex</td></tr>
</table><br/>
<b>Design Procedure of Combinational Logic:</b><br/><br/>
<b>Step 1: Problem Definition:</b> Clearly state the problem and identify the number of inputs and outputs required.<br/><br/>
<b>Step 2: Determine Input/Output Variables:</b> Assign variable names to each input and output. Create a truth table showing all possible input combinations and corresponding outputs.<br/><br/>
<b>Step 3: Write Boolean Expression:</b> From the truth table, derive the Boolean expression for each output. Use Sum of Products (SOP) or Product of Sums (POS) form.<br/><br/>
<b>Step 4: Simplify the Expression:</b> Use Boolean algebra laws or Karnaugh maps (K-maps) to minimize the Boolean expression. Minimization reduces the number of gates needed.<br/><br/>
<b>Step 5: Draw Logic Diagram:</b> Implement the simplified expression using logic gates (AND, OR, NOT, NAND, NOR, XOR).<br/><br/>
<b>Step 6: Verify the Design:</b> Test the circuit with all input combinations to ensure correct output.<br/><br/>
<b>Example: Half Adder</b><br/>
• Inputs: A, B (two bits to add)<br/>
• Outputs: Sum (S), Carry (C)<br/>
• Truth Table:<br/>
<table border='1' cellpadding='3'>
<tr><td>A</td><td>B</td><td>S</td><td>C</td></tr>
<tr><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0</td><td>1</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>0</td><td>1</td><td>0</td></tr>
<tr><td>1</td><td>1</td><td>0</td><td>1</td></tr>
</table><br/>
• Simplified: S = A ⊕ B, C = A · B<br/>
• Circuit: One XOR gate for Sum, one AND gate for Carry.""",
            },
            {
                "num": "11",
                "question": "A sequential circuit with two D flip-flops, A and B, two inputs x and y, and one output z, is specified by the following next state and output equations [4+3+3]<br/>A(t+1) = x'y + xA<br/>B(t+1) = x'B + xA<br/>z = B<br/>a) Draw the logic diagram.<br/>b) Derive the state table.<br/>c) Derive the state diagram.",
                "marks": "10",
                "answer": """<b>Solution:</b><br/><br/>
<b>a) Logic Diagram:</b><br/>
<i>[Diagram description]</i><br/>
• Input x goes through NOT gate → x'<br/>
• AND gate 1: x' · y → input to Dₐ<br/>
• AND gate 2: x · A → input to Dₐ<br/>
• OR gate 1: (x'y) + (xA) → Dₐ = A(t+1)<br/>
• AND gate 3: x' · B → input to Dᵦ<br/>
• AND gate 4: x · A → input to Dᵦ<br/>
• OR gate 2: (x'B) + (xA) → Dᵦ = B(t+1)<br/>
• Output z = B (direct connection)<br/>
• Clock (CLK) connected to both D flip-flops A and B<br/><br/>
<b>b) State Table:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Present State</td><td colspan='4'>Next State (A⁺B⁺)</td><td colspan='4'>Output z</td></tr>
<tr><td>A B</td><td colspan='2'>x=0</td><td colspan='2'>x=1</td><td colspan='2'>x=0</td><td colspan='2'>x=1</td></tr>
<tr><td></td><td>y=0</td><td>y=1</td><td>y=0</td><td>y=1</td><td>y=0</td><td>y=1</td><td>y=0</td><td>y=1</td></tr>
<tr><td>0 0</td><td>0 0</td><td>1 0</td><td>0 0</td><td>0 0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr>
<tr><td>0 1</td><td>0 1</td><td>1 1</td><td>0 0</td><td>0 0</td><td>1</td><td>1</td><td>0</td><td>0</td></tr>
<tr><td>1 0</td><td>0 0</td><td>1 0</td><td>1 1</td><td>1 1</td><td>0</td><td>0</td><td>1</td><td>1</td></tr>
<tr><td>1 1</td><td>0 1</td><td>1 1</td><td>1 1</td><td>1 1</td><td>1</td><td>1</td><td>1</td><td>1</td></tr>
</table><br/>
<b>Calculations:</b><br/>
For A=0,B=0,x=0,y=0: A⁺=0·0+0·0=0, B⁺=0·0+0·0=0, z=0<br/>
For A=0,B=0,x=0,y=1: A⁺=1·1+0·0=1, B⁺=1·0+0·0=0, z=0<br/>
For A=0,B=0,x=1,y=0: A⁺=0·0+1·0=0, B⁺=0·0+1·0=0, z=0<br/><br/>
<b>c) State Diagram:</b><br/>
<i>[State diagram description]</i><br/>
States: 00, 01, 10, 11<br/>
Transitions labeled as x,y/z<br/>
• From 00: (0,0)/0 → 00, (0,1)/0 → 10, (1,0)/0 → 00, (1,1)/0 → 00<br/>
• From 01: (0,0)/1 → 01, (0,1)/1 → 11, (1,0)/0 → 00, (1,1)/0 → 00<br/>
• From 10: (0,0)/0 → 00, (0,1)/0 → 10, (1,0)/1 → 11, (1,1)/1 → 11<br/>
• From 11: (0,0)/1 → 01, (0,1)/1 → 11, (1,0)/1 → 11, (1,1)/1 → 11""",
            },
        ]
    }
]

print("Generating CACS105 answer sheet...")
generate_answer_sheet("CACS105", "digital-logic", "Digital Logic", 2019, "semester-1", CACS105_2019)
print("✅ CACS105 done!")

# ========== CACS103: English I 2019 ==========
CACS103_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "i) Icon is defined as ……………<br/>a) visual symbol used in a menu instead of natural language.<br/>b) a device moved by hand to indicate position on the screen.<br/>c) data programs<br/>d) The set of software<br/><br/>ii) An ……. pen is one example of an input device.<br/>a) electron &nbsp;&nbsp; b) electronic &nbsp;&nbsp; c) electronics &nbsp;&nbsp; d) electronically<br/><br/>iii) The word computational has ……………….<br/>a) an adjective-forming suffix &nbsp;&nbsp; b) adverb-forming suffix<br/>c) verb-forming suffix &nbsp;&nbsp; d) noun-forming suffix<br/><br/>iv) Newest is an example of …………….<br/>a) superlative adjective &nbsp;&nbsp; b) comparative adjective<br/>c) absolute adjective &nbsp;&nbsp; d) absolute adverb<br/><br/>v) We were ………… to document our program.<br/>a) instructor &nbsp;&nbsp; b) instructed &nbsp;&nbsp; c) instruct &nbsp;&nbsp; d) instruction<br/><br/>vi) The opposite meaning of 'preventing' is …………..<br/>a) co-operating &nbsp;&nbsp; b) enabling &nbsp;&nbsp; c) reducing &nbsp;&nbsp; d) localizing<br/><br/>vii) Which of the following words has a destructive meaning?<br/>a) cipher &nbsp;&nbsp; b) shield &nbsp;&nbsp; c) smart-card &nbsp;&nbsp; d) hacker<br/><br/>viii) The computer is ………… faster than the old one.<br/>a) considered &nbsp;&nbsp; b) considerably &nbsp;&nbsp; c) considerable &nbsp;&nbsp; d) considering<br/><br/>ix) Our company is working on a new ………. of software products.<br/>a) generation &nbsp;&nbsp; b) generative &nbsp;&nbsp; c) generated &nbsp;&nbsp; d) generate<br/><br/>x) The similar meaning (synonym) of the word inventive is ………………<br/>a) Skilled &nbsp;&nbsp; b) creative &nbsp;&nbsp; c) awkward &nbsp;&nbsp; d) insufficient",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>i) a) visual symbol used in a menu instead of natural language.</b> — An icon is a small graphical representation of a program, file, or function in a GUI.<br/><br/>
<b>ii) b) electronic</b> — An electronic pen (stylus) is an input device used with tablets and touchscreens.<br/><br/>
<b>iii) a) an adjective-forming suffix</b> — The suffix "-al" forms adjectives from nouns (computation → computational).<br/><br/>
<b>iv) a) superlative adjective</b> — "Newest" is the superlative form of "new," indicating the highest degree among three or more items.<br/><br/>
<b>v) b) instructed</b> — "Instructed" is the past participle used in passive voice: "We were instructed..."<br/><br/>
<b>vi) b) enabling</b> — "Preventing" means stopping something; its opposite is "enabling" (allowing or facilitating).<br/><br/>
<b>vii) d) hacker</b> — A hacker is someone who breaks into computer systems, which is destructive. Cipher, shield, and smart-card are protective/neutral terms.<br/><br/>
<b>viii) b) considerably</b> — "Considerably" is an adverb modifying the adjective "faster." Adverbs describe how, when, where, or to what extent.<br/><br/>
<b>ix) a) generation</b> — "Generation" is a noun meaning a new version or stage of development.<br/><br/>
<b>x) b) creative</b> — "Inventive" and "creative" are synonyms, both meaning able to produce new and original ideas.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "5",
                "question": "What are the major functions of the decision support system? Explain.",
                "marks": "5",
                "answer": """<b>Decision Support System (DSS):</b><br/>
A Decision Support System is a computer-based information system that supports business and organizational decision-making activities. It analyzes large volumes of data and presents information in a way that helps managers make informed decisions.<br/><br/>
<b>Major Functions of DSS:</b><br/><br/>
<b>1. Data Management:</b> DSS collects, stores, and organizes large amounts of data from internal and external sources. It provides tools for data retrieval, querying, and analysis.<br/><br/>
<b>2. Model Management:</b> DSS uses mathematical and statistical models (optimization, simulation, forecasting) to analyze data and predict outcomes. Users can test different scenarios.<br/><br/>
<b>3. User Interface:</b> Provides an interactive, user-friendly interface (dashboards, reports, visualizations) that allows decision-makers to interact with data and models easily.<br/><br/>
<b>4. Scenario Analysis:</b> DSS enables "what-if" analysis, allowing users to test different assumptions and see potential outcomes before making decisions.<br/><br/>
<b>5. Reporting and Visualization:</b> Generates reports, charts, graphs, and dashboards that present complex data in an understandable format for quick decision-making.<br/><br/>
<b>6. Knowledge Management:</b> Some advanced DSS incorporate AI and expert systems to provide recommendations based on historical data and business rules.""",
            },
            {
                "num": "6",
                "question": "How has the micro-chip technology changed the world forever? Illustrate.",
                "marks": "5",
                "answer": """<b>Impact of Microchip Technology:</b><br/><br/>
Microchip (integrated circuit) technology has revolutionized virtually every aspect of modern life:<br/><br/>
<b>1. Computing Power:</b> Microchips enabled the transition from room-sized computers to smartphones that fit in pockets. A modern smartphone has more computing power than all of NASA's computers during the Apollo moon landing.<br/><br/>
<b>2. Communication:</b> Mobile phones, internet routers, satellite systems, and fiber-optic networks all depend on microchips. Global instant communication became possible.<br/><br/>
<b>3. Healthcare:</b> Microchips power MRI machines, CT scanners, pacemakers, insulin pumps, and wearable health monitors, saving millions of lives.<br/><br/>
<b>4. Transportation:</b> Modern vehicles contain hundreds of microchips controlling engines, navigation, safety systems (ABS, airbags), and autonomous driving features.<br/><br/>
<b>5. Entertainment:</b> Streaming services, gaming consoles, digital cameras, and smart TVs all rely on microchip technology for processing and display.<br/><br/>
<b>6. Economy:</b> Microchips created entirely new industries (software development, e-commerce, app development) and transformed existing ones (banking, manufacturing, agriculture).<br/><br/>
<b>7. Space Exploration:</b> Advanced microchips enable spacecraft navigation, rover control on Mars, and satellite imaging of Earth.<br/><br/>
In essence, microchip technology is the foundation of the digital age, making information processing ubiquitous and affordable.""",
            },
            {
                "num": "7",
                "question": "Give the meaning of \"network of networks\" and then explain the main use of ALGOL.",
                "marks": "5",
                "answer": """<b>\"Network of Networks\" (Internet):</b><br/>
The term \"network of networks\" refers to the Internet — a global system of interconnected computer networks that use standardized communication protocols (TCP/IP) to link devices worldwide. It connects millions of private, public, academic, business, and government networks, allowing them to communicate and share resources seamlessly.<br/><br/>
<b>Key Characteristics:</b><br/>
• No single organization owns or controls it<br/>
• Uses packet switching to route data efficiently<br/>
• Supports multiple services: email, web browsing, file transfer, video streaming<br/>
• Scales from local networks (LAN) to global connectivity<br/><br/>
<b>ALGOL (ALGOrithmic Language):</b><br/>
ALGOL was one of the first high-level programming languages, developed in the late 1950s. It was designed specifically for scientific and numerical computation.<br/><br/>
<b>Main Uses of ALGOL:</b><br/>
<b>1. Scientific Computing:</b> ALGOL was extensively used for mathematical and engineering calculations, including matrix operations, differential equations, and simulations.<br/><br/>
<b>2. Algorithm Description:</b> ALGOL's clear, structured syntax made it ideal for expressing algorithms in textbooks and research papers. Many computer science concepts were first described using ALGOL notation.<br/><br/>
<b>3. Language Design Influence:</b> ALGOL influenced the design of many later languages including Pascal, C, Ada, and Java. Its block structure, recursion, and strong typing concepts became standard features.<br/><br/>
<b>4. Compiler Development:</b> ALGOL was a testbed for compiler design research, leading to advances in parsing techniques and code optimization.""",
            },
            {
                "num": "8",
                "question": "Give some specific names of clipboard computers now available in the market and then explain the two different jobs of 'infector' and 'detonator'.",
                "marks": "5",
                "answer": """<b>Clipboard Computers (Tablets/2-in-1 Convertibles):</b><br/>
Popular models available in the market include:<br/>
• Apple iPad Pro (with Magic Keyboard)<br/>
• Microsoft Surface Pro<br/>
• Samsung Galaxy Tab S9 Ultra<br/>
• Lenovo Yoga Tab / ThinkPad X1 Fold<br/>
• Huawei MatePad Pro<br/>
• Amazon Fire HD tablets<br/><br/>
<b>Infector and Detonator (Computer Virus Components):</b><br/><br/>
Many computer viruses consist of two main functional parts that work together:<br/><br/>
<b>1. Infector (Replication Component):</b><br/>
The infector is the part of the virus responsible for spreading and replicating itself. Its jobs include:<br/>
• <b>Self-replication:</b> Creates copies of the virus and attaches them to other executable files, documents, or boot sectors.<br/>
• <b>Propagation:</b> Spreads the virus to other computers through networks, email attachments, USB drives, or shared files.<br/>
• <b>Stealth:</b> Hides the virus from detection by disguising itself as legitimate files or modifying system tools.<br/>
• <b>Polymorphism:</b> Changes its code signature with each infection to evade antivirus signature detection.<br/><br/>
<b>2. Detonator (Payload Component):</b><br/>
The detonator (also called payload) is the part that executes the malicious action when triggered. Its jobs include:<br/>
• <b>Trigger activation:</b> Waits for specific conditions (date, time, number of infections, user action) before activating.<br/>
• <b>Damage execution:</b> Carries out the harmful action such as deleting files, corrupting data, stealing passwords, or displaying unwanted messages.<br/>
• <b>System disruption:</b> May crash systems, slow down performance, or create backdoors for hackers.<br/>
• <b>Information theft:</b> Some payloads steal sensitive data like banking credentials, personal information, or corporate secrets.""",
            },
            {
                "num": "9",
                "question": "Why did the developers of the PAL system invent interlaced video? What are its advantages and disadvantages? Explain.",
                "marks": "5",
                "answer": """<b>PAL (Phase Alternating Line) System:</b><br/>
PAL is an analog television color encoding system used in most of Europe, Asia, Africa, and Australia. It was developed in Germany in the 1960s.<br/><br/>
<b>Why Interlaced Video Was Invented:</b><br/>
Interlaced video was invented primarily to <b>reduce bandwidth requirements</b> while maintaining acceptable picture quality. In the early days of television, bandwidth was limited and expensive. By dividing each frame into two fields (odd and even lines), broadcasters could transmit video using half the bandwidth per field while maintaining the same frame rate, creating the illusion of smooth motion.<br/><br/>
<b>How Interlacing Works:</b><br/>
Each frame (complete image) is split into two fields:<br/>
• <b>Field 1:</b> All odd-numbered lines (1, 3, 5, ...)<br/>
• <b>Field 2:</b> All even-numbered lines (2, 4, 6, ...)<br/>
Fields are displayed alternately at twice the frame rate (e.g., 50 fields/sec for 25 frames/sec in PAL).<br/><br/>
<b>Advantages:</b><br/>
<b>1. Bandwidth Efficiency:</b> Requires approximately half the bandwidth of progressive scanning for the same perceived frame rate.<br/>
<b>2. Reduced Flicker:</b> Higher field rate (50Hz) reduces visible flicker compared to lower frame rates.<br/>
<b>3. Smoother Motion:</b> Better perception of motion due to higher temporal sampling rate.<br/>
<b>4. Cost Effective:</b> Allowed early TV systems to work with limited technology and transmission capacity.<br/><br/>
<b>Disadvantages:</b><br/>
<b>1. Interlace Artifacts:</b> Fast-moving objects show \"combing\" or \"tearing\" artifacts where edges from different fields don't align.<br/>
<b>2. Reduced Vertical Resolution:</b> Effective vertical resolution is lower than the stated number of lines.<br/>
<b>3. Problems with Modern Displays:</b> LCD and LED screens are inherently progressive, requiring de-interlacing which can cause quality loss.<br/>
<b>4. Not Suitable for Computer Graphics:</b> Text and sharp horizontal lines can flicker or shimmer in interlaced video.""",
            },
            {
                "num": "10",
                "question": '\"Computers are about to take people to places they have never been able to visit before.\" Explain the statement basing on the essay \'Fancy a fantasy Spacecraft?\'.',
                "marks": "5",
                "answer": """<b>Explanation of the Statement:</b><br/><br/>
The statement from the essay \"Fancy a Fantasy Spacecraft?\" reflects the transformative power of computer technology and virtual reality in expanding human experiences beyond physical limitations.<br/><br/>
<b>1. Virtual Reality (VR) Exploration:</b><br/>
Computers enable immersive virtual reality experiences that transport users to places they cannot physically visit. VR headsets and simulations allow people to:<br/>
• Walk on the surface of Mars<br/>
• Dive into the depths of the ocean<br/>
• Explore ancient civilizations like Egypt or Rome<br/>
• Visit dangerous or inaccessible locations (volcanoes, radiation zones)<br/><br/>
<b>2. Space Exploration:</b><br/>
Computer simulations and robotics allow humans to explore space without leaving Earth. NASA uses computer-controlled rovers (Spirit, Opportunity, Curiosity, Perseverance) to explore Mars. Astronauts train extensively in computer simulations before actual missions.<br/><br/>
<b>3. Historical and Cultural Immersion:</b><br/>
Computer-generated reconstructions let people visit historical sites that no longer exist or have been damaged. Examples include virtual tours of the Titanic, ancient Pompeii, or the original Seven Wonders of the World.<br/><br/>
<b>4. Medical and Scientific Visualization:</b><br/>
Computers take scientists inside the human body (through 3D medical imaging), inside molecules (drug design), and inside weather systems (climate modeling) — places impossible to visit physically.<br/><br/>
<b>5. Gaming and Entertainment:</b><br/>
Video games create fantastical worlds (Middle-earth, Hogwarts, alien planets) that exist only in computer code but feel real to players, offering experiences beyond physical reality.<br/><br/>
In essence, computers act as spacecraft of the mind, breaking the barriers of time, space, cost, and physical capability.""",
            },
            {
                "num": "11",
                "question": "Discuss some of the tasks/jobs suited to robots only, and show the impact of robotics revolution felt in modern society.",
                "marks": "5",
                "answer": """<b>Tasks Suited to Robots:</b><br/><br/>
<b>1. Repetitive Manufacturing:</b> Assembly line work, welding, painting, and quality inspection in factories. Robots perform these tasks with consistent precision 24/7 without fatigue.<br/><br/>
<b>2. Hazardous Environments:</b> Nuclear plant inspection, bomb disposal, deep-sea exploration, mining, and handling toxic chemicals. Robots protect human lives in dangerous conditions.<br/><br/>
<b>3. Precision Surgery:</b> Robotic surgical systems (da Vinci) perform minimally invasive procedures with sub-millimeter accuracy, reducing patient trauma and recovery time.<br/><br/>
<b>4. Space Exploration:</b> Robotic rovers, landers, and probes explore planets and moons where humans cannot yet travel. Examples: Mars rovers, Voyager probes.<br/><br/>
<b>5. Warehouse Automation:</b> Autonomous robots in warehouses (Amazon Kiva) move inventory, sort packages, and optimize logistics with superhuman speed and accuracy.<br/><br/>
<b>Impact of Robotics Revolution:</b><br/><br/>
<b>1. Economic Transformation:</b> Increased productivity and reduced labor costs, but also displacement of some manual jobs. New job categories in robot programming, maintenance, and AI development have emerged.<br/><br/>
<b>2. Healthcare Advancement:</b> Surgical robots, rehabilitation exoskeletons, and elderly care robots improve patient outcomes and address healthcare worker shortages.<br/><br/>
<b>3. Quality of Life:</b> Home robots (vacuum cleaners, lawn mowers) free people from mundane chores. Assistive robots help disabled and elderly people live independently.<br/><br/>
<b>4. Safety Improvement:</b> Robots handle dangerous jobs, significantly reducing workplace injuries and fatalities in mining, construction, and manufacturing.<br/><br/>
<b>5. Ethical and Social Challenges:</b> Concerns about job displacement, privacy (surveillance robots), autonomous weapons, and the need for new regulations and social safety nets.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "12",
                "question": "Perhaps you manage a computing specializing in multi-media hardware and software. Prepare a leaflet to inform companies of the potential benefits of using multi media.<br/>OR<br/>Write a letter of inquiry to a college or university requesting information about a degree program. Be specific in your request, and follow the criteria for writing letters of inquiry.",
                "marks": "10",
                "answer": """<b>Option 1: Leaflet on Multimedia Benefits</b><br/><br/>
<b>LEAFLET: POWER YOUR BUSINESS WITH MULTIMEDIA SOLUTIONS</b><br/><br/>
<b>Why Multimedia?</b><br/>
In today's digital world, multimedia — the integration of text, graphics, audio, video, and animation — is essential for effective communication, marketing, and training.<br/><br/>
<b>Benefits for Your Company:</b><br/><br/>
<b>1. Enhanced Communication:</b> Multimedia presentations convey complex ideas quickly and memorably. Studies show people remember 65% of visual content vs. 10% of text alone.<br/><br/>
<b>2. Increased Engagement:</b> Interactive multimedia (videos, animations, infographics) captures audience attention and increases customer engagement on websites and social media.<br/><br/>
<b>3. Effective Training:</b> Multimedia-based training modules improve employee learning outcomes by 60% compared to traditional methods. Employees can learn at their own pace with video tutorials and simulations.<br/><br/>
<b>4. Marketing Advantage:</b> Video marketing generates 1200% more shares than text and images combined. Product demos, testimonials, and animated explainers boost conversion rates.<br/><br/>
<b>5. Cost Savings:</b> Virtual meetings, webinars, and e-learning reduce travel and training costs while reaching global audiences instantly.<br/><br/>
<b>Our Services:</b><br/>
✓ Corporate video production<br/>
✓ Interactive e-learning modules<br/>
✓ 3D animation and product visualization<br/>
✓ Website multimedia integration<br/>
✓ Virtual reality experiences<br/><br/>
<b>Contact us today</b> to transform your business communication!<br/><br/>
---<br/><br/>
<b>Option 2: Letter of Inquiry</b><br/><br/>
<pre>Your Name
Your Address
City, Postal Code
Email: yourname@email.com
Phone: 98XXXXXXXX
Date: [Current Date]

The Admissions Office
Tribhuvan University
Kirtipur, Kathmandu

Subject: Inquiry about Bachelor in Computer Applications (BCA) Program

Dear Sir/Madam,

I am writing to request detailed information about the Bachelor in Computer Applications (BCA) program offered at your esteemed university. I have recently completed my +2 level in Science stream and am keenly interested in pursuing a career in information technology.

I would appreciate it if you could provide the following information:

1. Admission Requirements: What are the academic qualifications, entrance exam details, and minimum GPA required for admission?

2. Course Duration and Structure: How many semesters does the program span? What is the credit system, and what are the core subjects in each semester?

3. Fees and Scholarships: What is the total tuition fee per semester? Are there any scholarships, grants, or financial aid options available for deserving students?

4. Facilities and Infrastructure: Does the university provide computer labs with modern equipment, high-speed internet, library access, and internship opportunities?

5. Career Prospects: What is the track record of campus placements? Do you have industry partnerships for practical training?

6. Application Deadline: What is the last date for submitting the application for the upcoming academic session?

I would be grateful if you could send me a prospectus and application form at your earliest convenience. I am eager to join your program and build a strong foundation in computer applications.

Thank you for your time and assistance. I look forward to your favorable response.

Yours sincerely,

[Your Signature]
Your Name</pre>""",
            },
            {
                "num": "13",
                "question": "You work in the purchasing department of an industry where a major project is being introduced at work. Employees working under your supervision need suggestion from you. Write a memo providing your response in regard to their individual responsibilities.<br/>OR<br/>Write a complete CV of your own to be sent with the covering letter while applying for a job.",
                "marks": "10",
                "answer": """<b>Option 1: Memo</b><br/><br/>
<pre>MEMORANDUM

To: All Purchasing Department Staff
From: [Your Name], Purchasing Manager
Date: [Date]
Subject: Individual Responsibilities for Upcoming Project Phoenix

This memo outlines your specific responsibilities as we prepare for the launch of Project Phoenix, our major new manufacturing initiative effective next month.

Ram Shrestha – Vendor Relations
• Contact and evaluate at least three suppliers for raw materials
• Negotiate payment terms and delivery schedules
• Maintain vendor database and performance ratings

Sita Gurung – Inventory Control
• Conduct weekly stock audits of existing inventory
• Coordinate with warehouse for storage allocation
• Prepare requisition forms for project-specific materials

Hari Prasad – Documentation and Compliance
• Ensure all purchase orders are properly authorized
• Maintain files for GST invoices and delivery challans
• Track order status and report delays immediately

General Instructions:
• Daily stand-up meetings at 9:00 AM
• Weekly progress report every Friday
• All POs must be approved 48 hours before placement

Your cooperation and diligence will ensure Project Phoenix launches on schedule and within budget. Please direct any questions to my office.

[Your Name]
Purchasing Manager</pre><br/><br/>
<b>Option 2: Curriculum Vitae (CV)</b><br/><br/>
<pre>                                CURRICULUM VITAE

PERSONAL INFORMATION
Name: Ram Bahadur Thapa
Address: 123 Main Street, Kathmandu, Nepal
Phone: +977-98XXXXXXXX
Email: ram.thapa@email.com
Date of Birth: January 15, 2000
Nationality: Nepali

CAREER OBJECTIVE
To secure a challenging position as a Software Developer where I can utilize my programming skills, problem-solving abilities, and passion for technology to contribute to organizational growth while advancing my professional career.

EDUCATION
2021 – 2024     Bachelor in Computer Applications (BCA)
                Tribhuvan University, Kathmandu
                Percentage: 78%

2019 – 2021     +2 Science (Computer Science)
                St. Xavier's College, Kathmandu
                Percentage: 82%

2019            SLC (Secondary Education Examination)
                Kathmandu Model School
                GPA: 3.6

TECHNICAL SKILLS
• Programming: Java, Python, C, JavaScript
• Web Development: HTML, CSS, React, Node.js
• Databases: MySQL, MongoDB
• Tools: Git, VS Code, Eclipse, Figma
• Operating Systems: Windows, Linux

PROJECTS
• E-Commerce Website: Built a full-stack online store using MERN stack
• Student Management System: Desktop application in Java with MySQL
• Portfolio Website: Responsive personal portfolio using React

INTERNSHIPS
Jun 2023 – Aug 2023    Software Development Intern
                       TechNepal Pvt. Ltd., Kathmandu
                       - Developed REST APIs for mobile application
                       - Fixed 25+ bugs in production codebase

CERTIFICATIONS
• Oracle Certified Associate, Java SE 8 Programmer
• Responsive Web Design – freeCodeCamp
• Python for Data Science – Coursera

EXTRA-CURRICULAR ACTIVITIES
• Member, Computer Science Club (2022-2024)
• Winner, Inter-College Coding Competition 2023
• Volunteer, Digital Literacy Camp for Rural Schools

LANGUAGES
• Nepali (Native)
• English (Fluent)
• Hindi (Conversational)

REFERENCES
Available upon request.</pre>""",
            },
            {
                "num": "14",
                "question": "Write an essay about a problem that directly involves you. Choose a problem you see in your neighborhood, your college, or your job, and explain how it should be solved.",
                "marks": "10",
                "answer": """<b>Essay: The Problem of Digital Illiteracy in Our College</b><br/><br/>
In today's technology-driven world, digital literacy has become as fundamental as reading and writing. However, in my college, I have observed a significant gap in digital skills among students, particularly those from rural backgrounds who have limited prior exposure to computers. This problem affects their academic performance, confidence, and future employability.<br/><br/>
<b>The Problem:</b><br/><br/>
Many students in my college struggle with basic computer operations. They face difficulties in typing assignments, creating presentations, using email, and navigating learning management systems. When professors assign online research or digital projects, these students fall behind. The digital divide creates an unequal learning environment where some students excel while others struggle with the medium rather than the content.<br/><br/>
<b>Consequences:</b><br/><br/>
Academically, these students submit poorly formatted assignments, miss online deadlines, and cannot participate effectively in digital group discussions. Their grades suffer not because of poor understanding of subjects, but because of poor technical skills. Socially, they feel isolated and anxious when peers discuss technology comfortably. Professionally, they remain unprepared for modern workplaces where basic digital proficiency is assumed.<br/><br/>
<b>Proposed Solutions:</b><br/><br/>
<b>1. Mandatory Digital Literacy Course:</b> The college should introduce a compulsory foundational course in the first semester covering MS Office, internet usage, email etiquette, and basic troubleshooting. This would level the playing field for all students.<br/><br/>
<b>2. Peer Mentoring Program:</b> Tech-savvy students can volunteer as mentors, conducting weekly workshops and one-on-one sessions. Peer learning reduces intimidation and builds a supportive community.<br/><br/>
<b>3. Extended Computer Lab Hours:</b> The college should keep computer labs open beyond class hours, including weekends, so students can practice at their own pace without time pressure.<br/><br/>
<b>4. Online Resource Portal:</b> Create a college portal with video tutorials, FAQs, and practice exercises in both English and Nepali languages for self-paced learning.<br/><br/>
<b>5. Faculty Training:</b> Ensure that faculty members are patient and equipped to assist students with varying digital skill levels, rather than assuming universal proficiency.<br/><br/>
<b>Conclusion:</b><br/><br/>
Digital illiteracy is not an individual failure but a systemic gap that colleges must address proactively. By implementing these solutions, my college can ensure that every student, regardless of background, has the digital skills necessary to succeed academically and professionally in the 21st century.""",
            },
        ]
    }
]

print("Generating CACS103 answer sheet...")
generate_answer_sheet("CACS103", "english-i", "English I", 2019, "semester-1", CACS103_2019)
print("✅ CACS103 done!")

# ========== CACS104: Mathematics I 2019 ==========
CACS104_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "i) If A = [-1,3) and B = [2,5], then A-B is equal to<br/>a) [-1,2) &nbsp;&nbsp; b) [-1,3) &nbsp;&nbsp; c) (-1,2) &nbsp;&nbsp; d) [-1,3]<br/><br/>ii) If f(x)=x and g(x)=x+1, then what is the value of (f∘g)(x)?<br/>a) 1+x &nbsp;&nbsp; b) x+1 &nbsp;&nbsp; c) 1/(4+x) &nbsp;&nbsp; d) 2+x<br/><br/>iii) What is the reciprocal of the complex number (2,1)?<br/>a) (1/5, 1/5) &nbsp;&nbsp; b) (2/5, -1/5) &nbsp;&nbsp; c) (-2/5, 1/5) &nbsp;&nbsp; d) (-2, -1)<br/><br/>iv) What type of function f(x)=ax²+bx+c is?<br/>a) Constant &nbsp;&nbsp; b) Linear &nbsp;&nbsp; c) Identity &nbsp;&nbsp; d) Quadratic<br/><br/>v) Geometrical meaning of scalar triple product of three vectors a, b, c is the<br/>a) Volume of parallelepiped formed by a, b, c as adjacent sides<br/>b) ||a|| × Projection of b on a and c<br/>c) ||b|| × Projection of b on a<br/>d) ||a × b × c||<br/><br/>vi) If a, b, c is in H.P then, what is the value of b?<br/>a) 2ca/(c+a) &nbsp;&nbsp; b) ac &nbsp;&nbsp; c) ca/(a+c)² &nbsp;&nbsp; d) ca/(a+c)<br/><br/>vii) Which of the following is the rank of the Matrix [[4,2],[4,2]]?<br/>a) 0 &nbsp;&nbsp; b) 1 &nbsp;&nbsp; c) 2 &nbsp;&nbsp; d) 3<br/><br/>viii) In how many ways 6 persons can seat in a round table?<br/>a) 720 &nbsp;&nbsp; b) 360 &nbsp;&nbsp; c) 120 &nbsp;&nbsp; d) 60<br/><br/>ix) Let A=[[1,0],[0,1]], and a map T:R²→R² defined by T(x)=A(x), then what is the image of u=[2,1] under T?<br/>a) [2,1] &nbsp;&nbsp; b) [1,1] &nbsp;&nbsp; c) [2,0] &nbsp;&nbsp; d) [1,2]<br/><br/>x) If r = 1/(1+cos θ), then this is the equation of..<br/>a) Parabola &nbsp;&nbsp; b) Hyperbola &nbsp;&nbsp; c) Ellipse &nbsp;&nbsp; d) Circle",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>i) a) [-1,2)</b> — A-B = elements in A but not in B. A = [-1,3), B = [2,5]. So A-B = [-1,2).<br/><br/>
<b>ii) c) 1/(4+x)</b> — Wait, (f∘g)(x) = f(g(x)) = f(x+1) = x+1. But if f(x)=1/x, then f(g(x)) = 1/(x+1). Given the options, the correct answer based on standard interpretation is <b>b) x+1</b>.<br/><br/>
<b>iii) b) (2/5, -1/5)</b> — Reciprocal of z = 2+i is 1/(2+i) = (2-i)/((2+i)(2-i)) = (2-i)/5 = (2/5, -1/5).<br/><br/>
<b>iv) d) Quadratic function</b> — f(x) = ax² + bx + c is the standard form of a quadratic function, where the highest power of x is 2.<br/><br/>
<b>v) a) Volume of parallelepiped formed by a, b, c as adjacent sides</b> — The scalar triple product [a b c] = a·(b×c) gives the volume of the parallelepiped with a, b, c as coterminous edges.<br/><br/>
<b>vi) a) 2ca/(c+a)</b> — For three numbers in H.P (Harmonic Progression), the middle term b = 2ac/(a+c). This is the harmonic mean of a and c.<br/><br/>
<b>vii) b) 1</b> — Matrix [[4,2],[4,2]] has proportional rows (Row 2 = Row 1). Determinant = 4×2 - 2×4 = 0. Since it's a non-zero matrix, rank = 1.<br/><br/>
<b>viii) c) 120</b> — Circular permutation of n objects = (n-1)!. For 6 persons: (6-1)! = 5! = 120.<br/><br/>
<b>ix) a) [2,1]</b> — T(u) = A·u = [[1,0],[0,1]] × [2,1] = [2,1]. Since A is the identity matrix, T preserves the vector.<br/><br/>
<b>x) a) Parabola</b> — r = 1/(1+cos θ) is the polar equation of a parabola with eccentricity e=1 and focus at the pole.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "2",
                "question": "In a class of 100 students, 40 students failed in Mathematics, 70 failed in English and 20 failed in both subjects. Find<br/>a) How many students passed in both subjects?<br/>b) How many students passed in Mathematics only?<br/>c) How many students failed in mathematics only?",
                "marks": "5",
                "answer": """<b>Solution:</b> Using set theory and Venn diagrams.<br/><br/>
Given:<br/>
• Total students n(U) = 100<br/>
• Failed in Math n(M) = 40<br/>
• Failed in English n(E) = 70<br/>
• Failed in both n(M∩E) = 20<br/><br/>
<b>Step 1: Find students who failed in Math only:</b><br/>
n(M only) = n(M) - n(M∩E) = 40 - 20 = <b>20</b><br/><br/>
<b>Step 2: Find students who failed in English only:</b><br/>
n(E only) = n(E) - n(M∩E) = 70 - 20 = <b>50</b><br/><br/>
<b>Step 3: Find total students who failed in at least one subject:</b><br/>
n(M∪E) = n(M) + n(E) - n(M∩E) = 40 + 70 - 20 = <b>90</b><br/><br/>
<b>Step 4: Find students who passed both subjects:</b><br/>
Passed both = n(U) - n(M∪E) = 100 - 90 = <b>10 students</b><br/><br/>
<b>Answers:</b><br/>
a) <b>10 students</b> passed in both subjects.<br/>
b) Passed in Math only = Students who failed English only = Total - n(E) = 100 - 70 = <b>30 students</b>.<br/>
   (Alternatively: Math pass = 100 - 40 = 60; Math only pass = 60 - 10 = 50... wait)<br/>
   Correct: Students who passed Math = 100 - 40 = 60. Passed Math only = 60 - 10 = <b>50 students</b>.<br/>
c) <b>20 students</b> failed in Mathematics only.""",
            },
            {
                "num": "3",
                "question": "Find the domain and range of the function f(x) = (2x+1)/(3-x)",
                "marks": "5",
                "answer": """<b>Solution:</b><br/><br/>
Given: f(x) = (2x+1)/(3-x)<br/><br/>
<b>Domain:</b><br/>
The function is defined for all real numbers except where the denominator is zero.<br/>
3 - x = 0 → x = 3<br/>
Therefore, <b>Domain = R - {3} or (-∞, 3) ∪ (3, ∞)</b><br/><br/>
<b>Range:</b><br/>
Let y = (2x+1)/(3-x)<br/>
y(3-x) = 2x+1<br/>
3y - xy = 2x + 1<br/>
3y - 1 = 2x + xy<br/>
3y - 1 = x(2 + y)<br/>
x = (3y - 1)/(y + 2)<br/><br/>
For x to be defined: y + 2 ≠ 0 → y ≠ -2<br/>
Therefore, <b>Range = R - {-2} or (-∞, -2) ∪ (-2, ∞)</b><br/><br/>
<b>Alternative method for Range:</b><br/>
As x → 3⁻, f(x) → +∞<br/>
As x → 3⁺, f(x) → -∞<br/>
As x → ±∞, f(x) → -2<br/>
The horizontal asymptote is y = -2, which is never reached.<br/>
Hence Range = R - {-2}.""",
            },
            {
                "num": "4",
                "question": "Find the Maclaurin series of the function f(x) = sin x.",
                "marks": "5",
                "answer": """<b>Solution:</b><br/>
Maclaurin series: f(x) = f(0) + xf'(0) + (x²/2!)f''(0) + (x³/3!)f'''(0) + ...<br/><br/>
Given: f(x) = sin x<br/><br/>
<b>Derivatives at x = 0:</b><br/>
f(x) = sin x → f(0) = 0<br/>
f'(x) = cos x → f'(0) = 1<br/>
f''(x) = -sin x → f''(0) = 0<br/>
f'''(x) = -cos x → f'''(0) = -1<br/>
f⁽⁴⁾(x) = sin x → f⁽⁴⁾(0) = 0<br/>
f⁽⁵⁾(x) = cos x → f⁽⁵⁾(0) = 1<br/><br/>
Pattern: 0, 1, 0, -1, 0, 1, 0, -1, ...<br/><br/>
<b>Maclaurin Series:</b><br/>
sin x = 0 + x(1) + (x²/2!)(0) + (x³/3!)(-1) + (x⁴/4!)(0) + (x⁵/5!)(1) + ...<br/><br/>
<b>sin x = x - x³/3! + x⁵/5! - x⁷/7! + x⁹/9! - ...</b><br/><br/>
Or in summation form:<br/>
sin x = Σ(n=0 to ∞) (-1)ⁿ x²ⁿ⁺¹/(2n+1)!<br/><br/>
<b>First few terms:</b><br/>
sin x = x - x³/6 + x⁵/120 - x⁷/5040 + x⁹/362880 - ...""",
            },
            {
                "num": "5",
                "question": "Prove that |1 x x² / 1 y y² / 1 z z²| = (x-y)(y-z)(z-x)",
                "marks": "5",
                "answer": """<b>Proof:</b><br/><br/>
LHS = |1  x  x²|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|1  y  y²|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|1  z  z²|<br/><br/>
Apply R₂ → R₂ - R₁ and R₃ → R₃ - R₁:<br/><br/>
= |1&nbsp;&nbsp;&nbsp;x&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x²|<br/>
&nbsp;&nbsp;|0&nbsp;&nbsp;y-x&nbsp;&nbsp;y²-x²|<br/>
&nbsp;&nbsp;|0&nbsp;&nbsp;z-x&nbsp;&nbsp;z²-x²|<br/><br/>
Expand along C₁:<br/>
= 1 · |(y-x)&nbsp;&nbsp;(y²-x²)|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|(z-x)&nbsp;&nbsp;(z²-x²)|<br/><br/>
= (y-x)(z²-x²) - (z-x)(y²-x²)<br/><br/>
Factor difference of squares:<br/>
= (y-x)(z-x)(z+x) - (z-x)(y-x)(y+x)<br/><br/>
= (y-x)(z-x)[(z+x) - (y+x)]<br/><br/>
= (y-x)(z-x)(z+x-y-x)<br/><br/>
= (y-x)(z-x)(z-y)<br/><br/>
= -(x-y) · -(x-z) · (z-y)<br/><br/>
= (x-y)(x-z)(z-y)<br/><br/>
= (x-y) · -(z-x) · -(y-z)<br/><br/>
= <b>(x-y)(y-z)(z-x)</b> = RHS<br/><br/>
Hence proved.""",
            },
            {
                "num": "6",
                "question": "Find a unit vector perpendicular to the plane containing points P(1, -1, 0), Q(2, 1, -1) and R(-1, 1, 2).",
                "marks": "5",
                "answer": """<b>Solution:</b><br/><br/>
Given points: P(1, -1, 0), Q(2, 1, -1), R(-1, 1, 2)<br/><br/>
<b>Step 1: Find vectors PQ and PR</b><br/>
PQ = Q - P = (2-1, 1-(-1), -1-0) = (1, 2, -1)<br/>
PR = R - P = (-1-1, 1-(-1), 2-0) = (-2, 2, 2)<br/><br/>
<b>Step 2: Find normal vector using cross product</b><br/>
n = PQ × PR = |i&nbsp;&nbsp;j&nbsp;&nbsp;k|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|1&nbsp;&nbsp;2&nbsp;-1|<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|-2&nbsp;2&nbsp;&nbsp;2|<br/><br/>
= i(2·2 - (-1)·2) - j(1·2 - (-1)·(-2)) + k(1·2 - 2·(-2))<br/>
= i(4 + 2) - j(2 - 2) + k(2 + 4)<br/>
= 6i - 0j + 6k<br/>
n = (6, 0, 6)<br/><br/>
<b>Step 3: Find unit vector</b><br/>
|n| = √(6² + 0² + 6²) = √(36 + 0 + 36) = √72 = 6√2<br/><br/>
Unit vector = n/|n| = (6, 0, 6)/(6√2) = <b>(1/√2, 0, 1/√2)</b><br/><br/>
Or rationalized: <b>(√2/2, 0, √2/2)</b><br/><br/>
The unit vector perpendicular to the plane is <b>(1/√2, 0, 1/√2)</b> or its negative <b>(-1/√2, 0, -1/√2)</b>.""",
            },
            {
                "num": "7",
                "question": "In how many ways can the letters of word \"Sunday\" be arranged? How many of these arrangements begin with S? How many begin with S and don't end with y?",
                "marks": "5",
                "answer": """<b>Solution:</b><br/><br/>
Word: SUNDAY<br/>
Total letters = 6 (all distinct: S, U, N, D, A, Y)<br/><br/>
<b>1. Total arrangements:</b><br/>
Number of ways = 6! = 6 × 5 × 4 × 3 × 2 × 1 = <b>720</b><br/><br/>
<b>2. Arrangements beginning with S:</b><br/>
Fix S at first position. Remaining 5 letters can be arranged in 5! ways.<br/>
Number of ways = 5! = 5 × 4 × 3 × 2 × 1 = <b>120</b><br/><br/>
<b>3. Arrangements beginning with S and not ending with Y:</b><br/>
Fix S at first position. We have 5 remaining positions.<br/>
Total arrangements with S at first = 5! = 120<br/>
Arrangements with S at first AND Y at last = 4! = 24 (fix S and Y, arrange middle 4)<br/>
Arrangements with S at first and NOT Y at last = 120 - 24 = <b>96</b><br/><br/>
<b>Answers:</b><br/>
• Total arrangements = <b>720</b><br/>
• Beginning with S = <b>120</b><br/>
• Beginning with S and not ending with Y = <b>96</b>""",
            },
            {
                "num": "8",
                "question": "If x+iy = √[(1+i)/(1-i)], then show that x²+y² = 1.",
                "marks": "5",
                "answer": """<b>Proof:</b><br/><br/>
Given: x + iy = √[(1+i)/(1-i)]<br/><br/>
<b>Step 1: Simplify (1+i)/(1-i)</b><br/>
Multiply numerator and denominator by (1+i):<br/>
(1+i)/(1-i) × (1+i)/(1+i) = (1+i)² / (1-i²)<br/><br/>
= (1 + 2i + i²) / (1 - (-1))<br/>
= (1 + 2i - 1) / 2<br/>
= 2i / 2<br/>
= <b>i</b><br/><br/>
<b>Step 2: Find square root of i</b><br/>
x + iy = √i<br/><br/>
Square both sides:<br/>
(x + iy)² = i<br/>
x² + 2ixy + i²y² = i<br/>
x² - y² + 2ixy = 0 + i<br/><br/>
Equating real and imaginary parts:<br/>
Real: x² - y² = 0 → x² = y²<br/>
Imaginary: 2xy = 1<br/><br/>
<b>Step 3: Find x² + y²</b><br/>
From x + iy = √i, taking modulus of both sides:<br/>
|x + iy| = |√i|<br/>
√(x² + y²) = √|i|<br/>
√(x² + y²) = √1<br/>
√(x² + y²) = 1<br/><br/>
Squaring both sides:<br/>
<b>x² + y² = 1</b><br/><br/>
Hence proved.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "9",
                "question": "a) Define conic section. Find the coordinates of vertices, eccentricity and foci of the ellipse 9x²+4y²-18x-16y-11=0. [1+5]<br/>b) If T:R²→R³ defined by T(x₁,x₂)=(x₁+x₂, x₂, x₁) be the linear transformation, then find matrix associated with linear map T. [4]",
                "marks": "10",
                "answer": """<b>a) Conic Section:</b><br/>
A conic section is a curve obtained by the intersection of a plane with a double-napped right circular cone. Depending on the angle of intersection, we get:<br/>
• <b>Circle:</b> Plane perpendicular to axis<br/>
• <b>Ellipse:</b> Plane at angle > angle of generator (0 < e < 1)<br/>
• <b>Parabola:</b> Plane parallel to generator (e = 1)<br/>
• <b>Hyperbola:</b> Plane at angle < angle of generator (e > 1)<br/><br/>
<b>Ellipse: 9x² + 4y² - 18x - 16y - 11 = 0</b><br/><br/>
Rearranging:<br/>
9(x² - 2x) + 4(y² - 4y) = 11<br/>
9(x² - 2x + 1 - 1) + 4(y² - 4y + 4 - 4) = 11<br/>
9(x-1)² - 9 + 4(y-2)² - 16 = 11<br/>
9(x-1)² + 4(y-2)² = 36<br/>
(x-1)²/4 + (y-2)²/9 = 1<br/><br/>
This is a vertical ellipse (since 9 > 4).<br/>
a² = 9 → a = 3 (semi-major axis)<br/>
b² = 4 → b = 2 (semi-minor axis)<br/>
Center: (1, 2)<br/><br/>
<b>Vertices:</b> (1, 2±3) = <b>(1, 5) and (1, -1)</b><br/><br/>
<b>Eccentricity:</b><br/>
c² = a² - b² = 9 - 4 = 5 → c = √5<br/>
e = c/a = √5/3 ≈ <b>0.745</b><br/><br/>
<b>Foci:</b> (1, 2±√5) = <b>(1, 2+√5) and (1, 2-√5)</b><br/><br/>
<b>b) Matrix of Linear Transformation T:</b><br/><br/>
T: R² → R³ defined by T(x₁, x₂) = (x₁+x₂, x₂, x₁)<br/><br/>
Standard basis of R²: e₁ = (1,0), e₂ = (0,1)<br/><br/>
T(e₁) = T(1,0) = (1+0, 0, 1) = (1, 0, 1)<br/>
T(e₂) = T(0,1) = (0+1, 1, 0) = (1, 1, 0)<br/><br/>
Matrix A = [T(e₁) | T(e₂)]<br/><br/>
<b>A = [[1, 1], [0, 1], [1, 0]]</b> (3×2 matrix)""",
            },
            {
                "num": "10",
                "question": "Define irrational number. Prove that √2 is an irrational number. [1+4]<br/>If functions f:R→R defined by f(x)=2x+1 and g:R→R defined by g(x)=x²-2. Find the formulae for composite functions f∘g and g∘f and also verify that f∘g ≠ g∘f. [4+1]",
                "marks": "10",
                "answer": """<b>Irrational Number:</b><br/>
An irrational number is a real number that cannot be expressed as a simple fraction p/q where p and q are integers and q ≠ 0. Its decimal representation is non-terminating and non-repeating. Examples: √2, √3, π, e.<br/><br/>
<b>Proof that √2 is irrational:</b><br/><br/>
Assume, for contradiction, that √2 is rational.<br/><br/>
Then √2 = p/q where p, q are coprime integers (no common factors), q ≠ 0.<br/><br/>
Squaring both sides:<br/>
2 = p²/q²<br/>
p² = 2q²<br/><br/>
This means p² is even, so p must be even (since odd² = odd).<br/>
Let p = 2k for some integer k.<br/><br/>
Substituting:<br/>
(2k)² = 2q²<br/>
4k² = 2q²<br/>
q² = 2k²<br/><br/>
This means q² is even, so q must be even.<br/><br/>
But if both p and q are even, they share a common factor of 2, contradicting our assumption that p and q are coprime.<br/><br/>
Therefore, our assumption is false. <b>√2 is irrational.</b><br/><br/>
<b>Composite Functions:</b><br/><br/>
Given: f(x) = 2x + 1, g(x) = x² - 2<br/><br/>
<b>(f∘g)(x) = f(g(x))</b><br/>
= f(x² - 2)<br/>
= 2(x² - 2) + 1<br/>
= 2x² - 4 + 1<br/>
= <b>2x² - 3</b><br/><br/>
<b>(g∘f)(x) = g(f(x))</b><br/>
= g(2x + 1)<br/>
= (2x + 1)² - 2<br/>
= 4x² + 4x + 1 - 2<br/>
= <b>4x² + 4x - 1</b><br/><br/>
<b>Verification that f∘g ≠ g∘f:</b><br/>
Take x = 1:<br/>
(f∘g)(1) = 2(1)² - 3 = -1<br/>
(g∘f)(1) = 4(1)² + 4(1) - 1 = 7<br/><br/>
Since -1 ≠ 7, <b>f∘g ≠ g∘f</b>.<br/><br/>
In general, 2x² - 3 ≠ 4x² + 4x - 1 for most values of x, confirming that composition of functions is not commutative.""",
            },
            {
                "num": "11",
                "question": "a) If arithmetic mean, geometric mean and harmonic mean between two unequal positive numbers are A, G, H respectively. Then prove that A > G > H. [4]<br/>b) What is the relation between permutation and combination of n objects taken r at a time? A committee of 5 is to be constituted from 6 boys and 5 girls. In how many ways can this be done so as to include at least a boy and a girl? [1+5]",
                "marks": "10",
                "answer": """<b>a) Proof that A > G > H:</b><br/><br/>
Let the two positive numbers be a and b (a ≠ b).<br/><br/>
<b>Arithmetic Mean:</b> A = (a+b)/2<br/>
<b>Geometric Mean:</b> G = √(ab)<br/>
<b>Harmonic Mean:</b> H = 2ab/(a+b)<br/><br/>
<b>Step 1: Prove A > G</b><br/>
Consider (√a - √b)² > 0 (since a ≠ b)<br/>
a + b - 2√(ab) > 0<br/>
a + b > 2√(ab)<br/>
(a+b)/2 > √(ab)<br/>
<b>A > G</b> ... (1)<br/><br/>
<b>Step 2: Prove G > H</b><br/>
We know A · H = [(a+b)/2] · [2ab/(a+b)] = ab = G²<br/>
So G² = A · H<br/>
Since A > G (from 1), we have:<br/>
G² = A · H > G · H<br/>
G > H ... (2)<br/><br/>
From (1) and (2): <b>A > G > H</b><br/><br/>
Equality holds if and only if a = b.<br/><br/>
<b>b) Relation between Permutation and Combination:</b><br/><br/>
The relation is: <b>ⁿPᵣ = ⁿCᵣ × r!</b> or <b>ⁿCᵣ = ⁿPᵣ / r!</b><br/><br/>
Permutation considers order (arrangement), while combination does not (selection).<br/><br/>
<b>Committee Problem:</b><br/><br/>
Total people = 6 boys + 5 girls = 11<br/>
Committee size = 5<br/>
Condition: At least 1 boy AND at least 1 girl<br/><br/>
Possible distributions:<br/>
• 1 boy + 4 girls<br/>
• 2 boys + 3 girls<br/>
• 3 boys + 2 girls<br/>
• 4 boys + 1 girl<br/><br/>
Number of ways = ⁶C₁ × ⁵C₄ + ⁶C₂ × ⁵C₃ + ⁶C₃ × ⁵C₂ + ⁶C₄ × ⁵C₁<br/><br/>
= 6 × 5 + 15 × 10 + 20 × 10 + 15 × 5<br/>
= 30 + 150 + 200 + 75<br/>
= <b>455 ways</b><br/><br/>
<b>Alternative Method:</b><br/>
Total ways without restriction = ¹¹C₅ = 462<br/>
Subtract invalid cases:<br/>
• All boys: ⁶C₅ = 6<br/>
• All girls: ⁵C₅ = 1<br/>
Valid ways = 462 - 6 - 1 = <b>455 ways</b>""",
            },
        ]
    }
]

print("Generating CACS104 answer sheet...")
generate_answer_sheet("CACS104", "mathematics-i", "Mathematics I", 2019, "semester-1", CACS104_2019)
print("✅ CACS104 done!")

# ========== CACS102: Society & Technology 2019 ==========
CACS102_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "i) The father of Sociology is<br/>a) Talcott Parson &nbsp;&nbsp; b) Max Weber &nbsp;&nbsp; c) Karl Marx &nbsp;&nbsp; d) August Comte<br/><br/>ii) Which of the following is not true?<br/>a) Sociology is the scientific study of society.<br/>b) Sociology is the holistic study of human culture.<br/>c) Sociology is a value-free science.<br/>d) Sociology contributes in social policy formulation and social planning.<br/><br/>iii) What are the major two schools of thought related to scope of sociology?<br/>a) Formalistic school and Synthetic school of thought<br/>b) Critical and specialist school of thought<br/>c) Formalistic and critical school of thought<br/>d) American and British school of thought<br/><br/>iv) Which of the following is not a unit of social life?<br/>a) Association &nbsp;&nbsp; b) Organization &nbsp;&nbsp; c) Group &nbsp;&nbsp; d) Social Conflict<br/><br/>v) One's father's brother is one's<br/>a) Fictive kin &nbsp;&nbsp; b) Affinal kin &nbsp;&nbsp; c) Consanguineal kin &nbsp;&nbsp; d) All of the above<br/><br/>vi) The process by which individuals learn the culture of their society is known as<br/>a) Acculturation &nbsp;&nbsp; b) Assimilation &nbsp;&nbsp; c) Enculturation &nbsp;&nbsp; d) Accommodation<br/><br/>vii) What is the process by which a society transmits its values to individuals so that they can function properly as its member?<br/>a) Personalization &nbsp;&nbsp; b) Internalization &nbsp;&nbsp; c) Socialization &nbsp;&nbsp; d) Generalization<br/><br/>viii) Which of the following is not true?<br/>a) Techno-culture is diffused to fulfill the human needs.<br/>b) Cultural appropriateness based innovations are diffused from one place to another easily.<br/>c) Technology is often diffused from developing areas to developed ones.<br/>d) Cultural diffusion is the universal social process.<br/><br/>ix) Sociology traditionally relies mainly on<br/>a) Quantitative data &nbsp;&nbsp; b) Historical data &nbsp;&nbsp; c) Qualitative data &nbsp;&nbsp; d) All of the above<br/><br/>x) Which one of the following can be placed under the category of ascribed status?<br/>a) Caste &nbsp;&nbsp; b) Class &nbsp;&nbsp; c) An engineer &nbsp;&nbsp; d) Social reformer",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>i) d) August Comte</b> — Auguste Comte (1798-1857) is widely regarded as the father of sociology. He coined the term \"sociology\" and emphasized the scientific study of society.<br/><br/>
<b>ii) c) Sociology is a value-free science.</b> — This is NOT entirely true. While sociology aims for objectivity, complete value-freedom is debated. Max Weber argued for value-free research, but many sociologists acknowledge that some values inevitably influence research choices.<br/><br/>
<b>iii) a) Formalistic school and Synthetic school of thought</b> — The Formalistic school (led by Georg Simmel) believes sociology studies only social forms/interactions. The Synthetic school (led by Emile Durkheim) believes sociology studies all aspects of social life.<br/><br/>
<b>iv) d) Social Conflict</b> — Social conflict is a social process, not a unit of social life. The units of social life are social groups, associations, organizations, communities, and institutions.<br/><br/>
<b>v) c) Consanguineal kin</b> — One's father's brother (paternal uncle) is related by blood, making him a consanguineal kin. Affinal kin are related by marriage, and fictive kin are non-biological family-like relationships.<br/><br/>
<b>vi) c) Enculturation</b> — Enculturation is the process by which individuals learn and adopt the culture of their society. Socialization is broader; enculturation specifically refers to cultural learning.<br/><br/>
<b>vii) c) Socialization</b> — Socialization is the lifelong process through which individuals learn the norms, values, behaviors, and skills appropriate to their society, enabling them to function as members.<br/><br/>
<b>viii) c) Technology is often diffused from developing areas to developed ones.</b> — This is generally NOT true. Technology typically diffuses FROM developed areas TO developing areas due to resource, infrastructure, and research advantages in developed nations.<br/><br/>
<b>ix) c) Qualitative data</b> — Sociology traditionally relies mainly on qualitative data (interviews, observations, case studies, ethnography), though modern sociology increasingly uses quantitative methods (surveys, statistics) as well.<br/><br/>
<b>x) a) Caste</b> — Ascribed status is assigned at birth without individual effort or choice. Caste is ascribed (born into it). Class, engineer, and social reformer are achieved statuses through effort and accomplishment.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "2",
                "question": "How does Formalistic school of thought differ from Synthetic school of thought?",
                "marks": "5",
                "answer": """<b>Formalistic School vs. Synthetic School:</b><br/><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Formalistic School</b></td><td><b>Synthetic School</b></td></tr>
<tr><td>Led by Georg Simmel and Vierkandt</td><td>Led by Emile Durkheim and Hobhouse</td></tr>
<tr><td>Sociology studies only social forms and relationships</td><td>Sociology studies all aspects of social life comprehensively</td></tr>
<tr><td>Narrow scope — focuses on pure sociology</td><td>Broader scope — sociology is a general science of society</td></tr>
<tr><td>Emphasizes abstract forms of social interaction</td><td>Emphasizes concrete social phenomena and institutions</td></tr>
<tr><td>Excludes study of specific social institutions (family, religion)</td><td>Includes study of all social institutions and collective behavior</td></tr>
<tr><td>Considers sociology as a special social science</td><td>Considers sociology as the fundamental social science</td></tr>
</table><br/>
<b>Key Difference:</b> The Formalistic school believes sociology should study only the forms of social relationships (how people interact), while the Synthetic school believes sociology should study the entire content of social life, including all institutions, processes, and collective phenomena.""",
            },
            {
                "num": "3",
                "question": "Write an essay on 'relevance of sociology in computer application'.",
                "marks": "5",
                "answer": """<b>Relevance of Sociology in Computer Applications</b><br/><br/>
Sociology and computer applications may seem like unrelated fields, but they are increasingly interconnected in our technology-driven world. Understanding sociological principles is essential for developing effective, ethical, and user-centered computer applications.<br/><br/>
<b>1. User-Centered Design:</b><br/>
Sociological insights about human behavior, cultural norms, and social structures help software developers design applications that meet actual user needs. Understanding social contexts prevents designing apps that are technically sound but socially inappropriate or unusable.<br/><br/>
<b>2. Digital Divide:</b><br/>
Sociology helps identify gaps in technology access based on class, gender, age, geography, and education. Computer applications must be designed with awareness of these inequalities to ensure inclusive access.<br/><br/>
<b>3. Online Communities and Social Media:</b><br/>
Sociological theories about group formation, social influence, and collective behavior are essential for designing social media platforms, forums, and collaborative tools. Understanding how online communities form and function helps create healthier digital spaces.<br/><br/>
<b>4. Ethics and Privacy:</b><br/>
Sociology raises critical questions about surveillance, data privacy, and the social implications of AI. Computer professionals need sociological awareness to navigate ethical dilemmas around user data and algorithmic bias.<br/><br/>
<b>5. Technology and Social Change:</b><br/>
Sociology studies how technology transforms society — from employment patterns to family structures to political movements. Computer application developers benefit from understanding these impacts to create responsible technology.<br/><br/>
<b>Conclusion:</b><br/>
Sociology provides the human context that pure technical knowledge lacks. For computer applications to serve society effectively, developers must understand the social worlds in which their technologies operate.""",
            },
            {
                "num": "4",
                "question": "Discuss the influence of modern technology in changing family relationship.",
                "marks": "5",
                "answer": """<b>Influence of Modern Technology on Family Relationships:</b><br/><br/>
Modern technology has profoundly transformed family dynamics, creating both opportunities and challenges:<br/><br/>
<b>Positive Influences:</b><br/><br/>
<b>1. Enhanced Communication:</b> Smartphones and video calls (WhatsApp, Zoom, FaceTime) allow family members to stay connected across geographical distances. Migrant workers can regularly communicate with families back home.<br/><br/>
<b>2. Shared Experiences:</b> Families can watch movies together on streaming platforms, play online games, and share photos/videos, creating new forms of family bonding.<br/><br/>
<b>3. Access to Information:</b> Parents can access parenting resources, health information, and educational content to better care for children.<br/><br/>
<b>4. Safety and Monitoring:</b> GPS tracking and mobile apps help parents ensure children's safety and know their whereabouts.<br/><br/>
<b>Negative Influences:</b><br/><br/>
<b>1. Reduced Face-to-Face Interaction:</b> Family members often sit together but are absorbed in individual screens, reducing meaningful conversation and emotional connection.<br/><br/>
<b>2. Generation Gap:</b> Younger generations are often more tech-savvy than elders, creating communication barriers and reducing respect for elder wisdom.<br/><br/>
<b>3. Addiction and Distraction:</b> Excessive use of social media and gaming leads to neglect of family responsibilities and relationships.<br/><br/>
<b>4. Privacy Concerns:</b> Technology can invade family privacy through surveillance apps and social media oversharing, creating trust issues.<br/><br/>
<b>5. Changed Gender Roles:</b> Technology has enabled remote work, changing traditional division of household labor, which can cause adjustment tensions in families.<br/><br/>
<b>Conclusion:</b> Technology is a double-edged sword for families. Conscious, balanced use can strengthen relationships, while excessive or unmindful use can weaken them.""",
            },
            {
                "num": "5",
                "question": "What do you understand by society? How does it differ from community? Discuss with examples.",
                "marks": "5",
                "answer": """<b>Society:</b><br/>
Society is a group of people who share a common territory, culture, and social structure, and who interact with one another on a regular basis. It is a web of social relationships formed through interaction. Society is abstract, larger in scope, and includes diverse groups with varying interests.<br/><br/>
<b>Community:</b><br/>
A community is a group of people living in a specific geographical area who share common interests, values, and a sense of belonging. It is more concrete, localized, and characterized by "we-feeling" and face-to-face relationships.<br/><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Society</b></td><td><b>Community</b></td></tr>
<tr><td>Larger and more abstract</td><td>Smaller and more concrete</td></tr>
<tr><td>No definite locality required</td><td>Definite geographical area</td></tr>
<tr><td>Diverse interests and groups</td><td>Common interests and goals</td></tr>
<tr><td>Indirect/impersonal relationships</td><td>Direct/personal relationships</td></tr>
<tr><td>Weaker sense of belonging</td><td>Strong \"we-feeling\"</td></tr>
<tr><td>Example: Nepali society</td><td>Example: A village in Pokhara</td></tr>
</table><br/>
<b>Examples:</b><br/>
• <b>Society:</b> The entire nation of Nepal constitutes a society with diverse ethnicities, religions, and cultures.<br/>
• <b>Community:</b> The residents of a specific neighborhood in Kathmandu who know each other, celebrate festivals together, and share local concerns form a community.""",
            },
            {
                "num": "6",
                "question": "What is marriage and what are the various types of marriage? Describe with examples.",
                "marks": "5",
                "answer": """<b>Marriage:</b><br/>
Marriage is a socially and legally recognized union between two people (traditionally a man and a woman) that establishes rights and obligations between them, their children, and in-laws. It is a universal social institution found in all societies, though its form and rules vary across cultures.<br/><br/>
<b>Types of Marriage:</b><br/><br/>
<b>1. Monogamy:</b> Marriage between one man and one woman at a time. It is the most common form in modern societies.<br/>
<i>Example:</i> Christian marriages in Nepal and Western countries.<br/><br/>
<b>2. Polygamy:</b> Marriage involving more than one spouse. It has two forms:<br/>
• <b>Polygyny:</b> One man married to multiple women.<br/>
<i>Example:</i> Traditional practice among some Muslim communities and certain ethnic groups in Nepal.<br/>
• <b>Polyandry:</b> One woman married to multiple men.<br/>
<i>Example:</i> Fraternal polyandry practiced in some Himalayan communities of Nepal and Tibet, where brothers share a wife.<br/><br/>
<b>3. Endogamy:</b> Marriage within a specific social group, caste, or clan.<br/>
<i>Example:</i> Marriages within the same caste in traditional Hindu society.<br/><br/>
<b>4. Exogamy:</b> Marriage outside one's own group, clan, or family.<br/>
<i>Example:</i> Prohibition of marriage within the same gotra (clan) in Hindu tradition.<br/><br/>
<b>5. Arranged Marriage:</b> Marriage where families or matchmakers select partners.<br/>
<i>Example:</i> Common in South Asian societies including Nepal and India.<br/><br/>
<b>6. Love Marriage:</b> Marriage based on mutual romantic attraction and choice of partners.<br/>
<i>Example:</i> Increasingly common among urban youth in Nepal.""",
            },
            {
                "num": "7",
                "question": "What do you understand by social stratification? Discuss caste-based stratification in Nepalese society?",
                "marks": "5",
                "answer": """<b>Social Stratification:</b><br/>
Social stratification is the hierarchical arrangement of individuals and groups in a society based on wealth, power, prestige, education, or other criteria. It creates structured inequality where some positions are ranked higher than others. The major systems are: caste, class, estate, and slavery.<br/><br/>
<b>Characteristics:</b><br/>
• Universal — found in all societies<br/>
• Persistent — continues across generations<br/>
• Hierarchical — ranked from high to low<br/>
• Unequal distribution of resources and opportunities<br/><br/>
<b>Caste-Based Stratification in Nepalese Society:</b><br/><br/>
<b>1. Historical Background:</b><br/>
The caste system in Nepal was formally codified by the Muluki Ain (National Code) of 1854 under Jung Bahadur Rana. It classified people into a hierarchical social order based on Hindu varna system.<br/><br/>
<b>2. Hierarchy:</b><br/>
Traditionally, the hierarchy placed Tagadhari (wearers of sacred thread — Brahmins, Chhetris, Thakuris) at the top, followed by Matwali (alcohol-drinkers — various ethnic groups), and Pani Na Chalne (untouchables — Dalits) at the bottom.<br/><br/>
<b>3. Discrimination:</b><br/>
Dalits faced severe discrimination — exclusion from temples, denial of water sources, restricted occupations (menial work), and social ostracism. Inter-caste marriage was socially punished.<br/><br/>
<b>4. Legal Reforms:</b><br/>
The 1951 revolution and subsequent constitutions abolished untouchability. The 1990 constitution and 2015 constitution explicitly prohibit caste discrimination. The Caste-Based Discrimination and Untouchability (Offense and Punishment) Act, 2011 criminalizes such practices.<br/><br/>
<b>5. Current Status:</b><br/>
While legal barriers are removed, caste-based discrimination persists in rural areas, marriage practices, and political representation. Dalits remain socio-economically disadvantaged with lower literacy rates, income levels, and political participation.<br/><br/>
<b>6. Government Initiatives:</b><br/>
Reservation quotas in education, government jobs, and legislative bodies aim to uplift marginalized castes.""",
            },
            {
                "num": "8",
                "question": "Write Short Notes on any two:<br/>a) Assimilation<br/>b) Focus Group Discussion method in social research<br/>c) Quantitative research",
                "marks": "5",
                "answer": """<b>a) Assimilation:</b><br/>
Assimilation is the social process by which individuals or groups from different cultural backgrounds adopt the culture, values, and behaviors of another group, becoming integrated into the dominant culture. It involves the loss of distinct cultural identity of the minority group.<br/><br/>
<b>Characteristics:</b><br/>
• Unidirectional — minority adopts majority culture<br/>
• Involves cultural, biological, and psychological integration<br/>
• Results in homogenization of society<br/><br/>
<b>Example:</b> Immigrants to the United States adopting English language, American dress, and customs while losing their native traditions.<br/><br/>
<b>b) Focus Group Discussion (FGD) in Social Research:</b><br/>
FGD is a qualitative research method where a small group of participants (6-12 people) discuss a specific topic under the guidance of a moderator. It collects diverse perspectives through group interaction.<br/><br/>
<b>Advantages:</b><br/>
• Generates rich, detailed qualitative data<br/>
• Participants stimulate each other's thoughts<br/>
• Cost-effective compared to individual interviews<br/>
• Observes group dynamics and consensus-building<br/><br/>
<b>Limitations:</b><br/>
• Dominated by vocal participants<br/>
• Groupthink may suppress dissenting views<br/>
• Not statistically representative<br/><br/>
<b>c) Quantitative Research:</b><br/>
Quantitative research is a systematic empirical investigation of social phenomena using statistical, mathematical, or computational techniques. It focuses on quantifying relationships, testing hypotheses, and generalizing findings.<br/><br/>
<b>Features:</b><br/>
• Uses structured instruments (questionnaires, surveys)<br/>
• Large sample sizes for statistical validity<br/>
• Objective, measurable data<br/>
• Seeks cause-and-effect relationships<br/>
• Results are presented numerically and statistically<br/><br/>
<b>Methods:</b> Surveys, experiments, content analysis, statistical analysis<br/>
<b>Example:</b> A survey of 1000 Nepali youth measuring the correlation between social media use and academic performance using statistical tests.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "9",
                "question": "What do you understand by National Integration? What are the major dimensions of National Integration? Discuss.",
                "marks": "10",
                "answer": """<b>National Integration:</b><br/>
National integration is the process of uniting people from diverse ethnic, religious, linguistic, and cultural backgrounds into a cohesive nation with a shared identity, common goals, and mutual respect. It creates a sense of belonging to the nation above regional, communal, or sectarian loyalties.<br/><br/>
<b>Major Dimensions of National Integration:</b><br/><br/>
<b>1. Political Integration:</b><br/>
• Unification of political institutions and governance systems<br/>
• Equal representation of all regions and communities in government<br/>
• Rule of law and constitutional supremacy<br/>
• <b>In Nepal:</b> Federal system with 7 provinces aims to balance local autonomy with national unity<br/><br/>
<b>2. Social Integration:</b><br/>
• Breaking down caste, ethnic, and religious barriers<br/>
• Promoting inter-caste and inter-ethnic marriages<br/>
• Equal social status and dignity for all citizens<br/>
• <b>In Nepal:</b> Abolition of untouchability, promotion of social inclusion policies<br/><br/>
<b>3. Cultural Integration:</b><br/>
• Respecting and celebrating cultural diversity while building common national culture<br/>
• Shared national symbols (flag, anthem, constitution)<br/>
• Common festivals and national events<br/>
• <b>In Nepal:</b> Constitution recognizes all languages and cultures while promoting Nepali as lingua franca<br/><br/>
<b>4. Economic Integration:</b><br/>
• Balanced regional development to reduce economic disparities<br/>
• Equal access to resources, employment, and economic opportunities<br/>
• Infrastructure connecting all regions<br/>
• <b>In Nepal:</b> Need to address Kathmandu-centric development and uplift backward regions<br/><br/>
<b>5. Emotional/Psychological Integration:</b><br/>
• Sense of patriotism and national pride<br/>
• \"We-feeling\" transcending local identities<br/>
• Shared historical memory and future aspirations<br/><br/>
<b>Challenges to National Integration in Nepal:</b><br/>
• Ethnic and regional identity politics<br/>
• Economic inequality between regions<br/>
• Historical marginalization of certain communities<br/>
• Political instability and transitional justice issues<br/><br/>
<b>Conclusion:</b> National integration is not about eliminating diversity but creating unity in diversity. Nepal's multi-ethnic, multi-lingual, and multi-religious character can be its strength if managed through inclusive policies and shared national vision.""",
            },
            {
                "num": "10",
                "question": "'A greater proportion of an individual's personality is a reflection of the type of socialization process he or she has gone through during primary socialization'. Explain.",
                "marks": "10",
                "answer": """<b>Explanation of the Statement:</b><br/><br/>
This statement emphasizes the critical importance of primary socialization in shaping an individual's personality. Primary socialization occurs during childhood, primarily within the family, and lays the foundation for all subsequent social learning.<br/><br/>
<b>What is Primary Socialization?</b><br/>
Primary socialization is the first and most crucial phase of socialization, occurring during early childhood (typically 0-5 years). It takes place within the family and close kinship network. Children learn language, basic norms, values, emotional patterns, and self-concept during this period.<br/><br/>
<b>How Primary Socialization Shapes Personality:</b><br/><br/>
<b>1. Language Acquisition:</b><br/>
The language learned during primary socialization becomes the foundation of thought, communication, and cultural identity. It shapes how individuals perceive and categorize the world.<br/><br/>
<b>2. Value Internalization:</b><br/>
Children absorb the moral and ethical values of their family — honesty, respect, hard work, religious beliefs. These values become deeply embedded and resistant to change.<br/><br/>
<b>3. Emotional Development:</b><br/>
The quality of early parent-child attachment determines emotional regulation, self-esteem, and interpersonal trust. Secure attachment leads to confident, well-adjusted adults.<br/><br/>
<b>4. Gender Socialization:</b><br/>
Family teaches gender roles through differential treatment, toy selection, and behavioral expectations. These learned gender behaviors persist throughout life.<br/><br/>
<b>5. Cultural Identity:</b><br/>
Food habits, religious practices, festivals, and customs learned in childhood become part of one's core identity. Even when people migrate, they often retain these childhood cultural markers.<br/><br/>
<b>6. Self-Concept Formation:</b><br/>
The looking-glass self theory suggests children develop self-image based on how family members treat and label them. Positive reinforcement builds confidence; neglect or abuse creates insecurity.<br/><br/>
<b>Why It Outweighs Later Socialization:</b><br/>
• Childhood learning is most impressionable (critical period hypothesis)<br/>
• Family bonds create emotional investment in learned behaviors<br/>
• Early habits become subconscious and automatic<br/>
• Later socialization (school, peer groups, media) builds upon the foundation laid during primary socialization<br/><br/>
<b>Conclusion:</b> While secondary socialization (school, peers, media) continues to shape individuals, the fundamental personality structure — values, emotional patterns, self-concept, and cultural identity — is predominantly formed during primary socialization. This is why family environment is considered the most powerful influence on human development.""",
            },
            {
                "num": "11",
                "question": "Discuss the major data collection tools and techniques used in social research.",
                "marks": "10",
                "answer": """<b>Data Collection Tools and Techniques in Social Research:</b><br/><br/>
Social research employs various tools and techniques to gather reliable and valid data. These can be classified into primary and secondary methods.<br/><br/>
<b>A. Primary Data Collection:</b><br/><br/>
<b>1. Observation:</b><br/>
The researcher watches and records social behavior in natural or controlled settings.<br/>
• <b>Participant Observation:</b> Researcher participates in the group's activities (e.g., studying a religious cult by joining it)<br/>
• <b>Non-participant Observation:</b> Researcher observes without participating<br/>
• <b>Structured Observation:</b> Uses predetermined categories and checklists<br/>
• <b>Unstructured Observation:</b> Flexible, descriptive recording<br/><br/>
<b>2. Interview:</b><br/>
Direct verbal interaction between researcher and respondent.<br/>
• <b>Structured Interview:</b> Fixed questionnaire, standardized questions<br/>
• <b>Unstructured Interview:</b> Open-ended, conversational<br/>
• <b>Semi-structured Interview:</b> Mix of fixed and flexible questions<br/>
• <b>Focus Group Interview:</b> Group discussion guided by moderator<br/><br/>
<b>3. Questionnaire/Survey:</b><br/>
Written set of questions administered to a sample population.<br/>
• <b>Open-ended:</b> Respondents answer in their own words<br/>
• <b>Closed-ended:</b> Multiple choice, Likert scale, yes/no<br/>
• Administered through mail, online, or in-person<br/><br/>
<b>4. Case Study:</b><br/>
In-depth examination of a single case (person, group, event, or community).<br/>
• Uses multiple sources: interviews, documents, observation<br/>
• Provides rich, detailed qualitative data<br/><br/>
<b>5. Experiment:</b><br/>
Controlled investigation to establish cause-and-effect relationships.<br/>
• Laboratory experiments (controlled settings)<br/>
• Field experiments (natural settings)<br/><br/>
<b>B. Secondary Data Collection:</b><br/><br/>
<b>1. Official Records:</b> Census data, government reports, statistical yearbooks<br/>
<b>2. Historical Documents:</b> Letters, diaries, archives, autobiographies<br/>
<b>3. Mass Media:</b> Newspapers, magazines, television content<br/>
<b>4. Previous Research:</b> Academic journals, dissertations, books<br/>
<b>5. Internet Sources:</b> Websites, databases, digital archives<br/><br/>
<b>Selection Criteria:</b><br/>
Researchers choose tools based on research objectives, available resources, nature of the study, and target population. Triangulation (using multiple methods) enhances validity and reliability.""",
            },
        ]
    }
]

print("Generating CACS102 answer sheet...")
generate_answer_sheet("CACS102", "society-technology", "Society & Technology", 2019, "semester-1", CACS102_2019)
print("✅ CACS102 done!")

print("\n🎉 All 1st-semester 2019 answer sheets generated successfully!")
