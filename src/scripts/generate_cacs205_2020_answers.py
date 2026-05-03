#!/usr/bin/env python3
import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS205_2020 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What is HTML5? Explain characteristics of HTML5.",
                "marks": "5",
                "answer": """<b>HTML5:</b> HTML5 is the fifth and current major version of the Hypertext Markup Language (HTML), the standard markup language used for structuring and presenting content on the World Wide Web. It was developed by the W3C (World Wide Web Consortium) and WHATWG (Web Hypertext Application Technology Working Group) and became a W3C Recommendation in October 2014. HTML5 introduces new elements, attributes, and behaviors, and provides a larger set of technologies that allows building diverse and powerful Web sites and applications.<br/><br/>
<b>Characteristics of HTML5:</b><br/>
1. <b>Semantic Elements:</b> HTML5 introduces semantic tags that clearly describe their meaning to both the browser and the developer. Examples include &lt;header&gt;, &lt;footer&gt;, &lt;article&gt;, &lt;section&gt;, &lt;nav&gt;, &lt;aside&gt;, and &lt;main&gt;. These improve accessibility and SEO.<br/>
2. <b>Multimedia Support:</b> Native support for audio and video through &lt;audio&gt; and &lt;video&gt; tags without requiring third-party plugins like Flash. The &lt;canvas&gt; element enables dynamic, scriptable rendering of 2D shapes and bitmap images.<br/>
3. <b>Graphics and Effects:</b> The &lt;canvas&gt; element allows drawing graphics via JavaScript. SVG (Scalable Vector Graphics) is also supported natively for resolution-independent graphics.<br/>
4. <b>Form Enhancements:</b> New input types such as email, url, date, time, number, range, color, and search. New form attributes like placeholder, required, pattern, autofocus, and autocomplete improve user experience and validation.<br/>
5. <b>Geolocation API:</b> Allows websites to access the user's geographical location with permission, enabling location-based services.<br/>
6. <b>Local Storage:</b> HTML5 provides web storage mechanisms — localStorage (persistent) and sessionStorage (per-session) — allowing websites to store data locally within the user's browser, replacing cookies for larger storage needs.<br/>
7. <b>Offline Web Applications:</b> The Application Cache (AppCache) and Service Workers enable web applications to work offline by caching resources locally.<br/>
8. <b>Drag and Drop:</b> Native API for dragging and dropping elements within a webpage, enabling intuitive user interfaces.<br/>
9. <b>Web Workers:</b> Allows JavaScript to run in background threads, improving performance for computation-intensive tasks without blocking the UI.<br/>
10. <b>Cross-Document Messaging:</b> The postMessage API enables secure communication between documents from different origins (cross-origin messaging).<br/>
11. <b>Improved Code:</b> HTML5 provides cleaner, more consistent code with a simplified DOCTYPE (&lt;!DOCTYPE html&gt;) and charset declaration (&lt;meta charset="UTF-8"&gt;).""",
            },
            {
                "num": "3",
                "question": "Write HTML tag to generate the following table.",
                "marks": "5",
                "answer": """The table shows Average Red Eyes data for Males and Females with Weight and Eyes percentages.<br/><br/>
<b>HTML Code:</b><br/>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Average Red Eyes Table&lt;/title&gt;
    &lt;style&gt;
        table {
            border-collapse: collapse;
            width: 50%;
            margin: 20px auto;
        }
        th, td {
            border: 1px solid black;
            padding: 10px;
            text-align: center;
        }
        th {
            background-color: #f2f2f2;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;table&gt;
        &lt;tr&gt;
            &lt;th rowspan="2"&gt;Average&lt;/th&gt;
            &lt;th colspan="2"&gt;Red Eyes&lt;/th&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
            &lt;th&gt;Weight&lt;/th&gt;
            &lt;th&gt;Eyes&lt;/th&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
            &lt;td&gt;Males&lt;/td&gt;
            &lt;td&gt;1.45%&lt;/td&gt;
            &lt;td&gt;40%&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
            &lt;td&gt;Females&lt;/td&gt;
            &lt;td&gt;1.47%&lt;/td&gt;
            &lt;td&gt;43%&lt;/td&gt;
        &lt;/tr&gt;
    &lt;/table&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre><br/>
<b>Explanation:</b><br/>
• The &lt;table&gt; tag creates the table structure.<br/>
• &lt;tr&gt; defines each table row.<br/>
• &lt;th&gt; defines header cells with rowspan="2" for the "Average" cell spanning two rows, and colspan="2" for the "Red Eyes" header spanning two columns.<br/>
• &lt;td&gt; defines standard data cells for Males and Females rows with their respective values.<br/>
• CSS styling is applied for borders, padding, and background colors to make the table visually appealing.""",
            },
            {
                "num": "4",
                "question": "Design the following website's Menu with use of HTML list and appropriate CSS.",
                "marks": "5",
                "answer": """Design a horizontal website menu with items: Home | News | Contact | About using HTML list and CSS.<br/><br/>
<b>HTML and CSS Code:</b><br/>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Website Menu&lt;/title&gt;
    &lt;style&gt;
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
        }
        nav {
            background-color: #333;
            padding: 0;
        }
        nav ul {
            list-style-type: none;
            overflow: hidden;
            display: flex;
            justify-content: center;
        }
        nav ul li {
            display: inline-block;
        }
        nav ul li a {
            display: block;
            color: white;
            text-align: center;
            padding: 14px 20px;
            text-decoration: none;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        nav ul li a:hover {
            background-color: #555;
            color: #ffd700;
        }
        nav ul li a.active {
            background-color: #4CAF50;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;nav&gt;
        &lt;ul&gt;
            &lt;li&gt;&lt;a href="#home" class="active"&gt;Home&lt;/a&gt;&lt;/li&gt;
            &lt;li&gt;&lt;a href="#news"&gt;News&lt;/a&gt;&lt;/li&gt;
            &lt;li&gt;&lt;a href="#contact"&gt;Contact&lt;/a&gt;&lt;/li&gt;
            &lt;li&gt;&lt;a href="#about"&gt;About&lt;/a&gt;&lt;/li&gt;
        &lt;/ul&gt;
    &lt;/nav&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre><br/>
<b>Explanation:</b><br/>
• &lt;ul&gt; (unordered list) creates the menu structure with &lt;li&gt; (list items) for each menu option.<br/>
• list-style-type: none removes default bullet points.<br/>
• display: flex and justify-content: center create a horizontal, centered menu.<br/>
• The &lt;a&gt; tags inside &lt;li&gt; make each item clickable.<br/>
• padding: 14px 20px provides comfortable spacing around menu items.<br/>
• text-decoration: none removes underlines from links.<br/>
• :hover pseudo-class changes background and text color when mouse hovers.<br/>
• .active class highlights the current page with a different background color.""",
            },
            {
                "num": "5",
                "question": "Compare and contrast between a block-level element and an inline element in HTML?",
                "marks": "5",
                "answer": """<b>Block-Level Elements vs Inline Elements in HTML:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>Block-Level Elements</b></td><td><b>Inline Elements</b></td></tr>
<tr><td>Display Behavior</td><td>Always start on a new line and take up the full width available</td><td>Do not start on a new line and only take up as much width as necessary</td></tr>
<tr><td>Width</td><td>Occupy 100% of parent container width by default</td><td>Occupy only the space required by their content</td></tr>
<tr><td>Height</td><td>Height can be set explicitly; stacks vertically</td><td>Height and width cannot be set directly (ignored in standard HTML)</td></tr>
<tr><td>Margin & Padding</td><td>Respect all margin and padding properties (top, bottom, left, right)</td><td>Respect left and right margins/padding; top and bottom may not affect layout</td></tr>
<tr><td>Nesting</td><td>Can contain both block-level and inline elements</td><td>Can only contain data and other inline elements (not block-level)</td></tr>
<tr><td>Examples</td><td>&lt;div&gt;, &lt;p&gt;, &lt;h1&gt;-&lt;h6&gt;, &lt;ul&gt;, &lt;li&gt;, &lt;table&gt;, &lt;form&gt;, &lt;header&gt;, &lt;footer&gt;, &lt;section&gt;</td><td>&lt;span&gt;, &lt;a&gt;, &lt;img&gt;, &lt;strong&gt;, &lt;em&gt;, &lt;label&gt;, &lt;input&gt;, &lt;br&gt;, &lt;code&gt;</td></tr>
<tr><td>CSS Display</td><td>display: block (default)</td><td>display: inline (default)</td></tr>
<tr><td>Use Case</td><td>Structural layout, containers, sections, paragraphs</td><td>Styling text within content, links, emphasis, inline images</td></tr>
</table><br/><br/>
<b>Example Illustrating Both:</b><br/>
<pre>
&lt;div style="background-color: yellow;"&gt;
    This is a block-level div. It takes full width.
&lt;/div&gt;
&lt;p&gt;This is another block element.&lt;/p&gt;
&lt;span style="background-color: lightblue;"&gt;
    This is inline
&lt;/span&gt;
&lt;a href="#" style="background-color: lightgreen;"&gt;
    This link is also inline
&lt;/a&gt;
&lt;span&gt; — they sit side by side.&lt;/span&gt;
</pre><br/>
<b>Note:</b> CSS provides display: inline-block which combines characteristics of both — the element is inline (sits in text flow) but can have block-level properties like width, height, and vertical margins.""",
            },
            {
                "num": "6",
                "question": "What is CSS Selector? Explain different types of selector with suitable example.",
                "marks": "1+4",
                "answer": """<b>CSS Selector:</b> A CSS selector is a pattern used to select and target HTML elements that you want to style. Selectors are the bridge between your HTML structure and CSS rules. When a browser parses CSS, it uses selectors to determine which elements should receive the declared styles. CSS selectors can target elements by name, ID, class, attribute, state, or relationship to other elements.<br/><br/>
<b>Types of CSS Selectors with Examples:</b><br/><br/>
1. <b>Universal Selector (*):</b> Selects all elements on the page.<br/>
<pre>
* {
    margin: 0;
    padding: 0;
}
</pre><br/>
2. <b>Element/Type Selector:</b> Selects all elements of a specific type.<br/>
<pre>
p {
    color: blue;
    font-size: 16px;
}
</pre><br/>
3. <b>Class Selector (.):</b> Selects elements with a specific class attribute. Can be used multiple times.<br/>
<pre>
.highlight {
    background-color: yellow;
}
// HTML: &lt;p class="highlight"&gt;Important text&lt;/p&gt;
</pre><br/>
4. <b>ID Selector (#):</b> Selects a single element with a specific ID. Must be unique per page.<br/>
<pre>
#header {
    background-color: #333;
    color: white;
}
// HTML: &lt;div id="header"&gt;Welcome&lt;/div&gt;
</pre><br/>
5. <b>Descendant Selector (space):</b> Selects elements that are descendants of a specified element.<br/>
<pre>
div p {
    color: red;  // All &lt;p&gt; inside any &lt;div&gt;
}
</pre><br/>
6. <b>Child Selector (&gt;):</b> Selects direct children only.<br/>
<pre>
ul > li {
    list-style-type: square;  // Only direct &lt;li&gt; children of &lt;ul&gt;
}
</pre><br/>
7. <b>Adjacent Sibling Selector (+):</b> Selects an element immediately preceded by a specified element.<br/>
<pre>
h2 + p {
    font-style: italic;  // First &lt;p&gt; immediately after &lt;h2&gt;
}
</pre><br/>
8. <b>General Sibling Selector (~):</b> Selects all siblings preceded by a specified element.<br/>
<pre>
h2 ~ p {
    color: gray;  // All &lt;p&gt; siblings after &lt;h2&gt;
}
</pre><br/>
9. <b>Attribute Selector:</b> Selects elements based on an attribute or attribute value.<br/>
<pre>
input[type="text"] {
    border: 1px solid blue;
}
a[href^="https"] {
    color: green;  // Links starting with https
}
</pre><br/>
10. <b>Pseudo-class Selector (:):</b> Selects elements in a specific state.<br/>
<pre>
a:hover {
    color: red;
}
input:focus {
    border-color: orange;
}
li:nth-child(odd) {
    background-color: #f0f0f0;
}
</pre><br/>
11. <b>Pseudo-element Selector (::):</b> Selects specific parts of an element.<br/>
<pre>
p::first-line {
    font-weight: bold;
}
p::after {
    content: " ✓";
    color: green;
}
</pre>""",
            },
            {
                "num": "7",
                "question": "Why session is required in web development? Explain how you set and remove values stored in Session with suitable example?",
                "marks": "1+4",
                "answer": """<b>Why Session is Required in Web Development:</b><br/>
HTTP is a stateless protocol, meaning each request from a client to a server is independent and the server does not retain any information about previous requests. Sessions are required in web development to maintain state and persist user-specific data across multiple page requests. Key reasons for using sessions include:<br/>
1. <b>User Authentication:</b> Sessions keep users logged in as they navigate between pages.<br/>
2. <b>Shopping Carts:</b> E-commerce sites use sessions to remember items added to a cart.<br/>
3. <b>Personalization:</b> Remembering user preferences like language, theme, or settings.<br/>
4. <b>Form Data:</b> Preserving multi-step form data across pages.<br/>
5. <b>Security:</b> Storing sensitive information server-side rather than in cookies.<br/><br/>
<b>Setting and Removing Session Values (PHP Example):</b><br/><br/>
<b>Setting Session Values:</b><br/>
<pre>
&lt;?php
// Start the session (must be first before any output)
session_start();

// Set session variables
$_SESSION["username"] = "ram123";
$_SESSION["email"] = "ram@example.com";
$_SESSION["login_time"] = date("Y-m-d H:i:s");

echo "Session values set successfully!&lt;br&gt;";
echo "Welcome, " . $_SESSION["username"];
?&gt;
</pre><br/>
<b>Accessing Session Values:</b><br/>
<pre>
&lt;?php
session_start();

if (isset($_SESSION["username"])) {
    echo "User: " . $_SESSION["username"] . "&lt;br&gt;";
    echo "Email: " . $_SESSION["email"];
} else {
    echo "No session data found.";
}
?&gt;
</pre><br/>
<b>Removing Session Values:</b><br/>
<pre>
&lt;?php
session_start();

// Remove a single session variable
unset($_SESSION["email"]);
echo "Email removed from session.&lt;br&gt;";

// Remove all session variables
$_SESSION = array();
echo "All session variables cleared.&lt;br&gt;";

// Destroy the session completely
session_destroy();
echo "Session destroyed.";
?&gt;
</pre><br/>
<b>Logout Example:</b><br/>
<pre>
&lt;?php
session_start();
$_SESSION = array();

// Also delete the session cookie
if (isset($_COOKIE[session_name()])) {
    setcookie(session_name(), '', time()-3600, '/');
}

session_destroy();
header("Location: login.php");
exit();
?&gt;
</pre><br/>
<b>Explanation:</b><br/>
• session_start() must be called at the beginning of every PHP page that uses sessions.<br/>
• $_SESSION is a superglobal array used to store session data.<br/>
• unset() removes a specific session variable.<br/>
• $_SESSION = array() clears all session data.<br/>
• session_destroy() destroys the session file on the server.<br/>
• The session ID is typically passed via a cookie, which should also be cleared during logout.""",
            },
            {
                "num": "8",
                "question": "Critically analysis the pitfall of the 3-tier technology in comparison with n-tier technology.",
                "marks": "5",
                "answer": """<b>Critical Analysis: Pitfalls of 3-Tier Technology vs N-Tier Technology</b><br/><br/>
<b>3-Tier Architecture:</b> Consists of Presentation Tier (UI), Application Tier (Business Logic), and Data Tier (Database).<br/><br/>
<b>N-Tier Architecture:</b> Extends 3-tier by further decomposing tiers into more specialized layers (e.g., separating business logic into service layer, domain layer, validation layer, caching layer, etc.).<br/><br/>
<b>Pitfalls of 3-Tier compared to N-Tier:</b><br/><br/>
1. <b>Limited Scalability:</b><br/>
   In 3-tier, the application tier handles all business logic, which can become a bottleneck as user load increases. N-tier distributes functionality across multiple specialized servers, allowing independent scaling of specific components (e.g., scaling only the caching layer without scaling the entire application tier).<br/><br/>
2. <b>Tight Coupling:</b><br/>
   3-tier tends to bundle many responsibilities into a single application tier, leading to tight coupling between different business functions. N-tier promotes loose coupling by separating concerns into distinct, independent services that communicate through well-defined APIs.<br/><br/>
3. <b>Poor Maintainability:</b><br/>
   As applications grow, the monolithic application tier in 3-tier becomes complex and difficult to maintain. A change in one business rule may affect unrelated functionality. N-tier isolates changes to specific layers, reducing the risk of unintended side effects.<br/><br/>
4. <b>Technology Stack Constraints:</b><br/>
   In 3-tier, all business logic typically uses the same technology stack. N-tier allows different tiers to use the most appropriate technology for their specific purpose (e.g., Node.js for API gateway, Python for data processing, Java for business rules).<br/><br/>
5. <b>Deployment Challenges:</b><br/>
   Deploying updates in 3-tier often requires redeploying the entire application tier, causing downtime. N-tier enables independent deployment of individual services, supporting continuous delivery and reducing deployment risk.<br/><br/>
6. <b>Fault Isolation:</b><br/>
   In 3-tier, a failure in one part of the application tier can bring down the entire tier. N-tier provides better fault isolation — if the notification service fails, other services continue functioning.<br/><br/>
<b>When 3-Tier is Still Appropriate:</b><br/>
• Small to medium applications with straightforward requirements<br/>
• Projects with limited budget and development resources<br/>
• Applications where simplicity is preferred over flexibility<br/>
• Teams without microservices or distributed systems expertise<br/><br/>
<b>Conclusion:</b> While 3-tier is simpler to design and implement initially, it struggles with the demands of large, complex, evolving applications. N-tier (and its modern evolution, microservices) provides superior scalability, maintainability, and flexibility at the cost of increased complexity in deployment, monitoring, and inter-service communication.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Design the following layout of webpage with use of div and appropriate CSS.",
                "marks": "10",
                "answer": """Design a webpage layout with Logo, Navigation, Header Banner, Side Bar, Body Area, and Footer sections using div and CSS.<br/><br/>
<b>HTML Code:</b><br/>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Webpage Layout&lt;/title&gt;
    &lt;style&gt;
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: Arial, sans-serif;
        }
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
        }
        #logo {
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            text-align: left;
            font-size: 24px;
            font-weight: bold;
        }
        #navigation {
            background-color: #34495e;
            padding: 15px;
        }
        #navigation ul {
            list-style: none;
            display: flex;
        }
        #navigation ul li {
            margin-right: 20px;
        }
        #navigation ul li a {
            color: white;
            text-decoration: none;
            font-size: 16px;
        }
        #navigation ul li a:hover {
            color: #3498db;
        }
        #header-banner {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 60px 20px;
            text-align: center;
            font-size: 28px;
        }
        .content-wrapper {
            display: flex;
            min-height: 400px;
        }
        #sidebar {
            width: 25%;
            background-color: #ecf0f1;
            padding: 20px;
        }
        #sidebar h3 {
            margin-bottom: 15px;
            color: #2c3e50;
        }
        #sidebar ul {
            list-style: none;
        }
        #sidebar ul li {
            padding: 10px 0;
            border-bottom: 1px solid #bdc3c7;
        }
        #body-area {
            width: 75%;
            padding: 20px;
            background-color: #ffffff;
        }
        #body-area h2 {
            color: #2c3e50;
            margin-bottom: 15px;
        }
        #body-area p {
            line-height: 1.6;
            color: #555;
        }
        #footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container"&gt;
        &lt;div id="logo"&gt;MyWebsite Logo&lt;/div&gt;
        
        &lt;div id="navigation"&gt;
            &lt;ul&gt;
                &lt;li&gt;&lt;a href="#"&gt;Home&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;About&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Services&lt;/a&gt;&lt;/li&gt;
                &lt;li&gt;&lt;a href="#"&gt;Contact&lt;/a&gt;&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/div&gt;
        
        &lt;div id="header-banner"&gt;
            Welcome to Our Website
        &lt;/div&gt;
        
        &lt;div class="content-wrapper"&gt;
            &lt;div id="sidebar"&gt;
                &lt;h3&gt;Sidebar&lt;/h3&gt;
                &lt;ul&gt;
                    &lt;li&gt;Category 1&lt;/li&gt;
                    &lt;li&gt;Category 2&lt;/li&gt;
                    &lt;li&gt;Category 3&lt;/li&gt;
                    &lt;li&gt;Category 4&lt;/li&gt;
                &lt;/ul&gt;
            &lt;/div&gt;
            &lt;div id="body-area"&gt;
                &lt;h2&gt;Body Area&lt;/h2&gt;
                &lt;p&gt;This is the main content area of the webpage. 
                Here you can place articles, blog posts, product 
                information, or any other primary content. The layout 
                uses CSS Flexbox to create a responsive two-column 
                design with a sidebar and main body area.&lt;/p&gt;
            &lt;/div&gt;
        &lt;/div&gt;
        
        &lt;div id="footer"&gt;
            &amp;copy; 2020 MyWebsite. All rights reserved.
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre><br/>
<b>Explanation:</b><br/>
• Each section (logo, navigation, header-banner, sidebar, body-area, footer) is enclosed in a &lt;div&gt; with a unique ID.<br/>
• The container div centers the layout and sets a maximum width.<br/>
• display: flex on content-wrapper creates the two-column layout for sidebar and body area.<br/>
• width: 25% for sidebar and width: 75% for body area divides the space proportionally.<br/>
• CSS styling provides colors, padding, and responsive behavior for each section.""",
            },
            {
                "num": "10",
                "question": "Write a server-site script for login process assume that user name and password have already exist on database TU under the user table (id, user, password).",
                "marks": "10",
                "answer": """<b>Server-Side Login Script (PHP with MySQL):</b><br/><br/>
<b>Database Setup:</b><br/>
<pre>
CREATE DATABASE TU;
USE TU;

CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

-- Insert sample users (passwords should be hashed in production)
INSERT INTO user (user, password) VALUES 
('admin', MD5('admin123')),
('student1', MD5('pass123')),
('ram', MD5('ram2020'));
</pre><br/>
<b>Login Form (login.html):</b><br/>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Login&lt;/title&gt;
    &lt;style&gt;
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-box {
            background: white;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width: 350px;
        }
        .login-box h2 {
            text-align: center;
            color: #333;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            color: #555;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 14px;
        }
        .form-group input[type="submit"] {
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
            font-size: 16px;
            padding: 12px;
        }
        .form-group input[type="submit"]:hover {
            background-color: #45a049;
        }
        .links {
            text-align: center;
            margin-top: 15px;
        }
        .links a {
            color: #4CAF50;
            text-decoration: none;
            font-size: 14px;
        }
        .error {
            color: red;
            text-align: center;
            margin-bottom: 15px;
        }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="login-box"&gt;
        &lt;h2&gt;Login Form&lt;/h2&gt;
        &lt;form action="login.php" method="POST"&gt;
            &lt;div class="form-group"&gt;
                &lt;label&gt;User Name&lt;/label&gt;
                &lt;input type="text" name="username" required&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
                &lt;label&gt;Password&lt;/label&gt;
                &lt;input type="password" name="password" required&gt;
            &lt;/div&gt;
            &lt;div class="form-group"&gt;
                &lt;input type="submit" name="login" value="Login"&gt;
            &lt;/div&gt;
            &lt;div class="links"&gt;
                &lt;a href="#"&gt;Lost your password?&lt;/a&gt;&lt;br&gt;&lt;br&gt;
                &lt;a href="#"&gt;Don't have an account? Signup here!&lt;/a&gt;
            &lt;/div&gt;
        &lt;/form&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre><br/>
<b>Login Processing Script (login.php):</b><br/>
<pre>
&lt;?php
session_start();

// Database connection
$host = "localhost";
$dbuser = "root";
$dbpass = "";
$dbname = "TU";

$conn = new mysqli($host, $dbuser, $dbpass, $dbname);

if ($conn-&gt;connect_error) {
    die("Connection failed: " . $conn-&gt;connect_error);
}

if (isset($_POST['login'])) {
    $username = $conn-&gt;real_escape_string($_POST['username']);
    $password = md5($_POST['password']); // MD5 for demo; use password_hash() in production
    
    $sql = "SELECT * FROM user WHERE user='$username' AND password='$password'";
    $result = $conn-&gt;query($sql);
    
    if ($result-&gt;num_rows == 1) {
        $row = $result-&gt;fetch_assoc();
        $_SESSION['user_id'] = $row['id'];
        $_SESSION['username'] = $row['user'];
        
        echo "&lt;script&gt;alert('Login Successful!');&lt;/script&gt;";
        echo "Welcome, " . $_SESSION['username'] . "!";
        // header("Location: dashboard.php");
    } else {
        echo "&lt;script&gt;alert('Invalid username or password!');&lt;/script&gt;";
        echo "&lt;a href='login.html'&gt;Go Back&lt;/a&gt;";
    }
}

$conn-&gt;close();
?&gt;
</pre><br/>
<b>Secure Version with Prepared Statements (login_secure.php):</b><br/>
<pre>
&lt;?php
session_start();
$conn = new mysqli("localhost", "root", "", "TU");

if (isset($_POST['login'])) {
    $stmt = $conn-&gt;prepare("SELECT id, user FROM user WHERE user = ? AND password = MD5(?)");
    $stmt-&gt;bind_param("ss", $_POST['username'], $_POST['password']);
    $stmt-&gt;execute();
    $result = $stmt-&gt;get_result();
    
    if ($result-&gt;num_rows == 1) {
        $user = $result-&gt;fetch_assoc();
        $_SESSION['user_id'] = $user['id'];
        $_SESSION['username'] = $user['user'];
        header("Location: dashboard.php");
        exit();
    } else {
        header("Location: login.html?error=invalid");
        exit();
    }
}
?&gt;
</pre><br/>
<b>Explanation:</b><br/>
• The login form collects username and password via POST method.<br/>
• login.php connects to the TU database and queries the user table.<br/>
• Passwords are compared using MD5 hashing (for demonstration; production should use password_hash() and password_verify()).<br/>
• On successful login, session variables are set and user is redirected.<br/>
• The secure version uses prepared statements to prevent SQL injection attacks.""",
            },
            {
                "num": "11",
                "question": "What are the rules for Well-formed xml document? Create a sample well-formed xml and validate it with DTD Schema.",
                "marks": "5+5",
                "answer": """<b>Rules for Well-Formed XML Document:</b><br/>
A well-formed XML document must follow these syntactic rules defined by the W3C XML specification:<br/>
1. <b>Prolog:</b> The document should begin with an XML declaration (optional but recommended): &lt;?xml version="1.0" encoding="UTF-8"?&gt;<br/>
2. <b>Single Root Element:</b> There must be exactly one root element that contains all other elements.<br/>
3. <b>Proper Nesting:</b> All elements must be properly nested. Overlapping tags are not allowed (&lt;b&gt;&lt;i&gt;text&lt;/i&gt;&lt;/b&gt; is correct; &lt;b&gt;&lt;i&gt;text&lt;/b&gt;&lt;/i&gt; is incorrect).<br/>
4. <b>Closing Tags:</b> Every opening tag must have a corresponding closing tag, unless it is an empty element which must be self-closing (&lt;br/&gt; or &lt;br&gt;&lt;/br&gt;).<br/>
5. <b>Case Sensitivity:</b> XML is case-sensitive. Opening and closing tags must match exactly (&lt;Book&gt; and &lt;/book&gt; are different).<br/>
6. <b>Attribute Quotes:</b> All attribute values must be enclosed in either single or double quotation marks.<br/>
7. <b>Unique Attributes:</b> An element cannot have two attributes with the same name.<br/>
8. <b>Special Characters:</b> Certain characters (&lt;, &gt;, &amp;, ', ") must be escaped using entities (&amp;lt;, &amp;gt;, &amp;amp;, &amp;apos;, &amp;quot;) or placed in CDATA sections.<br/>
9. <b>Valid Names:</b> Element and attribute names must start with a letter or underscore, not a number or special character (except underscore).<br/>
10. <b>No Spaces in Tags:</b> There should be no spaces between the opening bracket and the element name (&lt; book&gt; is invalid).<br/><br/>
<b>Sample Well-Formed XML Document:</b><br/>
<pre>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;!DOCTYPE library SYSTEM "library.dtd"&gt;
&lt;library&gt;
    &lt;book id="b001"&gt;
        &lt;title&gt;Data Structures&lt;/title&gt;
        &lt;author&gt;Mark Allen Weiss&lt;/author&gt;
        &lt;year&gt;2018&lt;/year&gt;
        &lt;price&gt;45.00&lt;/price&gt;
    &lt;/book&gt;
    &lt;book id="b002"&gt;
        &lt;title&gt;Web Technology&lt;/title&gt;
        &lt;author&gt;Robert W. Sebesta&lt;/author&gt;
        &lt;year&gt;2019&lt;/year&gt;
        &lt;price&gt;38.50&lt;/price&gt;
    &lt;/book&gt;
    &lt;book id="b003"&gt;
        &lt;title&gt;System Analysis&lt;/title&gt;
        &lt;author&gt;Jeffrey L. Whitten&lt;/author&gt;
        &lt;year&gt;2020&lt;/year&gt;
        &lt;price&gt;52.00&lt;/price&gt;
    &lt;/book&gt;
&lt;/library&gt;
</pre><br/>
<b>DTD Schema (library.dtd):</b><br/>
<pre>
&lt;!DOCTYPE library [
    &lt;!ELEMENT library (book+)&gt;
    &lt;!ELEMENT book (title, author, year, price)&gt;
    &lt;!ATTLIST book id ID #REQUIRED&gt;
    &lt;!ELEMENT title (#PCDATA)&gt;
    &lt;!ELEMENT author (#PCDATA)&gt;
    &lt;!ELEMENT year (#PCDATA)&gt;
    &lt;!ELEMENT price (#PCDATA)&gt;
]&gt;
</pre><br/>
<b>DTD Explanation:</b><br/>
• &lt;!ELEMENT library (book+)&gt; — The library element must contain one or more book elements.<br/>
• &lt;!ELEMENT book (title, author, year, price)&gt; — Each book element must contain exactly one title, author, year, and price in that order.<br/>
• &lt;!ATTLIST book id ID #REQUIRED&gt; — The book element must have an id attribute of type ID, which is required and must be unique.<br/>
• &lt;!ELEMENT title (#PCDATA)&gt; — The title element contains parsed character data (text).<br/>
• Similarly, author, year, and price contain #PCDATA.<br/><br/>
<b>How to Validate:</b><br/>
1. Save the XML as library.xml and DTD as library.dtd in the same directory.<br/>
2. Use an XML parser or validator tool (like XMLSpy, Oxygen XML Editor, or online validators).<br/>
3. In PHP, use DOMDocument:<br/>
<pre>
&lt;?php
$xml = new DOMDocument();
$xml-&gt;load('library.xml');
if ($xml-&gt;validate()) {
    echo "XML is valid according to DTD!";
} else {
    echo "XML is NOT valid!";
}
?&gt;
</pre><br/>
4. In Python, use lxml:<br/>
<pre>
from lxml import etree

dtd = etree.DTD(open('library.dtd'))
tree = etree.parse('library.xml')
print(dtd.validate(tree))  # True if valid
</pre>""",
            },
        ]
    }
]

generate_answer_sheet("CACS205", "web-technology", "Web Technology", 2020, "semester-3", CACS205_2020)
