#!/usr/bin/env python3
"""Generate answer sheet for CACS253 Software Engineering 2019."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS253_2019 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What are the attributes of good software? What are the key challenges that software engineering faces during software development? Explain.",
                "marks": "5",
                "answer": """<b>Attributes of Good Software:</b><br/>
<b>1. Maintainability:</b> Software should be written so that it can evolve to meet changing customer needs. Clean code, documentation, and modular design help.<br/>
<b>2. Dependability:</b> Software must be reliable, secure, and safe. It should not cause physical or economic damage in case of failure.<br/>
<b>3. Efficiency:</b> Software should not make wasteful use of system resources such as memory and processor cycles.<br/>
<b>4. Usability:</b> Software must be easy to use for the intended users. Good UI/UX design, appropriate documentation, and intuitive workflows are essential.<br/>
<b>5. Portability:</b> Software should be able to run on different platforms and environments with minimal changes.<br/><br/>
<b>Key Challenges in Software Engineering:</b><br/>
<b>1. Changing Requirements:</b> Requirements often change during development, leading to rework and schedule slips.<br/>
<b>2. Increasing Complexity:</b> Modern systems are large, distributed, and integrated with legacy systems.<br/>
<b>3. Time and Cost Constraints:</b> Pressure to deliver quickly while maintaining quality.<br/>
<b>4. Quality Assurance:</b> Ensuring the software is bug-free, secure, and performant across diverse environments.<br/>
<b>5. Legacy System Integration:</b> Maintaining and integrating with older systems while adopting new technologies.<br/>
<b>6. Security Threats:</b> Protecting against cyber attacks, data breaches, and ensuring privacy compliance.<br/>
<b>7. Team Coordination:</b> Managing distributed teams, communication gaps, and knowledge silos.<br/>
<b>8. Technology Evolution:</b> Keeping up with rapidly changing frameworks, languages, and platforms.""",
            },
            {
                "num": "3",
                "question": "What is software process model? List the types of software model. Explain agile methods and their principles.",
                "marks": "5",
                "answer": """<b>Software Process Model:</b><br/>
A software process model is a simplified representation of a software process. It defines the workflow, activities, and phases involved in software development from conception to retirement. It provides structure and discipline to the development effort.<br/><br/>
<b>Types of Software Process Models:</b><br/>
1. <b>Waterfall Model</b> — Linear sequential approach.<br/>
2. <b>Incremental Model</b> — Build the system in increments.<br/>
3. <b>Iterative Model</b> — Repeat cycles of design, build, test.<br/>
4. <b>Spiral Model</b> — Risk-driven iterative model.<br/>
5. <b>V-Model</b> — Verification and validation parallel phases.<br/>
6. <b>Agile Model</b> — Flexible, iterative, customer-centric.<br/>
7. <b>Prototyping Model</b> — Build prototypes to clarify requirements.<br/>
8. <b>Rad Model (Rapid Application Development)</b> — Fast development with user involvement.<br/><br/>
<b>Agile Methods and Principles:</b><br/>
Agile is an iterative approach to software delivery that builds solutions incrementally from the start of the project, instead of trying to deliver it all at once near the end.<br/><br/>
<b>Key Agile Methods:</b><br/>
• <b>Scrum:</b> Uses sprints (2-4 weeks), daily stand-ups, product backlog, and Scrum roles (Product Owner, Scrum Master, Team).<br/>
• <b>Extreme Programming (XP):</b> Emphasizes pair programming, continuous integration, test-driven development, and frequent releases.<br/>
• <b>Kanban:</b> Visual workflow management using boards and WIP limits.<br/><br/>
<b>Twelve Principles of Agile Manifesto:</b><br/>
1. Highest priority is to satisfy the customer through early and continuous delivery.<br/>
2. Welcome changing requirements, even late in development.<br/>
3. Deliver working software frequently (weeks rather than months).<br/>
4. Business people and developers must work together daily.<br/>
5. Build projects around motivated individuals; give them the environment and support they need.<br/>
6. Face-to-face conversation is the most efficient method of conveying information.<br/>
7. Working software is the primary measure of progress.<br/>
8. Agile processes promote sustainable development.<br/>
9. Continuous attention to technical excellence and good design enhances agility.<br/>
10. Simplicity — the art of maximizing the amount of work not done — is essential.<br/>
11. The best architectures, requirements, and designs emerge from self-organizing teams.<br/>
12. At regular intervals, the team reflects on how to become more effective and adjusts accordingly.""",
            },
            {
                "num": "4",
                "question": "What are requirements? Explain functional, non-functional, domain and organizational requirements.",
                "marks": "5",
                "answer": """<b>Requirements:</b><br/>
Requirements are descriptions of what a software system should do and the constraints under which it must operate. They form the basis for software design, implementation, testing, and acceptance.<br/><br/>
<b>Types of Requirements:</b><br/><br/>
<b>1. Functional Requirements:</b><br/>
These describe the specific services the system should provide, how it should react to particular inputs, and what it should not do.<br/>
• Example: "The system shall allow users to search for products by name, category, or price range."<br/>
• Example: "The system shall generate an invoice after each purchase."<br/><br/>
<b>2. Non-Functional Requirements:</b><br/>
These define system qualities, constraints, and performance criteria rather than specific behaviors.<br/>
• <b>Performance:</b> "The system shall process 1000 transactions per second."<br/>
• <b>Security:</b> "All user passwords must be encrypted using AES-256."<br/>
• <b>Reliability:</b> "System uptime must be 99.9%."<br/>
• <b>Usability:</b> "New users shall complete onboarding in under 5 minutes."<br/><br/>
<b>3. Domain Requirements:</b><br/>
These are requirements that come from the application domain of the system. They reflect characteristics of that domain and may be functional or non-functional.<br/>
• Example (Healthcare): "The system must comply with HIPAA regulations for patient data."<br/>
• Example (Banking): "All transactions must support double-entry bookkeeping."<br/><br/>
<b>4. Organizational Requirements:</b><br/>
These are broad system requirements derived from policies and procedures in the customer's and developer's organizations.<br/>
• <b>Operational:</b> "The system must run on the organization's existing Linux servers."<br/>
• <b>Development:</b> "All code must follow the company's Java coding standards."<br/>
• <b>Environmental:</b> "The system must use the organization's single sign-on (SSO) provider."<br/>
• <b>Regulatory:</b> "The software must comply with GDPR for EU users."<br/><br/>
<b>Summary:</b> Functional requirements define what the system does; non-functional define how well; domain requirements reflect industry-specific rules; organizational requirements reflect company policies.""",
            },
            {
                "num": "5",
                "question": "What is modularization? Differentiate cohesion and coupling.",
                "marks": "5",
                "answer": """<b>Modularization:</b><br/>
Modularization is the process of dividing a software system into separate, independent modules (components or subsystems). Each module is a self-contained unit that performs a specific function and interacts with other modules through well-defined interfaces. The goals are to reduce complexity, improve maintainability, enable parallel development, and promote code reuse.<br/><br/>
<b>Difference between Cohesion and Coupling:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Aspect</b></td><td><b>Cohesion</b></td><td><b>Coupling</b></td></tr>
<tr><td>Definition</td><td>Measures how closely related and focused the responsibilities of a single module are.</td><td>Measures the degree of interdependence between different modules.</td></tr>
<tr><td>Goal</td><td>High cohesion is desired (each module does one thing well).</td><td>Low coupling is desired (modules are as independent as possible).</td></tr>
<tr><td>Types</td><td>Coincidental, Logical, Temporal, Procedural, Communicational, Sequential, Functional.</td><td>Content, Common, External, Control, Stamp, Data.</td></tr>
<tr><td>Effect on maintenance</td><td>High cohesion makes a module easier to understand, modify, and test.</td><td>Low coupling reduces ripple effects when one module is changed.</td></tr>
<tr><td>Example</td><td>A module that calculates tax (functional cohesion) is better than one that mixes tax, reporting, and email (coincidental).</td><td>Two modules sharing only necessary data (data coupling) is better than one controlling another's logic (control coupling).</td></tr>
</table><br/>
<b>Conclusion:</b> Good software design aims for <b>high cohesion and low coupling</b> to create maintainable, scalable systems.""",
            },
            {
                "num": "6",
                "question": "Why is UI design important? How is UI design visualized? Discuss.",
                "marks": "5",
                "answer": """<b>Importance of UI Design:</b><br/>
<b>1. First Impression:</b> The UI is the first thing users see. A well-designed UI creates trust and encourages users to engage with the system.<br/>
<b>2. Usability:</b> Good UI design makes software easy to learn and use, reducing training time and support costs.<br/>
<b>3. Productivity:</b> Intuitive layouts and workflows help users complete tasks faster and with fewer errors.<br/>
<b>4. Accessibility:</b> Proper UI design ensures the software is usable by people with disabilities (screen readers, keyboard navigation, color contrast).<br/>
<b>5. Competitive Advantage:</b> A polished UI differentiates the product in the market and increases customer satisfaction.<br/>
<b>6. Reduced Errors:</b> Clear labels, feedback, and validation prevent user mistakes and data entry errors.<br/><br/>
<b>How UI Design is Visualized:</b><br/>
<b>1. Wireframes:</b> Low-fidelity sketches that show layout, content placement, and navigation without color or graphics. Tools: Balsamiq, Sketch.<br/>
<b>2. Mockups:</b> High-fidelity static designs that include colors, typography, and imagery. They show the final look and feel.<br/>
<b>3. Prototypes:</b> Interactive simulations of the UI that allow stakeholders to click through screens and experience the flow. Tools: Figma, Adobe XD.<br/>
<b>4. Storyboards:</b> Visual narratives showing how users interact with the system in real-world scenarios.<br/>
<b>5. User Flow Diagrams:</b> Flowcharts that map the steps a user takes to complete a task, identifying decision points and screens.<br/>
<b>6. Design Systems:</b> Collections of reusable components (buttons, forms, menus) with defined standards for consistency across the application.<br/><br/>
<b>UI Design Principles:</b><br/>
• <b>Consistency:</b> Uniform design language throughout the application.<br/>
• <b>Feedback:</b> Inform users about actions (loaders, success messages).<br/>
• <b>Simplicity:</b> Reduce clutter; focus on essential elements.<br/>
• <b>Flexibility:</b> Accommodate both novice and expert users (shortcuts).<br/>
• <b>Recovery:</b> Allow undo and error correction.""",
            },
            {
                "num": "7",
                "question": "Why is software testing considered as major component in SDLC? Explain software testing.",
                "marks": "5",
                "answer": """<b>Why Software Testing is a Major Component in SDLC:</b><br/>
<b>1. Quality Assurance:</b> Testing ensures the software meets specified requirements and performs as expected.<br/>
<b>2. Bug Detection:</b> Identifies defects early, reducing the cost of fixing them later in the lifecycle.<br/>
<b>3. Risk Mitigation:</b> Prevents failures in production that could cause financial loss, data breaches, or safety hazards.<br/>
<b>4. Customer Satisfaction:</b> Delivering reliable software builds trust and meets user expectations.<br/>
<b>5. Validation and Verification:</b> Confirms that the product is built correctly (verification) and is the right product (validation).<br/>
<b>6. Compliance:</b> Ensures adherence to regulatory and industry standards.<br/><br/>
<b>Explanation of Software Testing:</b><br/>
Software testing is the process of evaluating a software application to find differences between given input and expected output. It includes manual and automated activities to verify and validate software.<br/><br/>
<b>Levels of Testing:</b><br/>
<b>1. Unit Testing:</b> Tests individual components or functions in isolation.<br/>
<b>2. Integration Testing:</b> Tests combined parts of the application to ensure they work together.<br/>
<b>3. System Testing:</b> Tests the complete integrated system against requirements.<br/>
<b>4. Acceptance Testing:</b> Validates the software against business needs; includes UAT (User Acceptance Testing).<br/><br/>
<b>Types of Testing:</b><br/>
• <b>Functional Testing:</b> Black-box testing of features (unit, integration, system).<br/>
• <b>Non-Functional Testing:</b> Performance, security, usability, compatibility.<br/>
• <b>Regression Testing:</b> Ensures new changes do not break existing functionality.<br/>
• <b>Smoke Testing:</b> Basic checks to verify the build is stable enough for further testing.<br/><br/>
<b>Testing Process:</b><br/>
1. Test Planning → 2. Test Design → 3. Test Execution → 4. Defect Reporting → 5. Test Closure.<br/><br/>
<b>Conclusion:</b> Testing is integral to SDLC because it directly impacts software quality, reliability, and user satisfaction.""",
            },
            {
                "num": "8",
                "question": "What is project management? Why is it important? Explain.",
                "marks": "5",
                "answer": """<b>Project Management:</b><br/>
Project management is the application of knowledge, skills, tools, and techniques to project activities to meet project requirements. In software engineering, it involves planning, organizing, staffing, directing, and controlling the development of software systems within constraints of time, cost, scope, and quality.<br/><br/>
<b>Why Project Management is Important:</b><br/>
<b>1. On-Time Delivery:</b> Ensures projects are completed within deadlines through scheduling (Gantt charts, PERT, CPM).<br/>
<b>2. Budget Control:</b> Manages costs and resources to prevent overruns.<br/>
<b>3. Scope Management:</b> Defines and controls what is included in the project, preventing scope creep.<br/>
<b>4. Quality Assurance:</b> Integrates quality standards and testing into the development process.<br/>
<b>5. Risk Management:</b> Identifies potential risks early and develops mitigation strategies.<br/>
<b>6. Resource Optimization:</b> Allocates human, technical, and financial resources efficiently.<br/>
<b>7. Stakeholder Communication:</b> Maintains transparency and alignment between clients, developers, and management.<br/>
<b>8. Team Coordination:</b> Facilitates collaboration, resolves conflicts, and keeps the team motivated.<br/><br/>
<b>Key Knowledge Areas (PMBOK):</b><br/>
• Integration Management<br/>
• Scope Management<br/>
• Time Management<br/>
• Cost Management<br/>
• Quality Management<br/>
• Human Resource Management<br/>
• Communications Management<br/>
• Risk Management<br/>
• Procurement Management<br/>
• Stakeholder Management<br/><br/>
<b>Conclusion:</b> Without effective project management, software projects are likely to fail due to missed deadlines, budget overruns, poor quality, and unmet user needs.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Explain different software projects and their characteristics.",
                "marks": "10",
                "answer": """<b>Types of Software Projects and Their Characteristics:</b><br/><br/>
<b>1. Web Development Projects:</b><br/>
• Delivered via browsers; responsive design required.<br/>
• Technologies: HTML, CSS, JavaScript, React, Angular, Node.js.<br/>
• Characteristics: Rapid deployment, continuous updates, SEO considerations, cross-browser compatibility.<br/>
• Examples: E-commerce sites, blogs, SaaS platforms.<br/><br/>
<b>2. Mobile Application Projects:</b><br/>
• Target iOS and/or Android platforms.<br/>
• Technologies: Swift, Kotlin, Flutter, React Native.<br/>
• Characteristics: Touch-based UI, offline capability, push notifications, app store compliance, device fragmentation.<br/>
• Examples: Fitness trackers, food delivery apps, mobile banking.<br/><br/>
<b>3. Embedded Systems Projects:</b><br/>
• Software runs on dedicated hardware with limited resources.<br/>
• Technologies: C, C++, Assembly, RTOS.<br/>
• Characteristics: Real-time constraints, memory optimization, hardware interfacing, safety-critical requirements.<br/>
• Examples: Automotive ECU, medical devices, IoT sensors.<br/><br/>
<b>4. Enterprise Software Projects:</b><br/>
• Large-scale systems for business operations.<br/>
• Technologies: Java, .NET, Oracle, SAP.<br/>
• Characteristics: High security, scalability, integration with legacy systems, multi-tenancy, regulatory compliance.<br/>
• Examples: ERP, CRM, HR management systems.<br/><br/>
<b>5. Data Science / AI Projects:</b><br/>
• Focus on data processing, machine learning, and predictive analytics.<br/>
• Technologies: Python, R, TensorFlow, PyTorch, SQL.<br/>
• Characteristics: Large data volumes, experimentation-driven, model training and validation, deployment challenges (MLOps).<br/>
• Examples: Recommendation engines, fraud detection, chatbots.<br/><br/>
<b>6. Game Development Projects:</b><br/>
• Highly interactive, graphics-intensive applications.<br/>
• Technologies: Unity, Unreal Engine, C#, C++.<br/>
• Characteristics: Real-time rendering, physics simulation, multiplayer networking, asset management.<br/>
• Examples: Mobile games, AAA console games, VR experiences.<br/><br/>
<b>7. Open Source Projects:</b><br/>
• Developed collaboratively by a community.<br/>
• Characteristics: Transparent development, public codebase, community governance, diverse contributor base.<br/>
• Examples: Linux, Apache, Mozilla Firefox.<br/><br/>
<b>Comparison Table:</b><br/>
<table border='1' cellpadding='4'>
<tr><td>Type</td><td>Team Size</td><td>Timeline</td><td>Risk Level</td><td>Key Challenge</td></tr>
<tr><td>Web</td><td>Small-Medium</td><td>Short-Medium</td><td>Medium</td><td>Browser compatibility</td></tr>
<tr><td>Mobile</td><td>Small-Medium</td><td>Short</td><td>Medium</td><td>Device fragmentation</td></tr>
<tr><td>Embedded</td><td>Small</td><td>Medium-Long</td><td>High</td><td>Resource constraints</td></tr>
<tr><td>Enterprise</td><td>Large</td><td>Long</td><td>High</td><td>Integration complexity</td></tr>
<tr><td>Data/AI</td><td>Medium</td><td>Medium</td><td>Medium</td><td>Data quality & model accuracy</td></tr>
<tr><td>Game</td><td>Medium-Large</td><td>Long</td><td>High</td><td>Performance optimization</td></tr>
</table>""",
            },
            {
                "num": "10",
                "question": "Explain Black box testing and White box testing.",
                "marks": "10",
                "answer": """<b>Black Box Testing:</b><br/>
Black box testing treats the software as a "black box" where the internal structure/design/implementation is not known to the tester. Tests are based on requirements and specifications.<br/><br/>
<b>Characteristics:</b><br/>
• Focuses on inputs and expected outputs.<br/>
• No knowledge of internal code required.<br/>
• Tests functional and non-functional requirements.<br/>
• Performed by QA teams and end-users.<br/><br/>
<b>Techniques:</b><br/>
• <b>Equivalence Partitioning:</b> Divide input data into valid and invalid partitions.<br/>
• <b>Boundary Value Analysis:</b> Test values at boundaries (min, max, just inside/outside).<br/>
• <b>Decision Table Testing:</b> Map business rules to test cases.<br/>
• <b>State Transition Testing:</b> Test different states of the application.<br/>
• <b>Use Case Testing:</b> Validate end-to-end user scenarios.<br/><br/>
<b>Advantages:</b> Unbiased testing, simulates real user behavior, no programming knowledge needed.<br/>
<b>Disadvantages:</b> Cannot test all paths, difficult to identify root cause of failures.<br/><br/>
<b>White Box Testing:</b><br/>
White box testing examines the internal structure, logic, and code of the software. Testers need programming knowledge and access to source code.<br/><br/>
<b>Characteristics:</b><br/>
• Focuses on code coverage (statements, branches, paths).<br/>
• Validates internal security, data flow, and control flow.<br/>
• Performed by developers.<br/><br/>
<b>Techniques:</b><br/>
• <b>Statement Coverage:</b> Every statement is executed at least once.<br/>
• <b>Branch Coverage:</b> Every decision branch (true/false) is tested.<br/>
• <b>Path Coverage:</b> All possible paths through the code are tested.<br/>
• <b>Condition Coverage:</b> Each boolean sub-expression is evaluated to true and false.<br/>
• <b>Loop Testing:</b> Test loops for zero, one, many, and maximum iterations.<br/><br/>
<b>Advantages:</b> Thorough testing of internal logic, early bug detection, optimization opportunities.<br/>
<b>Disadvantages:</b> Time-consuming, expensive, requires skilled testers, may miss missing features.<br/><br/>
<b>Comparison:</b><br/>
<table border='1' cellpadding='4'>
<tr><td>Aspect</td><td>Black Box</td><td>White Box</td></tr>
<tr><td>Knowledge of code</td><td>Not required</td><td>Required</td></tr>
<tr><td>Focus</td><td>External behavior</td><td>Internal logic</td></tr>
<tr><td>Testers</td><td>QA / End users</td><td>Developers</td></tr>
<tr><td>Coverage metric</td><td>Requirements coverage</td><td>Code coverage</td></tr>
<tr><td>When performed</td><td>System / Acceptance testing</td><td>Unit / Integration testing</td></tr>
</table><br/>
<b>Conclusion:</b> Both techniques are complementary. Black box ensures the system meets user needs; white box ensures the code is robust and free of internal defects.""",
            },
            {
                "num": "11",
                "question": "Explain ISO 9001 quality standards.",
                "marks": "10",
                "answer": """<b>ISO 9001 Quality Standards:</b><br/>
ISO 9001 is an international standard that specifies requirements for a Quality Management System (QMS). It is part of the ISO 9000 family of standards and is the only standard in the family that can be certified. Organizations use ISO 9001 to demonstrate their ability to consistently provide products and services that meet customer and regulatory requirements.<br/><br/>
<b>Key Principles of ISO 9001:</b><br/>
<b>1. Customer Focus:</b> Understand current and future customer needs, meet customer requirements, and strive to exceed expectations.<br/>
<b>2. Leadership:</b> Establish unity of purpose and direction. Leaders create an environment where people are engaged in achieving quality objectives.<br/>
<b>3. Engagement of People:</b> Competent, empowered, and engaged people at all levels are essential to enhance the organization's capability to create value.<br/>
<b>4. Process Approach:</b> Consistent and predictable results are achieved more effectively when activities are understood and managed as interrelated processes.<br/>
<b>5. Improvement:</b> Ongoing improvement of the organization's overall performance should be a permanent objective.<br/>
<b>6. Evidence-Based Decision Making:</b> Decisions based on analysis and evaluation of data are more likely to produce desired results.<br/>
<b>7. Relationship Management:</b> An organization and its external providers (suppliers, partners) are interdependent, and a mutually beneficial relationship enhances the ability of both to create value.<br/><br/>
<b>ISO 9001:2015 Structure (High-Level Structure):</b><br/>
• <b>Clause 4:</b> Context of the Organization<br/>
• <b>Clause 5:</b> Leadership<br/>
• <b>Clause 6:</b> Planning (including risk-based thinking)<br/>
• <b>Clause 7:</b> Support (resources, competence, awareness, communication)<br/>
• <b>Clause 8:</b> Operation (process execution)<br/>
• <b>Clause 9:</b> Performance Evaluation (monitoring, measurement, analysis, internal audit)<br/>
• <b>Clause 10:</b> Improvement (nonconformity, corrective action, continual improvement)<br/><br/>
<b>Benefits of ISO 9001 Certification:</b><br/>
• Improved product and service quality.<br/>
• Increased customer satisfaction and trust.<br/>
• Better process efficiency and waste reduction.<br/>
• Enhanced market credibility and competitive advantage.<br/>
• Foundation for other standards (ISO 27001, ISO 14001).<br/><br/>
<b>ISO 9001 in Software Engineering:</b><br/>
Software companies adopt ISO 9001 to formalize their development processes, ensure traceability of requirements, manage changes, and maintain documentation. It complements agile practices by adding structure to quality assurance and continuous improvement.""",
            },
        ]
    }
]

if __name__ == "__main__":
    print("Generating CACS253 Software Engineering 2019 answer sheet...")
    generate_answer_sheet("CACS253", "software-engineering", "Software Engineering", 2019, "semester-4", CACS253_2019)
    print("✅ CACS253 2019 answer sheet generated!")
