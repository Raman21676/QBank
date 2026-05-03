#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS203_2024 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "Define system. Explain components of system including its characteristics.",
                "marks": "1+2+2",
                "answer": """<b>Definition of System:</b><br/>
A system is a collection of interrelated components or elements that work together in an organized manner to achieve a common goal or purpose. A system takes inputs from its environment, processes them, and produces outputs. Systems can be physical (like a computer) or abstract (like an information system). Every system has boundaries that separate it from its environment.<br/><br/>

<b>Components of a System:</b><br/><br/>

<b>1. Input:</b> The raw data, resources, or information that enter the system from the external environment. Inputs are the materials or signals that the system processes. For example, in a payroll system, inputs include employee attendance records, salary rates, and deduction information.<br/><br/>

<b>2. Process:</b> The transformation mechanism that converts inputs into outputs. Processing involves calculations, logical operations, sorting, classifying, or any other operation that adds value to the input. In an information system, processing is performed by software applications and hardware.<br/><br/>

<b>3. Output:</b> The result or product that the system produces after processing the inputs. Outputs are returned to the environment and should meet the intended purpose. Examples include reports, pay slips, decisions, or control signals.<br/><br/>

<b>4. Feedback:</b> Information about the system's performance that is sent back to the system for evaluation and adjustment. Feedback helps the system monitor its outputs and make necessary corrections. For example, user complaints about slow system response may lead to performance optimization.<br/><br/>

<b>5. Control:</b> The mechanism that regulates the system's operations to ensure it achieves its goals. Controls include policies, procedures, standards, and monitoring mechanisms that keep the system on track and handle exceptions.<br/><br/>

<b>6. Environment:</b> Everything outside the system boundary that interacts with the system. The environment provides inputs and receives outputs. Changes in the environment may require system modifications.<br/><br/>

<b>7. Boundary:</b> The limit that defines what is inside the system and what is outside. The boundary determines the scope of the system and its interactions with the environment.<br/><br/>

<b>Characteristics of a System:</b><br/><br/>

<b>1. Organization (Structure):</b> A system is composed of multiple components that are arranged in a specific structure. The components are organized in a hierarchical or network arrangement to achieve coordination.<br/><br/>

<b>2. Interaction:</b> The components of a system interact with each other. The output of one component often serves as the input to another. These interactions create the overall behavior of the system.<br/><br/>

<b>3. Interdependence:</b> The components depend on each other. A change in one component affects other components and the system as a whole. No component can function independently without impacting the system.<br/><br/>

<b>4. Integration:</b> The components are integrated or linked together to form a unified whole. Integration ensures that all parts work harmoniously toward the common objective.<br/><br/>

<b>5. Central Objective:</b> Every system has a specific goal or purpose. All components and processes are designed to contribute to achieving this central objective. Without a clear objective, a system lacks direction.<br/><br/>

<b>6. Entropy:</b> Systems tend toward disorder or decay over time without maintenance. Information systems require regular updates, maintenance, and monitoring to counteract entropy and remain effective.<br/><br/>

<b>7. Emergent Properties:</b> A system exhibits properties that are not present in its individual components. The whole is greater than the sum of its parts. For example, an information system can generate management reports that no single component can produce alone.""",
            },
            {
                "num": "3",
                "question": "Define CASE tool. Explain different types of CASE tools that can be used in different phases of SDLC.",
                "marks": "1+4",
                "answer": """<b>CASE Tool:</b><br/>
CASE stands for <b>Computer-Aided Software Engineering</b>. A CASE tool is a software application that automates and supports one or more activities of the Software Development Life Cycle (SDLC). CASE tools help system analysts and software engineers in designing, developing, testing, and maintaining software systems. They improve productivity, reduce errors, ensure consistency, and facilitate documentation throughout the development process.<br/><br/>

<b>Types of CASE Tools and Their Use in SDLC Phases:</b><br/><br/>

<b>1. Upper CASE Tools (Front-End CASE):</b><br/>
These tools support the early phases of SDLC — planning, analysis, and design.<br/>
• <b>Requirements Analysis:</b> Tools like Rational RequisitePro help capture, organize, and manage user requirements.<br/>
• <b>Data Modeling:</b> ER diagram tools like ERwin, MySQL Workbench help design database schemas and entity-relationship diagrams.<br/>
• <b>Process Modeling:</b> Tools like Microsoft Visio, Lucidchart, and Dia support creation of Data Flow Diagrams (DFDs), flowcharts, and process models.<br/>
• <b>System Design:</b> UML modeling tools like IBM Rational Rose, StarUML, and Visual Paradigm help create use case diagrams, class diagrams, sequence diagrams, and activity diagrams.<br/><br/>

<b>2. Lower CASE Tools (Back-End CASE):</b><br/>
These tools support the later phases of SDLC — coding, testing, and maintenance.<br/>
• <b>Code Generators:</b> Tools that automatically generate source code from design specifications. Examples include code generation features in Visual Paradigm and MATLAB Simulink.<br/>
• <b>Compilers and Debuggers:</b> IDEs like Visual Studio, Eclipse, and IntelliJ IDEA assist in writing, compiling, and debugging code.<br/>
• <b>Testing Tools:</b> Automated testing tools like Selenium (web testing), JUnit (unit testing), and LoadRunner (performance testing) support the testing phase.<br/>
• <b>Version Control:</b> Tools like Git, SVN, and Mercurial manage code versions and collaboration during development and maintenance.<br/><br/>

<b>3. Integrated CASE Tools (I-CASE):</b><br/>
These tools span across multiple or all phases of SDLC, providing seamless integration between analysis, design, and implementation.<br/>
• <b>Examples:</b> Oracle Designer, PowerDesigner, Rational Software Architect, and Enterprise Architect.<br/>
• They maintain a central repository of all system models, code, and documentation, ensuring consistency across phases.<br/>
• Changes in design automatically reflect in generated code and documentation.<br/><br/>

<b>4. Specific CASE Tool Categories:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Category</b></td><td><b>Purpose</b></td><td><b>Examples</b></td></tr>
<tr><td>Diagramming Tools</td><td>Create visual models and diagrams</td><td>Visio, Lucidchart, Draw.io</td></tr>
<tr><td>Repository Tools</td><td>Store and manage project metadata</td><td>ERwin, PowerDesigner</td></tr>
<tr><td>Documentation Tools</td><td>Generate and manage documentation</td><td>Doxygen, Javadoc</td></tr>
<tr><td>Project Management Tools</td><td>Plan, schedule, and track projects</td><td>MS Project, Jira, Trello</td></tr>
<tr><td>Prototyping Tools</td><td>Create UI/UX prototypes</td><td>Figma, Adobe XD, Balsamiq</td></tr>
<tr><td>Reverse Engineering Tools</td><td>Generate design from existing code</td><td>Enterprise Architect, StarUML</td></tr>
</table><br/>

<b>Benefits of CASE Tools:</b><br/>
• Faster development through automation<br/>
• Improved accuracy and consistency<br/>
• Better documentation and communication<br/>
• Easier maintenance through traceability<br/>
• Enhanced collaboration among team members<br/>
• Support for standardization and best practices""",
            },
            {
                "num": "4",
                "question": "Define information system planning. How is top-down planning approach different from bottom-up planning approach? Explain.",
                "marks": "1+4",
                "answer": """<b>Information System Planning (ISP):</b><br/>
Information System Planning is the process of identifying and selecting information system projects that support the strategic goals and objectives of an organization. It involves assessing the current state of information systems, determining future needs, prioritizing projects, allocating resources, and developing a roadmap for system development. ISP ensures that technology investments align with business strategy and deliver maximum value. It typically covers a multi-year horizon and considers organizational structure, business processes, data requirements, and technological capabilities.<br/><br/>

<b>Difference between Top-Down and Bottom-Up Planning Approaches:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Basis</b></td><td><b>Top-Down Planning</b></td><td><b>Bottom-Up Planning</b></td></tr>
<tr><td>Starting point</td><td>Starts from organizational goals and overall strategy</td><td>Starts from individual user needs and departmental requirements</td></tr>
<tr><td>Direction</td><td>Flows from top management to lower levels</td><td>Flows from operational levels to top management</td></tr>
<tr><td>Focus</td><td>Enterprise-wide systems and strategic alignment</td><td>Specific applications and local problem-solving</td></tr>
<tr><td>Scope</td><td>Broad, comprehensive, and organization-wide</td><td>Narrow, focused on specific departments or functions</td></tr>
<tr><td>Decision making</td><td>Driven by senior management and executives</td><td>Driven by end users, department heads, and operational staff</td></tr>
<tr><td>Resource allocation</td><td>Centralized and coordinated across the organization</td><td>Decentralized; departments control their own budgets</td></tr>
<tr><td>Integration</td><td>High integration between systems from the start</td><td>Integration is addressed later, often leading to inconsistencies</td></tr>
<tr><td>Time horizon</td><td>Long-term planning (3-5 years or more)</td><td>Short-term planning focused on immediate needs</td></tr>
<tr><td>Risk</td><td>Lower risk of strategic misalignment; higher initial investment</td><td>Lower initial investment; higher risk of redundancy and inconsistency</td></tr>
<tr><td>Implementation speed</td><td>Slower due to comprehensive analysis and coordination</td><td>Faster implementation of individual solutions</td></tr>
<tr><td>Examples</td><td>Enterprise Resource Planning (ERP) implementation</td><td>Departmental spreadsheet applications or local databases</td></tr>
</table><br/>

<b>Explanation of Top-Down Planning:</b><br/>
In top-down planning, senior management first defines the organization's strategic objectives. Then, information system requirements are derived from these objectives. The planning team analyzes the entire organization to identify critical success factors, key business processes, and enterprise-wide data needs. This approach ensures that all IS projects directly support organizational goals. It promotes standardization, reduces redundancy, and facilitates integration. However, it requires significant time, resources, and commitment from top management. There is also a risk of overlooking operational-level needs if not properly communicated.<br/><br/>

<b>Explanation of Bottom-Up Planning:</b><br/>
In bottom-up planning, individual departments or business units identify their own information needs and propose system solutions independently. These proposals are then aggregated and reviewed by higher management. This approach is responsive to local needs, encourages user involvement, and can deliver quick wins. However, it often leads to fragmented systems, data redundancy, inconsistent standards, and difficulty in integration across departments. Organizations may end up with multiple incompatible systems that cannot share data effectively.<br/><br/>

<b>Best Practice:</b> Many organizations use a <b>combined approach</b> where top-down strategic direction guides bottom-up requirement gathering, balancing enterprise alignment with operational responsiveness.""",
            },
            {
                "num": "5",
                "question": "Define JAD. List out different contemporary requirements determining techniques and explain them in comprehensive way.",
                "marks": "1+4",
                "answer": """<b>JAD (Joint Application Development):</b><br/>
JAD is a structured workshop-based approach to requirements gathering and system design that brings together key stakeholders — including users, managers, system analysts, and developers — in facilitated sessions. Developed by IBM in the late 1970s, JAD aims to accelerate the development process by fostering collaboration, reducing miscommunication, and building consensus among stakeholders. A trained JAD facilitator guides the sessions to ensure productive discussions and conflict resolution. JAD sessions typically last from a few hours to several days and produce detailed requirements documentation, prototypes, and design specifications.<br/><br/>

<b>Contemporary Requirements Determining Techniques:</b><br/><br/>

<b>1. Interviews:</b><br/>
One-on-one or group conversations between analysts and stakeholders to gather requirements. Interviews can be structured (with predefined questions), unstructured (open-ended), or semi-structured.<br/>
<b>Advantages:</b> Deep insights, clarification of complex issues, builds rapport.<br/>
<b>Disadvantages:</b> Time-consuming, potential bias from interviewer's influence, may miss tacit knowledge.<br/><br/>

<b>2. Questionnaires and Surveys:</b><br/>
Standardized sets of questions distributed to a large number of stakeholders to collect quantitative and qualitative data. Can be paper-based or electronic.<br/>
<b>Advantages:</b> Reaches many people quickly, cost-effective, easy to analyze statistically.<br/>
<b>Disadvantages:</b> Low response rates, superficial answers, cannot probe deeper responses.<br/><br/>

<b>3. Observation (Job Shadowing):</b><br/>
Analysts observe users performing their actual work to understand workflows, pain points, and unspoken requirements. Can be passive (watching without interaction) or active (asking questions during observation).<br/>
<b>Advantages:</b> Captures real behavior rather than reported behavior, identifies inefficiencies and workarounds.<br/>
<b>Disadvantages:</b> Time-consuming, observer effect (people behave differently when watched), may not reveal reasoning behind actions.<br/><br/>

<b>4. Document Analysis:</b><br/>
Reviewing existing documents such as forms, reports, policy manuals, organizational charts, and previous system documentation to understand current processes and data requirements.<br/>
<b>Advantages:</b> Provides historical context, reveals formal procedures, low cost.<br/>
<b>Disadvantages:</b> Documents may be outdated or inaccurate, may not reflect actual practice, can be voluminous.<br/><br/>

<b>5. Prototyping:</b><br/>
Creating preliminary working models (prototypes) of the system to help users visualize and interact with the proposed solution. Types include throwaway prototyping, evolutionary prototyping, and incremental prototyping.<br/>
<b>Advantages:</b> Early user feedback, clarifies ambiguous requirements, reduces risk of misunderstanding.<br/>
<b>Disadvantages:</b> Users may confuse prototype with final product, can be expensive if over-engineered.<br/><br/>

<b>6. Brainstorming:</b><br/>
A group creativity technique where team members generate a large number of ideas freely without immediate criticism. Useful for identifying innovative features and solutions.<br/>
<b>Advantages:</b> Generates diverse ideas quickly, encourages participation, builds team cohesion.<br/>
<b>Disadvantages:</b> Domination by vocal individuals, groupthink, many ideas may be impractical.<br/><br/>

<b>7. Focus Groups:</b><br/>
Moderated discussions with a small group of stakeholders (typically 6-10) to gather collective opinions, attitudes, and suggestions about system requirements.<br/>
<b>Advantages:</b> Synergy from group interaction, diverse perspectives, efficient use of time.<br/>
<b>Disadvantages:</b> Group dynamics may suppress dissent, moderator bias, not representative of all users.<br/><br/>

<b>8. Storyboarding and Scenarios:</b><br/>
Creating narrative descriptions or visual sequences that illustrate how users will interact with the system in specific situations. User stories in agile development are a form of scenario-based requirements.<br/>
<b>Advantages:</b> Easy to understand, user-centered, captures context and motivation.<br/>
<b>Disadvantages:</b> May miss edge cases, can be time-consuming to create comprehensive scenarios.<br/><br/>

<b>9. Reverse Engineering:</b><br/>
Analyzing an existing system (software, hardware, or process) to identify its components, relationships, and functionality. Used when documentation is missing or when migrating legacy systems.<br/>
<b>Advantages:</b> Uncovers hidden requirements, useful for legacy system replacement.<br/>
<b>Disadvantages:</b> Cannot capture original design intent, may be legally restricted.<br/><br/>

<b>10. Joint Application Development (JAD):</b><br/>
As defined above, JAD brings stakeholders together in facilitated workshops to collaboratively define requirements and design solutions.<br/>
<b>Advantages:</b> Rapid requirements gathering, consensus building, reduced iteration cycles.<br/>
<b>Disadvantages:</b> Requires skilled facilitator, scheduling difficulties, high initial time commitment.""",
            },
            {
                "num": "6",
                "question": "Define data modeling. Explain logical data model in detail.",
                "marks": "1+4",
                "answer": """<b>Data Modeling:</b><br/>
Data modeling is the process of creating a visual representation of data objects, their relationships, and the rules that govern them. It is a critical activity in system analysis and design that helps stakeholders understand the data requirements of an information system. Data models serve as blueprints for database design and ensure that data is organized efficiently, consistently, and accurately. There are three levels of data modeling: conceptual, logical, and physical. Data modeling uses notations such as Entity-Relationship (ER) diagrams, UML class diagrams, and dimensional models depending on the type of system being developed.<br/><br/>

<b>Logical Data Model:</b><br/>
A logical data model describes the structure of the data elements and the relationships between them, independent of any specific database management system (DBMS) or physical storage considerations. It is more detailed than the conceptual model and serves as a bridge between business requirements and technical implementation. The logical data model focuses on <b>what</b> data is needed and <b>how</b> it relates, without specifying <b>how</b> it will be physically stored.<br/><br/>

<b>Components of a Logical Data Model:</b><br/><br/>

<b>1. Entities:</b><br/>
An entity represents a real-world object, concept, or event about which data is collected. Each entity has a unique identifier (primary key) and consists of attributes that describe its properties.<br/>
<b>Examples:</b> Student, Course, Employee, Department, Product, Customer<br/>
In an ER diagram, entities are represented by rectangles.<br/><br/>

<b>2. Attributes:</b><br/>
Attributes are the properties or characteristics of an entity. They describe the data that needs to be stored for each entity instance.<br/>
<b>Types of Attributes:</b><br/>
• <b>Simple:</b> Cannot be divided further (e.g., StudentID, Age)<br/>
• <b>Composite:</b> Can be divided into sub-parts (e.g., Name = FirstName + LastName)<br/>
• <b>Single-valued:</b> Have only one value per entity instance (e.g., DateOfBirth)<br/>
• <b>Multi-valued:</b> Can have multiple values (e.g., PhoneNumbers, EmailAddresses)<br/>
• <b>Derived:</b> Can be calculated from other attributes (e.g., Age from DateOfBirth)<br/>
• <b>Key attributes:</b> Uniquely identify an entity instance (underlined in ER diagrams)<br/><br/>

<b>3. Relationships:</b><br/>
Relationships describe how entities are associated with each other. They are represented by diamond shapes in ER diagrams.<br/>
<b>Types of Relationships (Cardinality):</b><br/>
• <b>One-to-One (1:1):</b> One instance of entity A is associated with exactly one instance of entity B. Example: Employee — ParkingSpace (one employee gets one parking space).<br/>
• <b>One-to-Many (1:N):</b> One instance of entity A is associated with many instances of entity B. Example: Department — Employee (one department has many employees).<br/>
• <b>Many-to-Many (M:N):</b> Many instances of entity A are associated with many instances of entity B. Example: Student — Course (a student enrolls in many courses; a course has many students).<br/><br/>

<b>4. Keys:</b><br/>
• <b>Primary Key (PK):</b> A unique identifier for each record in an entity.<br/>
• <b>Foreign Key (FK):</b> An attribute in one entity that references the primary key of another entity, establishing a relationship.<br/>
• <b>Candidate Key:</b> An attribute or set of attributes that can uniquely identify a record; one candidate key is chosen as the primary key.<br/>
• <b>Composite Key:</b> A primary key composed of multiple attributes.<br/><br/>

<b>5. Normalization:</b><br/>
Logical data models often incorporate normalization principles to eliminate redundancy and ensure data integrity:<br/>
• <b>First Normal Form (1NF):</b> Eliminate repeating groups; all attributes contain atomic values.<br/>
• <b>Second Normal Form (2NF):</b> Eliminate partial dependencies (non-key attributes depend on the full primary key).<br/>
• <b>Third Normal Form (3NF):</b> Eliminate transitive dependencies (non-key attributes depend only on the primary key).<br/><br/>

<b>Example of a Logical Data Model (University System):</b><br/>
<pre>
Entity: STUDENT
  Attributes: StudentID (PK), FirstName, LastName, DateOfBirth, Email, Major

Entity: COURSE
  Attributes: CourseID (PK), CourseName, Credits, DepartmentID (FK)

Entity: DEPARTMENT
  Attributes: DepartmentID (PK), DepartmentName, Location

Entity: ENROLLMENT
  Attributes: StudentID (FK), CourseID (FK), Semester, Grade
  Primary Key: (StudentID, CourseID, Semester)

Relationships:
  STUDENT --enrolls in--> ENROLLMENT (1:N)
  COURSE --has enrollments--> ENROLLMENT (1:N)
  DEPARTMENT --offers--> COURSE (1:N)
</pre><br/>

<b>Advantages of Logical Data Model:</b><br/>
• Independent of DBMS technology, providing flexibility<br/>
• Serves as a communication tool between business and technical teams<br/>
• Ensures data integrity through normalization and key constraints<br/>
• Facilitates database design and application development<br/>
• Provides a stable foundation that remains valid even as technology changes""",
            },
            {
                "num": "7",
                "question": "What are the various types of menu design which can be adopted to meet the system complexity and usability?",
                "marks": "5",
                "answer": """<b>Types of Menu Design:</b><br/>
Menu design is a critical aspect of user interface design in information systems. The choice of menu type depends on system complexity, user expertise, task frequency, and the amount of information to be presented. Well-designed menus improve usability, reduce learning time, and minimize user errors.<br/><br/>

<b>1. Single-Level Menu (Flat Menu):</b><br/>
All options are displayed at one level without any hierarchy. Users can see all available choices simultaneously.<br/>
<b>Best for:</b> Simple systems with a small number of options (typically ≤ 8-10).<br/>
<b>Advantages:</b> Simple, no navigation required, all options visible.<br/>
<b>Disadvantages:</b> Becomes overwhelming with many options; not scalable.<br/>
<b>Example:</b> A simple ATM menu with options: Withdraw, Deposit, Balance, Transfer, Exit.<br/><br/>

<b>2. Hierarchical Menu (Tree Menu / Multi-Level Menu):</b><br/>
Options are organized in a tree-like structure with parent and child menus. Users navigate through levels to reach specific functions.<br/>
<b>Best for:</b> Complex systems with many options that can be logically grouped.<br/>
<b>Advantages:</b> Scalable, organizes large numbers of options, logical grouping.<br/>
<b>Disadvantages:</b> Requires multiple clicks/cl keystrokes; users can get lost in deep hierarchies.<br/>
<b>Example:</b> File → Open → Project → From Version Control → Git.<br/><br/>

<b>3. Drop-Down Menu (Pull-Down Menu):</b><br/>
A menu that appears when the user clicks or hovers over a menu bar item. Options drop down from the menu bar.<br/>
<b>Best for:</b> Desktop applications and web applications with moderate complexity.<br/>
<b>Advantages:</b> Saves screen space, familiar to users, supports keyboard shortcuts.<br/>
<b>Disadvantages:</b> Can become long and unwieldy; requires precise mouse control.<br/>
<b>Example:</b> Microsoft Word menu bar: File, Edit, View, Insert, Format, Tools.<br/><br/>

<b>4. Pop-Up Menu (Context Menu / Right-Click Menu):</b><br/>
A menu that appears at the cursor position when the user right-clicks or long-presses on an object. It provides context-specific options.<br/>
<b>Best for:</b> Systems where users need quick access to actions relevant to a specific object.<br/>
<b>Advantages:</b> Context-sensitive, reduces screen clutter, fast access to common actions.<br/>
<b>Disadvantages:</b> Not discoverable for novice users; options vary by context.<br/>
<b>Example:</b> Right-clicking on a file to see options: Open, Copy, Cut, Rename, Delete, Properties.<br/><br/>

<b>5. Tab Menu:</b><br/>
Options are organized as tabs across the top or side of a window. Clicking a tab displays a different set of content or functions.<br/>
<b>Best for:</b> Systems where users need to switch between related views or settings.<br/>
<b>Advantages:</b> Clear visual organization, easy to switch contexts, all top-level options visible.<br/>
<b>Disadvantages:</b> Limited number of tabs before they become cramped; hidden content within tabs.<br/>
<b>Example:</b> Browser tabs, Excel ribbon tabs (Home, Insert, Page Layout, Formulas).<br/><br/>

<b>6. Icon-Based Menu (Graphical Menu / Toolbar):</b><br/>
Functions are represented by icons or graphical symbols rather than text. Often used in conjunction with tooltips.<br/>
<b>Best for:</b> Applications where visual recognition is faster than reading, or for international users.<br/>
<b>Advantages:</b> Fast recognition, compact, language-independent, visually appealing.<br/>
<b>Disadvantages:</b> Icons may be ambiguous; not suitable for functions without obvious visual metaphors.<br/>
<b>Example:</b> Photoshop toolbar, mobile app home screens, video player controls.<br/><br/>

<b>7. Form-Fill Menu:</b><br/>
Users interact with the system by filling out on-screen forms with fields, checkboxes, radio buttons, and dropdown lists.<br/>
<b>Best for:</b> Data entry systems, registration forms, configuration settings.<br/>
<b>Advantages:</b> Structured input, validation support, clear data requirements.<br/>
<b>Disadvantages:</b> Can be lengthy and tedious; poor for quick navigation.<br/>
<b>Example:</b> Online registration forms, ERP data entry screens, flight booking forms.<br/><br/>

<b>8. Voice Menu (Interactive Voice Response - IVR):</b><br/>
Users navigate through a system using voice commands or keypad inputs in response to audio prompts.<br/>
<b>Best for:</b> Telephone-based systems, hands-free environments, accessibility.<br/>
<b>Advantages:</b> No visual display needed, accessible to visually impaired users, convenient for phone interactions.<br/>
<b>Disadvantages:</b> Slow navigation, speech recognition errors, limited options per level.<br/>
<b>Example:</b> Bank phone banking: "Press 1 for account balance, Press 2 for fund transfer..."<br/><br/>

<b>9. Breadcrumb Navigation:</b><br/>
A secondary menu that shows the user's current location within the system hierarchy and allows quick navigation to parent levels.<br/>
<b>Best for:</b> Deep hierarchical websites and applications.<br/>
<b>Advantages:</b> Prevents user disorientation, provides context, enables quick upward navigation.<br/>
<b>Example:</b> Home > Electronics > Computers > Laptops > Gaming Laptops.<br/><br/>

<b>Menu Design Principles for Usability:</b><br/>
• Use clear, concise, and familiar labels<br/>
• Group related options logically<br/>
• Place frequently used options at the top<br/>
• Provide visual feedback for selected items<br/>
• Support keyboard navigation and shortcuts<br/>
• Limit menu depth to 3 levels when possible<br/>
• Use separators to group related items within menus""",
            },
            {
                "num": "8",
                "question": "Why do software projects often fail? Explain different types of software testing.",
                "marks": "1+4",
                "answer": """<b>Why Software Projects Often Fail:</b><br/>
Software project failure is a significant problem in the IT industry, with studies showing that a large percentage of projects exceed budget, miss deadlines, or fail to deliver expected value. The major reasons include:<br/><br/>

<b>1. Unclear or Changing Requirements:</b><br/>
When requirements are poorly defined, ambiguous, or constantly changing without proper change control, the final product may not meet user expectations. Scope creep — the uncontrolled expansion of project scope — is one of the most common causes of failure.<br/><br/>

<b>2. Poor Planning and Unrealistic Estimation:</b><br/>
Inadequate project planning, unrealistic timelines, and underestimated budgets lead to rushed development, cutting corners, and compromised quality. Without a realistic plan, projects cannot be properly monitored or controlled.<br/><br/>

<b>3. Inadequate Communication:</b><br/>
Lack of effective communication between stakeholders, developers, and users results in misunderstandings, misaligned goals, and missed expectations. Siloed teams and poor documentation exacerbate this problem.<br/><br/>

<b>4. Lack of User Involvement:</b><br/>
When end users are not involved throughout the development process, the system may not address real-world needs. Systems built without user feedback are often rejected after deployment.<br/><br/>

<b>5. Poor Project Management:</b><br/>
Ineffective leadership, lack of risk management, insufficient progress tracking, and inability to resolve issues promptly can derail even technically sound projects.<br/><br/>

<b>6. Technical Complexity and Debt:</b><br/>
Overly ambitious architectures, use of immature technologies, poor code quality, and accumulation of technical debt create insurmountable challenges as the project progresses.<br/><br/>

<b>7. Insufficient Testing:</b><br/>
When testing is treated as an afterthought or given insufficient time and resources, critical bugs reach production, damaging user trust and requiring expensive fixes.<br/><br/>

<b>8. Staff Turnover and Skill Gaps:</b><br/>
Losing key team members or hiring underqualified personnel disrupts momentum and reduces team capability, especially if knowledge is not properly documented.<br/><br/>

<b>9. Organizational Issues:</b><br/>
Political conflicts, lack of executive support, competing priorities, and resistance to change within the organization can sabotage projects.<br/><br/>

<b>Different Types of Software Testing:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Type</b></td><td><b>Description</b></td></tr>
<tr><td><b>Unit Testing</b></td><td>Tests individual modules, functions, or classes in isolation to verify they work correctly. Usually performed by developers during coding.</td></tr>
<tr><td><b>Integration Testing</b></td><td>Tests the interaction between integrated modules to detect interface defects, data flow issues, and communication problems.</td></tr>
<tr><td><b>System Testing</b></td><td>Tests the complete, integrated system as a whole against specified requirements to verify overall behavior.</td></tr>
<tr><td><b>Acceptance Testing</b></td><td>Conducted by end users or clients (UAT — User Acceptance Testing) to determine whether the system meets business needs and is acceptable for delivery.</td></tr>
<tr><td><b>Regression Testing</b></td><td>Re-tests the system after modifications to ensure existing functionality still works and new bugs were not introduced.</td></tr>
<tr><td><b>Alpha Testing</b></td><td>Internal testing performed by the organization in a controlled environment before releasing to external users.</td></tr>
<tr><td><b>Beta Testing</b></td><td>External testing by a limited number of real users in their own environment to identify issues before general release.</td></tr>
<tr><td><b>Performance Testing</b></td><td>Evaluates system responsiveness, throughput, and stability under expected load conditions.</td></tr>
<tr><td><b>Stress Testing</b></td><td>Pushes the system beyond normal operational limits to identify its breaking point and ensure graceful failure.</td></tr>
<tr><td><b>Security Testing</b></td><td>Identifies vulnerabilities, threats, and risks to protect data and prevent unauthorized access.</td></tr>
<tr><td><b>Usability Testing</b></td><td>Evaluates how easy and intuitive the system is for end users to learn and operate.</td></tr>
<tr><td><b>Compatibility Testing</b></td><td>Checks whether the software works correctly across different devices, operating systems, browsers, and network environments.</td></tr>
<tr><td><b>White-Box Testing</b></td><td>Tests internal structure, logic, and code paths with knowledge of the source code. Focuses on control flow and data flow.</td></tr>
<tr><td><b>Black-Box Testing</b></td><td>Tests functionality without knowledge of internal code, based solely on requirements and expected inputs/outputs.</td></tr>
</table>""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Explain phases of SDLC, also discuss the role of Project Manager in software project development.",
                "marks": "7+3",
                "answer": """<b>Phases of SDLC (Software Development Life Cycle):</b><br/><br/>

<b>1. Planning:</b><br/>
This is the first and most critical phase where the project's scope, objectives, feasibility, and resources are determined. It involves:<br/>
• Identifying business problems and opportunities<br/>
• Conducting feasibility studies (technical, economic, operational, schedule)<br/>
• Defining project scope, constraints, and deliverables<br/>
• Estimating costs, timelines, and resource requirements<br/>
• Creating a project plan and obtaining management approval<br/>
<b>Output:</b> Project Plan, Feasibility Report, Cost-Benefit Analysis<br/><br/>

<b>2. Requirements Analysis:</b><br/>
In this phase, system analysts work closely with stakeholders to gather, analyze, and document detailed system requirements. Techniques include interviews, surveys, observation, JAD sessions, and prototyping.<br/>
• Functional requirements: What the system should do<br/>
• Non-functional requirements: Performance, security, usability, reliability<br/>
• User requirements, system requirements, and domain constraints<br/>
<b>Output:</b> Software Requirements Specification (SRS) Document, Use Cases<br/><br/>

<b>3. System Design:</b><br/>
The design phase translates requirements into a technical blueprint for the system. It includes:<br/>
• <b>Architectural Design:</b> Overall system structure, technology stack, deployment architecture<br/>
• <b>Database Design:</b> ER diagrams, data dictionaries, schema design, normalization<br/>
• <b>Interface Design:</b> User interface mockups, screen layouts, navigation flows<br/>
• <b>Module Design:</b> Detailed design of each component, class diagrams, sequence diagrams<br/>
• <b>Input/Output Design:</b> Forms, reports, and data exchange formats<br/>
<b>Output:</b> Design Document, DFDs, ERDs, UML Diagrams, Prototypes<br/><br/>

<b>4. Implementation (Coding):</b><br/>
Developers write the actual code based on design specifications. This phase involves:<br/>
• Setting up the development environment<br/>
• Writing and compiling source code<br/>
• Code reviews and peer programming<br/>
• Unit testing by developers<br/>
• Version control and build management<br/>
<b>Output:</b> Source Code, Unit Test Results, Technical Documentation<br/><br/>

<b>5. Testing:</b><br/>
The system is rigorously tested to identify and fix defects. Types of testing include unit testing, integration testing, system testing, acceptance testing, performance testing, and security testing.<br/>
• Developing test plans and test cases<br/>
• Executing manual and automated tests<br/>
• Tracking and fixing bugs<br/>
• Regression testing after fixes<br/>
• User Acceptance Testing (UAT)<br/>
<b>Output:</b> Test Plans, Test Reports, Bug Reports, UAT Sign-off<br/><br/>

<b>6. Deployment (Installation):</b><br/>
The tested system is installed in the production environment and made available to users. Deployment strategies include:<br/>
• <b>Direct Cutover:</b> Immediate switch from old to new system<br/>
• <b>Parallel:</b> Old and new systems run simultaneously<br/>
• <b>Phased:</b> System implemented in stages or modules<br/>
• <b>Pilot:</b> System introduced in one part of the organization first<br/>
<b>Output:</b> Deployed System, User Manuals, Training Materials<br/><br/>

<b>7. Maintenance:</b><br/>
After deployment, the system requires ongoing maintenance to remain effective. Types include:<br/>
• <b>Corrective Maintenance:</b> Fixing bugs and errors discovered after deployment<br/>
• <b>Adaptive Maintenance:</b> Modifying the system to work in changed environments (new OS, regulations)<br/>
• <b>Perfective Maintenance:</b> Enhancing performance or adding new features based on user feedback<br/>
• <b>Preventive Maintenance:</b> Making changes to prevent future problems<br/>
<b>Output:</b> Updated System, Patches, Release Notes, Maintenance Logs<br/><br/>

<b>Role of Project Manager in Software Project Development:</b><br/><br/>

<b>1. Project Planning and Scope Management:</b><br/>
The project manager defines the project scope, creates work breakdown structures (WBS), develops schedules using Gantt charts or PERT, and sets milestones. They ensure the project stays within scope and manage change requests.<br/><br/>

<b>2. Team Leadership and Resource Management:</b><br/>
The PM assembles the project team, assigns roles and responsibilities based on skills, motivates team members, resolves conflicts, and ensures optimal utilization of human, financial, and technical resources.<br/><br/>

<b>3. Risk Management:</b><br/>
The PM identifies potential risks early, assesses their probability and impact, develops mitigation strategies, and maintains a risk register throughout the project lifecycle.<br/><br/>

<b>4. Communication and Stakeholder Management:</b><br/>
The PM serves as the primary point of contact between the team, clients, and upper management. They conduct status meetings, prepare progress reports, manage expectations, and ensure transparent communication.<br/><br/>

<b>5. Quality Assurance:</b><br/>
The PM establishes quality standards, monitors deliverables against requirements, ensures testing is thorough, and verifies that the final product meets acceptance criteria.<br/><br/>

<b>6. Budget and Schedule Control:</b><br/>
The PM monitors expenditures against the budget, tracks progress against the schedule, identifies variances, and takes corrective actions to keep the project on time and within budget.<br/><br/>

<b>7. Issue Resolution and Decision Making:</b><br/>
The PM addresses technical and non-technical problems promptly, makes critical decisions when obstacles arise, and escalates issues when necessary.<br/><br/>

<b>8. Project Closure:</b><br/>
The PM ensures proper handover of deliverables, obtains final sign-off from stakeholders, conducts post-implementation reviews, documents lessons learned, and formally closes the project.""",
            },
            {
                "num": "10",
                "question": "What is process modeling? Why do we need DFD? Draw up to top level DFD for Online hotel room booking system.",
                "marks": "1+2+7",
                "answer": """<b>Process Modeling:</b><br/>
Process modeling is a technique used in system analysis and design to represent the flow of data and the processes that transform data within an information system. It provides a graphical representation of business processes, showing how data moves between processes, data stores, and external entities. Process modeling helps analysts understand current systems, identify inefficiencies, and design improved systems. The most widely used process modeling technique is the <b>Data Flow Diagram (DFD)</b>, which illustrates the logical flow of data without regard to physical implementation details.<br/><br/>

<b>Why We Need DFD (Data Flow Diagram):</b><br/><br/>

<b>1. Visual Communication:</b><br/>
DFDs provide a clear, visual representation of system processes that is easily understood by both technical and non-technical stakeholders. They bridge the communication gap between system analysts, developers, and business users.<br/><br/>

<b>2. Understanding System Logic:</b><br/>
DFDs focus on <b>what</b> the system does (logical view) rather than <b>how</b> it does it (physical view). This helps analysts understand business requirements independent of technology constraints.<br/><br/>

<b>3. Identifying Data Dependencies:</b><br/>
DFDs clearly show where data originates, how it is transformed, where it is stored, and where it is consumed. This helps identify data redundancy, missing data flows, and incorrect data handling.<br/><br/>

<b>4. Scope Definition:</b><br/>
The Context Diagram (Level 0 DFD) defines the system boundary by showing the system as a single process interacting with external entities. This helps establish the scope of the project.<br/><br/>

<b>5. Decomposition and Leveling:</b><br/>
DFDs support top-down decomposition. Complex processes can be broken down into lower-level DFDs, allowing analysts to manage complexity and examine details progressively.<br/><br/>

<b>6. Documentation:</b><br/>
DFDs serve as essential documentation for system design, implementation, testing, and maintenance. They provide a blueprint that guides development and helps new team members understand the system.<br/><br/>

<b>7. Error Detection:</b><br/>
By mapping data flows, analysts can detect inconsistencies, missing processes, unbalanced data flows, and potential bottlenecks before coding begins.<br/><br/>

<b>Components of DFD:</b><br/>
• <b>Process (Circle/Bubble):</b> Represents an activity that transforms data. Named with a verb phrase.<br/>
• <b>External Entity (Rectangle):</b> Represents sources or destinations of data outside the system boundary.<br/>
• <b>Data Store (Open Rectangle):</b> Represents data repositories like databases or files.<br/>
• <b>Data Flow (Arrow):</b> Represents the movement of data between components, labeled with data names.<br/><br/>

<b>Context Diagram (Level 0 DFD) for Online Hotel Room Booking System:</b><br/>
<pre>
                    +------------------+
                    |   Hotel Manager  |
                    +--------+---------+
                             |
            Room Availability|Reports
                             |
        +--------------------+--------------------+
        |                                         |
        |     [0] Online Hotel Room               |
+-------+--------+    Booking System    +----------+-------+
|    Guest       |<-------------------->|  Payment Gateway  |
+----------------+                      +----------+-------+
        |                                          |
Booking |Request                        Payment    |Confirmation
Details |                                     /    |
        |                                    /     |
        |               +-------------------+
        |               |
        |               | Booking Confirmation
        |               | / Cancellation Notice
        |              \|/
        |        +-------------+
        +------->|  Email/SMS  |
                 |   Service   |
                 +-------------+
</pre><br/>

<b>Data Flows in Context Diagram:</b><br/>
• Guest → System: Booking Request (dates, room type, guest details)<br/>
• System → Guest: Booking Confirmation / Cancellation Notice / Availability Info<br/>
• System → Payment Gateway: Payment Details<br/>
• Payment Gateway → System: Payment Confirmation / Rejection<br/>
• Hotel Manager → System: Room Rates, Availability Updates<br/>
• System → Hotel Manager: Booking Reports, Revenue Reports<br/>
• System → Email/SMS Service: Notification Triggers<br/>
<br/>

<b>Level 1 DFD for Online Hotel Room Booking System:</b><br/>
<pre>
+-------+          +------------------+          +------------------+
|Guest  |--------->| 1.0 Search &     |          |                  |
+-------+ Booking  |    Check         |          |  D1 Room         |
       Request     |    Availability  |<-------->|    Database      |
                   +--------+---------+ Query    |                  |
                            |                     +------------------+
                            | Availability
                            | Results
                            |
                   +--------v---------+
                   | 2.0 Make         |
+-------+ Booking  |    Reservation   |--------->+------------------+
|Guest  |--------->|                  |  Save    |  D2 Booking      |
+-------+ Details  +--------+---------+ Booking  |    Database      |
                            |                     +------------------+
                            | Booking
                            | Summary
                            |
                   +--------v---------+          +------------------+
                   | 3.0 Process      | Payment  |  Payment Gateway  |
                   |    Payment       |--------->|                  |
                   +--------+---------+          +--------+---------+
                            |                            |
                            | Payment                    | Confirmation
                            | Result                     |
                            |                            |
                   +--------v---------+          +------------------+
                   | 4.0 Confirm &    | Notify   |  Email/SMS       |
                   |    Notify        |--------->|  Service         |
                   +--------+---------+          +------------------+
                            |
                            | Confirmation/
                            | Cancellation
                            |
                   +--------v---------+
                   | Guest            |
                   +------------------+
</pre><br/>

<b>Description of Level 1 Processes:</b><br/>

<b>Process 1.0 — Search & Check Availability:</b><br/>
Receives booking request dates and room preferences from the guest. Queries the Room Database (D1) to check available rooms matching the criteria. Returns availability results including room types, prices, and amenities to the guest.<br/><br/>

<b>Process 2.0 — Make Reservation:</b><br/>
Receives guest details and selected room information. Validates the booking request, calculates total cost, and saves the booking record to the Booking Database (D2). Generates a booking summary and passes it to the payment process.<br/><br/>

<b>Process 3.0 — Process Payment:</b><br/>
Receives booking summary and payment details. Communicates with the external Payment Gateway to authorize and process the transaction. Receives payment confirmation or rejection. Updates booking status in D2 accordingly.<br/><br/>

<b>Process 4.0 — Confirm & Notify:</b><br/>
Receives payment result. If successful, generates booking confirmation with reservation ID and sends notification to the guest via Email/SMS Service. If payment fails, sends cancellation notice with reason. Also notifies the Hotel Manager of new bookings through reporting.<br/><br/>

<b>Data Stores:</b><br/>
• <b>D1 — Room Database:</b> Stores room types, room numbers, rates, amenities, and current availability status.<br/>
• <b>D2 — Booking Database:</b> Stores guest information, reservation details, booking dates, payment status, and cancellation records.<br/><br/>

<b>External Entities:</b><br/>
• <b>Guest:</b> The customer searching for and booking hotel rooms.<br/>
• <b>Payment Gateway:</b> External financial service for processing credit card and digital payments.<br/>
• <b>Email/SMS Service:</b> External notification service for sending confirmations and alerts.<br/>
• <b>Hotel Manager:</b> Administrator who manages room inventory, pricing, and views reports.""",
                "diagram": "Context Diagram and Level 1 DFD for Online Hotel Room Booking System showing processes, data stores, external entities, and data flows.",
            },
            {
                "num": "11",
                "question": "List out different activities that are associated with implementation phase. Explain each of them in detail. What are the different methods of training and supporting users? Explain.",
                "marks": "6+4",
                "answer": """<b>Activities Associated with Implementation Phase:</b><br/><br/>

<b>1. Coding and Unit Testing:</b><br/>
Developers write the actual program code based on design specifications. Each module is coded individually and then subjected to unit testing to verify that it functions correctly in isolation. Developers use IDEs, version control systems, and coding standards to ensure quality. Unit tests validate individual functions, methods, and classes against expected outputs.<br/><br/>

<b>2. Integration and System Testing:</b><br/>
After individual modules are developed and unit-tested, they are integrated into a complete system. Integration testing checks whether modules work together correctly, verifying data flows and interfaces between components. System testing evaluates the entire system against requirements, including functional testing, performance testing, security testing, and usability testing.<br/><br/>

<b>3. Data Conversion and Migration:</b><br/>
Existing data from legacy systems must be converted into formats compatible with the new system. This involves:<br/>
• Extracting data from old systems<br/>
• Cleaning and transforming data to remove inconsistencies and errors<br/>
• Loading data into the new system's database<br/>
• Validating migrated data for accuracy and completeness<br/>
Data conversion is critical to ensure business continuity and prevent data loss.<br/><br/>

<b>4. Documentation Preparation:</b><br/>
Comprehensive documentation is created for both users and technical staff:<br/>
• <b>User Documentation:</b> User manuals, quick start guides, FAQs, help files, and online tutorials that explain how to use the system.<br/>
• <b>Technical Documentation:</b> System design documents, API documentation, database schemas, code comments, and deployment guides for developers and administrators.<br/><br/>

<b>5. Installation and Deployment:</b><br/>
The system is installed in the production environment. This includes:<br/>
• Setting up hardware, servers, networks, and cloud infrastructure<br/>
• Installing and configuring software, databases, and middleware<br/>
• Deploying application code and static assets<br/>
• Conducting smoke tests to verify the deployment<br/>
Organizations may use direct cutover, parallel, phased, or pilot deployment strategies.<br/><br/>

<b>6. User Training:</b><br/>
End users are trained to operate the new system effectively. Training programs ensure users understand system functionality, data entry procedures, report generation, and troubleshooting basics. Without proper training, even well-designed systems may be underutilized or misused.<br/><br/>

<b>7. Change Management:</b><br/>
Implementation often requires organizational changes. Change management activities include:<br/>
• Communicating the benefits of the new system to stakeholders<br/>
• Addressing resistance to change<br/>
• Redefining job roles and responsibilities<br/>
• Updating policies and procedures to align with the new system<br/><br/>

<b>8. User Acceptance Testing (UAT):</b><br/>
Before full deployment, end users test the system in a real or simulated environment to ensure it meets their needs. UAT validates that the system performs correctly under actual working conditions and that users can complete their tasks. Sign-off from users indicates formal acceptance of the system.<br/><br/>

<b>9. Post-Implementation Review:</b><br/>
After the system goes live, the project team evaluates whether objectives were met. This includes:<br/>
• Comparing actual outcomes with planned outcomes<br/>
• Measuring system performance and user satisfaction<br/>
• Identifying remaining issues and areas for improvement<br/>
• Documenting lessons learned for future projects<br/><br/>

<b>Different Methods of Training and Supporting Users:</b><br/><br/>

<b>1. Instructor-Led Training (ILT):</b><br/>
Traditional classroom-style training where an instructor teaches users in person. It allows for immediate questions, hands-on practice, and group discussions.<br/>
<b>Advantages:</b> Personal interaction, immediate feedback, structured learning.<br/>
<b>Disadvantages:</b> Expensive, scheduling difficulties, not scalable for large or distributed user bases.<br/><br/>

<b>2. Online Training / E-Learning:</b><br/>
Training delivered through web-based platforms, video tutorials, webinars, and interactive modules. Users can learn at their own pace.<br/>
<b>Advantages:</b> Scalable, cost-effective, flexible timing, can be recorded for future reference.<br/>
<b>Disadvantages:</b> Less personal interaction, requires self-discipline, technical issues may disrupt learning.<br/><br/>

<b>3. Hands-On Workshops:</b><br/>
Practical sessions where users perform real tasks on the system with guidance from trainers. Users learn by doing rather than just observing.<br/>
<b>Advantages:</b> Builds confidence, reinforces learning through practice, identifies usability issues.<br/>
<b>Disadvantages:</b> Requires access to training environment, time-intensive.<br/><br/>

<b>4. Self-Paced Learning Materials:</b><br/>
Users learn from manuals, quick reference guides, FAQs, help files, and knowledge bases at their own convenience.<br/>
<b>Advantages:</b> Always available, no scheduling needed, good for reference.<br/>
<b>Disadvantages:</b> May not cover all user questions, requires reading effort, can become outdated.<br/><br/>

<b>5. One-on-One Coaching / Mentoring:</b><br/>
Experienced users or trainers work individually with new users, providing personalized guidance and addressing specific needs.<br/>
<b>Advantages:</b> Highly personalized, addresses individual difficulties, builds strong skills.<br/>
<b>Disadvantages:</b> Very resource-intensive, not feasible for large numbers of users.<br/><br/>

<b>6. Train-the-Trainer Approach:</b><br/>
A small group of users (often department heads or power users) is intensively trained, and they then train their colleagues.<br/>
<b>Advantages:</b> Scalable, cost-effective, trainers understand local context and language.<br/>
<b>Disadvantages:</b> Quality depends on trainer capability, may introduce inconsistencies.<br/><br/>

<b>Methods of Supporting Users:</b><br/>

<b>1. Help Desk / Service Desk:</b><br/>
A centralized support team handles user queries, troubleshooting, and issue escalation via phone, email, or ticketing systems.<br/><br/>

<b>2. Online Support Portals:</b><br/>
Web-based portals with FAQs, knowledge bases, video tutorials, community forums, and chatbots where users can find self-help resources.<br/><br/>

<b>3. On-Site Support:</b><br/>
Technical staff are physically present at user locations to provide immediate assistance, especially during the initial rollout period.<br/><br/>

<b>4. Remote Support:</b><br/>
Technicians access user systems remotely using tools like TeamViewer, AnyDesk, or built-in remote assistance to diagnose and fix problems.<br/><br/>

<b>5. Regular Follow-Up and Feedback:</b><br/>
Scheduled check-ins with users to identify ongoing issues, gather improvement suggestions, and ensure user satisfaction.""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet(
        "CACS203", "system-analysis-design", "System Analysis & Design",
        2024, "semester-3", CACS203_2024
    )
    print("Answer sheet generation complete for CACS203 2024!")
