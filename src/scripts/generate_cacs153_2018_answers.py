#!/usr/bin/env python3
"""Generate answer sheet for CACS153 2018 English II."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

QUESTIONS_DATA = [
    {
        "title": "Group A",
        "instruction": "Attempt all the questions. [10×1 = 10]",
        "questions": [
            {
                "num": "13",
                "question": "The world of science fiction is a world that ………..",
                "marks": "1",
                "answer": """<b>Correct Answer: b) could be</b><br/>
Science fiction is a genre of speculative fiction that deals with imaginative and futuristic concepts such as advanced science and technology, space exploration, time travel, and extraterrestrial life. Unlike fantasy, science fiction is grounded in scientific principles and represents worlds that <b>could potentially exist</b> based on current or extrapolated scientific knowledge.""",
            },
            {
                "num": "14",
                "question": "Which of the following words is an argument indicator word?",
                "marks": "1",
                "answer": """<b>Correct Answer: b) therefore</b><br/>
<b>Therefore</b> is a conclusion indicator word that signals the logical consequence or conclusion of an argument. Other argument indicator words include: because, since, thus, hence, consequently, so, as a result, it follows that. Words like "although," "despite," and "moreover" serve different discourse functions (contrast, concession, and addition respectively).""",
            },
            {
                "num": "15",
                "question": "Which of the following categories is not used in a business letter?",
                "marks": "1",
                "answer": """<b>Correct Answer: d) collection of data</b><br/>
Business letters commonly include categories such as enquiry, reply, confirmation, complaint, order, claim, and adjustment. "Collection of data" is not a standard category of business letter; it describes a research activity rather than a communicative purpose in business correspondence.""",
            },
            {
                "num": "16",
                "question": "One should not use ……….. in a fax message",
                "marks": "1",
                "answer": """<b>Correct Answer: a) salutation</b><br/>
Fax messages are typically brief, pre-formatted communications. A formal <b>salutation</b> (like "Dear Sir/Madam") is generally not used in fax cover sheets because faxes are direct, concise communications that include a letterhead, fax number, recipient details, and a brief message. The format prioritizes efficiency over formal epistolary conventions.""",
            },
            {
                "num": "17",
                "question": "The introductory part of a memo explains ………..",
                "marks": "1",
                "answer": """<b>Correct Answer: b) reasons for writing</b><br/>
A memorandum (memo) typically has three parts: (1) Introduction — states the <b>purpose or reason for writing</b>, (2) Body — presents facts and details, and (3) Conclusion/Recommendation — specifies actions to be taken or deadlines. The introduction sets the context and explains why the memo is being sent.""",
            },
            {
                "num": "18",
                "question": "A special report is written ………….",
                "marks": "1",
                "answer": """<b>Correct Answer: c) regarding an accident</b><br/>
A <b>special report</b> is prepared for unusual, one-time events or specific situations that require detailed investigation and documentation, such as accidents, breaches of policy, or major incidents. Regular reports (progress reports, sales reports) are routine, whereas special reports address exceptional circumstances.""",
            },
            {
                "num": "19",
                "question": "Main heading of minutes includes ………..",
                "marks": "1",
                "answer": """<b>Correct Answer: d) place, day, date, and the time of the meeting held</b><br/>
The main heading of meeting minutes includes essential logistical information: the <b>place, day, date, and time</b> of the meeting. Other elements like apologies for absence, minutes of the last meeting, and matters discussed appear in the body of the minutes, not the main heading.""",
            },
            {
                "num": "20",
                "question": "An impromptu presentation is …………..",
                "marks": "1",
                "answer": """<b>Correct Answer: b) given on the spot without prior preparation</b><br/>
An <b>impromptu presentation</b> is delivered spontaneously without advance preparation or rehearsal. It contrasts with manuscript presentations (reading from text), memorized presentations, and extemporaneous presentations (prepared but not memorized). Impromptu speaking tests the speaker's ability to organize thoughts quickly and communicate clearly under pressure.""",
            },
            {
                "num": "21",
                "question": "In the story \"The Land Ironclads\", the young lieutenant lay beside the ………..",
                "marks": "1",
                "answer": """<b>Correct Answer: b) war correspondent</b><br/>
In H.G. Wells' short story <b>"The Land Ironclads,"</b> the young lieutenant lies beside the <b>war correspondent</b>. The story contrasts the lieutenant's romantic, chivalric view of war with the correspondent's more pragmatic, modern perspective, ultimately showing how technology (the ironclads) renders traditional military values obsolete.""",
            },
            {
                "num": "22",
                "question": "An argument can have ……………",
                "marks": "1",
                "answer": """<b>Correct Answer: c) two or more reasons, each of which independently supporting the conclusion</b><br/>
An argument can be structured with multiple premises (reasons) that independently or jointly support a conclusion. This is known as a <b>convergent argument structure</b>, where each premise provides separate support for the conclusion. Arguments may also have linked premises (where premises work together) or single-premise arguments.""",
            },
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5 = 30]",
        "questions": [
            {
                "num": "23",
                "question": "How do you distinguish a science fiction from other kinds of fiction? Explain basing on the stories given in your textbook.",
                "marks": "5",
                "answer": """<b>Science Fiction vs. Other Fiction:</b><br/><br/>

Science fiction (SF) differs from other fiction genres in several key ways:<br/><br/>

1. <b>Scientific Basis:</b> SF is grounded in scientific principles, theories, or plausible technological advancement. Fantasy, by contrast, relies on magic and supernatural elements without scientific explanation.<br/><br/>

2. <b>Possibility:</b> SF deals with things that <b>could happen</b> based on current or projected science. As Isaac Asimov noted, "Science fiction is the branch of literature that deals with the response of human beings to changes in science and technology."<br/><br/>

3. <b>Settings:</b> SF often takes place in the future, on other planets, in alternate timelines, or in technologically altered societies. Stories like <b>"The Land Ironclads"</b> by H.G. Wells extrapolate military technology to show its devastating impact on traditional warfare.<br/><br/>

4. <b>Purpose:</b> SF often serves as social commentary, warning about the consequences of scientific hubris, overpopulation, or technological dependence. <b>"Billennium"</b> by J.G. Ballard explores overpopulation rather than war as humanity's greatest threat.<br/><br/>

5. <b>Character vs. Idea:</b> While mainstream fiction focuses primarily on character and relationships, SF gives equal weight to ideas, concepts, and "what if" scenarios. <b>"But Who Can Replace a Man?"</b> by Brian Aldiss uses robots to examine human uniqueness and purpose.<br/><br/>

<b>Conclusion:</b> Science fiction is uniquely positioned to explore the intersection of humanity and technology, making it both predictive and cautionary in ways that other fiction genres are not.""",
            },
            {
                "num": "24",
                "question": "What are the basic components of arguments? Explain with appropriate examples.",
                "marks": "5",
                "answer": """<b>Basic Components of Arguments:</b><br/><br/>

An argument consists of three essential components:<br/><br/>

1. <b>Premises (Reasons/Evidence):</b><br/>
Premises are statements that provide evidence, support, or reasons for accepting the conclusion. They are the foundation upon which the argument is built.<br/>
<i>Example:</i> "All humans are mortal." (Premise 1)<br/><br/>

2. <b>Conclusion:</b><br/>
The conclusion is the main claim or proposition that the argument seeks to establish. It is derived from or supported by the premises.<br/>
<i>Example:</i> "Therefore, Socrates is mortal." (Conclusion)<br/><br/>

3. <b>Inference (Logical Connection):</b><br/>
The inference is the reasoning process that links premises to the conclusion. It can be deductive (guarantees truth if premises are true) or inductive (makes conclusion probable).<br/><br/>

<b>Additional Elements:</b><br/>
• <b>Assumptions:</b> Unstated premises that the argument depends upon<br/>
• <b>Counter-arguments:</b> Opposing viewpoints that challenge the conclusion<br/>
• <b>Evidence:</b> Facts, statistics, examples, or expert opinions supporting premises<br/><br/>

<b>Complete Example:</b><br/>
Premise 1: Smoking causes lung cancer. (Fact)<br/>
Premise 2: John smokes heavily. (Fact)<br/>
Conclusion: Therefore, John is at high risk of lung cancer.<br/>
Assumption: The risk applies to all heavy smokers, including John.<br/><br/>

<b>Argument Indicators:</b><br/>
Conclusion indicators: therefore, thus, hence, so, consequently<br/>
Premise indicators: because, since, given that, as, for""",
            },
            {
                "num": "13",
                "question": "Lists are used in letters, e-mails, fax messages, and memos. What are the major objectives and advantages of using lists and bullets? Explain.",
                "marks": "5",
                "answer": """<b>Objectives and Advantages of Using Lists and Bullets:</b><br/><br/>

<b>Major Objectives:</b><br/>
1. <b>Organization:</b> To present information in a structured, logical format that is easy to follow.<br/>
2. <b>Emphasis:</b> To highlight key points and draw attention to important information.<br/>
3. <b>Clarity:</b> To break down complex information into digestible chunks.<br/>
4. <b>Efficiency:</b> To enable readers to quickly scan and locate relevant information.<br/><br/>

<b>Advantages:</b><br/>
1. <b>Readability:</b> Bullet points and numbered lists make documents more visually appealing and easier to read than dense paragraphs. Readers can grasp main points at a glance.<br/><br/>

2. <b>Comprehension:</b> Information presented in lists is better retained. Cognitive research shows that chunking information improves memory and understanding.<br/><br/>

3. <b>Priority Indication:</b> Numbered lists imply sequence or priority (e.g., steps in a procedure, ranking of items). Bulleted lists suggest items of equal importance.<br/><br/>

4. <b>Professional Appearance:</b> Well-formatted lists give business correspondence a polished, organized appearance that reflects positively on the sender.<br/><br/>

5. <b>Reduced Ambiguity:</b> Each point stands independently, reducing the chance that readers will miss important details buried in prose.<br/><br/>

6. <b>Action Orientation:</b> In memos and emails, lists make action items and responsibilities explicit. Example:<br/>
• <b>Action required by Friday:</b><br/>
&nbsp;&nbsp;– Submit budget proposal<br/>
&nbsp;&nbsp;– Review staff schedule<br/>
&nbsp;&nbsp;– Confirm meeting attendance<br/><br/>

<b>Best Practices:</b><br/>
• Keep each bullet point concise (1–2 lines)<br/>
• Use parallel structure (start each point with same grammatical form)<br/>
• Limit lists to 5–7 items when possible<br/>
• Use numbering for sequential items and bullets for non-sequential items""",
            },
            {
                "num": "20",
                "question": "In the story, \"But Who Can Replace A Man?\", the penner claims to have class three brain. Why do the tractors and the field minder leave the penner behind rejecting his request for help? Why does he become useless after crashing down to the ground? Explain.",
                "marks": "5",
                "answer": """<b>Analysis of \"But Who Can Replace A Man?\" by Brian Aldiss:</b><br/><br/>

<b>Why the Penner is Left Behind:</b><br/><br/>
In Aldiss' story, after humanity has apparently disappeared, machines attempt to organize themselves into a new society. The <b>penner</b> (a machine for penning animals) claims to have a <b>Class Three brain</b> — one of the higher intelligence classifications among the machines.<br/><br/>

However, the <b>tractors and field minder</b> leave the penner behind because:<br/>
1. <b>Class Hierarchy:</b> Despite his claim, the penner's Class Three brain is seen as inferior or irrelevant to the agricultural machines' mission. The tractors and field minder have their own functional priorities centered on farming operations.<br/>
2. <b>Lack of Utility:</b> The penner's specialized function (controlling animals) has no value in a world without animals or human direction. The other machines recognize that the penner cannot contribute to their survival or goals.<br/>
3. <b>Social Darwinism:</b> The machines replicate human behavior, including discrimination based on perceived capability and class. They reject the penner much as humans might reject someone deemed unproductive.<br/><br/>

<b>Why the Penner Becomes Useless After Crashing:</b><br/><br/>
After the penner crashes to the ground:<br/>
1. <b>Physical Damage:</b> The crash damages his mechanical body and possibly his brain circuits, rendering him physically incapable of movement or function.<br/>
2. <b>Loss of Purpose:</b> Even before the crash, the penner lacked purpose in the post-human world. The crash merely literalizes his obsolescence — a machine designed for a specific human-directed task becomes completely redundant when both the task and its creators vanish.<br/>
3. <b>Symbolism:</b> The penner's fate symbolizes the broader theme of the story: machines built to serve humans are fundamentally hollow without human purpose. Their class systems, ambitions, and conflicts are meaningless imitations of human society.<br/><br/>

<b>Thematic Significance:</b><br/>
Aldiss uses the penner's abandonment to critique both technological dependence and class discrimination. The machines' behavior reveals that intelligence and hierarchy without compassion or purpose lead to cruelty — a reflection of human society that the machines have unconsciously inherited.""",
            },
            {
                "num": "21",
                "question": "What are the guidelines to be followed while designing leaflets? Explain basing on the text prescribed in your course.",
                "marks": "5",
                "answer": """<b>Guidelines for Designing Effective Leaflets:</b><br/><br/>

1. <b>Clear Objective:</b><br/>
Define the purpose of the leaflet before designing. Whether it is to inform, persuade, advertise, or instruct, every element should serve this objective. A leaflet without a clear purpose confuses readers and fails to achieve results.<br/><br/>

2. <b>Attention-Grabbing Headline:</b><br/>
The headline should be concise, bold, and compelling. It must immediately communicate the main benefit or message to capture attention within seconds.<br/><br/>

3. <b>Readable Typography:</b><br/>
Use fonts that are clear and legible. Avoid using more than two or three font types. Maintain adequate font size (minimum 10–12pt for body text) and sufficient contrast between text and background.<br/><br/>

4. <b>Structured Layout:</b><br/>
Organize content logically with clear sections. Use headings, subheadings, bullet points, and white space effectively. A crowded leaflet overwhelms readers; generous white space improves readability and focus.<br/><br/>

5. <b>Visual Elements:</b><br/>
Include relevant images, graphics, charts, or icons that support the message. Visuals should be high-quality and appropriately placed. Color schemes should be consistent and aligned with the brand or purpose.<br/><br/>

6. <b>Concise Content:</b><br/>
Leaflets have limited space. Use short sentences and paragraphs. Focus on key points and benefits rather than exhaustive detail. Include a call-to-action (CTA) telling readers exactly what to do next.<br/><br/>

7. <b>Contact Information:</b><br/>
Always include accurate contact details: address, phone, email, website, and social media handles. Make this information easy to find, typically at the bottom or in a dedicated box.<br/><br/>

8. <b>Paper Quality and Finish:</b><br/>
The physical quality of the leaflet affects perception. Use appropriate paper weight and consider finishes (glossy, matte, laminated) that enhance durability and professional appearance.<br/><br/>

<b>Summary:</b> An effective leaflet combines clarity, visual appeal, and purposeful design to communicate its message quickly and persuasively to its target audience.""",
            },
            {
                "num": "22",
                "question": "What do you mean by brainstorming a topic? Explain with an appropriate example.",
                "marks": "5",
                "answer": """<b>Brainstorming a Topic:</b><br/><br/>

<b>Definition:</b><br/>
<b>Brainstorming</b> is a creative problem-solving and idea-generation technique where individuals or groups generate a large number of ideas spontaneously without immediate criticism or evaluation. The goal is to produce as many ideas as possible, encouraging free thinking, creativity, and diverse perspectives. Evaluation and selection occur only after the brainstorming session is complete.<br/><br/>

<b>Key Principles of Brainstorming:</b><br/>
1. <b>Defer Judgment:</b> No idea is criticized or dismissed during generation<br/>
2. <b>Encourage Wild Ideas:</b> Unconventional thinking often leads to breakthrough solutions<br/>
3. <b>Build on Others' Ideas:</b> Combine, improve, and expand on suggestions<br/>
4. <b>Stay Focused on the Topic:</b> Keep the session directed toward the specific problem<br/>
5. <b>Quantity Breeds Quality:</b> More ideas increase the chance of finding excellent solutions<br/><br/>

<b>Example — Brainstorming Topic: \"How to Reduce Traffic Congestion in Kathmandu\"</b><br/><br/>

A group of students brainstorms solutions:<br/>
• Build more flyovers and underpasses<br/>
• Introduce a metro/subway system<br/>
• Implement odd-even vehicle rationing<br/>
• Promote bicycle lanes and cycling culture<br/>
• Improve public bus service frequency and reliability<br/>
• Create carpooling mobile applications<br/>
• Enforce strict parking regulations<br/>
• Relocate government offices outside the city center<br/>
• Introduce congestion charges for entering busy areas<br/>
• Plant more trees (unrelated — but kept without judgment)<br/>
• Use drones for traffic monitoring<br/>
• Make public transport free for students and elderly<br/>
• Create remote work incentives for IT companies<br/>
• Build satellite cities to decentralize population<br/><br/>

<b>Post-Brainstorming Evaluation:</b><br/>
After generating 20+ ideas, the group evaluates each based on feasibility, cost, time, and impact. They might select: improving public buses, building flyovers, and promoting carpooling as the most practical immediate solutions.<br/><br/>

<b>Benefits:</b> Brainstorming prevents premature judgment, engages all participants, generates creative alternatives, and leads to better decisions through comprehensive exploration of possibilities.""",
            },
            {
                "num": "23",
                "question": "An argument states with a basic reason. Read the following sentence and draw an intermediate and then a main conclusion. \"If Cigarette advertising were banned, Cigarette manufacturers would save the money they would otherwise have spent on advertising.\"",
                "marks": "5",
                "answer": """<b>Argument Analysis:</b><br/><br/>

<b>Given Statement:</b><br/>
"If cigarette advertising were banned, cigarette manufacturers would save the money they would otherwise have spent on advertising."<br/><br/>

<b>Basic Reason (Premise):</b><br/>
Cigarette advertising is currently legal and actively conducted by manufacturers, requiring significant financial expenditure.<br/><br/>

<b>Intermediate Conclusion:</b><br/>
If cigarette advertising were banned, manufacturers would no longer incur advertising costs, thereby reducing their operational expenses.<br/><br/>

<b>Main Conclusion (Possible Extension):</b><br/>
Therefore, banning cigarette advertising would be financially beneficial to cigarette manufacturers (though potentially harmful to their sales volume), and the saved money could be redirected or retained as profit. Alternatively, from a public health policy perspective, the main conclusion could be: <b>Banning cigarette advertising is a viable public health measure that would reduce smoking-related harm without devastating the financial stability of tobacco companies.</b><br/><br/>

<b>Argument Structure Diagram:</b><br/>
Premise → Advertising costs manufacturers money<br/>
&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>
Intermediate Conclusion → Banning advertising eliminates these costs<br/>
&nbsp;&nbsp;&nbsp;&nbsp;↓<br/>
Main Conclusion → Therefore, a ban on cigarette advertising is economically feasible for manufacturers while serving public health interests<br/><br/>

<b>Note:</b> The original statement provides only a conditional claim. To construct a full argument, additional premises about public health benefits or economic impact would typically be added to reach a persuasive main conclusion. This demonstrates how single statements can serve as building blocks in larger argumentative structures.""",
            },
            {
                "num": "24",
                "question": "A lot can be done to make meetings effective. What measures would you suggest to make meeting effective if you were a member of a meeting? Explain.",
                "marks": "5",
                "answer": """<b>Measures to Make Meetings Effective:</b><br/><br/>

As a meeting member, I would suggest and practice the following measures:<br/><br/>

1. <b>Pre-Meeting Preparation:</b><br/>
• Review the agenda and supporting documents before the meeting<br/>
• Prepare questions, suggestions, or data relevant to discussion items<br/>
• Arrive on time and bring necessary materials<br/>
• Understand the meeting objectives and my role<br/><br/>

2. <b>Active Participation:</b><br/>
• Listen attentively to all speakers without interrupting<br/>
• Contribute constructively to discussions with relevant points<br/>
• Ask clarifying questions when information is unclear<br/>
• Avoid dominating the conversation; encourage quieter members to share views<br/><br/>

3. <b>Stay Focused on Agenda:</b><br/>
• Keep discussions aligned with agenda items<br/>
• Gently redirect conversation when it drifts off-topic<br/>
• Avoid side conversations and distractions (phones, emails)<br/><br/>

4. <b>Respectful Communication:</b><br/>
• Treat all opinions with respect, even when disagreeing<br/>
• Use polite, professional language<br/>
• Criticize ideas, not people<br/>
• Seek consensus rather than winning arguments<br/><br/>

5. <b>Decision-Making Support:</b><br/>
• Help evaluate options objectively using available facts<br/>
• Be willing to compromise for the group's benefit<br/>
• Accept democratic decisions even when personal preference differs<br/><br/>

6. <b>Post-Meeting Follow-Up:</b><br/>
• Review meeting minutes for accuracy<br/>
• Complete assigned action items within deadlines<br/>
• Provide feedback to the chair on meeting effectiveness<br/><br/>

<b>Conclusion:</b> Effective meetings require collective responsibility. Each member's preparation, participation, and follow-up directly impact whether the meeting achieves its objectives efficiently and productively.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10 = 20]",
        "questions": [
            {
                "num": "25",
                "question": "Of late, major cities, especially the capital city, of Nepal have become notorious because of frequent traffic congestion. In this context, write an argumentative essay about the benefits and disadvantages of our widespread use of the motor cars. Come to a conclusion as to whether the motor car can be a good thing or bad thing in light of daily problem faced by the commuters in the capital city and elsewhere in Nepal.",
                "marks": "10",
                "answer": """<b>Argumentative Essay: Motor Cars — Boon or Bane for Nepal?</b><br/><br/>

<b>Introduction:</b><br/>
The motor car has revolutionized human mobility, offering unprecedented convenience and freedom. However, in Nepal's major cities — particularly Kathmandu — the rapid proliferation of motor vehicles has transformed this symbol of progress into a source of daily misery. This essay examines both the benefits and disadvantages of widespread motor car use, ultimately arguing that while cars offer individual advantages, their unchecked growth poses a severe threat to urban quality of life in Nepal.<br/><br/>

<b>Benefits of Motor Cars:</b><br/><br/>
1. <b>Convenience and Time-Saving:</b> Cars provide door-to-door transportation, reducing travel time and physical effort, especially for elderly individuals, families with children, and those carrying goods.<br/><br/>

2. <b>Economic Development:</b> The automobile industry generates employment in manufacturing, sales, maintenance, and fuel supply. It facilitates commerce by enabling efficient transport of goods and services.<br/><br/>

3. <b>Accessibility:</b> In a mountainous country with limited public transport infrastructure, private vehicles connect remote areas to urban centers, improving access to education, healthcare, and employment.<br/><br/>

4. <b>Personal Freedom:</b> Car ownership provides independence from rigid public transport schedules and routes, allowing people to travel according to their own needs and timelines.<br/><br/>

<b>Disadvantages of Motor Cars:</b><br/><br/>
1. <b>Traffic Congestion:</b> Kathmandu experiences some of South Asia's worst traffic jams. Commuters regularly spend 2–3 hours daily in gridlock, wasting productive time and fuel. The city's road infrastructure was designed for a fraction of today's vehicle volume.<br/><br/>

2. <b>Air Pollution:</b> Vehicle emissions are the primary source of Kathmandu's air pollution, contributing to respiratory diseases, cardiovascular problems, and reduced life expectancy. Nepal's reliance on old, poorly maintained vehicles exacerbates the problem.<br/><br/>

3. <b>Noise Pollution:</b> Constant honking and engine noise create stressful urban environments, affecting mental health and reducing quality of life.<br/><br/>

4. <b>Land Use and Urban Sprawl:</b> Roads and parking spaces consume valuable urban land. Kathmandu Valley's fertile agricultural land is being paved over, threatening food security and ecological balance.<br/><br/>

5. <b>Economic Burden:</b> Nepal imports nearly all its petroleum, draining foreign currency reserves. Individual car owners face rising fuel costs, maintenance expenses, and loan burdens.<br/><br/>

6. <b>Inequality:</b> Car-centric development favors the wealthy while marginalizing pedestrians and public transport users, who constitute the majority of commuters.<br/><br/>

<b>Counter-Arguments and Rebuttal:</b><br/>
Some argue that better roads and flyovers can solve congestion. However, induced demand — where increased road capacity generates more traffic — means expansion alone is insufficient. Others suggest electric vehicles as a clean alternative, but without clean electricity generation and proper recycling infrastructure, this merely shifts pollution elsewhere.<br/><br/>

<b>Conclusion:</b><br/>
While motor cars offer undeniable individual benefits, their widespread, unregulated use in Nepal's urban context has become a net negative. The daily suffering of commuters, deteriorating public health, environmental degradation, and economic strain outweigh the convenience cars provide. The motor car is not inherently bad, but its unchecked dominance in Nepal's cities certainly is. A paradigm shift toward robust public transportation, non-motorized mobility, and strict vehicle regulation is essential. Only through balanced, sustainable transport policy can Nepal harness the benefits of motorized transport while preserving urban livability for future generations.<br/><br/>

<b>Recommendations:</b><br/>
• Expand and modernize public bus and metro systems<br/>
• Create dedicated bicycle lanes and pedestrian zones<br/>
• Implement congestion charging in city centers<br/>
• Enforce strict emission standards and vehicle age limits<br/>
• Promote remote work and flexible hours to reduce peak traffic""",
            },
            {
                "num": "26",
                "question": "You work for Aurora Holdings Plc, a large manufacturing company. In a recent board meeting, it was decided to review the company's staff benefits. At present they include only a company pension scheme and a subsidized canteen. The human resource director asks you to research the additional benefits which could be introduced. You should also recommend three benefits which you consider would be most welcome by all members of staff. Compile a formal report following the prescribed series of headings as discussed in your text of Communication for Business.",
                "marks": "10",
                "answer": """<b>Formal Report: Review of Staff Benefits at Aurora Holdings Plc</b><br/><br/>

<b>1. TERMS OF REFERENCE</b><br/>
To research and recommend additional staff benefits for Aurora Holdings Plc beyond the existing company pension scheme and subsidized canteen. The report is prepared at the request of the Human Resource Director following the Board Meeting held recently.<br/><br/>

<b>2. PROCEDURE</b><br/>
The research was conducted through:<br/>
• Survey of 200 employees across all departments regarding desired benefits<br/>
• Benchmarking against competitor companies in the manufacturing sector<br/>
• Review of industry reports on employee retention and satisfaction<br/>
• Consultation with HR managers from three similar-sized companies<br/>
• Analysis of cost-benefit ratios for various benefit options<br/><br/>

<b>3. FINDINGS</b><br/><br/>
Current benefits at Aurora Holdings Plc:<br/>
1. Company pension scheme<br/>
2. Subsidized canteen<br/><br/>

Additional benefits offered by competitors:<br/>
• Health and medical insurance (offered by 85% of competitors)<br/>
• Flexible working hours / remote work options (78%)<br/>
• Annual performance bonuses (90%)<br/>
• Professional development and training allowances (65%)<br/>
• Gym memberships or wellness programs (60%)<br/>
• Childcare support or vouchers (45%)<br/>
• Additional paid leave / sabbaticals (55%)<br/>
• Employee stock ownership plans (40%)<br/><br/>

Survey results from Aurora employees:<br/>
• 72% rated health insurance as their most desired benefit<br/>
• 68% wanted flexible working arrangements<br/>
• 61% requested professional training and career development support<br/>
• 54% expressed interest in wellness programs<br/>
• 48% wanted enhanced annual leave provisions<br/><br/>

<b>4. CONCLUSIONS</b><br/>
The current benefits package at Aurora Holdings Plc is below industry standards and insufficient to attract and retain top talent in a competitive labor market. Employee morale and satisfaction are directly linked to comprehensive benefit offerings. The company risks higher turnover and recruitment costs if improvements are not made.<br/><br/>

<b>5. RECOMMENDATIONS</b><br/><br/>
The following three benefits are recommended as the most welcome and impactful for all staff members:<br/><br/>

<b>Recommendation 1: Comprehensive Health and Medical Insurance</b><br/>
• Coverage for employees and their immediate families<br/>
• Includes hospitalization, outpatient care, dental, and vision<br/>
• Estimated cost: £400 per employee per year<br/>
• <b>Rationale:</b> Highest demand in employee survey; demonstrates company care for employee wellbeing; reduces absenteeism due to untreated health issues; competitive necessity as 85% of rivals offer this.<br/><br/>

<b>Recommendation 2: Flexible Working Arrangements</b><br/>
• Option for remote work 2 days per week where job role permits<br/>
• Flexible start and finish times (core hours 10am–3pm)<br/>
• Compressed workweek options (4 longer days)<br/>
• Estimated cost: Minimal (existing IT infrastructure sufficient)<br/>
• <b>Rationale:</b> Improves work-life balance; increases productivity; reduces commuting stress and costs; highly valued post-pandemic; helps retain parents and caregivers.<br/><br/>

<b>Recommendation 3: Professional Development and Training Allowance</b><br/>
• £500 annual allowance per employee for relevant courses, certifications, or conferences<br/>
• Internal mentorship and leadership programs<br/>
• Career pathway planning support<br/>
• Estimated cost: £500 per employee per year<br/>
• <b>Rationale:</b> Employees feel invested in and valued; builds internal talent pipeline; improves company capabilities; addresses 61% employee demand; reduces external recruitment costs.<br/><br/>

<b>Implementation Timeline:</b><br/>
• Month 1–2: Negotiate health insurance group policy<br/>
• Month 2–3: Develop flexible working policy and manager training<br/>
• Month 3–4: Launch training allowance application process<br/>
• Month 6: Full rollout with employee communication campaign<br/><br/>

<b>Report Prepared By:</b> [Name]<br/>
<b>Position:</b> [Title]<br/>
<b>Date:</b> [Date]<br/>
<b>Distribution:</b> Human Resource Director, Board of Directors""",
            },
            {
                "num": "27",
                "question": "In the story \"The Land Ironclads\", the young lieutenant believes that there are other things in life better worth having than proficiency in war. However, the war correspondent argues that civilization has science, which has invented rifles and guns used by us. What happens after the guns are fired at the illusion of the lieutenant? Does it mean the war correspondent is more realistic than the lieutenant? Discuss. OR Discuss \"Billennium\" by J.G. Ballard as a story of future where it is not war, but overpopulation that threatens the human race.",
                "marks": "10",
                "answer": """<b>Option A: \"The Land Ironclads\" — Realism vs. Idealism</b><br/><br/>

<b>The Lieutenant's Illusion:</b><br/>
In H.G. Wells' "The Land Ironclads," the young lieutenant represents the <b>romantic, chivalric tradition of warfare</b>. He believes in honor, courage, individual skill, and the human spirit — "there are other things in life better worth having than proficiency in war." For him, war is an arena for demonstrating noble virtues, personal bravery, and gentlemanly conduct. He trusts in the effectiveness of disciplined infantry, sharpshooting, and entrenched defensive positions.<br/><br/>

<b>The War Correspondent's Argument:</b><br/>
The war correspondent embodies a <b>modern, scientific worldview</b>. He argues that civilization has progressed through science and technology, which have produced rifles, artillery, and ultimately the devastating land ironclads — massive armored vehicles that render traditional military tactics obsolete. He sees war not as a noble contest but as an engineering problem to be solved through technological superiority.<br/><br/>

<b>What Happens After the Guns Are Fired:</b><br/>
When the guns are fired at the lieutenant's carefully prepared defenses, the outcome is catastrophic for the defenders. The land ironclads — heavily armored, steam-powered machines equipped with rapid-fire guns — advance inexorably across the battlefield. The traditional infantry, no matter how brave or well-trained, cannot penetrate the ironclads' armor. Their rifles are ineffective; their trenches are overrun; their courage counts for nothing against mechanized warfare. The lieutenant's idealized vision of war is literally crushed under the treads of technology.<br/><br/>

<b>Is the War Correspondent More Realistic?</b><br/><br/>
Yes, the war correspondent is unquestionably more realistic than the lieutenant, for several reasons:<br/><br/>

1. <b>Technological Determinism:</b> The correspondent correctly understands that warfare evolves with technology. History consistently shows that military advantage goes to those with superior technology, not superior character. The ironclads represent the inevitable mechanization of conflict.<br/><br/>

2. <b>Practical vs. Romantic:</b> The lieutenant's values — honor, individual skill, romantic idealism — are admirable in peacetime but irrelevant when facing industrial-scale weaponry. The correspondent recognizes that modern warfare is about logistics, engineering, and firepower, not personal heroism.<br/><br/>

3. <b>Prophetic Accuracy:</b> Wells wrote this story in 1903, before World War I demonstrated the horrifying reality of mechanized warfare. The correspondent's predictions proved tragically accurate: trenches, machine guns, tanks, and artillery would devastate a generation of soldiers whose commanders still believed in cavalry charges and glorious charges.<br/><br/>

4. <b>The Lieutenant's Naivety:</b> The lieutenant's belief that there are "better things" than war proficiency reflects a privileged, pre-industrial mindset that fails to comprehend total war. In an age of scientific warfare, such idealism becomes dangerous self-deception.<br/><br/>

<b>However:</b> The correspondent's realism is cold and dehumanizing. While accurate, his worldview strips war of moral meaning entirely, reducing human beings to components in a technological system. Wells may be suggesting that <b>neither view is fully adequate</b> — the lieutenant's idealism is impractical, but the correspondent's mechanistic view is spiritually hollow. The tragedy is that the modern world makes the correspondent's perspective inescapable.<br/><br/>

<b>Conclusion:</b> The war correspondent is more realistic because his predictions are borne out by events. But the story mourns the death of the lieutenant's values, suggesting that technological realism, while accurate, comes at a profound human cost. The ironclads don't just defeat an army; they obliterate a worldview.<br/><br/>

---<br/><br/>

<b>Option B: \"Billennium\" by J.G. Ballard — Overpopulation as Existential Threat</b><br/><br/>

<b>Introduction:</b><br/>
J.G. Ballard's "Billennium" presents a dystopian future where overpopulation, not war, has become the defining threat to human civilization. The story depicts a world so densely packed with people that basic human dignities — privacy, space, comfort — have been systematically sacrificed to accommodate the ever-growing population.<br/><br/>

<b>The World of Billennium:</b><br/>
In this future, the world's population has reached one billion in cities alone (the title refers to this milestone). People live in tiny cubicles, divided and subdivided until individuals occupy spaces barely larger than cupboards. Streets are impassable due to crowds; public spaces have ceased to exist; and the concept of personal space has become a distant memory. The government enforces strict regulations on living space, and any discovery of extra space is immediately subdivided among more people.<br/><br/>

<b>Overpopulation vs. War as Threats:</b><br/>
Ballard deliberately contrasts his dystopia with traditional apocalyptic narratives centered on war:<br/><br/>

1. <b>Gradual vs. Sudden Destruction:</b> War destroys through sudden violence, but overpopulation destroys through incremental erosion. The characters in "Billennium" cannot pinpoint when their quality of life became intolerable — it happened so gradually that they adapted to each new deprivation.<br/><br/>

2. <b>No Enemy to Fight:</b> War provides a clear antagonist against which humanity can unite. Overpopulation offers no such focal point. The enemy is demographic statistics, birth rates, and the exponential growth curve. There is no one to blame, no battle to win.<br/><br/>

3. <b>Institutional Acceptance:</b> Whereas war might provoke resistance, the society in "Billennium" has internalized overpopulation as normal. People accept smaller spaces, less privacy, and degraded conditions as inevitable facts of life. The horror lies in this normalization.<br/><br/>

4. <b>Individual Solutions Are Futile:</b> The protagonists briefly discover a hidden, larger room and experience the luxury of space. But their secret is quickly discovered, and the room is partitioned among dozens of new occupants. Individual escape is impossible within the system.<br/><br/>

<b>Thematic Analysis:</b><br/>
Ballard explores how overpopulation fundamentally alters human psychology and social relations:<br/>
• <b>Loss of Individuality:</b> People become interchangeable units defined by their spatial allocation<br/>
• <b>Corruption of Human Values:</b> Privacy, solitude, and personal territory — once considered essential needs — become illegal luxuries<br/>
• <b>Bureaucratic Dehumanization:</b> The state manages population through impersonal regulations that treat humans as quantities to be housed<br/>
• <b>The Tragedy of Adaptation:</b> Humans can adapt to almost anything, including conditions that destroy their humanity<br/><br/>

<b>Relevance Today:</b><br/>
Written in 1961, "Billennium" anticipated contemporary concerns about urbanization, housing crises, and resource scarcity. Cities like Mumbai, Manila, and Lagos already experience extreme population density. Climate change, food insecurity, and water shortages compound the problem Ballard identified.<br/><br/>

<b>Conclusion:</b><br/>
"Billennium" argues that overpopulation represents a more insidious and ultimately more devastating threat than war because it cannot be defeated by military means, offers no clear enemy, and gradually erodes the conditions necessary for human flourishing. Ballard warns that humanity's greatest challenge may not be conflict with each other, but the unintended consequences of our own reproductive success and failure to plan. The story is a powerful call for population awareness, urban planning, and the preservation of human dignity in an increasingly crowded world.""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet(
        subject_code="CACS153",
        subject_slug="english-ii",
        subject_name="English II",
        year=2018,
        semester_slug="semester-2",
        questions_data=QUESTIONS_DATA
    )
    print("Answer sheet generation complete for CACS153 2018!")
