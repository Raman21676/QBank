import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS103_2020 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What are the limitations of personal computers? Do you think students should be allowed to use computers in class?",
                "marks": "3+2",
                "answer": """<b>Limitations of Personal Computers:</b><br/><br/>
1. <b>Limited Processing Power:</b> Personal computers typically have less processing power, memory, and storage compared to workstations, servers, or mainframes. They cannot efficiently handle extremely large datasets, complex scientific simulations, or heavy multi-user workloads.<br/><br/>
2. <b>Single-User Design:</b> PCs are primarily designed for individual use. They lack the multi-user capabilities, robust security features, and concurrent processing abilities of larger systems.<br/><br/>
3. <b>Hardware Constraints:</b> Most personal computers have limited expansion slots, restricted graphics capabilities (in basic models), and fixed physical resources that cannot easily scale for professional-grade tasks.<br/><br/>
4. <b>Security Vulnerabilities:</b> PCs connected to the internet are exposed to viruses, malware, ransomware, and hacking attempts. Individual users often lack enterprise-level security infrastructure.<br/><br/>
5. <b>Physical Durability:</b> Consumer-grade PCs may not withstand extreme environmental conditions (temperature, humidity, dust) that industrial or specialized computers can endure.<br/><br/>
6. <b>Distraction and Health Issues:</b> Prolonged computer use can cause eye strain, repetitive strain injury (RSI), and sedentary lifestyle-related health problems. Additionally, easy access to entertainment and social media can reduce productivity.<br/><br/>
<b>Should Students Be Allowed to Use Computers in Class?</b><br/><br/>
Yes, students should be allowed to use computers in class, but with appropriate guidelines. Computers provide access to vast educational resources, enable interactive learning, facilitate research, and develop digital literacy skills essential for modern careers. However, schools should implement measures to minimize distractions — such as blocking non-educational sites during class, teaching digital responsibility, and balancing screen time with traditional learning methods. When used purposefully, computers significantly enhance educational outcomes.""",
            },
            {
                "num": "3",
                "question": "What kinds of facilities do online service provide? What online services are available in your country?",
                "marks": "3+2",
                "answer": """<b>Facilities Provided by Online Services:</b><br/><br/>
1. <b>Communication:</b> Email, instant messaging, video conferencing, and social networking that connect people globally in real-time.<br/><br/>
2. <b>Information Retrieval:</b> Search engines, digital libraries, news portals, and educational resources providing instant access to vast amounts of information.<br/><br/>
3. <b>E-Commerce:</b> Online shopping, digital payment systems, online banking, and financial transaction services that enable commercial activities without physical presence.<br/><br/>
4. <b>Entertainment:</b> Streaming services for movies, music, and games; digital downloads; and online gaming platforms.<br/><br/>
5. <b>Education and Training:</b> E-learning platforms, online courses, virtual classrooms, webinars, and digital certification programs.<br/><br/>
6. <b>Cloud Storage and Computing:</b> Remote data storage, file sharing, backup services, and access to software applications via the internet.<br/><br/>
7. <b>Government and Public Services:</b> E-governance portals for tax filing, passport applications, license renewals, and access to public records.<br/><br/>
<b>Online Services Available in Nepal:</b><br/><br/>
Nepal has rapidly expanded its digital service infrastructure. Major online services include:<br/>
• <b>Financial:</b> Mobile banking (via apps like eSewa, Khalti, IME Pay), internet banking from commercial banks, and digital wallets.<br/>
• <b>E-Commerce:</b> Daraz, SastoDeal, and various Facebook/Instagram-based businesses.<br/>
• <b>Communication:</b> Viber, WhatsApp, Messenger, Zoom, Google Meet, and Microsoft Teams.<br/>
• <b>Transportation:</b> Pathao, InDriver, and ride-sharing apps.<br/>
• <b>Food Delivery:</b> Foodmandu, Bhojdeals.<br/>
• <b>Government:</b> Nagarik App (for citizenship and passport services), IRD online tax system, and company registration portals.<br/>
• <b>Education:</b> Online learning platforms, virtual classes, and digital libraries from universities and schools.""",
            },
            {
                "num": "4",
                "question": "How is digital transmission different from analog transmission?",
                "marks": "5",
                "answer": """<b>Digital Transmission vs Analog Transmission</b><br/><br/>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Basis of Difference</b></td><td><b>Analog Transmission</b></td><td><b>Digital Transmission</b></td></tr>
<tr><td>Signal Form</td><td>Transmits continuous signals that vary in amplitude, frequency, or phase</td><td>Transmits discrete signals represented as binary digits (0s and 1s)</td></tr>
<tr><td>Waveform</td><td>Uses sinusoidal waves that are smooth and continuous</td><td>Uses square waves with discrete voltage levels (high/low)</td></tr>
<tr><td>Noise Immunity</td><td>Highly susceptible to noise and signal degradation over distance</td><td>Less susceptible to noise; can be regenerated using repeaters</td></tr>
<tr><td>Quality</td><td>Quality degrades with distance and interference</td><td>Quality remains consistent; information can be perfectly reproduced</td></tr>
<tr><td>Bandwidth Usage</td><td>Generally requires less bandwidth</td><td>Requires more bandwidth but allows multiplexing and compression</td></tr>
<tr><td>Error Detection</td><td>Difficult to detect and correct errors</td><td>Easy to implement error detection and correction codes</td></tr>
<tr><td>Equipment</td><td>Simpler, less expensive basic equipment</td><td>More complex but increasingly affordable electronics</td></tr>
<tr><td>Examples</td><td>Traditional radio broadcasts, landline telephones, vinyl records, cassette tapes</td><td>Computer networks, CD/DVD, digital TV, mobile phones, fiber optic communication</td></tr>
</table><br/>
<b>Key Advantage of Digital:</b> Digital signals can be compressed, encrypted, and processed by computers directly. They enable modern technologies such as the internet, streaming, and cloud computing. Analog systems have largely been replaced by digital systems in most communication domains due to superior reliability and flexibility.""",
            },
            {
                "num": "5",
                "question": "What is a DBMS? What is its function?",
                "marks": "2+3",
                "answer": """<b>DBMS (Database Management System)</b><br/>
A Database Management System is software that enables users to create, manage, and manipulate databases. It serves as an interface between users/applications and the physical database, abstracting the complexity of data storage and retrieval. Popular DBMS examples include MySQL, Oracle, PostgreSQL, Microsoft SQL Server, and MongoDB. A DBMS ensures that data is organized, accessible, secure, and consistent.<br/><br/>
<b>Functions of DBMS:</b><br/><br/>
1. <b>Data Definition:</b><br/>
DBMS provides Data Definition Language (DDL) for defining the database structure, including tables, fields, relationships, constraints, and indexes. It maintains a data dictionary (catalog) that stores metadata about the database.<br/><br/>
2. <b>Data Manipulation:</b><br/>
Through Data Manipulation Language (DML), users can insert, update, delete, and retrieve data. Query languages like SQL allow complex searches, sorting, filtering, and aggregation of data.<br/><br/>
3. <b>Data Security and Integrity:</b><br/>
DBMS enforces security through authentication (user login), authorization (access privileges), and encryption. It maintains data integrity by enforcing constraints (primary keys, foreign keys, unique constraints, check constraints) and ensuring that data remains accurate and consistent.<br/><br/>
4. <b>Concurrency Control:</b><br/>
In multi-user environments, DBMS manages simultaneous access to data using locking mechanisms and transaction management. This prevents conflicts, data corruption, and ensures that each user sees a consistent view of the data.<br/><br/>
5. <b>Backup and Recovery:</b><br/>
DBMS provides tools for regular data backup and recovery procedures in case of system failures, crashes, or human errors. It uses logging and checkpoint mechanisms to restore the database to a consistent state.<br/><br/>
6. <b>Data Independence:</b><br/>
DBMS separates logical data structure (how data appears to users) from physical storage (how data is actually stored on disk). This allows changes to storage without affecting applications, and changes to logical structure without rewriting physical storage.""",
            },
            {
                "num": "6",
                "question": "What is operating system? Why is it important to assess it on a computer before buying one?",
                "marks": "2+3",
                "answer": """<b>Operating System (OS)</b><br/>
An Operating System is system software that manages computer hardware and software resources and provides common services for computer programs. It acts as an intermediary between users and the computer hardware. Examples include Microsoft Windows, macOS, Linux distributions (Ubuntu, Fedora), Android, and iOS. The OS handles process management, memory management, file systems, device control, security, and user interface.<br/><br/>
<b>Why It Is Important to Assess the OS Before Buying a Computer:</b><br/><br/>
1. <b>Software Compatibility:</b><br/>
Different operating systems support different software applications. If you need specific professional software (e.g., Adobe Creative Suite, AutoCAD, specific development tools), you must ensure the OS supports it. Some software is exclusive to certain platforms — for example, Final Cut Pro only runs on macOS, while many enterprise applications are designed for Windows.<br/><br/>
2. <b>User Interface and Ease of Use:</b><br/>
The OS determines the user experience. Windows offers broad compatibility and familiar interface; macOS provides a polished, integrated ecosystem for Apple devices; Linux offers customization and power for technical users. Choosing an OS that matches your comfort level and workflow improves productivity.<br/><br/>
3. <b>Hardware Requirements and Performance:</b><br/>
Different operating systems have varying hardware demands. Modern versions of Windows require more RAM and processing power than lightweight Linux distributions. Assessing the OS ensures that the computer's specifications can run it smoothly without lag or performance issues.<br/><br/>
4. <b>Security and Stability:</b><br/>
Operating systems differ in their security architecture and vulnerability profiles. Linux and macOS are generally considered more secure against viruses than Windows due to their architecture and smaller malware targeting. For users handling sensitive data, OS security features (encryption, sandboxing, update mechanisms) are critical considerations.<br/><br/>
5. <b>Cost and Licensing:</b><br/>
Windows and macOS typically involve licensing costs (included in computer price), while most Linux distributions are free and open-source. For budget-conscious buyers or organizations deploying many machines, the OS licensing model significantly impacts total cost of ownership.<br/><br/>
6. <b>Support and Updates:</b><br/>
The vendor's commitment to updates, patches, and technical support affects the computer's longevity. An OS with long-term support ensures security updates and compatibility with new hardware and software for years to come.""",
            },
            {
                "num": "7",
                "question": "Make a list of the applications of computers you think of which are related to machine and patient care.",
                "marks": "5",
                "answer": """<b>Applications of Computers in Machine and Patient Care (Healthcare and Medical Technology)</b><br/><br/>
Computers play an indispensable role in modern healthcare, enhancing both the management of medical machinery and the direct care of patients. The following are key applications:<br/><br/>
1. <b>Medical Imaging and Diagnostics:</b><br/>
Computers power advanced imaging machines such as CT scanners, MRI machines, X-ray systems, ultrasound devices, and PET scanners. They process raw data from these machines to generate detailed images of internal organs, tissues, and bones, enabling accurate diagnosis of diseases, tumors, fractures, and abnormalities.<br/><br/>
2. <b>Patient Monitoring Systems:</b><br/>
In intensive care units (ICU) and operating rooms, computerized monitoring systems continuously track vital signs — heart rate, blood pressure, oxygen saturation, respiratory rate, and temperature. These systems alert medical staff immediately when readings fall outside safe ranges, enabling rapid intervention.<br/><br/>
3. <b>Robotic Surgery:</b><br/>
Computer-assisted surgical robots (such as the da Vinci Surgical System) allow surgeons to perform minimally invasive procedures with extreme precision. Computers translate the surgeon's hand movements into smaller, more precise movements of tiny instruments inside the patient's body, reducing trauma and recovery time.<br/><br/>
4. <b>Electronic Health Records (EHR):</b><br/>
Computerized EHR systems store comprehensive patient information including medical history, diagnoses, medications, allergies, lab results, and treatment plans. They improve coordination among healthcare providers, reduce medical errors, and ensure continuity of care.<br/><br/>
5. <b>Computerized Physician Order Entry (CPOE):</b><br/>
Doctors use computer systems to directly enter medication orders, lab tests, and procedure requests. This eliminates errors from illegible handwriting and enables automated checks for drug interactions, allergies, and correct dosages.<br/><br/>
6. <b>Medical Laboratory Automation:</b><br/>
Computers control automated laboratory equipment that analyzes blood, urine, tissue samples, and genetic material. They process thousands of tests per hour with high accuracy, manage sample tracking, and generate reports.<br/><br/>
7. <b>Radiation Therapy and Treatment Planning:</b><br/>
In cancer treatment, computers calculate precise radiation doses and control linear accelerators that deliver radiation to tumors while minimizing damage to surrounding healthy tissue. Computer simulations create 3D treatment plans customized for each patient.<br/><br/>
8. <b>Telemedicine and Remote Care:</b><br/>
Computers enable video consultations, remote diagnosis, and home monitoring for patients in distant or underserved areas. Wearable devices connected to computers transmit health data to physicians in real-time.<br/><br/>
9. <b>Pharmacy Management:</b><br/>
Computerized pharmacy systems manage drug inventories, track expiration dates, automate dispensing, and ensure patients receive correct medications with proper instructions.<br/><br/>
10. <b>Artificial Intelligence in Healthcare:</b><br/>
AI-powered computer systems analyze vast datasets to detect patterns, predict disease outbreaks, assist in drug discovery, and even diagnose conditions (such as diabetic retinopathy or skin cancer) from medical images with accuracy matching or exceeding human specialists.""",
            },
            {
                "num": "8",
                "question": "What do you think of young people using a PC only to play games and surfing the internet?",
                "marks": "5",
                "answer": """<b>Young People Using PCs Only for Games and Internet Surfing</b><br/><br/>
Using a PC solely for gaming and internet surfing represents a narrow and potentially wasteful application of a powerful tool. While both activities have legitimate value, an exclusive focus on them raises several concerns as well as acknowledging some benefits.<br/><br/>
<b>Concerns and Negative Aspects:</b><br/><br/>
1. <b>Missed Educational Opportunities:</b><br/>
A personal computer is a gateway to programming, graphic design, video editing, data analysis, and countless other productive skills. Using it only for entertainment means missing opportunities to develop digital competencies that are increasingly essential for careers.<br/><br/>
2. <b>Time Management Issues:</b><br/>
Excessive gaming and unproductive internet surfing can become addictive, consuming hours that could be spent on studies, physical exercise, social interaction, or skill development. This can lead to poor academic performance and neglected responsibilities.<br/><br/>
3. <b>Health Consequences:</b><br/>
Prolonged screen time without breaks causes eye strain, headaches, sleep disruption (due to blue light exposure), and sedentary lifestyle-related problems such as obesity and poor posture.<br/><br/>
4. <b>Exposure to Inappropriate Content:</b><br/>
Unsupervised internet surfing can expose young people to harmful content, cyberbullying, online predators, and misinformation.<br/><br/>
<b>Positive Aspects (When Balanced):</b><br/><br/>
1. <b>Skill Development Through Gaming:</b><br/>
Certain games develop problem-solving, strategic thinking, hand-eye coordination, teamwork, and even programming logic (e.g., Minecraft, puzzle games, simulation games). Esports has also become a legitimate career path for some.<br/><br/>
2. <b>Information Access:</b><br/>
The internet is the world's largest library. Even casual surfing can lead to discovery of new interests, current affairs awareness, and exposure to diverse perspectives and cultures.<br/><br/>
3. <b>Social Connection:</b><br/>
Online gaming and social platforms help young people connect with friends and communities, especially important for those in remote areas or with limited local social circles.<br/><br/>
<b>Conclusion:</b><br/>
The issue is not gaming or internet use itself, but <b>balance and purpose</b>. Young people should be encouraged to use computers diversely — for learning, creativity, communication, and productivity alongside entertainment. Parents, educators, and society should guide youth toward productive digital habits rather than condemning technology use outright. Digital literacy education should emphasize that a PC is a tool for creation and growth, not merely consumption.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Discuss in detail about the uses of computers at home and in offices. What are the benefits and harmful aspects of replacing people with computers?",
                "marks": "5+5",
                "answer": """<b>Uses of Computers at Home:</b><br/><br/>
1. <b>Education and Learning:</b> Students use computers for online research, e-learning, completing assignments, and accessing digital libraries and educational videos.<br/><br/>
2. <b>Communication:</b> Email, social media, video calls (Zoom, Skype, WhatsApp), and messaging apps keep families connected with relatives and friends worldwide.<br/><br/>
3. <b>Entertainment:</b> Streaming movies and music, playing games, reading e-books, and viewing digital photographs.<br/><br/>
4. <b>Home Management:</b> Online shopping, banking, bill payments, budgeting software, and smart home automation (controlling lights, thermostats, security systems).<br/><br/>
5. <b>Work from Home:</b> Freelancing, remote work, online business management, and teleconferencing have become standard, especially after the COVID-19 pandemic.<br/><br/>
6. <b>Creative Activities:</b> Photo and video editing, music composition, writing blogs, and graphic design.<br/><br/>
<b>Uses of Computers in Offices:</b><br/><br/>
1. <b>Word Processing and Documentation:</b> Creating, editing, formatting, and storing documents, reports, memos, and letters using software like Microsoft Word and Google Docs.<br/><br/>
2. <b>Data Management:</b> Spreadsheets (Excel, Google Sheets) for calculations, budgeting, financial analysis, and record-keeping.<br/><br/>
3. <b>Communication and Collaboration:</b> Email, intranets, project management tools (Trello, Asana), and collaborative platforms (Slack, Microsoft Teams).<br/><br/>
4. <b>Presentation:</b> Creating professional presentations using PowerPoint or Prezi for meetings, training, and client pitches.<br/><br/>
5. <b>Accounting and Finance:</b> Automated bookkeeping, payroll processing, tax calculation, and financial reporting through specialized software (Tally, QuickBooks).<br/><br/>
6. <b>Customer Relationship Management (CRM):</b> Tracking customer interactions, sales pipelines, and marketing campaigns.<br/><br/>
7. <b>Inventory and Supply Chain Management:</b> Monitoring stock levels, orders, deliveries, and logistics.<br/><br/>
8. <b>Human Resources Management:</b> Recruitment, employee records, attendance tracking, and performance evaluation systems.<br/><br/>
<b>Benefits of Replacing People with Computers:</b><br/><br/>
• <b>Speed and Efficiency:</b> Computers process data millions of times faster than humans.<br/>
• <b>Accuracy:</b> Computers perform repetitive calculations without errors, reducing mistakes in data processing.<br/>
• <b>Cost Reduction:</b> Over time, automation reduces labor costs, benefits, and training expenses.<br/>
• <b>24/7 Operation:</b> Computers can work continuously without fatigue, breaks, or sleep.<br/>
• <b>Consistency:</b> Automated systems produce uniform output quality regardless of volume.<br/>
• <b>Handling Dangerous Tasks:</b> Robots and automated systems can work in hazardous environments (chemical plants, mines, nuclear facilities) where human safety would be at risk.<br/><br/>
<b>Harmful Aspects of Replacing People with Computers:</b><br/><br/>
• <b>Unemployment:</b> Automation displaces workers, particularly in manufacturing, data entry, and customer service, causing economic hardship and social instability.<br/>
• <b>Loss of Human Judgment:</b> Computers lack empathy, intuition, creativity, and ethical reasoning. Some decisions require human context and moral judgment.<br/>
• <b>Initial Investment:</b> Implementing computer systems requires significant capital for hardware, software, and infrastructure.<br/>
• <b>Dependency and Vulnerability:</b> Over-reliance on computers creates vulnerability to system failures, cyberattacks, and power outages.<br/>
• <b>Reduced Personal Interaction:</b> Automated customer service and digital workflows can degrade human relationships and customer satisfaction.<br/>
• <b>Skill Degradation:</b> As people rely on computers, manual skills and critical thinking abilities may atrophy.<br/>
• <b>Inequality:</b> The benefits of automation often accrue to business owners and skilled technologists, while low-skilled workers bear the costs, widening economic inequality.""",
            },
            {
                "num": "10",
                "question": "Write an advertisement for a real or imaginary notebook computer. Your material should include its name, type, size, price, capacity, and the features that make it superior to other models.",
                "marks": "10",
                "answer": """<b>ADVERTISEMENT</b><br/><br/>
<b>Introducing the NEPALTECH UltraBook Pro X1</b><br/>
<i>"Power Meets Portability — Engineered for the Modern Professional"</i><br/><br/>
Are you tired of sluggish laptops that weigh you down? Meet the <b>UltraBook Pro X1</b>, the notebook computer designed to revolutionize your digital experience. Whether you are a student, software developer, content creator, or business executive, the UltraBook Pro X1 delivers uncompromising performance in an ultra-sleek package.<br/><br/>
<b>Product Specifications:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Name</b></td><td>NEPALTECH UltraBook Pro X1</td></tr>
<tr><td><b>Type</b></td><td>Ultra-thin Premium Notebook / Ultrabook</td></tr>
<tr><td><b>Size</b></td><td>13.3-inch 4K OLED Touch Display (2880×1800), 1.1 kg, 14.8 mm thickness</td></tr>
<tr><td><b>Price</b></td><td>Rs. 1,45,000 (Intel Core i7) / Rs. 1,85,000 (Intel Core i9)</td></tr>
<tr><td><b>Storage Capacity</b></td><td>1TB NVMe Gen4 SSD (expandable to 2TB)</td></tr>
<tr><td><b>RAM</b></td><td>16GB LPDDR5X (upgradeable to 32GB)</td></tr>
<tr><td><b>Processor</b></td><td>13th Gen Intel Core i7/i9 or AMD Ryzen 9 7940HS</td></tr>
<tr><td><b>Battery</b></td><td>72Wh — Up to 16 hours of continuous use</td></tr>
</table><br/>
<b>Features That Make It Superior:</b><br/><br/>
1. <b>Stunning 4K OLED Display:</b> Experience true-to-life colors, deeper blacks, and infinite contrast ratios. Perfect for photo editing, video production, and immersive entertainment — a feature rarely found in this price range.<br/><br/>
2. <b>All-Day Battery Life:</b> With intelligent power management and a 72Wh battery, work unplugged for up to 16 hours. Fast charging provides 50% charge in just 30 minutes.<br/><br/>
3. <b>Ultra-Light Aerospace Aluminum Body:</b> At only 1.1 kg and 14.8 mm thin, the UltraBook Pro X1 is built for mobility without sacrificing durability. It meets MIL-STD-810G military standards for toughness.<br/><br/>
4. <b>AI-Powered Performance:</b> Built-in Neural Processing Unit (NPU) accelerates AI tasks such as real-time background blur in video calls, voice recognition, and intelligent photo organization.<br/><br/>
5. <b>Comprehensive Connectivity:</b> Two Thunderbolt 4 ports, USB-C, HDMI 2.1, Wi-Fi 6E, and Bluetooth 5.3. Connect up to three external 4K monitors simultaneously.<br/><br/>
6. <b>Advanced Cooling System:</b> Vapor chamber cooling with dual fans keeps the system silent under light loads and cool under heavy workloads — no more overheating or noisy fans during meetings.<br/><br/>
7. <b>Security First:</b> Fingerprint scanner integrated into the power button, IR camera for Windows Hello facial recognition, TPM 2.0 chip, and physical webcam shutter for privacy.<br/><br/>
8. <b>Eco-Friendly:</b> Made from 90% recycled aluminum and 100% recycled packaging. Energy Star certified and carbon-neutral manufacturing.<br/><br/>
<b>Why Choose UltraBook Pro X1 Over Competitors?</b><br/>
Unlike other ultrabooks that compromise on ports, battery life, or display quality, the UltraBook Pro X1 refuses to cut corners. It offers the perfect balance of performance, portability, and price — giving you flagship features at a fraction of the cost of MacBook Pro or Dell XPS equivalents.<br/><br/>
<b>Available Now at:</b> All major computer stores across Nepal and online at www.nepaltech.com<br/><br/>
<i>UltraBook Pro X1 — Work Without Limits.</i>""",
            },
            {
                "num": "11",
                "question": "Reread the following passage and answer the questions that follow:<br/>Computers are machines that can help us in many ways. But, they cannot think or do things on their own. Humans have to feed them with information and tell them what to do with it. They cannot come up with any new information. But, they can save much time and work. For example: all the information and the office files can be stored in a computer's \"memory\". If a clerk were to trace any information from a particular file, the computer would only take seconds to find it. It would take a clerk days or even weeks to go through every file if no computers were used.",
                "marks": "10",
                "answer": """<b>Comprehension Questions and Answers:</b><br/><br/>
<b>Q1. What are computers according to the passage?</b><br/>
<b>Answer:</b> According to the passage, computers are machines that can help humans in many ways. They are tools that process information and perform tasks when instructed by humans. They are capable of storing large amounts of data, retrieving information quickly, and saving considerable time and effort in performing repetitive or data-intensive tasks.<br/><br/>
<b>Q2. Can computers think or do things on their own? Explain.</b><br/>
<b>Answer:</b> No, computers cannot think or do things on their own. The passage clearly states that computers lack independent thinking ability. They depend entirely on humans to feed them with information and provide instructions on what to do with that information. Computers cannot generate new information or make autonomous decisions. They are only capable of processing the data they receive according to programmed instructions.<br/><br/>
<b>Q3. How do computers help in saving time and work?</b><br/>
<b>Answer:</b> Computers save time and work by storing vast amounts of information in their memory and retrieving it almost instantly. The passage provides an example from an office setting: when a clerk needs to find information from a particular file, a computer can locate it within seconds. Without computers, the same task would require manually searching through every file, which could take days or even weeks. This dramatic reduction in search time translates into massive productivity gains.<br/><br/>
<b>Q4. What does the passage say about computers and new information?</b><br/>
<b>Answer:</b> The passage explicitly states that computers "cannot come up with any new information." They can only process, organize, store, and retrieve the information that humans have already provided. Unlike human beings who can think creatively, reason, and generate original ideas, computers are limited to executing predefined operations on existing data. This highlights the fundamental difference between human intelligence and artificial processing.<br/><br/>
<b>Q5. What would happen if no computers were used in an office?</b><br/>
<b>Answer:</b> If no computers were used in an office, tasks that currently take seconds would take days or even weeks. All information would have to be stored in physical files, requiring extensive space and manual organization. Clerks would need to search through paper files individually to find specific information. The efficiency of office operations would decrease dramatically, errors would be more common, and the cost of labor and storage would increase significantly. The passage emphasizes that computers have become essential tools for modern productivity.""",
            },
        ]
    }
]

generate_answer_sheet("CACS103", "english-i", "English I", 2020, "semester-1", CACS103_2020)
