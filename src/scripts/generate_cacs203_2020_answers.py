#!/usr/bin/env python3
import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS203_2020 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What is system? What are the phases of SDLC? Explain briefly.",
                "marks": "1+4",
                "answer": """<b>System:</b> A system is a collection of interrelated components that work together to achieve a common goal. It accepts inputs, processes them, and produces outputs. A system has boundaries, interacts with its environment, and is composed of subsystems that are themselves systems. Examples include information systems, operating systems, and ecosystems. Characteristics of a system include components, interrelatedness, boundaries, purpose, and environment.<br/><br/>
<b>Phases of SDLC (System Development Life Cycle):</b><br/>
1. <b>Planning:</b> Identifying the need for a new system, conducting feasibility studies (technical, economic, operational), defining project scope, and obtaining approval. The project plan, schedule, and budget are created.<br/>
2. <b>Analysis:</b> Gathering detailed requirements from stakeholders through interviews, surveys, and observation. Current system is studied to identify problems and opportunities. Requirements are documented in SRS (Software Requirements Specification).<br/>
3. <b>Design:</b> Creating system architecture, database design, interface design, and detailed module specifications. Design documents include DFDs, ERDs, data dictionaries, and prototype screens.<br/>
4. <b>Implementation (Development):</b> Actual coding and programming based on design specifications. Developers write code, perform unit testing, and integrate modules. This is the phase where the system is actually built.<br/>
5. <b>Testing:</b> Verifying that the system meets requirements and is free of defects. Includes unit testing, integration testing, system testing, and user acceptance testing (UAT).<br/>
6. <b>Deployment:</b> Installing the system in the production environment, training users, and migrating data from the old system. Can be done through direct cutover, parallel running, phased implementation, or pilot approach.<br/>
7. <b>Maintenance:</b> Ongoing support, bug fixes, enhancements, and updates after deployment. Types include corrective, adaptive, perfective, and preventive maintenance.""",
            },
            {
                "num": "3",
                "question": "What do you mean by planning? Write the process of planning for Information System Development Project.",
                "marks": "1+4",
                "answer": """<b>Planning:</b> Planning is the process of defining goals, establishing strategies, and developing plans to coordinate activities. In the context of information systems, planning involves determining what needs to be done, how it will be done, who will do it, when it will be done, and what resources are required. Effective planning reduces uncertainty, minimizes waste, and establishes standards for controlling project progress.<br/><br/>
<b>Process of Planning for Information System Development Project:</b><br/>
1. <b>Define Project Scope and Objectives:</b> Clearly state what the project will accomplish, identify stakeholders, and establish measurable objectives. Define what is in scope and what is out of scope.<br/>
2. <b>Conduct Feasibility Study:</b> Evaluate the project from multiple perspectives:<br/>
   • <b>Technical feasibility:</b> Can the technology support the proposed solution?<br/>
   • <b>Economic feasibility:</b> Is the project financially viable? (cost-benefit analysis, ROI)<br/>
   • <b>Operational feasibility:</b> Will the system be used effectively within the organization?<br/>
   • <b>Schedule feasibility:</b> Can the project be completed within the required timeframe?<br/>
3. <b>Estimate Resources:</b> Determine human resources (analysts, developers, testers), hardware, software, and budget requirements needed for the project.<br/>
4. <b>Develop Work Breakdown Structure (WBS):</b> Break down the project into smaller, manageable tasks and subtasks. Each task should have clear deliverables and responsible persons.<br/>
5. <b>Create Project Schedule:</b> Estimate time for each task, identify dependencies, and create a timeline using Gantt charts or PERT/CPM networks. Identify the critical path.<br/>
6. <b>Identify Risks:</b> Identify potential risks (technical, organizational, external), assess their probability and impact, and develop mitigation strategies.<br/>
7. <b>Prepare Project Plan Document:</b> Compile all planning information into a formal project plan including scope, schedule, budget, resources, risk management plan, and communication plan.<br/>
8. <b>Obtain Approval:</b> Present the project plan to management and stakeholders for review and approval before proceeding.""",
            },
            {
                "num": "4",
                "question": "Define process modeling. Explain DFD with example.",
                "marks": "1+4",
                "answer": """<b>Process Modeling:</b> Process modeling is the graphical representation of the processes (functions or activities) that capture, manipulate, store, and distribute data between a system and its environment and among system components. It helps analysts understand how data flows through an organization and how it is transformed. Data Flow Diagram (DFD) is the most common tool used for process modeling.<br/><br/>
<b>Data Flow Diagram (DFD):</b><br/>
A DFD is a graphical representation of the flow of data through an information system. It shows how data is input, processed, stored, and output by the system. DFDs can be drawn at different levels of detail (context diagram, level 0, level 1, etc.).<br/><br/>
<b>Components of DFD:</b><br/>
1. <b>Process (Circle/Bubble):</b> Represents an activity or function that transforms data. Named with a verb phrase (e.g., "Validate Order", "Calculate Payroll").<br/>
2. <b>External Entity (Rectangle):</b> Represents sources or destinations of data outside the system being modeled (e.g., "Customer", "Bank", "Supplier").<br/>
3. <b>Data Store (Open Rectangle/Parallel Lines):</b> Represents a repository where data is stored (e.g., "Customer Database", "Order File", "Inventory Master").<br/>
4. <b>Data Flow (Arrow):</b> Represents the movement of data between processes, entities, and data stores. Labeled with the data name.<br/><br/>
<b>Example — Online Order Processing System:</b><br/>
<b>Context Diagram (Level 0):</b><br/>
External Entities: Customer, Warehouse, Bank<br/>
Process: Order Processing System<br/>
Data Flows: Order Details (Customer → System), Payment Info (Customer → System), Order Confirmation (System → Customer), Shipping Request (System → Warehouse), Payment Authorization (System → Bank)<br/><br/>
<b>Level 1 DFD:</b><br/>
Processes:<br/>
• P1: Receive Order (Customer → P1 → Order File)<br/>
• P2: Validate Payment (P1 → P2 → Bank → P2 → Payment File)<br/>
• P3: Process Order (P2 → P3 → Order File, Inventory File)<br/>
• P4: Generate Invoice (P3 → P4 → Customer)<br/>
• P5: Ship Order (P3 → P5 → Warehouse → Customer)""",
            },
            {
                "num": "5",
                "question": "List and explain the skills and responsibilities of project manager.",
                "marks": "2.5+2.5",
                "answer": """<b>Skills of a Project Manager:</b><br/>
1. <b>Leadership:</b> Ability to inspire, motivate, and guide team members toward achieving project goals. Includes delegation, conflict resolution, and decision-making.<br/>
2. <b>Communication:</b> Strong verbal and written communication skills to interact with stakeholders, team members, and clients. Includes active listening and presentation skills.<br/>
3. <b>Technical Knowledge:</b> Understanding of the technical aspects of the project, tools, and methodologies being used. For IS projects, knowledge of databases, programming, and system design.<br/>
4. <b>Time Management:</b> Ability to prioritize tasks, meet deadlines, and manage schedules effectively using tools like Gantt charts and project management software.<br/>
5. <b>Risk Management:</b> Identifying potential risks, assessing their impact, and developing mitigation strategies to minimize project disruptions.<br/>
6. <b>Budget Management:</b> Planning, estimating, and controlling project costs to ensure the project is completed within the approved budget.<br/>
7. <b>Problem-Solving:</b> Analytical thinking and creativity to resolve issues that arise during the project lifecycle.<br/>
8. <b>Negotiation:</b> Ability to negotiate with stakeholders, vendors, and team members for resources, timelines, and scope adjustments.<br/><br/>
<b>Responsibilities of a Project Manager:</b><br/>
1. <b>Project Planning:</b> Defining project scope, objectives, deliverables, and creating detailed project plans including schedules and budgets.<br/>
2. <b>Resource Allocation:</b> Assigning the right people to the right tasks and ensuring necessary resources (hardware, software, budget) are available.<br/>
3. <b>Team Management:</b> Building and leading the project team, defining roles and responsibilities, and fostering a collaborative work environment.<br/>
4. <b>Stakeholder Communication:</b> Keeping all stakeholders informed about project progress, issues, and changes through regular meetings and status reports.<br/>
5. <b>Quality Assurance:</b> Ensuring that project deliverables meet the required quality standards and satisfy stakeholder requirements.<br/>
6. <b>Risk Monitoring:</b> Continuously tracking identified risks, identifying new risks, and implementing contingency plans when necessary.<br/>
7. <b>Change Management:</b> Managing scope changes, assessing their impact on schedule and budget, and obtaining proper approvals.<br/>
8. <b>Project Closure:</b> Ensuring all project deliverables are completed, conducting post-project reviews, documenting lessons learned, and formally closing the project.""",
            },
            {
                "num": "6",
                "question": "Explain the guidelines to design an interface and dialogue box for e-commerce system.",
                "marks": "5",
                "answer": """<b>Guidelines for Designing Interface and Dialogue Box for E-Commerce System:</b><br/><br/>
1. <b>Simplicity and Clarity:</b> Keep the interface clean and uncluttered. Use clear labels, intuitive icons, and familiar navigation patterns. Avoid unnecessary elements that distract users from their shopping goals.<br/><br/>
2. <b>Consistent Layout:</b> Maintain consistency in color schemes, fonts, button styles, and navigation across all pages. The header, footer, and navigation should appear the same on every page.<br/><br/>
3. <b>Responsive Design:</b> Ensure the interface adapts seamlessly to different screen sizes (desktop, tablet, mobile). Use flexible grids, scalable images, and touch-friendly buttons.<br/><br/>
4. <b>Prominent Call-to-Action (CTA):</b> Buttons like "Add to Cart", "Buy Now", and "Checkout" should be visually prominent using contrasting colors and appropriate sizing.<br/><br/>
5. <b>Search and Filter Functionality:</b> Provide a visible search bar with auto-suggestions. Include filters for category, price range, brand, ratings, etc.<br/><br/>
6. <b>Clear Product Information:</b> Display high-quality product images, detailed descriptions, prices, availability status, reviews, and shipping information clearly.<br/><br/>
7. <b>Dialogue Box Design Guidelines:</b><br/>
   • <b>Confirmation Dialogues:</b> Use modal dialogs for critical actions (delete cart, cancel order) with clear "Confirm" and "Cancel" options.<br/>
   • <b>Error Messages:</b> Display user-friendly error messages explaining what went wrong and how to fix it (e.g., "Invalid card number. Please check and re-enter.").<br/>
   • <b>Progress Indicators:</b> Show loading spinners or progress bars during checkout, payment processing, or order placement.<br/>
   • <b>Success Messages:</b> Provide clear confirmation after successful actions (e.g., "Order placed successfully! Order #12345").<br/>
   • <b>Input Validation:</b> Validate form inputs in real-time and display inline error messages near the relevant fields.<br/><br/>
8. <b>Security Indicators:</b> Display security badges, SSL certificates, and trusted payment icons to build user trust during checkout.<br/><br/>
9. <b>Accessibility:</b> Follow WCAG guidelines — ensure sufficient color contrast, keyboard navigation support, alt text for images, and screen reader compatibility.<br/><br/>
10. <b>User Feedback:</b> Provide immediate visual or auditory feedback for user actions (hover effects, button clicks, cart updates) to enhance interactivity.""",
            },
            {
                "num": "7",
                "question": "Differentiate between system and user documentation with their applications.",
                "marks": "5",
                "answer": """<b>Difference between System Documentation and User Documentation:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>System Documentation</b></td><td><b>User Documentation</b></td></tr>
<tr><td>Target Audience</td><td>Developers, programmers, system analysts, technical staff</td><td>End users, operators, non-technical staff</td></tr>
<tr><td>Content</td><td>System design, architecture, code comments, data dictionaries, DFDs, ERDs, API references</td><td>User manuals, help guides, FAQs, tutorials, quick start guides</td></tr>
<tr><td>Technical Depth</td><td>Highly technical and detailed</td><td>Non-technical, simple language</td></tr>
<tr><td>Purpose</td><td>To understand, maintain, and modify the system</td><td>To learn how to use the system effectively</td></tr>
<tr><td>Created By</td><td>System analysts and developers during development</td><td>Technical writers and trainers after development</td></tr>
<tr><td>Update Frequency</td><td>Updated when system is modified</td><td>Updated when user interface or workflows change</td></tr>
</table><br/><br/>
<b>Applications of System Documentation:</b><br/>
1. <b>System Maintenance:</b> Helps developers understand existing code when fixing bugs or adding features.<br/>
2. <b>System Enhancement:</b> Provides the foundation for making improvements or adding new modules.<br/>
3. <b>Knowledge Transfer:</b> Enables new team members to understand the system architecture quickly.<br/>
4. <b>Quality Assurance:</b> Serves as a reference for testers to verify that the system meets design specifications.<br/>
5. <b>Disaster Recovery:</b> Helps rebuild or restore the system in case of failures.<br/><br/>
<b>Applications of User Documentation:</b><br/>
1. <b>User Training:</b> Helps new users learn how to operate the system through tutorials and guides.<br/>
2. <b>Reference:</b> Serves as a lookup resource when users encounter unfamiliar situations.<br/>
3. <b>Troubleshooting:</b> Helps users resolve common problems without contacting support.<br/>
4. <b>Reducing Support Costs:</b> Well-documented systems reduce the number of support calls and emails.<br/>
5. <b>Compliance:</b> Some industries require documented procedures for audit and regulatory purposes.""",
            },
            {
                "num": "8",
                "question": "Define software testing. Explain software quality assurance activities.",
                "marks": "1+4",
                "answer": """<b>Software Testing:</b> Software testing is the process of evaluating and verifying that a software product or application does what it is supposed to do. It involves executing a program with the intent of finding errors, defects, or gaps between actual and expected requirements. Testing can be done manually or through automated tools and includes various types such as unit testing, integration testing, system testing, and acceptance testing. The goal is to ensure the software is reliable, secure, and performs well under expected conditions.<br/><br/>
<b>Software Quality Assurance (SQA) Activities:</b><br/>
1. <b>Quality Planning:</b> Defining quality goals, standards, and criteria for the project. Creating a quality management plan that outlines how quality will be measured and ensured throughout the project.<br/>
2. <b>Process Definition and Improvement:</b> Establishing standardized development processes, methodologies, and best practices. Using frameworks like ISO 9000, CMMI, or Six Sigma to improve process maturity.<br/>
3. <b>Reviews and Audits:</b> Conducting formal reviews of requirements, design documents, and code. Audits verify that processes are being followed and deliverables meet standards.<br/>
4. <b>Testing:</b> Executing various levels of testing including unit testing (individual modules), integration testing (combined modules), system testing (complete system), and acceptance testing (user validation).<br/>
5. <b>Defect Tracking and Management:</b> Recording, categorizing, prioritizing, and tracking defects from discovery through resolution. Using tools like JIRA, Bugzilla, or Trello.<br/>
6. <b>Configuration Management:</b> Controlling changes to software artifacts through version control, change management, and release management. Ensures traceability and consistency.<br/>
7. <b>Metrics and Measurement:</b> Collecting and analyzing data on defect density, test coverage, code complexity, and customer satisfaction. Using metrics to identify trends and drive improvements.<br/>
8. <b>Training:</b> Ensuring team members have the necessary skills and knowledge to follow quality processes and use tools effectively.<br/>
9. <b>Documentation Control:</b> Maintaining accurate and up-to-date documentation throughout the software lifecycle.<br/>
10. <b>Customer Feedback Analysis:</b> Gathering and analyzing user feedback to identify quality issues and improvement opportunities.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "What are the major differences between Agile methodologies and waterfall model? Why should you use agile methodologies? Explain.",
                "marks": "5+5",
                "answer": """<b>Major Differences between Agile and Waterfall Model:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>Waterfall Model</b></td><td><b>Agile Methodologies</b></td></tr>
<tr><td>Approach</td><td>Sequential and linear</td><td>Iterative and incremental</td></tr>
<tr><td>Flexibility</td><td>Rigid, difficult to change requirements</td><td>Flexible, welcomes changing requirements</td></tr>
<tr><td>Customer Involvement</td><td>Limited, mainly at beginning and end</td><td>Continuous throughout development</td></tr>
<tr><td>Delivery</td><td>Single final product at the end</td><td>Working software delivered frequently (weeks)</td></tr>
<tr><td>Testing</td><td>Done after implementation phase</td><td>Done concurrently with development</td></tr>
<tr><td>Documentation</td><td>Heavy documentation at each phase</td><td>Lightweight, working software over documentation</td></tr>
<tr><td>Risk Management</td><td>Risks identified late, hard to mitigate</td><td>Risks identified early and addressed in each sprint</td></tr>
<tr><td>Team Structure</td><td>Formal, role-based hierarchy</td><td>Self-organizing, cross-functional teams</td></tr>
<tr><td>Best For</td><td>Projects with clear, stable requirements</td><td>Projects with evolving or unclear requirements</td></tr>
</table><br/><br/>
<b>Why Use Agile Methodologies:</b><br/>
1. <b>Adaptability to Change:</b> In today's fast-paced business environment, requirements change frequently. Agile embraces change and allows teams to pivot quickly based on market feedback or stakeholder input.<br/><br/>
2. <b>Faster Time to Market:</b> Agile delivers working software in short iterations (typically 2-4 weeks). This means valuable features reach users sooner, providing competitive advantage and earlier ROI.<br/><br/>
3. <b>Improved Customer Satisfaction:</b> Continuous customer involvement ensures the final product aligns with actual needs rather than initial assumptions. Customers see progress regularly and can provide feedback.<br/><br/>
4. <b>Higher Quality:</b> Continuous testing, integration, and code reviews in each sprint catch defects early when they are cheaper to fix. The definition of done ensures quality standards are met.<br/><br/>
5. <b>Better Risk Management:</b> Short iterations mean risks are identified and mitigated early. Technical and business risks surface quickly rather than at the end of a long development cycle.<br/><br/>
6. <b>Transparency and Visibility:</b> Daily stand-ups, sprint reviews, and burndown charts provide clear visibility into project progress. Stakeholders always know the project status.<br/><br/>
7. <b>Team Empowerment:</b> Self-organizing teams are more motivated and productive. Team members have autonomy to decide how to best accomplish their work.<br/><br/>
8. <b>Reduced Waste:</b> Agile focuses on delivering the most valuable features first. If the project needs to be scaled back, the most important functionality is already built.<br/><br/>
9. <b>Continuous Improvement:</b> Sprint retrospectives create a culture of learning and improvement. Teams regularly reflect on what went well and what can be improved.<br/><br/>
10. <b>Cost Control:</b> By delivering incrementally, organizations can stop development when sufficient value has been delivered, avoiding unnecessary spending on low-priority features.""",
            },
            {
                "num": "10",
                "question": "How can you transform ER Diagram into relation? Explain with your own suitable example.",
                "marks": "10",
                "answer": """<b>Transforming ER Diagram into Relational Model:</b><br/>
The process of converting an Entity-Relationship (ER) diagram into a set of relations (tables) is called logical database design. The following rules guide this transformation:<br/><br/>
<b>Rule 1: Strong Entity to Relation</b><br/>
Each strong entity type becomes a relation (table). The attributes of the entity become columns of the table. The primary key of the entity becomes the primary key of the table.<br/><br/>
<b>Rule 2: Weak Entity to Relation</b><br/>
A weak entity becomes a relation that includes a foreign key referencing the primary key of the identifying strong entity. The primary key of the weak entity is a composite key consisting of the partial key of the weak entity plus the foreign key.<br/><br/>
<b>Rule 3: 1:1 Relationship</b><br/>
Add the primary key of one entity as a foreign key in the other entity's relation. It is better to add the foreign key to the entity with total participation.<br/><br/>
<b>Rule 4: 1:N Relationship</b><br/>
Add the primary key of the entity on the "1" side as a foreign key in the relation of the entity on the "N" side.<br/><br/>
<b>Rule 5: M:N Relationship</b><br/>
Create a new relation (junction/associative entity) that includes the primary keys of both participating entities as foreign keys. These foreign keys together form the primary key of the new relation. Any attributes of the relationship also become columns.<br/><br/>
<b>Rule 6: Multivalued Attribute</b><br/>
Create a separate relation for the multivalued attribute. The relation includes the multivalued attribute and a foreign key referencing the primary key of the original entity.<br/><br/>
<b>Example — University Database:</b><br/>
Consider an ER Diagram with:<br/>
• <b>Entity: STUDENT</b> (student_id, name, email, phone)<br/>
• <b>Entity: COURSE</b> (course_id, title, credits)<br/>
• <b>Entity: DEPARTMENT</b> (dept_id, dept_name)<br/>
• <b>Relationship: ENROLLS</b> (M:N between STUDENT and COURSE, attribute: grade)<br/>
• <b>Relationship: BELONGS_TO</b> (N:1 between STUDENT and DEPARTMENT)<br/><br/>
<b>Transformed Relations:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Relation</b></td><td><b>Attributes</b></td><td><b>Keys</b></td></tr>
<tr><td>STUDENT</td><td>student_id, name, email, phone, dept_id</td><td>PK: student_id, FK: dept_id</td></tr>
<tr><td>COURSE</td><td>course_id, title, credits</td><td>PK: course_id</td></tr>
<tr><td>DEPARTMENT</td><td>dept_id, dept_name</td><td>PK: dept_id</td></tr>
<tr><td>ENROLLS</td><td>student_id, course_id, grade</td><td>PK: (student_id, course_id), FK: student_id, course_id</td></tr>
</table><br/><br/>
<b>Explanation:</b><br/>
• STUDENT and COURSE are strong entities, so they become separate tables.<br/>
• DEPARTMENT is also a strong entity with its own table.<br/>
• The BELONGS_TO relationship (N:1) is handled by adding dept_id as a foreign key in the STUDENT table.<br/>
• The ENROLLS relationship (M:N) requires a separate ENROLLS table containing both primary keys as foreign keys, plus the relationship attribute grade.<br/>
• The composite primary key of ENROLLS ensures a student can enroll in multiple courses and a course can have multiple students.""",
            },
            {
                "num": "11",
                "question": "Why is the project management important? Describe the concept of integrated CASE tools with its applications.",
                "marks": "3+7",
                "answer": """<b>Importance of Project Management:</b><br/>
1. <b>Achieving Objectives:</b> Project management ensures that projects are completed on time, within budget, and according to specifications. Without proper management, projects often fail to meet their goals.<br/>
2. <b>Resource Optimization:</b> Effective project management allocates resources (human, financial, technical) efficiently, preventing waste and ensuring maximum productivity.<br/>
3. <b>Risk Mitigation:</b> Project management identifies potential risks early and develops strategies to minimize their impact, reducing the likelihood of project failure.<br/>
4. <b>Quality Control:</b> Structured project management includes quality checkpoints and standards, ensuring deliverables meet stakeholder expectations.<br/>
5. <b>Stakeholder Satisfaction:</b> Clear communication and expectation management keep stakeholders informed and satisfied throughout the project lifecycle.<br/>
6. <b>Scope Management:</b> Prevents scope creep by clearly defining what is included and excluded, and managing change requests formally.<br/>
7. <b>Competitive Advantage:</b> Organizations with strong project management capabilities can deliver products faster and more reliably than competitors.<br/><br/>
<b>Integrated CASE Tools (Computer-Aided Software Engineering):</b><br/>
Integrated CASE tools (I-CASE) are software applications that provide comprehensive support for the entire software development lifecycle (SDLC) within a single, unified environment. Unlike upper CASE (front-end) tools that focus on analysis and design, or lower CASE (back-end) tools that focus on implementation and testing, I-CASE covers all phases from requirements gathering to maintenance.<br/><br/>
<b>Concept of Integrated CASE Tools:</b><br/>
I-CASE tools provide a seamless environment where:<br/>
• Data entered in one phase is automatically available in subsequent phases<br/>
• Changes in one diagram or specification are propagated throughout related artifacts<br/>
• A central repository stores all project information (encyclopedia/dictionary)<br/>
• Multiple team members can collaborate on the same project simultaneously<br/>
• Traceability is maintained from requirements through design to code and testing<br/><br/>
<b>Applications of Integrated CASE Tools:</b><br/>
1. <b>Requirements Management:</b> Tools like IBM Rational RequisitePro and DOORS help capture, organize, and trace requirements throughout the development process.<br/>
2. <b>Modeling and Design:</b> Tools like Enterprise Architect, Visual Paradigm, and StarUML support UML modeling (use case, class, sequence, activity diagrams) and automatically generate code skeletons.<br/>
3. <b>Code Generation and Reverse Engineering:</b> I-CASE tools can generate source code from design models and reverse-engineer code back into design diagrams, maintaining synchronization.<br/>
4. <b>Project Planning and Tracking:</b> Integrated Gantt charts, resource allocation, and progress tracking help managers monitor project health.<br/>
5. <b>Testing Support:</b> Test case generation, test execution, defect tracking, and coverage analysis are integrated within the same environment.<br/>
6. <b>Version Control and Configuration Management:</b> Built-in version control manages changes to all project artifacts, enabling rollback and audit trails.<br/>
7. <b>Documentation:</b> Automatic generation of technical documentation, user manuals, and reports from the central repository.<br/>
8. <b>Database Design:</b> Tools like ERwin and PowerDesigner support ER modeling and automatic generation of database schemas for multiple DBMS platforms.<br/><br/>
<b>Examples of Integrated CASE Tools:</b><br/>
• <b>IBM Rational Suite:</b> Comprehensive toolset covering requirements, modeling, development, and testing.<br/>
• <b>Microsoft Visual Studio:</b> IDE with integrated design, coding, debugging, and deployment capabilities.<br/>
• <b>Oracle JDeveloper:</b> Complete development environment for Java and Oracle applications.<br/>
• <b>Sparx Systems Enterprise Architect:</b> Full lifecycle modeling tool supporting UML, BPMN, and SysML.""",
            },
        ]
    }
]

generate_answer_sheet("CACS203", "system-analysis-design", "System Analysis & Design", 2020, "semester-3", CACS203_2020)
