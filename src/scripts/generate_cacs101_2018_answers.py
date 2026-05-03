#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS101_2018 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6\u00d75 = 30]",
        "questions": [
            {
                "num": "11",
                "question": "Define Computer. Explain the anatomy of digital computer with block diagram.",
                "marks": "1+4",
                "answer": """<b>Definition of Computer:</b><br/>
A computer is an electronic device that accepts raw data as input, processes it under the control of a set of instructions (program), stores the data and instructions in memory, and produces meaningful information as output. It works on the IPO (Input-Process-Output) cycle and can perform complex calculations at very high speed with accuracy.<br/><br/>
<b>Anatomy of a Digital Computer (Block Diagram Description):</b><br/>
A digital computer consists of the following major components connected through a system bus:<br/><br/>
<b>1. Input Unit:</b> Devices like keyboard, mouse, scanner, etc., are used to enter data and instructions into the computer. It converts human-readable data into machine-readable binary form.<br/><br/>
<b>2. Central Processing Unit (CPU):</b> The brain of the computer consisting of three parts:<br/>
\u2022 <b>Arithmetic Logic Unit (ALU):</b> Performs arithmetic (+, \u2212, \u00d7, \u00f7) and logical (AND, OR, NOT, comparison) operations.<br/>
\u2022 <b>Control Unit (CU):</b> Coordinates and controls all operations. It fetches instructions from memory, decodes them, and directs the ALU, memory, and I/O devices accordingly.<br/>
\u2022 <b>Registers:</b> Small, high-speed storage locations inside the CPU used to hold temporary data and instructions during processing.<br/><br/>
<b>3. Memory Unit:</b><br/>
\u2022 <b>Primary Memory (Main Memory):</b> Includes RAM (volatile, temporary storage for running programs) and ROM (non-volatile, stores BIOS/firmware).<br/>
\u2022 <b>Cache Memory:</b> Very fast memory between CPU and RAM to speed up data access.<br/>
\u2022 <b>Secondary Memory:</b> Permanent storage devices like HDD, SSD, CD/DVD, USB drives where data is stored long-term.<br/><br/>
<b>4. Output Unit:</b> Devices like monitor, printer, speaker that convert processed binary data into human-readable form and display results.<br/><br/>
<b>5. System Bus:</b> Communication pathways (data bus, address bus, control bus) that connect CPU, memory, and I/O devices, allowing data and control signals to flow between components.<br/><br/>
<b>Working:</b> Data enters via input \u2192 stored in memory \u2192 CPU fetches, decodes, and executes instructions (ALU performs operations) \u2192 results sent to output unit or stored back in memory/secondary storage.""",
                "diagram": "Draw a block diagram with Input Unit on the left connected to CPU (ALU + CU + Registers) in the center. CPU is connected to Memory (RAM/ROM) and Secondary Storage. Output Unit is on the right. All components are linked through System Bus lines labeled Data Bus, Address Bus, and Control Bus."
            },
            {
                "num": "12",
                "question": "Define Operating System. Explain the functions of Operating System.",
                "marks": "1+4",
                "answer": """<b>Operating System (OS):</b><br/>
An Operating System is a system software that acts as an intermediary between computer hardware and the user. It manages hardware resources, provides a user interface, and creates an environment in which application software can run. Examples: Windows, Linux, macOS, Android.<br/><br/>
<b>Functions of Operating System:</b><br/><br/>
<b>1. Process Management:</b> The OS creates, schedules, suspends, resumes, and terminates processes. It allocates the CPU to processes using scheduling algorithms (FCFS, SJF, Round Robin) and handles inter-process communication and synchronization.<br/><br/>
<b>2. Memory Management:</b> It keeps track of memory usage, allocates memory to programs when requested, and frees it when no longer needed. It manages virtual memory (paging, segmentation) to run large programs in limited physical RAM.<br/><br/>
<b>3. File Management:</b> The OS organizes data into files and directories, controls access permissions, and manages storage space on disks. It provides file system services like creation, deletion, copying, moving, and renaming files.<br/><br/>
<b>4. Device Management:</b> It manages all hardware devices through device drivers. The OS allocates devices to processes, handles I/O operations, and monitors device status (spooling, buffering, caching).<br/><br/>
<b>5. Security and Access Control:</b> It protects system resources from unauthorized access using authentication (username/password, biometrics) and authorization (permissions, ACLs). It also detects intrusions and maintains logs.<br/><br/>
<b>6. User Interface:</b> Provides Command Line Interface (CLI) or Graphical User Interface (GUI) for users to interact with the computer easily.<br/><br/>
<b>7. Error Handling:</b> Detects and recovers from errors (hardware failure, power issues, software bugs) to maintain system stability and data integrity.<br/><br/>
<b>8. Networking:</b> Manages network connections, protocols (TCP/IP), and communication between computers over a network."""
            },
            {
                "num": "13",
                "question": "Define DBMS. Explain the different database models with their merits and demerits.",
                "marks": "1+4",
                "answer": """<b>DBMS (Database Management System):</b><br/>
A DBMS is a software system that enables users to create, maintain, and manipulate databases. It provides an organized way to store, retrieve, update, and manage data efficiently while ensuring data integrity, security, and consistency. Examples: MySQL, Oracle, PostgreSQL, Microsoft SQL Server.<br/><br/>
<b>Different Database Models:</b><br/><br/>
<b>1. Hierarchical Model:</b><br/>
Data is organized in a tree-like structure with parent-child relationships (one-to-many). The root node has no parent, and each child has exactly one parent.<br/>
<b>Merits:</b> Simple and easy to understand; data integrity is strong due to parent-child links; efficient for one-to-many relationships.<br/>
<b>Demerits:</b> Complex to implement many-to-many relationships; inflexible \u2014 adding a new relationship requires restructuring the tree; difficult to navigate for non-hierarchical data.<br/>
<b>Example:</b> IBM IMS.<br/><br/>
<b>2. Network Model:</b><br/>
An extension of the hierarchical model where a child can have multiple parents (many-to-many relationships). Data is represented as records and sets (links).<br/>
<b>Merits:</b> Handles complex relationships better than hierarchical; reduces data redundancy; supports many-to-many relationships.<br/>
<b>Demerits:</b> Complex structure and navigation; difficult to design and maintain; changes in structure affect applications (low independence).<br/>
<b>Example:</b> CODASYL DBTG model.<br/><br/>
<b>3. Relational Model:</b><br/>
Data is stored in two-dimensional tables (relations) consisting of rows (tuples/records) and columns (attributes/fields). Relationships are established using keys (primary key, foreign key).<br/>
<b>Merits:</b> Simple and flexible; uses powerful query language (SQL); high data independence; easy to add/modify data without affecting other parts.<br/>
<b>Demerits:</b> Can be slower for very large datasets; complex queries may degrade performance; poor handling of unstructured data (images, videos).<br/>
<b>Example:</b> MySQL, Oracle, PostgreSQL.<br/><br/>
<b>4. Object-Oriented Model:</b><br/>
Data is stored as objects, similar to OOP concepts. Objects contain data (attributes) and methods (behaviors). Supports encapsulation, inheritance, and polymorphism.<br/>
<b>Merits:</b> Ideal for complex data types (multimedia, spatial data); integrates well with object-oriented programming languages; supports advanced features like inheritance.<br/>
<b>Demerits:</b> Complex to design and implement; lacks universal query language; performance overhead for simple data.<br/>
<b>Example:</b> db4o, ObjectDB."""
            },
            {
                "num": "14",
                "question": "Explain the different types of LAN topologies with their advantages and disadvantages.",
                "marks": "5",
                "answer": """<b>LAN Topology:</b> Topology refers to the physical or logical arrangement of devices (nodes) in a computer network. The main types of LAN topologies are:<br/><br/>
<b>1. Bus Topology:</b><br/>
All devices are connected to a single central cable called the bus or backbone. Data travels in both directions along the bus, and terminators are placed at both ends to absorb signals.<br/>
<b>Advantages:</b> Easy to install and requires less cable; inexpensive for small networks; suitable for temporary networks.<br/>
<b>Disadvantages:</b> Difficult to troubleshoot; a single cable failure brings down the entire network; limited length and number of nodes; performance degrades as traffic increases.<br/><br/>
<b>2. Star Topology:</b><br/>
All devices are connected to a central device (hub or switch) via individual cables. The central device manages all communications.<br/>
<b>Advantages:</b> Easy to install and manage; failure of one node does not affect others; easy fault detection and removal; high scalability.<br/>
<b>Disadvantages:</b> If the central hub/switch fails, the entire network goes down; requires more cable than bus topology; cost increases with the number of nodes.<br/><br/>
<b>3. Ring Topology:</b><br/>
Each device is connected to exactly two other devices, forming a circular data path. Data travels in one direction (unidirectional) or both directions (bidirectional) around the ring, passing through each node until it reaches the destination.<br/>
<b>Advantages:</b> Equal access for all nodes; no central device required; predictable performance under heavy load; easy to install in small networks.<br/>
<b>Disadvantages:</b> A single node or cable failure can disrupt the entire network; adding or removing nodes is difficult; troubleshooting is complex; data must pass through intermediate nodes.<br/><br/>
<b>4. Mesh Topology:</b><br/>
Every device is connected to every other device with dedicated point-to-point links. It can be full mesh (all-to-all) or partial mesh (some critical nodes connected to all).<br/>
<b>Advantages:</b> Highly reliable and fault-tolerant \u2014 multiple paths available; high security and privacy (dedicated links); easy fault isolation; high traffic capacity.<br/>
<b>Disadvantages:</b> Very expensive due to excessive cabling and hardware; complex installation and configuration; difficult to manage and maintain.<br/><br/>
<b>5. Tree (Hybrid) Topology:</b><br/>
A combination of bus and star topologies. Groups of star-configured networks are connected to a linear bus backbone.<br/>
<b>Advantages:</b> Scalable and flexible; easy to expand by adding new branches; fault isolation is easier than in bus topology.<br/>
<b>Disadvantages:</b> If the backbone cable fails, entire segments are affected; configuration is complex; cost is higher than simple topologies.""",
                "diagram": "Draw diagrams for Bus (single line with nodes), Star (central hub with radiating lines), Ring (circle of nodes), and Mesh (interconnected nodes with multiple links). Label each diagram clearly."
            },
            {
                "num": "15",
                "question": "What is WWW? Differentiate between intranet, extranet and internet with example.",
                "marks": "1+4",
                "answer": """<b>WWW (World Wide Web):</b><br/>
The World Wide Web is a system of interlinked hypertext documents and multimedia content accessed via the Internet using a web browser. It was invented by Tim Berners-Lee in 1989 at CERN. Web pages are identified by URLs (Uniform Resource Locators), connected by hyperlinks, and transmitted using HTTP/HTTPS protocols. The WWW is a service that runs on top of the Internet, distinct from the Internet itself (which is the global network infrastructure).<br/><br/>
<b>Differentiate between Intranet, Extranet, and Internet:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Basis</b></td><td><b>Internet</b></td><td><b>Intranet</b></td><td><b>Extranet</b></td></tr>
<tr><td><b>Definition</b></td><td>A global public network of interconnected computer networks accessible to everyone.</td><td>A private network restricted to an organization\'s employees and internal users.</td><td>A private network that allows authorized external users (partners, vendors, customers) to access part of an organization\'s intranet.</td></tr>
<tr><td><b>Access</b></td><td>Public \u2014 anyone with an Internet connection.</td><td>Private \u2014 only authorized internal members.</td><td>Limited \u2014 specific external users with permission.</td></tr>
<tr><td><b>Security</b></td><td>Less secure; requires personal firewalls/antivirus.</td><td>Highly secure; protected by firewalls and internal policies.</td><td>Secure; protected by firewalls, VPNs, and access controls.</td></tr>
<tr><td><b>Ownership</b></td><td>No single owner; maintained by ISPs and global organizations.</td><td>Owned and managed by a single organization.</td><td>Owned by one organization but shared with trusted partners.</td></tr>
<tr><td><b>Purpose</b></td><td>Global information sharing, communication, e-commerce, entertainment.</td><td>Internal communication, document sharing, workflow management.</td><td>Collaboration with business partners, supply chain management, B2B communication.</td></tr>
<tr><td><b>Example</b></td><td>Google, Facebook, Wikipedia accessible via public browsers.</td><td>A university\'s internal portal for students and staff (e.g., campus LMS).</td><td>A supplier portal where vendors can view inventory and place orders (e.g., Dell\'s partner portal).</td></tr>
</table>"""
            },
            {
                "num": "16",
                "question": "What are contemporary technologies? Explain any two contemporary technologies with roles.",
                "marks": "1+4",
                "answer": """<b>Contemporary Technologies:</b><br/>
Contemporary technologies refer to modern, emerging, and cutting-edge technologies that are currently shaping the world and transforming industries. These technologies include Cloud Computing, Artificial Intelligence (AI), Internet of Things (IoT), Blockchain, Big Data Analytics, Virtual Reality (VR), Augmented Reality (AR), 5G, Robotics, and Quantum Computing. They improve efficiency, automation, decision-making, and connectivity in various sectors.<br/><br/>
<b>1. Cloud Computing:</b><br/>
Cloud Computing is the on-demand delivery of computing resources (servers, storage, databases, networking, software) over the Internet (\u201cthe cloud\u201d) on a pay-as-you-go basis. Instead of owning and maintaining physical data centers, organizations rent resources from cloud providers.<br/>
<b>Roles:</b><br/>
\u2022 <b>Data Storage and Backup:</b> Stores vast amounts of data securely off-site (e.g., Google Drive, Dropbox).<br/>
\u2022 <b>Software as a Service (SaaS):</b> Delivers applications over the Internet (e.g., Gmail, Microsoft 365).<br/>
\u2022 <b>Infrastructure as a Service (IaaS):</b> Provides virtualized computing resources (e.g., AWS EC2, Azure VMs).<br/>
\u2022 <b>Platform as a Service (PaaS):</b> Offers development platforms and tools for building applications (e.g., Heroku, Google App Engine).<br/>
\u2022 <b>Scalability and Cost Reduction:</b> Businesses can scale resources up or down instantly without heavy capital investment.<br/>
<b>Example:</b> Netflix uses AWS cloud to stream content globally.<br/><br/>
<b>2. Internet of Things (IoT):</b><br/>
IoT refers to a network of physical devices embedded with sensors, software, and connectivity that enables them to collect and exchange data over the Internet. These \u201csmart\u201d devices can communicate with each other and with humans.<br/>
<b>Roles:</b><br/>
\u2022 <b>Smart Homes:</b> Home automation systems control lighting, temperature, and security remotely (e.g., Philips Hue, Nest thermostat).<br/>
\u2022 <b>Healthcare:</b> Wearable devices monitor heart rate, blood pressure, and activity levels in real time (e.g., Fitbit, Apple Watch).<br/>
\u2022 <b>Smart Agriculture:</b> Soil moisture sensors and automated irrigation systems optimize water usage and crop yield.<br/>
\u2022 <b>Industrial Automation:</b> Predictive maintenance and real-time monitoring in manufacturing reduce downtime.<br/>
\u2022 <b>Smart Cities:</b> Traffic management, waste management, and energy distribution are optimized using IoT sensors.<br/>
<b>Example:</b> Smart traffic lights that adjust timing based on real-time vehicle density."""
            },
            {
                "num": "17",
                "question": "Write the DOS commands to complete following tasks.<br/>a) Create sub directory theory and practical inside d:\\exam\\<br/>b) Create the file name marks.txt inside theory writing the content, \"Theory marks in CFA\".<br/>c) Rename the file name marks.txt with CFAmarks.txt.<br/>d) Make hidden the file CFAmarks.txt.<br/>e) Search the all files with .pdf extension.",
                "marks": "5",
                "answer": """<b>Solution \u2014 DOS Commands:</b><br/><br/>
<b>a) Create subdirectories THEORY and PRACTICAL inside D:\\EXAM:</b><br/>
<pre>MD D:\\EXAM\\THEORY
MD D:\\EXAM\\PRACTICAL</pre>
Or using a single line:<br/>
<pre>MD D:\\EXAM\\THEORY D:\\EXAM\\PRACTICAL</pre>
(<i>MD</i> or <i>MKDIR</i> creates directories.)<br/><br/>
<b>b) Create the file MARKS.TXT inside THEORY with the given content:</b><br/>
<pre>ECHO Theory marks in CFA > D:\\EXAM\\THEORY\\MARKS.TXT</pre>
(<i>ECHO</i> displays text; the <i>></i> operator redirects the output into the file.)<br/><br/>
<b>c) Rename MARKS.TXT to CFAmarks.TXT:</b><br/>
<pre>REN D:\\EXAM\\THEORY\\MARKS.TXT CFAmarks.TXT</pre>
Or:<br/>
<pre>RENAME D:\\EXAM\\THEORY\\MARKS.TXT CFAmarks.TXT</pre><br/>
<b>d) Make the file CFAmarks.TXT hidden:</b><br/>
<pre>ATTRIB +H D:\\EXAM\\THEORY\\CFAmarks.TXT</pre>
(<i>ATTRIB</i> changes file attributes; <i>+H</i> sets the hidden attribute.)<br/><br/>
<b>e) Search all files with .PDF extension:</b><br/>
<pre>DIR D:\\*.PDF /S</pre>
Or to search within the EXAM directory tree only:<br/>
<pre>DIR D:\\EXAM\\*.PDF /S</pre>
(<i>DIR</i> lists directory contents; <i>/S</i> searches all subdirectories.)<br/><br/>
<b>Note:</b> In DOS, commands are case-insensitive. Always ensure the correct path is used, and use double quotes around paths that contain spaces."""
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2\u00d710 = 20]",
        "questions": [
            {
                "num": "18",
                "question": "i) You are provided following data: Bageswori Secondary School, Surkhet, Mark-Ledger (spreadsheet with student names and marks in 5 subjects) Write the formula in spread sheet package to calculate following on basis on given conditions:<br/>1. Calculate Total marks.<br/>2. Calculate Percentage.<br/>3. Mark the student with either \"PASS\" or \"FAIL\" [Pass Marks 35].<br/>4. Calculate the division [if percentage >=60 then First, if percentage >=45 and percentage <60 then Second, if percentage >=35 and percentage <45 then Third otherwise \"xxx\"]<br/>ii) Explain the features of Font control tools in word processing package.",
                "marks": "6+4",
                "answer": """<b>i) Spreadsheet Formulas (e.g., Microsoft Excel / LibreOffice Calc):</b><br/>
Assume:<br/>
\u2022 Column A = Student Name<br/>
\u2022 Columns B, C, D, E, F = Marks in 5 subjects (each out of 100)<br/>
\u2022 Column G = Total Marks<br/>
\u2022 Column H = Percentage<br/>
\u2022 Column I = Pass / Fail<br/>
\u2022 Column J = Division<br/>
Row 2 is the first data row.<br/><br/>
<b>1. Calculate Total Marks (in G2):</b><br/>
<pre>=SUM(B2:F2)</pre>
Or manually:<br/>
<pre>=B2+C2+D2+E2+F2</pre><br/>
<b>2. Calculate Percentage (in H2):</b><br/>
<pre>=(G2/500)*100</pre>
Or simply:<br/>
<pre>=G2/5</pre><br/>
<b>3. Mark PASS or FAIL (in I2) \u2014 Pass Marks = 35 in each subject:</b><br/>
<pre>=IF(AND(B2>=35,C2>=35,D2>=35,E2>=35,F2>=35),"PASS","FAIL")</pre>
Alternatively, using MIN to check if the lowest subject mark is at least 35:<br/>
<pre>=IF(MIN(B2:F2)>=35,"PASS","FAIL")</pre><br/>
<b>4. Calculate Division (in J2):</b><br/>
<pre>=IF(H2>=60,"First",IF(H2>=45,"Second",IF(H2>=35,"Third","xxx")))</pre><br/>
<b>Note:</b> After entering formulas in the first row, use the fill handle (drag down) to copy them to all student rows.<br/><br/>
<b>ii) Features of Font Control Tools in Word Processing:</b><br/>
Font control tools allow users to format text appearance for readability and emphasis. The main features are:<br/><br/>
<b>1. Font Typeface / Font Family:</b> Choose from various typefaces such as Times New Roman, Arial, Calibri, Verdana. Each font has a distinct style suitable for different document types.<br/><br/>
<b>2. Font Size:</b> Adjust the height of characters (measured in points, e.g., 10pt, 12pt, 14pt). Heading sizes are typically larger than body text.<br/><br/>
<b>3. Font Style (Bold, Italic, Underline):</b><br/>
\u2022 <b>Bold</b> \u2014 makes text darker and thicker for emphasis.<br/>
\u2022 <b>Italic</b> \u2014 slants text for titles, foreign words, or emphasis.<br/>
\u2022 <b>Underline</b> \u2014 draws a line beneath text; often used for headings or hyperlinks.<br/>
\u2022 Additional styles: <b>Strikethrough</b> (crosses out text), <b>Subscript</b> (below baseline), <b>Superscript</b> (above baseline).<br/><br/>
<b>4. Font Color:</b> Changes the color of text using a color palette or custom RGB values. Useful for headings, warnings, or highlighting.<br/><br/>
<b>5. Text Highlighting / Background Color:</b> Applies a background color behind text to make it stand out (like a highlighter pen).<br/><br/>
<b>6. Text Effects:</b> Shadow, reflection, glow, outline, emboss, and engrave effects add visual depth and style to text.<br/><br/>
<b>7. Character Spacing (Kerning & Tracking):</b> Adjusts the space between characters for tighter or looser text fitting.<br/><br/>
<b>8. Change Case:</b> Quickly convert text to UPPERCASE, lowercase, Title Case, or tOGGLE cASE.<br/><br/>
<b>9. Default Font Settings:</b> Set a default font and size for all new documents to maintain consistency."""
            },
            {
                "num": "19",
                "question": "i) Define computer peripherals. Differentiate between impact and non-impact printers.<br/>ii) Define Presentation. Write the features of good presentation package.",
                "marks": "5+5",
                "answer": """<b>i) Computer Peripherals:</b><br/>
Computer peripherals are external devices connected to the computer to expand its functionality. They are not part of the core computer architecture (CPU, memory) but are essential for input, output, storage, and communication. Peripherals are classified into:<br/>
\u2022 <b>Input Peripherals:</b> Keyboard, mouse, scanner, microphone, webcam<br/>
\u2022 <b>Output Peripherals:</b> Monitor, printer, speaker, plotter<br/>
\u2022 <b>Storage Peripherals:</b> External HDD, USB flash drive, optical disc<br/>
\u2022 <b>Communication Peripherals:</b> Modem, network card, router<br/><br/>
<b>Differentiate between Impact and Non-Impact Printers:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Basis</b></td><td><b>Impact Printers</b></td><td><b>Non-Impact Printers</b></td></tr>
<tr><td><b>Mechanism</b></td><td>Print head physically strikes an ink ribbon against the paper.</td><td>Uses ink spray, laser beam, heat, or electrostatic method without physical contact.</td></tr>
<tr><td><b>Noise</b></td><td>Noisy due to mechanical striking.</td><td>Quiet operation.</td></tr>
<tr><td><b>Speed</b></td><td>Slower (measured in characters per second).</td><td>Faster (measured in pages per minute).</td></tr>
<tr><td><b>Print Quality</b></td><td>Lower resolution; characters may appear dotty.</td><td>High resolution and sharp output (300\u20132400+ dpi).</td></tr>
<tr><td><b>Cost</b></td><td>Cheaper to purchase and maintain.</td><td>Higher initial cost but lower cost per page for high volume.</td></tr>
<tr><td><b>Color Capability</b></td><td>Generally limited or monochrome.</td><td>Excellent color printing capability.</td></tr>
<tr><td><b>Multi-part Forms</b></td><td>Can print on carbon copies (multi-layer paper).</td><td>Cannot print on carbon copies.</td></tr>
<tr><td><b>Examples</b></td><td>Dot Matrix Printer, Daisy Wheel Printer, Line Printer</td><td>Inkjet Printer, Laser Printer, Thermal Printer, LED Printer</td></tr>
</table><br/><br/>
<b>ii) Presentation:</b><br/>
A presentation is a visual communication tool used to convey information, ideas, or proposals to an audience in a structured and engaging manner. It typically consists of a series of slides containing text, images, charts, audio, video, and animations. Presentation software (e.g., Microsoft PowerPoint, Google Slides, LibreOffice Impress) helps create and deliver these slideshows.<br/><br/>
<b>Features of a Good Presentation Package:</b><br/><br/>
<b>1. Slide Creation and Management:</b> Easy creation, duplication, deletion, reordering, and organization of slides into sections.<br/><br/>
<b>2. Templates and Themes:</b> Pre-designed layouts, color schemes, and font combinations that ensure visual consistency and professional appearance.<br/><br/>
<b>3. Rich Multimedia Support:</b> Ability to insert images, audio, video, charts, graphs, tables, SmartArt, and 3D objects.<br/><br/>
<b>4. Animations and Transitions:</b> Customizable entrance, emphasis, and exit animations for slide elements; smooth slide transition effects to maintain audience engagement.<br/><br/>
<b>5. Master Slides:</b> A master template that controls the default layout, fonts, colors, and backgrounds across all slides, ensuring uniformity.<br/><br/>
<b>6. Drawing and Shape Tools:</b> Built-in shapes, lines, arrows, flowcharts, and freehand drawing tools for visual illustration.<br/><br/>
<b>7. Speaker Notes and Handouts:</b> Speaker notes for presenter reference and printable handout versions for the audience.<br/><br/>
<b>8. Collaboration and Sharing:</b> Real-time collaboration, cloud storage, export to PDF/Video, and online sharing options.<br/><br/>
<b>9. Slide Show Options:</b> Custom slide shows, rehearsal timing, laser pointer tool, pen/highlighter during presentation, and presenter view.<br/><br/>
<b>10. Integration:</b> Compatibility with other office applications, import/export of data from spreadsheets and word processors."""
            },
            {
                "num": "20",
                "question": "Define CMYK color model. Explain the basic tools and transforms available in Photoshop.",
                "marks": "2+8",
                "answer": """<b>CMYK Color Model:</b><br/>
CMYK is a subtractive color model used primarily in color printing. The name stands for the four ink colors used:<br/>
\u2022 <b>C</b> \u2014 Cyan (a blue-green color)<br/>
\u2022 <b>M</b> \u2014 Magenta (a pink-purple color)<br/>
\u2022 <b>Y</b> \u2014 Yellow<br/>
\u2022 <b>K</b> \u2014 Key (Black)<br/><br/>
In the subtractive model, colors are created by absorbing (subtracting) light. When cyan, magenta, and yellow inks are combined in equal amounts, they theoretically produce black. However, due to impurities in real inks, a muddy brown is produced, so black (K) ink is added to produce true dark tones, improve contrast, and save colored ink. CMYK is the standard for magazines, brochures, business cards, and any material printed on paper.<br/><br/>
<b>Basic Tools Available in Adobe Photoshop:</b><br/><br/>
<b>1. Selection Tools:</b><br/>
\u2022 <b>Marquee Tool:</b> Selects rectangular or elliptical areas.<br/>
\u2022 <b>Lasso Tool:</b> Freehand selection; includes Polygonal Lasso (straight-edged) and Magnetic Lasso (snaps to edges).<br/>
\u2022 <b>Magic Wand:</b> Selects regions of similar color with one click.<br/>
\u2022 <b>Quick Selection Tool:</b> Paints a selection using an adjustable brush; auto-detects edges.<br/><br/>
<b>2. Move Tool:</b> Moves layers, selections, and objects within the canvas.<br/><br/>
<b>3. Crop and Slice Tools:</b><br/>
\u2022 <b>Crop Tool:</b> Trims unwanted outer areas of an image and straightens horizons.<br/>
\u2022 <b>Slice Tool:</b> Divides an image into sections for web design.<br/><br/>
<b>4. Retouching Tools:</b><br/>
\u2022 <b>Healing Brush / Spot Healing Brush:</b> Removes blemishes by blending sampled pixels.<br/>
\u2022 <b>Clone Stamp Tool:</b> Copies pixels from one area to another.<br/>
\u2022 <b>Patch Tool:</b> Repairs selected areas using texture from another area.<br/>
\u2022 <b>Content-Aware Fill:</b> Intelligently fills selected areas using surrounding content.<br/><br/>
<b>5. Painting Tools:</b><br/>
\u2022 <b>Brush Tool:</b> Paints with soft or hard-edged strokes using various presets.<br/>
\u2022 <b>Pencil Tool:</b> Creates hard-edged freehand lines.<br/>
\u2022 <b>Color Replacement Tool:</b> Replaces a specific color with another.<br/>
\u2022 <b>Mixer Brush:</b> Simulates real painting techniques by mixing colors on the canvas.<br/><br/>
<b>6. Drawing and Type Tools:</b><br/>
\u2022 <b>Pen Tool:</b> Creates precise paths and shapes using B\u00e9zier curves.<br/>
\u2022 <b>Shape Tools:</b> Rectangle, rounded rectangle, ellipse, polygon, line, and custom shapes.<br/>
\u2022 <b>Horizontal/Vertical Type Tool:</b> Adds and edits text layers with full typographic control.<br/><br/>
<b>7. Navigation and Measurement:</b><br/>
\u2022 <b>Zoom Tool:</b> Magnifies or reduces the view.<br/>
\u2022 <b>Hand Tool:</b> Pans across a zoomed image.<br/>
\u2022 <b>Eyedropper Tool:</b> Samples a color from the image to set as the foreground color.<br/><br/>
<b>Transforms Available in Photoshop:</b><br/><br/>
<b>1. Scale:</b> Resizes an object or layer proportionally or non-proportionally.<br/><br/>
<b>2. Rotate:</b> Turns an object around a pivot point by a specified angle.<br/><br/>
<b>3. Skew:</b> Slants an object along the horizontal or vertical axis.<br/><br/>
<b>4. Distort:</b> Allows independent movement of each corner handle to stretch an object into any quadrilateral shape.<br/><br/>
<b>5. Perspective:</b> Simulates one-point perspective by moving opposite corners together, useful for correcting building photographs.<br/><br/>
<b>6. Warp:</b> Deforms an object using a customizable grid or preset shapes (arc, flag, wave, fisheye, etc.).<br/><br/>
<b>7. Flip Horizontal / Flip Vertical:</b> Mirrors an object horizontally or vertically.<br/><br/>
<b>8. Free Transform (Ctrl+T / Cmd+T):</b> Combines Scale, Rotate, Skew, Distort, and Perspective in a single interactive bounding box.<br/><br/>
<b>9. Puppet Warp:</b> Places pins on an object and drags them to bend and pose rigid objects naturally.<br/><br/>
<b>10. Liquify:</b> A dedicated workspace for pushing, pulling, rotating, reflecting, puffing, or reconstructing areas of an image \u2014 commonly used for portrait retouching."""
            },
        ]
    }
]

if __name__ == "__main__":
    print("Generating CACS101 2018 answer sheet...")
    generate_answer_sheet(
        "CACS101",
        "computer-fundamentals",
        "Computer Fundamentals & Applications",
        2018,
        "semester-1",
        CACS101_2018
    )
    print("\u2705 CACS101 2018 answer sheet generated successfully!")
