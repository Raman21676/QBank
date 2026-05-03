import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS101_2020 = [
    {
        "title": "Group A",
        "instruction": "Attempt all the questions. [10×1=10]",
        "questions": [
            {
                "num": "1.i",
                "question": "Which color mode is used for printing?",
                "marks": "1",
                "answer": """<b>Correct Answer: b) CMYK</b><br/>
CMYK (Cyan, Magenta, Yellow, Key/Black) is the standard color model used for printing. Unlike RGB which is used for digital screens, CMYK is a subtractive color model that creates colors by combining inks on paper. Printers use these four ink colors to produce a wide range of colors on physical media.""",
            },
            {
                "num": "1.ii",
                "question": "Which of the following short-cut key is used to open a new file in MS Word?",
                "marks": "1",
                "answer": """<b>Correct Answer: c) Ctrl + N</b><br/>
<b>Ctrl + N</b> is the standard keyboard shortcut to create a new document in MS Word and most other Windows applications. <br/>
• Ctrl + C = Copy<br/>
• Ctrl + V = Paste<br/>
• Ctrl + X = Cut<br/>
• Ctrl + N = New document""",
            },
            {
                "num": "1.iii",
                "question": "Which printer uses a combination of Laser-beam & electro photographic techniques?",
                "marks": "1",
                "answer": """<b>Correct Answer: a) Laser printers</b><br/>
Laser printers use a laser beam to project an image onto a rotating drum (photoconductor) that is electrostatically charged. The laser discharges specific areas of the drum, creating an electrostatic latent image. Toner particles are attracted to the charged areas and then transferred and fused onto paper using heat. This combination of laser technology and electrophotography produces high-quality, fast prints.""",
            },
            {
                "num": "1.iv",
                "question": "What kind of transmission medium is most appropriate to carry data in a computer network that is exposed to electrical interferences?",
                "marks": "1",
                "answer": """<b>Correct Answer: b) Optical fiber</b><br/>
Optical fiber is the most appropriate transmission medium in environments with electrical interference because it transmits data as light pulses through glass or plastic fibers, not electrical signals. Since it does not conduct electricity, it is completely immune to electromagnetic interference (EMI), radio frequency interference (RFI), and crosstalk. It also offers higher bandwidth, longer distances, and better security compared to copper cables.""",
            },
            {
                "num": "1.v",
                "question": "What is the easiest way to place same graphic in same place in all slides?",
                "marks": "1",
                "answer": """<b>Correct Answer: d) Place graphic in Slide Master</b><br/>
The <b>Slide Master</b> in PowerPoint controls the default layout and appearance of all slides in a presentation. By placing a graphic (such as a logo, watermark, or header) in the Slide Master, it automatically appears in the same position on every slide that uses that master layout. This ensures consistency and saves time compared to manually placing the graphic on each individual slide.""",
            },
            {
                "num": "1.vi",
                "question": "Which of the following is not function of DBA?",
                "marks": "1",
                "answer": """<b>Correct Answer: a) Network Maintenance</b><br/>
<b>Network Maintenance</b> is not a function of a Database Administrator (DBA). The primary functions of a DBA include:<br/>
• <b>Schema Definition:</b> Designing and defining the database structure<br/>
• <b>Routine Maintenance:</b> Backup, recovery, performance tuning, and optimization<br/>
• <b>Authorization for data access:</b> Granting and revoking user privileges<br/>
• Data integrity enforcement and security management<br/><br/>
Network maintenance is the responsibility of network administrators, not DBAs.""",
            },
            {
                "num": "1.vii",
                "question": "What is the role of internet to provide services such as the World Wide Web and E-mail?",
                "marks": "1",
                "answer": """<b>Correct Answer: d) Server</b><br/>
Servers are specialized computers or software systems that store, process, and deliver content and services to client devices over the internet. Web servers host websites and deliver web pages via HTTP/HTTPS, while mail servers handle sending, receiving, and storing email messages. Without servers, services like the World Wide Web and E-mail would not function, as they rely on server-client architecture where clients (browsers, email apps) request resources from servers.""",
            },
            {
                "num": "1.viii",
                "question": "Which of the following is purpose of GIS for Mapmakers?",
                "marks": "1",
                "answer": """<b>Correct Answer: d) store, use and view geographic information</b><br/>
A <b>Geographic Information System (GIS)</b> is a powerful tool for mapmakers that enables them to capture, store, manipulate, analyze, manage, and present spatial or geographic data. GIS integrates hardware, software, and data for capturing all types of geographically referenced information. Mapmakers use GIS to store geographic information in databases, analyze and use that information for various applications (urban planning, environmental management, navigation), and visualize it through interactive digital maps.""",
            },
            {
                "num": "1.ix",
                "question": "Where does bitcoin come from?",
                "marks": "1",
                "answer": """<b>Correct Answer: c) Mining</b><br/>
Bitcoins are created through a process called <b>mining</b>, which involves using powerful computers to solve complex mathematical problems (cryptographic hash functions). Miners compete to validate and add new blocks of transactions to the blockchain. As a reward for their computational work and for securing the network, miners receive newly created bitcoins. This process is called the Proof-of-Work consensus mechanism. The total supply of Bitcoin is capped at 21 million coins.""",
            },
            {
                "num": "1.x",
                "question": "Which of the following is the primary purpose of operating system?",
                "marks": "1",
                "answer": """<b>Correct Answer: a) To make the most efficient use of the computer hardware</b><br/>
The <b>primary purpose</b> of an operating system is to manage computer hardware resources efficiently and provide an environment for application software to run. While making computers easier to use (option d) and allowing people to use computers (option b) are important goals, the fundamental purpose is resource management — including CPU scheduling, memory management, disk I/O management, and device control — to maximize hardware utilization, throughput, and overall system performance.""",
            },
        ]
    }
]

generate_answer_sheet("CACS101", "computer-fundamentals", "Computer Fundamentals & Applications", 2020, "semester-1", CACS101_2020)
