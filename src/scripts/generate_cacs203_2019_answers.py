#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS203_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "i) Information systems aimed at improving routine business activities?<br/>a) Management Information System &nbsp;&nbsp; b) Decision Support System &nbsp;&nbsp; c) Transaction Processing Systems &nbsp;&nbsp; d) Executive Information System<br/><br/>ii) Project life cycle consists of?<br/>a) System analysis and design &nbsp;&nbsp; b) Programming and debugging &nbsp;&nbsp; c) Formulation and planning various activities &nbsp;&nbsp; d) None of the above<br/><br/>iii) Most important feature of spiral model?<br/>a) Quality management &nbsp;&nbsp; b) Version control &nbsp;&nbsp; c) Risk Management &nbsp;&nbsp; d) None of the above<br/><br/>iv) …includes existing system, proposed system, system flow charts, modular design?<br/>a) Feasibility report &nbsp;&nbsp; b) System specification report &nbsp;&nbsp; c) Design Specification Report &nbsp;&nbsp; d) System proposal report<br/><br/>v) Phase where developers decide roadmap for project plan?<br/>a) System Design &nbsp;&nbsp; b) System Analysis &nbsp;&nbsp; c) Coding &nbsp;&nbsp; d) Testing<br/><br/>vi) Approach where new system is tested in one part before implementing in others?<br/>a) parallel &nbsp;&nbsp; b) direct &nbsp;&nbsp; c) phased &nbsp;&nbsp; d) pilot<br/><br/>vii) …extends software beyond its original functional requirements?<br/>a) Corrective maintenance &nbsp;&nbsp; b) Perfective maintenance &nbsp;&nbsp; c) Adaptive maintenance &nbsp;&nbsp; d) Preventive maintenance<br/><br/>viii) Which normal form removes partial dependencies?<br/>a) First Normal Form &nbsp;&nbsp; b) Second Normal Form &nbsp;&nbsp; c) Third Normal Form &nbsp;&nbsp; d) Boyce-Codd Normal Form<br/><br/>ix) In ER diagrams, double ovals denote?<br/>a) Derived attributes &nbsp;&nbsp; b) Composite attributes &nbsp;&nbsp; c) Multi-value attributes &nbsp;&nbsp; d) Simple attributes<br/><br/>x) Testing beyond normal operational capacity is?<br/>a) Integration testing &nbsp;&nbsp; b) Stress testing &nbsp;&nbsp; c) Performance testing &nbsp;&nbsp; d) Acceptance testing",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>i) c) Transaction Processing Systems</b> — TPS are information systems that collect, store, modify, and retrieve the routine day-to-day transactions of an organization (e.g., payroll, order entry, reservation systems). They are designed to improve the efficiency of routine business activities.<br/><br/>
<b>ii) c) Formulation and planning various activities</b> — The project life cycle consists of phases that include formulation of the project idea, planning various activities, scheduling, execution, monitoring, and closure.<br/><br/>
<b>iii) c) Risk Management</b> — The spiral model, proposed by Barry Boehm, emphasizes iterative development with a focus on risk analysis at each cycle. Risk management is its most important feature, making it suitable for large, complex, and high-risk projects.<br/><br/>
<b>iv) c) Design Specification Report</b> — The Design Specification Report documents the existing system analysis, proposed system details, system flowcharts, modular design, data dictionary, input/output designs, and database design.<br/><br/>
<b>v) b) System Analysis</b> — In the System Analysis phase, analysts study the existing system, identify problems, gather requirements, and decide the roadmap and scope for the project plan, including feasibility studies.<br/><br/>
<b>vi) d) pilot</b> — In the pilot approach (pilot conversion), the new system is implemented in one part of the organization (e.g., one branch or department) as a test before rolling it out to the entire organization.<br/><br/>
<b>vii) b) Perfective maintenance</b> — Perfective maintenance involves enhancing and extending the software beyond its original functional requirements to improve performance, add new features, or refine existing functionality based on user feedback.<br/><br/>
<b>viii) b) Second Normal Form</b> — Second Normal Form (2NF) removes partial dependencies, where a non-prime attribute is functionally dependent on part of a composite primary key. A relation is in 2NF if it is in 1NF and has no partial dependencies.<br/><br/>
<b>ix) c) Multi-value attributes</b> — In ER diagrams, double ovals (or ellipses) represent multi-valued attributes, which are attributes that can hold multiple values for a single entity instance (e.g., a person can have multiple phone numbers).<br/><br/>
<b>x) b) Stress testing</b> — Stress testing evaluates the system's stability and reliability under extreme conditions by pushing it beyond its normal operational capacity (e.g., heavy load, limited resources) to identify breaking points.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "3",
                "question": "When would you use agile methodologies? How is it different from waterfall approach?",
                "marks": "5",
                "answer": """<b>When to use Agile Methodologies:</b><br/>
Agile methodologies are best suited for projects where:<br/>
• Requirements are uncertain, evolving, or likely to change frequently.<br/>
• The project is complex and requires frequent feedback from stakeholders.<br/>
• Rapid delivery of working software in small increments is preferred.<br/>
• The team is co-located and can collaborate closely with customers.<br/>
• There is a need for continuous improvement and adaptation.<br/>
• Startups, product development, and customer-facing applications benefit greatly from agile.<br/><br/>
<b>Differences between Agile and Waterfall Approach:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Basis</b></td><td><b>Agile</b></td><td><b>Waterfall</b></td></tr>
<tr><td>Model type</td><td>Iterative and incremental</td><td>Linear and sequential</td></tr>
<tr><td>Requirements</td><td>Evolving and flexible; changes are welcomed</td><td>Fixed at the beginning; changes are costly</td></tr>
<tr><td>Delivery</td><td>Working software delivered frequently in sprints</td><td>Software delivered at the end of the project</td></tr>
<tr><td>Customer involvement</td><td>High; continuous collaboration with stakeholders</td><td>Low; customer involved mainly at start and end</td></tr>
<tr><td>Testing</td><td>Continuous testing throughout development</td><td>Testing occurs only after development is complete</td></tr>
<tr><td>Documentation</td><td>Lightweight; working software over documentation</td><td>Heavy documentation at each phase</td></tr>
<tr><td>Risk management</td><td>Risks identified and mitigated in each iteration</td><td>Risks may surface late in the project</td></tr>
<tr><td>Examples</td><td>Scrum, Kanban, Extreme Programming (XP)</td><td>Traditional SDLC model</td></tr>
</table>""",
            },
            {
                "num": "4",
                "question": "Why is project management important? Explain activities performed by project manager during execution.",
                "marks": "5",
                "answer": """<b>Importance of Project Management:</b><br/>
Project management is crucial because it:<br/>
• Ensures projects are completed on time, within budget, and to the required quality standards.<br/>
• Provides clear goals, scope, and direction, minimizing confusion and rework.<br/>
• Helps identify and mitigate risks before they become critical issues.<br/>
• Optimizes resource allocation (human, financial, technical) efficiently.<br/>
• Improves communication and coordination among team members and stakeholders.<br/>
• Facilitates tracking progress through milestones and deliverables.<br/>
• Increases the probability of project success and customer satisfaction.<br/><br/>
<b>Activities Performed by Project Manager During Execution:</b><br/>
<b>1. Team Management:</b> Assigning tasks to team members based on skills, motivating the team, resolving conflicts, and ensuring collaboration.<br/><br/>
<b>2. Monitoring Progress:</b> Tracking project milestones, deadlines, and deliverables against the project plan using tools like Gantt charts and burn-down charts.<br/><br/>
<b>3. Quality Assurance:</b> Ensuring that outputs meet the defined quality standards through reviews, inspections, and testing.<br/><br/>
<b>4. Risk Management:</b> Continuously identifying new risks, assessing their impact, and implementing mitigation strategies.<br/><br/>
<b>5. Communication:</b> Conducting regular status meetings, preparing progress reports, and maintaining communication with stakeholders, clients, and upper management.<br/><br/>
<b>6. Change Control:</b> Managing scope creep by evaluating change requests, approving or rejecting changes, and updating plans accordingly.<br/><br/>
<b>7. Resource Allocation:</b> Ensuring that necessary resources (hardware, software, personnel) are available when needed and reallocating as priorities shift.<br/><br/>
<b>8. Issue Resolution:</b> Addressing technical and non-technical problems that arise during development promptly to avoid delays.<br/><br/>
<b>9. Budget Control:</b> Monitoring expenditures, comparing actual costs against the budget, and taking corrective action if variances occur.""",
            },
            {
                "num": "5",
                "question": "List various methods of interacting with a system. Explain factors to consider while designing a form.",
                "marks": "5",
                "answer": """<b>Methods of Interacting with a System:</b><br/>
1. <b>Command-Line Interface (CLI):</b> Users interact by typing text commands into a terminal or console.<br/>
2. <b>Graphical User Interface (GUI):</b> Users interact through visual elements like windows, icons, menus, buttons, and pointers (WIMP).<br/>
3. <b>Menu-Driven Interface:</b> Users select options from a list of displayed menus.<br/>
4. <b>Form-Based Interface:</b> Users enter data into predefined fields on a form layout.<br/>
5. <b>Natural Language Interface:</b> Users communicate using everyday language (e.g., chatbots, voice assistants).<br/>
6. <b>Touch-Based Interface:</b> Users interact by touching the screen (common in mobile devices and kiosks).<br/>
7. <b>Voice User Interface (VUI):</b> Users give spoken commands (e.g., Siri, Alexa, Google Assistant).<br/>
8. <b>Gesture-Based Interface:</b> Users interact through physical movements detected by sensors or cameras.<br/><br/>
<b>Factors to Consider While Designing a Form:</b><br/>
<b>1. Clarity and Simplicity:</b> The form should be easy to understand with clear labels and logical flow. Avoid clutter and unnecessary fields.<br/><br/>
<b>2. Consistency:</b> Use consistent fonts, colors, alignment, and spacing throughout the form. Buttons and input fields should follow a uniform style.<br/><br/>
<b>3. Logical Grouping:</b> Related fields should be grouped together (e.g., personal information, address details) using visual separators or fieldsets.<br/><br/>
<b>4. Input Validation:</b> Provide real-time validation and clear error messages to prevent incorrect data entry (e.g., date formats, email patterns).<br/><br/>
<b>5. Accessibility:</b> Ensure the form is usable by people with disabilities by supporting keyboard navigation, screen readers, and sufficient color contrast.<br/><br/>
<b>6. Appropriate Field Types:</b> Use the right input controls for the data type — dropdowns for limited options, radio buttons for single selection, checkboxes for multiple selections, and text areas for long text.<br/><br/>
<b>7. Defaults and Autofill:</b> Pre-fill known data where possible and set sensible defaults to speed up data entry.<br/><br/>
<b>8. Navigation and Instructions:</b> Provide clear instructions, tooltips, or help text. Include navigation buttons (Next, Previous, Submit, Cancel) at intuitive locations.<br/><br/>
<b>9. Minimize User Effort:</b> Reduce the number of fields to only what is essential. Use auto-complete and smart defaults to minimize typing.<br/><br/>
<b>10. Feedback:</b> Provide confirmation messages after submission and visual cues (loading indicators) during processing.""",
            },
            {
                "num": "6",
                "question": "What are deliverables from coding and testing? Explain different approaches to installation.",
                "marks": "5",
                "answer": """<b>Deliverables from Coding:</b><br/>
• <b>Source Code:</b> The actual program files written in the chosen programming language.<br/>
• <b>Compiled/Executable Code:</b> Machine-readable binaries or bytecode ready for deployment.<br/>
• <b>Code Documentation:</b> Inline comments, README files, and API documentation explaining the code structure.<br/>
• <b>Unit Test Results:</b> Reports showing that individual modules have been tested and passed.<br/>
• <b>Version Control Logs:</b> Commit history and change logs from tools like Git.<br/><br/>
<b>Deliverables from Testing:</b><br/>
• <b>Test Plans and Test Cases:</b> Documents detailing what was tested, how, and expected outcomes.<br/>
• <b>Test Scripts:</b> Automated test scripts for regression and continuous testing.<br/>
• <b>Bug/Defect Reports:</b> Documented list of identified bugs with severity, steps to reproduce, and status.<br/>
• <b>Test Summary Report:</b> Overall results including pass/fail statistics, coverage metrics, and risk assessment.<br/>
• <b>User Acceptance Test (UAT) Sign-off:</b> Formal approval from users/stakeholders confirming the system meets requirements.<br/><br/>
<b>Different Approaches to Installation:</b><br/>
<b>1. Direct Cutover (Big Bang):</b> The old system is completely replaced by the new system at a single point in time. It is simple but risky because any failure affects the entire organization immediately.<br/><br/>
<b>2. Parallel Installation:</b> Both old and new systems run simultaneously for a period. Output is compared for accuracy before fully switching over. It is the safest but most expensive approach due to duplicate effort.<br/><br/>
<b>3. Phased Installation:</b> The new system is implemented in stages or modules over time (e.g., by department or function). It reduces risk and allows learning from early phases, but integration between old and new parts can be complex.<br/><br/>
<b>4. Pilot Installation:</b> The new system is introduced in one part of the organization (e.g., one branch or location) first. After successful evaluation, it is rolled out to other parts. It allows testing in a real environment with limited risk.""",
            },
            {
                "num": "7",
                "question": "Why is normalization required? State second normal form and explain with example.",
                "marks": "5",
                "answer": """<b>Why Normalization is Required:</b><br/>
Normalization is the process of organizing data in a database to reduce redundancy and improve data integrity. It is required because:<br/>
• <b>Eliminates Data Redundancy:</b> Prevents the same data from being stored in multiple places, saving storage space.<br/>
• <b>Prevents Update Anomalies:</b> Avoids insertion, deletion, and modification anomalies that occur when redundant data is updated inconsistently.<br/>
• <b>Ensures Data Integrity:</b> Maintains accuracy and consistency of data across the database.<br/>
• <b>Improves Query Performance:</b> Well-structured tables can be queried more efficiently.<br/>
• <b>Simplifies Maintenance:</b> Changes to data structure are easier to manage in normalized databases.<br/><br/>
<b>Second Normal Form (2NF):</b><br/>
A relation is in Second Normal Form (2NF) if:<br/>
1. It is already in First Normal Form (1NF).<br/>
2. It has no partial dependency — that is, no non-prime attribute is functionally dependent on a proper subset of any candidate key (i.e., no non-prime attribute depends on part of a composite key).<br/><br/>
<b>Example:</b><br/>
Consider a relation <b>Enrollment(StudentID, CourseID, StudentName, CourseName, Grade)</b> with composite primary key (StudentID, CourseID).<br/><br/>
<b>Functional Dependencies:</b><br/>
• StudentID → StudentName (partial dependency — StudentName depends on only part of the key)<br/>
• CourseID → CourseName (partial dependency — CourseName depends on only part of the key)<br/>
• (StudentID, CourseID) → Grade (full dependency)<br/><br/>
This relation is in 1NF but NOT in 2NF because of partial dependencies.<br/><br/>
<b>Decomposition into 2NF:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Student</b> (StudentID, StudentName)</td><td>PK: StudentID</td></tr>
<tr><td><b>Course</b> (CourseID, CourseName)</td><td>PK: CourseID</td></tr>
<tr><td><b>Enrollment</b> (StudentID, CourseID, Grade)</td><td>PK: (StudentID, CourseID), FKs: StudentID, CourseID</td></tr>
</table><br/>
Now all non-prime attributes are fully functionally dependent on the entire primary key in each relation. Thus, the database is in 2NF.""",
            },
            {
                "num": "8",
                "question": "Construct an E-R Diagram for football club that has a name and a ground and is made up of players. A player can play for only one club and a manager identified by his name manages a club. A footballer has a registration number, name and age. A club manager also buys players. Each club plays against other clubs in the league and matches have a date, venue and score.",
                "marks": "5",
                "answer": """<b>ER Diagram Description for Football Club:</b><br/><br/>
<b>Entities and Attributes:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Entity</b></td><td><b>Attributes</b></td><td><b>Key</b></td></tr>
<tr><td>Club</td><td>Name, Ground</td><td>Name (Primary Key)</td></tr>
<tr><td>Player</td><td>RegistrationNumber, Name, Age</td><td>RegistrationNumber (Primary Key)</td></tr>
<tr><td>Manager</td><td>Name</td><td>Name (Primary Key)</td></tr>
<tr><td>Match</td><td>Date, Venue, Score</td><td>Composite key (Date, Venue) or MatchID</td></tr>
</table><br/>
<b>Relationships:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Relationship</b></td><td><b>Between Entities</b></td><td><b>Cardinality</b></td><td><b>Description</b></td></tr>
<tr><td>Made_up_of</td><td>Club — Player</td><td>1 : N</td><td>A club is made up of many players; a player plays for only one club.</td></tr>
<tr><td>Manages</td><td>Manager — Club</td><td>1 : 1</td><td>A manager manages exactly one club; each club has exactly one manager.</td></tr>
<tr><td>Buys</td><td>Manager — Player</td><td>M : N</td><td>A club manager buys many players; a player can be bought by managers over time (or interpret as Club buys Player).</td></tr>
<tr><td>Plays_against</td><td>Club — Match — Club</td><td>M : N (recursive)</td><td>Each club plays against other clubs in matches. A match involves two clubs. This is a recursive/ternary relationship.</td></tr>
</table><br/>
<b>Detailed ER Diagram Structure:</b><br/>
<pre>
[Club]                    [Manager]
  | Name (PK)               | Name (PK)
  | Ground                  |
  |                         |
  | 1                       | 1
  |                         |
Made_up_of               Manages
  |                         |
  | N                       | 1
  |                         |
[Player]                  [Club]
  | RegistrationNo (PK)     |
  | Name                    |
  | Age                     |
  |                         |
  | M                       |
  +----------Buys---------->+
       (Manager buys Player)

[Match] is connected to two Club entities via Plays_against:
   Club (1) ----< Plays_against >---- Match
   Club (1) ----< (Date, Venue, Score) >----
</pre><br/>
<b>Notes:</b><br/>
• Club and Player have a <b>one-to-many (1:N)</b> relationship because one club has many players, but each player belongs to only one club.<br/>
• Manager and Club have a <b>one-to-one (1:1)</b> relationship since one manager manages one club and vice versa.<br/>
• The "buys" relationship can be modeled between Manager and Player (M:N) or Club and Player depending on interpretation.<br/>
• The "plays against" relationship involves two clubs and a match; it can be represented as a ternary relationship or as a binary many-to-many between Club and Match with role names (HomeClub, AwayClub).<br/>
• In the diagram, rectangles represent entities, ovals represent attributes, diamonds represent relationships, and lines with cardinality ratios connect them.""",
            },
            {
                "num": "9",
                "question": "Maintenance is an on-going process. Do you agree? Explain the process of maintaining information systems.",
                "marks": "5",
                "answer": """<b>Yes, Maintenance is an On-going Process:</b><br/>
I completely agree that maintenance is an ongoing process. Information systems operate in dynamic environments where business requirements, technology, regulations, and user needs continuously change. Software does not wear out like physical hardware, but it becomes obsolete or defective over time due to changing conditions. Maintenance ensures that the system remains useful, efficient, secure, and aligned with organizational goals throughout its lifecycle. Studies show that maintenance can consume 60–80% of the total software lifecycle cost, highlighting its continuous nature.<br/><br/>
<b>Process of Maintaining Information Systems:</b><br/>
<b>1. Problem Identification / Modification Request:</b><br/>
Users, developers, or managers identify issues, bugs, or enhancement needs and submit a formal change request or problem report.<br/><br/>
<b>2. Problem Analysis:</b><br/>
The maintenance team analyzes the request to understand its nature (bug fix, enhancement, adaptation), impact on the system, feasibility, and cost. A decision is made on whether to approve the request.<br/><br/>
<b>3. Design of Modification:</b><br/>
If approved, the team designs the changes needed. This may involve modifying code, database schemas, interfaces, or documentation. Impact analysis ensures that changes do not break existing functionality.<br/><br/>
<b>4. Implementation / Coding:</b><br/>
The actual code changes are implemented by developers following coding standards. New modules may be added or existing ones modified.<br/><br/>
<b>5. Testing:</b><br/>
Rigorous testing is performed including unit testing, integration testing, regression testing, and system testing to ensure the modification works correctly and has not introduced new errors.<br/><br/>
<b>6. Deployment:</b><br/>
The updated system is deployed to the production environment. This may involve patching, version releases, or rolling updates.<br/><br/>
<b>7. Documentation Update:</b><br/>
All related documentation (user manuals, system manuals, design documents) is updated to reflect the changes.<br/><br/>
<b>8. Review and Feedback:</b><br/>
Post-implementation review evaluates whether the maintenance objective was achieved. User feedback is collected for future improvements.<br/><br/>
<b>Types of Maintenance:</b><br/>
• <b>Corrective:</b> Fixing bugs and errors.<br/>
• <b>Adaptive:</b> Modifying the system to work in a changed environment (OS, hardware, regulations).<br/>
• <b>Perfective:</b> Enhancing performance or adding new features.<br/>
• <b>Preventive:</b> Making changes to prevent future problems.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "10",
                "question": "Develop a context diagram and top level logical DFD for B&B mail-order company that distributes CDs, DVDs of music, games, movies, software at discount prices to club members. When an order processing clerk receives an order form, he/she verifies that the sender is a club member by checking the Member file. If not a member, returns the order with a membership application form. If a member, verifies order item data by checking the Item file. Then enters order data and saves it to the Daily Order file. Also prints an invoice and shipping list for each order, forwarded to Order Fulfillment Department.",
                "marks": "10",
                "answer": """<b>Context Diagram (Level 0 DFD) for B&B Mail-Order Company:</b><br/>
A Context Diagram shows the entire system as a single process with external entities and data flows.<br/>
<pre>
External Entities:                  Data Flows:
  [Club Member] --------Order Form----------> [0] B&B Mail-Order System
  [Club Member] <--------Membership App Form-- (if not member)
  [Club Member] <--------Invoice------------- (if member)
  [Club Member] <--------Shipping List-------- (if member)
  [Order Fulfillment Dept] <--Shipping List--- (if member)
</pre><br/>
<b>Description of Context Diagram:</b><br/>
• <b>External Entity: Club Member</b> — sends Order Form to the system; receives Membership Application Form (if not a member), Invoice, and Shipping List (if a member).<br/>
• <b>External Entity: Order Fulfillment Department</b> — receives the Shipping List to process physical delivery.<br/>
• <b>Process: 0 B&B Mail-Order System</b> — the entire system represented as a single bubble.<br/>
• <b>Data Stores (implied but not shown in context diagram):</b> Member File, Item File, Daily Order File.<br/><br/>
<b>Top Level Logical DFD (Level 1 DFD) for B&B Mail-Order Company:</b><br/>
The Level 1 DFD decomposes the single process into sub-processes:<br/>
<pre>
[Club Member] ---Order Form---> [1.0] Receive & Verify Order
                                      |
                                      | Check Member Status
                                      v
                                [D1] Member File
                                      |
                    +-----------------+-----------------+
                    | Not Member                          | Member
                    v                                     v
[Club Member] <--Membership App Form--      [2.0] Verify Order Items
                                                   |
                                                   | Check Item Data
                                                   v
                                             [D2] Item File
                                                   |
                                                   v
                                            [3.0] Process Order
                                                   |
                                      +------------+------------+
                                      |                         |
                                      v                         v
                                [D3] Daily Order File    [4.0] Print Documents
                                                                |
                                      +-------------------------+-------------------------+
                                      |                                                   |
                                      v                                                   v
                                [Club Member] <---Invoice---                  [Order Fulfillment Dept] <---Shipping List---
</pre><br/>
<b>Description of Level 1 DFD Processes:</b><br/>
<b>Process 1.0 — Receive & Verify Order:</b><br/>
The order processing clerk receives the Order Form and verifies whether the sender is a club member by querying the <b>Member File (D1)</b>.<br/>
• If <b>not a member</b>: returns the Order Form along with a <b>Membership Application Form</b> to the Club Member.<br/>
• If <b>a member</b>: passes the order to Process 2.0.<br/><br/>
<b>Process 2.0 — Verify Order Items:</b><br/>
The clerk verifies the ordered items (CDs, DVDs, games, movies, software) by checking the <b>Item File (D2)</b> to ensure item data is correct and available.<br/><br/>
<b>Process 3.0 — Process Order:</b><br/>
The clerk enters the verified order data and saves it to the <b>Daily Order File (D3)</b>. This creates a permanent record of the transaction.<br/><br/>
<b>Process 4.0 — Print Documents:</b><br/>
The system generates and prints two documents:<br/>
• <b>Invoice</b> — sent to the Club Member for payment.<br/>
• <b>Shipping List</b> — sent to the Order Fulfillment Department to pack and ship the items.<br/><br/>
<b>Data Stores:</b><br/>
• <b>D1 — Member File:</b> Contains member details used to verify club membership.<br/>
• <b>D2 — Item File:</b> Contains catalog information about CDs, DVDs, games, movies, and software.<br/>
• <b>D3 — Daily Order File:</b> Accumulates all orders processed during the day.<br/><br/>
<b>Data Flows Summary:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Data Flow</b></td><td><b>Source</b></td><td><b>Destination</b></td></tr>
<tr><td>Order Form</td><td>Club Member</td><td>Process 1.0</td></tr>
<tr><td>Member Status</td><td>D1 Member File</td><td>Process 1.0</td></tr>
<tr><td>Membership Application Form</td><td>Process 1.0</td><td>Club Member</td></tr>
<tr><td>Verified Order</td><td>Process 1.0</td><td>Process 2.0</td></tr>
<tr><td>Item Data</td><td>D2 Item File</td><td>Process 2.0</td></tr>
<tr><td>Validated Order</td><td>Process 2.0</td><td>Process 3.0</td></tr>
<tr><td>Order Record</td><td>Process 3.0</td><td>D3 Daily Order File</td></tr>
<tr><td>Print Request</td><td>Process 3.0</td><td>Process 4.0</td></tr>
<tr><td>Invoice</td><td>Process 4.0</td><td>Club Member</td></tr>
<tr><td>Shipping List</td><td>Process 4.0</td><td>Order Fulfillment Dept</td></tr>
</table>""",
            },
            {
                "num": "11",
                "question": "With proper reasoning, explain how CASE Tools aid in information system development? You have been hired as a system analyst in TU tech software development company and are asked to analyze the way system works. What qualities do you need to have to analyze such type of systems?",
                "marks": "10",
                "answer": """<b>How CASE Tools Aid in Information System Development:</b><br/>
CASE (Computer-Aided Software Engineering) Tools are software applications that automate and support various activities throughout the SDLC. They significantly improve productivity, quality, and consistency in information system development.<br/><br/>
<b>1. Requirement Analysis and Modeling:</b><br/>
CASE tools help analysts create visual models such as Data Flow Diagrams (DFDs), Entity-Relationship (ER) diagrams, UML diagrams (use case, class, sequence), and process models. Tools like Visio, Enterprise Architect, and Rational Rose provide drag-and-drop interfaces that make modeling faster and error-free. This ensures requirements are clearly documented and communicated.<br/><br/>
<b>2. Documentation Generation:</b><br/>
CASE tools automatically generate technical documentation, user manuals, and data dictionaries from models and code. This saves significant manual effort and ensures documentation stays synchronized with the system design.<br/><br/>
<b>3. Code Generation:</b><br/>
Upper CASE and Integrated CASE (I-CASE) tools can automatically generate code skeletons, database schemas (SQL), and even complete application code from design specifications. This reduces coding time and human error.<br/><br/>
<b>4. Project Management Support:</b><br/>
Many CASE tools include features for scheduling, resource allocation, progress tracking, and version control. They help managers monitor milestones, identify bottlenecks, and ensure timely delivery.<br/><br/>
<b>5. Reverse Engineering:</b><br/>
CASE tools can analyze existing source code and generate design diagrams and documentation. This is invaluable for maintaining legacy systems or understanding undocumented code.<br/><br/>
<b>6. Testing and Quality Assurance:</b><br/>
Some CASE tools support test case generation, simulation of models, and consistency checking between design and code. They help identify defects early in the lifecycle when they are cheaper to fix.<br/><br/>
<b>7. Repository Management:</b><br/>
Centralized repositories store all project artifacts (models, code, documents) in one place, enabling team collaboration, version control, and reuse of components across projects.<br/><br/>
<b>8. Standardization:</b><br/>
CASE tools enforce methodological standards (structured or object-oriented), ensuring that all team members follow consistent notations and practices.<br/><br/>
<b>Reasoning / Conclusion:</b><br/>
By automating repetitive tasks, reducing manual errors, improving communication through visual models, and maintaining consistency across phases, CASE tools dramatically increase development speed, reduce costs, and improve software quality.<br/><br/>
<b>Qualities Needed to Analyze Systems as a System Analyst at TU Tech:</b><br/>
<b>1. Analytical Thinking:</b> Ability to break down complex systems into components, identify patterns, understand interdependencies, and diagnose problems logically.<br/><br/>
<b>2. Technical Knowledge:</b> Strong understanding of databases, networks, programming concepts, software architecture, and current technologies to comprehend how systems function technically.<br/><br/>
<b>3. Communication Skills:</b> Must interact effectively with technical teams, non-technical users, and management. Needs to conduct interviews, write clear reports, and present findings persuasively.<br/><br/>
<b>4. Problem-Solving Ability:</b> Capacity to identify bottlenecks, inefficiencies, and risks in existing systems and propose practical, cost-effective solutions.<br/><br/>
<b>5. Attention to Detail:</b> Must meticulously document requirements, data flows, and processes without overlooking edge cases or exceptions.<br/><br/>
<b>6. Business Domain Knowledge:</b> Understanding of the company's business processes, goals, and industry trends to align technical solutions with business needs.<br/><br/>
<b>7. Interpersonal and Negotiation Skills:</b> Ability to manage stakeholder expectations, resolve conflicts between user groups, and build consensus on system changes.<br/><br/>
<b>8. Adaptability and Learning Agility:</b> Technology changes rapidly; an analyst must be willing to learn new tools, methodologies, and domains quickly.<br/><br/>
<b>9. Documentation and Modeling Skills:</b> Proficiency in creating DFDs, ERDs, UML diagrams, process maps, and writing specifications using CASE tools and diagramming software.<br/><br/>
<b>10. Ethics and Integrity:</b> Must handle sensitive organizational data responsibly and recommend solutions that are in the best interest of the organization rather than personal gain.""",
            },
            {
                "num": "11a",
                "question": "Why do software projects often fail? Explain different types of software testing.",
                "marks": "10",
                "answer": """<b>Why Software Projects Often Fail:</b><br/>
Software project failure is a common phenomenon in the IT industry. The major reasons include:<br/><br/>
<b>1. Unclear or Changing Requirements:</b><br/>
If requirements are poorly defined, ambiguous, or constantly changing without proper change control, the final product may not meet user expectations. Scope creep is a major contributor to failure.<br/><br/>
<b>2. Poor Planning and Estimation:</b><br/>
Unrealistic deadlines, underestimated budgets, and inadequate resource allocation lead to rushed development, cutting corners, and compromised quality.<br/><br/>
<b>3. Inadequate Communication:</b><br/>
Lack of communication between stakeholders, developers, and users results in misunderstandings, misaligned goals, and missed expectations.<br/><br/>
<b>4. Lack of User Involvement:</b><br/>
When end users are not involved throughout the development process, the system may not address real-world needs, leading to rejection after deployment.<br/><br/>
<b>5. Poor Project Management:</b><br/>
Ineffective leadership, lack of risk management, insufficient tracking of progress, and inability to resolve issues promptly can derail projects.<br/><br/>
<b>6. Technical Complexity:</b><br/>
Overly ambitious architectures, use of immature technologies, poor code quality, and inadequate testing create insurmountable technical debt.<br/><br/>
<b>7. Insufficient Testing:</b><br/>
When testing is treated as an afterthought or given insufficient time, critical bugs reach production, damaging user trust and requiring expensive fixes.<br/><br/>
<b>8. Staff Turnover and Skill Gaps:</b><br/>
Losing key team members or hiring underqualified personnel disrupts momentum and reduces team capability.<br/><br/>
<b>9. Organizational Issues:</b><br/>
Political conflicts, lack of executive support, competing priorities, and resistance to change within the organization can sabotage even well-planned projects.<br/><br/>
<b>Different Types of Software Testing:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Type</b></td><td><b>Description</b></td></tr>
<tr><td><b>Unit Testing</b></td><td>Tests individual modules or functions in isolation to verify they work correctly. Usually done by developers.</td></tr>
<tr><td><b>Integration Testing</b></td><td>Tests the interaction between integrated modules to detect interface defects and data flow issues.</td></tr>
<tr><td><b>System Testing</b></td><td>Tests the complete, integrated system as a whole to verify it meets specified requirements.</td></tr>
<tr><td><b>Acceptance Testing</b></td><td>Conducted by end users or clients to determine whether the system is acceptable for delivery (UAT — User Acceptance Testing).</td></tr>
<tr><td><b>Regression Testing</b></td><td>Re-tests the system after modifications to ensure that existing functionality still works and new bugs were not introduced.</td></tr>
<tr><td><b>Alpha Testing</b></td><td>Internal testing performed by the organization before releasing the software to external users.</td></tr>
<tr><td><b>Beta Testing</b></td><td>External testing by a limited number of real users in their own environment to identify issues before general release.</td></tr>
<tr><td><b>Performance Testing</b></td><td>Evaluates system responsiveness, throughput, and stability under expected load conditions.</td></tr>
<tr><td><b>Stress Testing</b></td><td>Pushes the system beyond normal operational limits to identify its breaking point and ensure graceful failure.</td></tr>
<tr><td><b>Security Testing</b></td><td>Identifies vulnerabilities, threats, and risks in the system to protect data and prevent unauthorized access.</td></tr>
<tr><td><b>Usability Testing</b></td><td>Evaluates how easy and intuitive the system is for end users to learn and operate.</td></tr>
<tr><td><b>White-Box Testing</b></td><td>Tests internal structure, logic, and code paths with knowledge of the source code.</td></tr>
<tr><td><b>Black-Box Testing</b></td><td>Tests functionality without knowledge of internal code, based solely on requirements and inputs/outputs.</td></tr>
</table>""",
            },
            {
                "num": "11b",
                "question": "List features of OOAD. Differentiate between structured methodologies and object oriented methodologies.",
                "marks": "10",
                "answer": """<b>Features of OOAD (Object-Oriented Analysis and Design):</b><br/>
OOAD is an approach to software engineering that models a system as a group of interacting objects. Its key features include:<br/><br/>
<b>1. Objects:</b><br/>
The basic building blocks that encapsulate both data (attributes) and behavior (methods). Objects represent real-world entities.<br/><br/>
<b>2. Classes:</b><br/>
Blueprints or templates from which objects are instantiated. A class defines the common properties and behaviors shared by all its objects.<br/><br/>
<b>3. Encapsulation:</b><br/>
The bundling of data and methods that operate on that data within a single unit (class), while restricting direct access to some components. This protects data integrity.<br/><br/>
<b>4. Inheritance:</b><br/>
A mechanism where a new class (subclass/derived class) acquires properties and behaviors from an existing class (superclass/base class), promoting code reuse and hierarchical classification.<br/><br/>
<b>5. Polymorphism:</b><br/>
The ability of different objects to respond to the same message (method call) in different ways. Achieved through method overriding and overloading, it increases flexibility.<br/><br/>
<b>6. Abstraction:</b><br/>
Hiding complex implementation details and exposing only essential features. Simplifies system modeling by focusing on what an object does rather than how it does it.<br/><br/>
<b>7. Message Passing:</b><br/>
Objects communicate by sending and receiving messages. This models real-world interactions between entities.<br/><br/>
<b>8. Modularity:</b><br/>
The system is decomposed into self-contained, loosely coupled objects/modules that can be developed, tested, and maintained independently.<br/><br/>
<b>Differentiation between Structured Methodologies and Object-Oriented Methodologies:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Basis</b></td><td><b>Structured Methodologies</b></td><td><b>Object-Oriented Methodologies</b></td></tr>
<tr><td>Approach</td><td>Function-oriented; focuses on processes and functions</td><td>Data-oriented; focuses on objects and data</td></tr>
<tr><td>Basic Unit</td><td>Function/Procedure</td><td>Object (data + methods)</td></tr>
<tr><td>Decomposition</td><td>Top-down functional decomposition</td><td>Bottom-up composition of objects</td></tr>
<tr><td>Data and Functions</td><td>Separated; global data shared among functions</td><td>Encapsulated together within objects</td></tr>
<tr><td>Reusability</td><td>Limited; functions are tightly coupled with data</td><td>High; classes and objects can be reused via inheritance and composition</td></tr>
<tr><td>Maintenance</td><td>Difficult; changes in data structure affect many functions</td><td>Easier; changes localized within objects</td></tr>
<tr><td>Modeling</td><td>Uses DFDs, Structure Charts, ERDs, Data Dictionaries</td><td>Uses UML diagrams (use case, class, sequence, activity, etc.)</td></tr>
<tr><td>System View</td><td>Process-centric</td><td>Entity-centric</td></tr>
<tr><td>Handling Complexity</td><td>Becomes difficult for large, complex systems</td><td>Scales well for complex, evolving systems</td></tr>
<tr><td><b>Change Adaptability</b></td><td>Less adaptable to requirement changes</td><td>More adaptable due to modularity and encapsulation</td></tr>
<tr><td>Examples</td><td>Structured Systems Analysis and Design Method (SSADM), Waterfall with structured analysis</td><td>Unified Process (UP), Rational Unified Process (RUP), Agile with UML</td></tr>
</table><br/>
<b>Summary:</b><br/>
Structured methodologies were dominant in the 1970s–1980s and work well for smaller, well-defined systems with stable requirements. Object-oriented methodologies emerged to handle the complexity of modern software by modeling systems around real-world entities, providing better reusability, maintainability, and scalability. Today, OOAD is the standard for most large-scale software development, often combined with agile practices.""",
            },
        ]
    },
]

if __name__ == "__main__":
    generate_answer_sheet("CACS203", "system-analysis-design", "System Analysis & Design", 2019, "semester-3", CACS203_2019)
