import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS102_2020 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "1",
                "question": "What is sociology? Discuss the nature of sociology.",
                "marks": "2+3",
                "answer": """<b>Sociology</b> is the scientific study of society, social relationships, and human behavior within group contexts. The term was coined by Auguste Comte in 1838. Sociology examines how social structures, institutions, and cultural values shape individual and collective behavior. It investigates patterns of social interaction, social stratification, group dynamics, and the processes that maintain or change social order.<br/><br/>
<b>Nature of Sociology:</b><br/>
1. <b>Scientific Discipline:</b> Sociology employs systematic methods of observation, comparison, and empirical analysis to study social phenomena. It follows the scientific method of hypothesis formulation, data collection, and verification.<br/><br/>
2. <b>Social Science:</b> As a social science, sociology studies human society and social behavior rather than natural phenomena. It focuses on relationships, institutions, organizations, and collective human activities.<br/><br/>
3. <b>Study of Social Groups:</b> Sociology is concerned with group life rather than individual behavior in isolation. It analyzes families, communities, organizations, and entire societies.<br/><br/>
4. <b>Objective and Value-Neutral:</b> Sociology strives for objectivity, seeking to describe and explain social reality without personal bias, though complete value-neutrality remains an ideal.<br/><br/>
5. <b>Abstract and Generalizing:</b> Sociology develops general theories and concepts (such as socialization, stratification, deviance) that apply across different societies and historical periods.<br/><br/>
6. <b>Relatively Independent:</b> While sociology overlaps with psychology, economics, political science, and anthropology, it maintains a distinct focus on the social dimension of human life.""",
            },
            {
                "num": "2",
                "question": "Write an essay on the \"relevance of sociology in computer application\".",
                "marks": "5",
                "answer": """<b>Relevance of Sociology in Computer Application</b><br/><br/>
Sociology and computer applications may seem unrelated at first glance, but they are deeply interconnected in the modern digital age. Understanding the sociological dimensions of technology is essential for developing effective, ethical, and user-centered computer systems.<br/><br/>
1. <b>Understanding User Behavior:</b><br/>
Sociology helps computer professionals understand how different social groups interact with technology. Factors such as age, education, culture, and socioeconomic status influence technology adoption and usage patterns. This knowledge enables designers to create inclusive applications that cater to diverse user needs.<br/><br/>
2. <b>Social Impact Assessment:</b><br/>
Computer applications have profound social consequences — affecting employment, communication, privacy, and social relationships. Sociological insights help developers anticipate these impacts and design systems that minimize harm while maximizing social benefit. For example, understanding digital divide issues can guide the creation of accessible technology for underserved communities.<br/><br/>
3. <b>Design of Social Media and Communication Platforms:</b><br/>
Social media platforms, messaging apps, and collaborative tools are fundamentally social systems. Sociology provides frameworks for understanding group dynamics, social networks, information diffusion, and online community formation. This understanding is crucial for designing features that foster positive interactions and prevent toxic behaviors such as cyberbullying and misinformation.<br/><br/>
4. <b>Ethical and Privacy Considerations:</b><br/>
Sociology examines power structures, inequality, and social control. These perspectives are vital when designing systems that handle personal data, implement algorithms, or deploy artificial intelligence. Sociological awareness helps developers recognize potential biases in algorithms and ensure that technology promotes fairness rather than reinforcing existing inequalities.<br/><br/>
5. <b>Organizational and Workplace Technology:</b><br/>
In organizational contexts, sociology helps design enterprise software that aligns with team structures, workflows, and organizational culture. Understanding how people collaborate, communicate, and resist change enables smoother technology implementation and higher adoption rates.<br/><br/>
6. <b>Human-Computer Interaction (HCI):</b><br/>
The field of HCI draws heavily from sociology to understand how users perceive, learn, and adapt to technology. Cultural differences, social norms, and collective practices all influence interface design and user experience.<br/><br/>
In conclusion, sociology provides computer professionals with the critical ability to see technology not merely as a technical artifact but as a social force that shapes and is shaped by human society.""",
            },
            {
                "num": "3",
                "question": "What do you understand by society? How does it differ from community? Discuss.",
                "marks": "2+3",
                "answer": """<b>Society</b> is a large group of people who share a common culture, territory, and way of life, and who interact with one another within a structured network of social relationships. It is a web of social institutions (family, education, religion, economy, government) that organize collective life. Society encompasses both the material and non-material aspects of social existence, including norms, values, customs, laws, and social roles.<br/><br/>
<b>Differences between Society and Community:</b><br/>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Basis</b></td><td><b>Society</b></td><td><b>Community</b></td></tr>
<tr><td>Size</td><td>Larger and more inclusive; may include millions of people</td><td>Smaller; a localized group within a society</td></tr>
<tr><td>Definition</td><td>Based on social relationships and shared culture</td><td>Based on locality (territory) and we-feeling</td></tr>
<tr><td>Consciousness</td><td>Members may not know each other personally</td><td>Members know each other and share a sense of belonging</td></tr>
<tr><td>Territory</td><td>May not have a definite territory</td><td>Has a definite geographic area</td></tr>
<tr><td>Examples</td><td>Nepalese society, American society</td><td>A village, a neighborhood, a town</td></tr>
<tr><td>Relationships</td><td>Formal, impersonal, and diverse</td><td>Informal, personal, and intimate</td></tr>
<tr><td>Goals</td><td>Aims at general welfare and social order</td><td>Aims at common interests of members</td></tr>
</table><br/>
In summary, while society is a broad, abstract concept referring to all social relationships in a culture, community is a concrete, localized group where people live together, interact directly, and share common interests and a sense of identity.""",
            },
            {
                "num": "4",
                "question": "What is family? What are the various types of family? Discuss with examples.",
                "marks": "2+3",
                "answer": """<b>Family</b> is a fundamental social institution defined as a group of people related by blood, marriage, or adoption, living together and cooperating for the welfare of the group. It is the primary unit of socialization, emotional support, and economic cooperation. The family fulfills essential functions such as reproduction, socialization of children, provision of care, and transmission of cultural values across generations.<br/><br/>
<b>Various Types of Family:</b><br/><br/>
1. <b>On the Basis of Structure:</b><br/><br/>
   a) <b>Nuclear Family:</b> Consists of husband, wife, and their unmarried children living together. Example: A couple with two children living in a city apartment.<br/><br/>
   b) <b>Joint/Extended Family:</b> Includes multiple generations living together — grandparents, parents, children, and sometimes aunts, uncles, and cousins. Example: A traditional Nepali household where three generations share a home and common kitchen.<br/><br/>
   c) <b>Single-Parent Family:</b> One parent raises children alone due to divorce, death, or choice. Example: A divorced mother raising her two children.<br/><br/>
   d) <b>Blended/Reconstituted Family:</b> Formed when one or both partners bring children from previous relationships. Example: A man with a daughter marries a woman with a son; they form a new family unit.<br/><br/>
2. <b>On the Basis of Residence:</b><br/><br/>
   a) <b>Patrilocal Family:</b> The wife moves to the husband's family home after marriage. Common in many South Asian societies.<br/><br/>
   b) <b>Matrilocal Family:</b> The husband moves to the wife's family home. Found in some matrilineal societies like the Khasi community in India.<br/><br/>
   c) <b>Neolocal Family:</b> The couple establishes a new independent residence. Common in modern urban societies.<br/><br/>
3. <b>On the Basis of Authority:</b><br/><br/>
   a) <b>Patriarchal Family:</b> Male is the head and holds primary authority. Common in traditional societies.<br/><br/>
   b) <b>Matriarchal Family:</b> Female is the head and holds primary authority. Example: The Minangkabau of Indonesia.<br/><br/>
   c) <b>Egalitarian Family:</b> Authority is shared equally between husband and wife. Increasingly common in modern societies.<br/><br/>
4. <b>On the Basis of Marriage:</b><br/><br/>
   a) <b>Monogamous Family:</b> One husband and one wife. The legally accepted form in most countries today.<br/><br/>
   b) <b>Polygamous Family:</b> One person has multiple spouses — polygyny (one husband, multiple wives) or polyandry (one wife, multiple husbands).""",
            },
            {
                "num": "5",
                "question": "What is social change? Discuss any four major factors of social change with suitable examples.",
                "marks": "2+3",
                "answer": """<b>Social Change</b> refers to the transformation of culture, behavior, social institutions, and social structure over time. It involves alterations in the way society is organized, the values people hold, and the norms that govern behavior. Social change can be gradual (evolutionary) or rapid (revolutionary), and it can affect small communities or entire civilizations. It is an ever-present phenomenon in all societies.<br/><br/>
<b>Four Major Factors of Social Change:</b><br/><br/>
1. <b>Technological Factors:</b><br/>
Technology is one of the most powerful drivers of social change. New inventions and innovations transform how people work, communicate, and live. The internet and smartphones have revolutionized communication, commerce, education, and social interaction. In Nepal, the spread of mobile banking and digital payment systems has transformed financial behavior, reducing reliance on cash and traditional banking.<br/><br/>
2. <b>Economic Factors:</b><br/>
Changes in the economic system — such as industrialization, globalization, and shifts from agrarian to industrial or service economies — profoundly reshape society. The adoption of remittance-based economy in Nepal, where millions of young people work abroad, has changed family structures, gender roles, consumption patterns, and village demographics. Economic development raises living standards but can also create inequality.<br/><br/>
3. <b>Cultural Factors:</b><br/>
Cultural changes including new ideas, values, beliefs, and knowledge systems drive social transformation. Education, media exposure, and contact with other cultures introduce new ways of thinking. For example, increased education for girls in Nepal has led to delayed marriage, lower fertility rates, greater female workforce participation, and changing attitudes toward gender equality.<br/><br/>
4. <b>Political Factors:</b><br/>
Political events, policies, and movements significantly impact social structure. The transition from monarchy to republic in Nepal (2008) brought fundamental changes in governance, citizenship rights, and social inclusion. Policies such as secularism, federalism, and affirmative action for marginalized groups have transformed social hierarchies that existed for centuries. Political revolutions, wars, and new legislation can rapidly restructure entire societies.""",
            },
            {
                "num": "6",
                "question": "Discuss the influence of modern technology in changing marriage institution with examples.",
                "marks": "5",
                "answer": """<b>Influence of Modern Technology on the Marriage Institution</b><br/><br/>
Modern technology has profoundly transformed the institution of marriage, affecting how people meet, form relationships, maintain marriages, and even dissolve them. These changes reflect broader shifts in social values, gender roles, and individual autonomy.<br/><br/>
1. <b>Changing Mate Selection:</b><br/>
Technology has revolutionized how people find partners. Online matrimonial websites (such as Shaadi.com, Nepali Vivah) and dating apps (Tinder, Bumble) have replaced or supplemented traditional arranged marriage systems. Young people now have greater autonomy in choosing partners across caste, class, and geographic boundaries. Example: A Nepali student in the USA can find a compatible partner through online platforms, bypassing traditional family networks.<br/><br/>
2. <b>Communication and Long-Distance Relationships:</b><br/>
Video calling, instant messaging, and social media enable couples to maintain relationships across distances. This has been particularly significant for families affected by labor migration. Example: A husband working in the Gulf can maintain daily visual contact with his wife and children in Nepal through WhatsApp video calls, reducing the emotional strain of separation.<br/><br/>
3. <b>Changing Gender Dynamics:</b><br/>
Technology has empowered women economically and socially, shifting power dynamics within marriage. Remote work, online education, and e-commerce enable women to earn independently, challenging traditional patriarchal structures. Example: A woman running an online business from home may negotiate more equality in marital decisions.<br/><br/>
4. <b>Impact on Marital Satisfaction and Stability:</b><br/>
While technology connects people, excessive use of social media and smartphones can create marital discord. Issues like online infidelity, jealousy triggered by social media interactions, and reduced face-to-face communication are emerging challenges. Example: Marital conflicts arising from one partner's secretive messaging habits or reconnecting with old romantic interests on Facebook.<br/><br/>
5. <b>Legal and Administrative Changes:</b><br/>
Online marriage registration, digital evidence in divorce proceedings, and virtual court hearings have modernized the legal aspects of marriage. Example: Courts in Nepal now accept digital communication records as evidence in divorce and domestic violence cases.<br/><br/>
6. <b>Redefinition of Family Roles:</b><br/>
Smart home technology, online grocery delivery, and digital parenting resources have altered domestic responsibilities. Technology can reduce the burden of household chores, but it also creates new tensions about screen time and digital parenting.""",
            },
            {
                "num": "7",
                "question": "Write short notes on any two: a) Interview b) Social Status c) Enculturation",
                "marks": "2.5+2.5",
                "answer": """<b>a) Interview:</b><br/>
An interview is a structured conversation between two or more people where one party (the interviewer) asks questions to elicit information, opinions, or experiences from the other party (the interviewee). It is a widely used method in social research, journalism, employment selection, and clinical settings.<br/><br/>
<b>Types of Interview:</b><br/>
• <b>Structured Interview:</b> Pre-set questions asked in fixed order; high reliability and comparability.<br/>
• <b>Unstructured Interview:</b> Flexible, open-ended conversation; allows in-depth exploration.<br/>
• <b>Semi-structured Interview:</b> Combines prepared questions with flexibility to probe further.<br/>
• <b>Focus Group Interview:</b> Group discussion guided by a moderator to gather collective perspectives.<br/><br/>
<b>Merits:</b> High response rate, ability to clarify questions, rich qualitative data, observation of non-verbal cues.<br/>
<b>Demerits:</b> Time-consuming, expensive, interviewer bias, difficulty in quantifying responses.<br/><br/>
<b>b) Social Status:</b><br/>
Social status refers to the position or rank an individual holds within a social system. It determines the prestige, respect, and privileges associated with that position. Status can be ascribed (assigned at birth based on race, caste, gender, family) or achieved (acquired through personal effort, education, occupation, or talent).<br/><br/>
<b>Types:</b><br/>
• <b>Ascribed Status:</b> Inherited or assigned involuntarily (e.g., being born into a royal family or a particular caste).<br/>
• <b>Achieved Status:</b> Earned through individual accomplishment (e.g., becoming a doctor, engineer, or elected official).<br/><br/>
An individual typically holds multiple statuses simultaneously (status set). The most significant status that dominates social identity is called the <b>master status</b>. Social status influences access to resources, social networks, and life opportunities.<br/><br/>
<b>c) Enculturation:</b><br/>
Enculturation is the process by which individuals learn and internalize the values, beliefs, norms, language, and practices of their culture. It is the socialization process specific to cultural learning — how a child becomes a competent member of a particular society. Unlike socialization, which is a broader term, enculturation emphasizes the cultural dimension of learning.<br/><br/>
<b>Agents of Enculturation:</b><br/>
• <b>Family:</b> First and most influential agent; teaches language, basic values, and cultural identity.<br/>
• <b>Education:</b> Schools transmit formal knowledge, national history, civic values, and social norms.<br/>
• <b>Religion:</b> Religious institutions teach moral codes, rituals, and spiritual beliefs.<br/>
• <b>Peers and Media:</b> Friends, popular culture, and mass media shape contemporary cultural practices and attitudes.<br/><br/>
Enculturation is a lifelong process that enables social cohesion by ensuring that members of a society share common understandings and behavioral expectations.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "What do you understand by socialization process? What are the agents that helped you in the process of socialization till date? Discuss each of them in detail.",
                "marks": "4+6",
                "answer": """<b>Socialization Process</b><br/>
Socialization is the lifelong process through which individuals learn the norms, values, behaviors, and social skills necessary to function effectively as members of society. It transforms biological beings (human infants) into social beings capable of participating in social life. Through socialization, individuals internalize cultural patterns, develop a sense of self-identity, and learn to conform to societal expectations. The process begins at birth and continues throughout life as individuals adapt to new roles, groups, and social changes.<br/><br/>
Socialization involves two key aspects: <b>primary socialization</b> (occurring in childhood, forming basic personality and identity) and <b>secondary socialization</b> (occurring later in life as individuals adapt to new social contexts such as school, workplace, or marriage).<br/><br/>
<b>Agents of Socialization:</b><br/><br/>
1. <b>Family:</b><br/>
The family is the first and most influential agent of socialization. From birth, children learn language, basic emotional responses, gender roles, religious beliefs, and cultural values within the family. Parents and siblings model behavior, enforce rules, and provide rewards and punishments that shape the child's conscience and personality. In Nepali society, the family transmits traditional values such as respect for elders, religious practices, and caste or ethnic identity.<br/><br/>
2. <b>School/Education:</b><br/>
Schools socialize children into broader society beyond the family. They teach formal knowledge (reading, writing, mathematics), but also implicit lessons about punctuality, discipline, competition, cooperation, and hierarchy. Schools transmit national culture, civic values, and prepare individuals for occupational roles. Peer interactions at school also teach social skills, friendship formation, and group dynamics.<br/><br/>
3. <b>Peer Groups:</b><br/>
As children grow, peer groups (friends, classmates, neighborhood groups) become increasingly important. Peer socialization operates outside adult control and provides a space for developing independent identities. Peers influence language use, fashion, recreational activities, and attitudes toward authority. Peer acceptance or rejection significantly impacts self-esteem and social development.<br/><br/>
4. <b>Mass Media:</b><br/>
Television, internet, social media, films, and video games are powerful modern agents of socialization. They expose individuals to diverse perspectives, global cultures, and political ideologies. Media shapes attitudes toward gender, beauty, violence, consumerism, and social issues. In the digital age, social media platforms have become primary spaces where young people learn about relationships, politics, and identity.<br/><br/>
5. <b>Religion:</b><br/>
Religious institutions provide moral frameworks, rituals, and community belonging. They teach concepts of right and wrong, the meaning of life, and cosmic order. Religious socialization often begins in childhood through family practices and is reinforced through temples, churches, mosques, or monasteries. In Nepal, religious festivals and rituals play a central role in transmitting cultural identity.<br/><br/>
6. <b>Workplace:</b><br/>
Entering the workforce represents a significant phase of secondary socialization. Individuals learn occupational skills, professional norms, organizational culture, and new role expectations. The workplace teaches punctuality, accountability, teamwork, and the relationship between effort and reward. Career changes require re-socialization into new professional identities.""",
            },
            {
                "num": "10",
                "question": "What is social research? Discuss the major data collection tools and techniques used in social research.",
                "marks": "3+7",
                "answer": """<b>Social Research</b><br/>
Social research is a systematic and objective investigation of social phenomena using scientific methods. It involves the collection, analysis, and interpretation of data to understand social relationships, institutions, behaviors, and problems. The goal of social research is to produce valid, reliable, and generalizable knowledge about society that can inform policy, theory, and practice. It follows a structured process: identifying a problem, reviewing literature, formulating hypotheses, designing methodology, collecting data, analyzing findings, and drawing conclusions.<br/><br/>
<b>Major Data Collection Tools and Techniques in Social Research:</b><br/><br/>
1. <b>Observation:</b><br/>
Observation involves watching and recording behavior, events, or social processes as they naturally occur. It can be:<br/>
• <b>Participant observation:</b> The researcher actively participates in the group being studied (e.g., living in a village to study rural life).<br/>
• <b>Non-participant observation:</b> The researcher observes without participating.<br/>
• <b>Structured observation:</b> Uses predetermined categories and checklists.<br/>
• <b>Unstructured observation:</b> Open-ended recording of all relevant behaviors.<br/><br/>
2. <b>Interview:</b><br/>
Interviews involve direct verbal interaction between researcher and respondent to gather in-depth information. Types include structured, semi-structured, unstructured, and focus group interviews. Interviews yield rich qualitative data and allow clarification of responses, but they are time-consuming and subject to interviewer bias.<br/><br/>
3. <b>Questionnaire/Survey:</b><br/>
Questionnaires are standardized sets of written questions administered to a large sample. They can be self-administered or conducted by enumerators. Surveys allow collection of quantifiable data from large populations, enabling statistical analysis and generalization. Well-designed questionnaires use clear, unbiased language and logical question ordering.<br/><br/>
4. <b>Case Study:</b><br/>
A case study is an intensive, in-depth examination of a single unit — such as a person, family, community, organization, or event. It uses multiple sources of data (interviews, documents, observation) to develop a comprehensive understanding. Case studies are valuable for exploring complex phenomena in real-life contexts.<br/><br/>
5. <b>Content Analysis:</b><br/>
Content analysis is a systematic technique for analyzing the content of communication — such as books, newspapers, films, speeches, or social media posts. It involves categorizing and quantifying textual or visual material to identify patterns, themes, biases, or trends. It is widely used in media studies, political science, and historical research.<br/><br/>
6. <b>Experiment:</b><br/>
Experiments involve manipulating one variable (independent variable) to observe its effect on another variable (dependent variable) while controlling other factors. Experiments provide strong evidence of causality but are often difficult to conduct in real social settings due to ethical and practical constraints. Field experiments and quasi-experiments are adaptations used in social research.<br/><br/>
7. <b>Secondary Data Analysis:</b><br/>
Researchers often use existing data collected by others, such as census reports, government statistics, organizational records, or previous research studies. Secondary data analysis is cost-effective and allows longitudinal or comparative studies, though researchers must critically evaluate data quality and relevance.<br/><br/>
8. <b>Participatory Rural Appraisal (PRA):</b><br/>
PRA techniques involve community members actively in the research process through mapping, diagramming, ranking, and seasonal calendars. These tools are particularly useful in development research for understanding local knowledge, needs, and priorities.""",
            },
            {
                "num": "11",
                "question": "Discuss the historical process of Nationhood in Nepal.",
                "marks": "10",
                "answer": """<b>Historical Process of Nationhood in Nepal</b><br/><br/>
The formation of Nepal as a modern nation-state was a long historical process involving territorial unification, state-building, cultural integration, and political evolution over several centuries.<br/><br/>
1. <b>Ancient and Medieval Foundations (Before 1768):</b><br/>
Before unification, the territory of present-day Nepal consisted of numerous small kingdoms and principalities. The Kathmandu Valley was ruled by the Malla kings, while other regions had their own rulers. The Kirat, Lichchavi, and Malla periods established early political and cultural foundations. Hinduism and Buddhism provided shared religious frameworks, while trade routes through the Himalayas connected diverse communities.<br/><br/>
2. <b>Unification under Prithvi Narayan Shah (1768-1769):</b><br/>
The modern Nepali state was founded through the military campaigns of King Prithvi Narayan Shah of Gorkha. He conquered the Kathmandu Valley in 1768-69 and continued expanding territories east to the Mechi River and west to the Mahakali River. This unification created a multi-ethnic, multi-lingual kingdom stretching from the plains to the Himalayas. Prithvi Narayan Shah famously described Nepal as a "garden of four castes and thirty-six sub-castes," acknowledging its diversity.<br/><br/>
3. <b>Expansion and Consolidation (1769-1814):</b><br/>
Successive rulers expanded Nepali territory significantly, reaching its maximum extent from the Sutlej River in the west to the Teesta River in the east. However, the Anglo-Nepalese War (1814-16) resulted in the Treaty of Sugauli, forcing Nepal to cede about one-third of its territory to British India. This defined Nepal's modern boundaries and marked the beginning of a more inward-focused state.<br/><br/>
4. <b>The Rana Regime (1846-1951):</b><br/>
The Kot Massacre of 1846 established the hereditary Rana prime ministership, reducing the Shah kings to figureheads. While the Ranas maintained Nepal's independence during British colonial expansion in South Asia, they also isolated Nepal from the outside world. Infrastructure development was minimal, and political participation was restricted to the elite. Nevertheless, this period solidified administrative structures and central state authority.<br/><br/>
5. <b>Democratic Opening and Monarchy (1951-1990):</b><br/>
The 1950-51 revolution ended the Rana regime and introduced multi-party democracy under the constitutional monarchy. King Tribhuvan, supported by the Nepali Congress and Indian assistance, restored royal authority. The first constitution (1959) and elected government marked Nepal's entry into modern constitutional politics, though the monarchy repeatedly intervened, dissolving elected governments.<br/><br/>
6. <b>Panchayat System (1960-1990):</b><br/>
King Mahendra dissolved democracy in 1960 and established the partyless Panchayat system, promoting a centralized, monarchical state with a nationalist ideology. The Panchayat emphasized Nepali language, Hindu culture, and loyalty to the monarchy as national unifying symbols. While this created a degree of national identity, it also marginalized ethnic minorities, indigenous groups (Janajati), and Madhesi communities.<br/><br/>
7. <b>Democracy and People's Movement (1990-2006):</b><br/>
The 1990 People's Movement restored multi-party democracy. The 1990 constitution defined Nepal as a multi-ethnic, multi-lingual Hindu kingdom. However, political instability, corruption, and the Maoist insurgency (1996-2006) challenged the state. The 2001 royal massacre and King Gyanendra's authoritarian rule further deepened the crisis.<br/><br/>
8. <b>Republic and Federalism (2006-Present):</b><br/>
The 2006 People's Movement ended the monarchy and established Nepal as a secular federal democratic republic. The 2015 constitution restructured Nepal into seven provinces and recognized diversity through federalism, proportional representation, and social inclusion policies. This represents a shift from a centralized, unitary state to a decentralized federation that attempts to accommodate Nepal's extraordinary ethnic, linguistic, and cultural diversity within a unified nation-state.<br/><br/>
The process of nationhood in Nepal continues as the country grapples with building national unity while respecting diversity, establishing effective federal governance, and achieving economic development.""",
            },
        ]
    }
]

generate_answer_sheet("CACS102", "society-technology", "Society & Technology", 2020, "semester-1", CACS102_2020)
