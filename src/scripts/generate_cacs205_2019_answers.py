#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS205_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt all. [10×1=10]",
        "questions": [
            {
                "num": "1",
                "question": """i) Why we use XSLT language?<br/>
a) Use to delete XML nodes &nbsp;&nbsp; b) Use to rename XML nodes &nbsp;&nbsp; c) Use to transform XML documents &nbsp;&nbsp; d) Use to sort XML nodes<br/><br/>
ii) Which is the correct CSS syntax?<br/>
a) body {color: black} &nbsp;&nbsp; b) body:color=black &nbsp;&nbsp; c) {body;color:black} &nbsp;&nbsp; d) {body=color:black}<br/><br/>
iii) SQL Query to delete all rows in a table without deleting the table structure?<br/>
a) DELETE FROM table_name; &nbsp;&nbsp; b) DROP TABLE table_name; &nbsp;&nbsp; c) REMOVE FROM table_name; &nbsp;&nbsp; d) TRUNCATE table_name;<br/><br/>
iv) Web design that makes your web page look good on all devices?<br/>
a) Static web design &nbsp;&nbsp; b) Dynamic web design &nbsp;&nbsp; c) Responsive web design &nbsp;&nbsp; d) Adaptive web design<br/><br/>
v) Constraint on the data per cookie?<br/>
a) 1 KB &nbsp;&nbsp; b) 2 KB &nbsp;&nbsp; c) 4 KB &nbsp;&nbsp; d) 8 KB<br/><br/>
vi) Which is not an inline element?<br/>
a) &lt;span&gt; &nbsp;&nbsp; b) &lt;a&gt; &nbsp;&nbsp; c) &lt;img&gt; &nbsp;&nbsp; d) &lt;div&gt;<br/><br/>
vii) Which is wrong in XQuery?<br/>
a) Used to query XML data &nbsp;&nbsp; b) Built on XPath expressions &nbsp;&nbsp; c) Used to generate tables for XSLT &nbsp;&nbsp; d) Used to extract and manipulate data from XML<br/><br/>
viii) Which method has much larger limit on amount of data that can be passed to web server?<br/>
a) Get method &nbsp;&nbsp; b) Post method &nbsp;&nbsp; c) Put method &nbsp;&nbsp; d) Delete method<br/><br/>
ix) In HTML form &lt;input type="text"&gt; is used for?<br/>
a) One-line text &nbsp;&nbsp; b) Multi-line text &nbsp;&nbsp; c) Password field &nbsp;&nbsp; d) Hidden field<br/><br/>
x) Which inline function embeds an independent HTML document into current document?<br/>
a) &lt;frame&gt; &nbsp;&nbsp; b) &lt;object&gt; &nbsp;&nbsp; c) &lt;iframe&gt; &nbsp;&nbsp; d) &lt;embed&gt;""",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>i) c) Use to transform XML documents</b> — XSLT (Extensible Stylesheet Language Transformations) is a language used to transform XML documents into other formats such as HTML, plain text, or another XML document. It uses XPath to navigate XML documents and define transformation rules.<br/><br/>
<b>ii) a) body {color: black}</b> — CSS syntax follows the pattern: selector {property: value;}. The correct syntax is <b>body {color: black;}</b> where 'body' is the selector, 'color' is the property, and 'black' is the value.<br/><br/>
<b>iii) a) DELETE FROM table_name;</b> — The DELETE statement removes all rows from a table while preserving the table structure, constraints, and indexes. TRUNCATE also removes all rows but is a DDL command. DROP TABLE removes the entire table including its structure.<br/><br/>
<b>iv) c) Responsive web design</b> — Responsive web design uses CSS media queries, flexible grids, and fluid images to automatically adjust the layout and content based on the screen size and orientation of the device (mobile, tablet, desktop).<br/><br/>
<b>v) c) 4 KB</b> — Cookies are limited to approximately 4 KB (4096 bytes) of data per cookie. Browsers also limit the total number of cookies per domain (typically around 20-50 cookies).<br/><br/>
<b>vi) d) &lt;div&gt;</b> — &lt;div&gt; is a block-level element that takes up the full width available and starts on a new line. &lt;span&gt;, &lt;a&gt;, and &lt;img&gt; are all inline elements that flow within text without breaking the line.<br/><br/>
<b>vii) c) Used to generate tables for XSLT</b> — This statement is wrong. XQuery is a query language for XML (like SQL for databases), built on XPath expressions. It is used to query, extract, and manipulate data from XML documents. XSLT is the language used for transforming XML, not XQuery.<br/><br/>
<b>viii) b) Post method</b> — The POST method sends data in the HTTP request body, allowing much larger amounts of data to be transmitted compared to GET, which appends data to the URL (limited by URL length, typically ~2048 characters). POST is also more secure for sensitive data.<br/><br/>
<b>ix) a) One-line text</b> — The &lt;input type="text"&gt; creates a single-line text input field where users can enter short text. For multi-line text, the &lt;textarea&gt; element is used.<br/><br/>
<b>x) c) &lt;iframe&gt;</b> — The &lt;iframe&gt; (inline frame) element embeds an independent HTML document within the current document. It is commonly used to embed external content such as maps, videos, or other web pages."""
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What is HTML Link? Explain different links used in HTML.",
                "marks": "1+4",
                "answer": """<b>HTML Link:</b><br/>
An HTML link (or hyperlink) is a reference to another resource on the web. It allows users to navigate from one page to another, download files, send emails, or jump to specific sections within the same page. Links are created using the <b>&lt;a&gt;</b> (anchor) tag with the <b>href</b> attribute.<br/><br/>
<b>Syntax:</b> &lt;a href="url"&gt;Link Text&lt;/a&gt;<br/><br/>
<b>Different Types of Links in HTML:</b><br/><br/>
<b>1. External Link (Absolute URL):</b> Links to a page on another website.<br/>
&lt;a href="https://www.example.com"&gt;Visit Example&lt;/a&gt;<br/><br/>
<b>2. Internal Link (Relative URL):</b> Links to a page within the same website.<br/>
&lt;a href="about.html"&gt;About Us&lt;/a&gt;<br/>
&lt;a href="/contact.html"&gt;Contact&lt;/a&gt;<br/><br/>
<b>3. Anchor Link (Bookmark):</b> Links to a specific section within the same page using id.<br/>
&lt;a href="#section1"&gt;Go to Section 1&lt;/a&gt;<br/>
&lt;h2 id="section1"&gt;Section 1&lt;/h2&gt;<br/><br/>
<b>4. Email Link:</b> Opens the default email client with a pre-filled address.<br/>
&lt;a href="mailto:someone@example.com"&gt;Send Email&lt;/a&gt;<br/><br/>
<b>5. Download Link:</b> Prompts the user to download a file.<br/>
&lt;a href="document.pdf" download&gt;Download PDF&lt;/a&gt;<br/><br/>
<b>6. Telephone Link:</b> Initiates a phone call on mobile devices.<br/>
&lt;a href="tel:+9771234567890"&gt;Call Us&lt;/a&gt;<br/><br/>
<b>7. Target Attribute:</b> Controls where the linked document opens.<br/>
&lt;a href="https://example.com" target="_blank"&gt;Open in New Tab&lt;/a&gt;"""
            },
            {
                "num": "3",
                "question": "Write HTML tags to generate a table with columns: Routine, Sunday, Monday, Break, Tuesday and rows: WT, DSA, SAD, Java, Statistics, Math.",
                "marks": "5",
                "answer": """<b>HTML Code for Class Routine Table:</b><br/>
<pre>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Class Routine&lt;/title&gt;
    &lt;style&gt;
        table { border-collapse: collapse; width: 80%; margin: auto; }
        th, td { border: 1px solid black; padding: 10px; text-align: center; }
        th { background-color: #4CAF50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;table&gt;
        &lt;tr&gt;
            &lt;th&gt;Routine&lt;/th&gt;
            &lt;th&gt;Sunday&lt;/th&gt;
            &lt;th&gt;Monday&lt;/th&gt;
            &lt;th&gt;Break&lt;/th&gt;
            &lt;th&gt;Tuesday&lt;/th&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
            &lt;td&gt;WT&lt;/td&gt;
            &lt;td&gt;DSA&lt;/td&gt;
            &lt;td&gt;SAD&lt;/td&gt;
            &lt;td&gt;-&lt;/td&gt;
            &lt;td&gt;Java&lt;/td&gt;
        &lt;/tr&gt;
        &lt;tr&gt;
            &lt;td&gt;Statistics&lt;/td&gt;
            &lt;td&gt;Math&lt;/td&gt;
            &lt;td&gt;-&lt;/td&gt;
            &lt;td&gt;-&lt;/td&gt;
            &lt;td&gt;WT&lt;/td&gt;
        &lt;/tr&gt;
    &lt;/table&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>"""
            },
            {
                "num": "4",
                "question": "Write HTML tags to generate nested list output: FOHSS (BCA -> IoT, BSW), FOM (BIM, BBA).",
                "marks": "5",
                "answer": """<b>HTML Code for Nested List:</b><br/>
<pre>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Nested List&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;ul&gt;
        &lt;li&gt;FOHSS
            &lt;ul&gt;
                &lt;li&gt;BCA
                    &lt;ul&gt;
                        &lt;li&gt;IoT&lt;/li&gt;
                        &lt;li&gt;BSW&lt;/li&gt;
                    &lt;/ul&gt;
                &lt;/li&gt;
            &lt;/ul&gt;
        &lt;/li&gt;
        &lt;li&gt;FOM
            &lt;ul&gt;
                &lt;li&gt;BIM&lt;/li&gt;
                &lt;li&gt;BBA&lt;/li&gt;
            &lt;/ul&gt;
        &lt;/li&gt;
    &lt;/ul&gt;
&lt;/body&gt;
&lt;/html&gt;</pre><br/>
<b>Output:</b><br/>
• FOHSS<br/>
&nbsp;&nbsp;○ BCA<br/>
&nbsp;&nbsp;&nbsp;&nbsp;▪ IoT<br/>
&nbsp;&nbsp;&nbsp;&nbsp;▪ BSW<br/>
• FOM<br/>
&nbsp;&nbsp;○ BIM<br/>
&nbsp;&nbsp;○ BBA"""
            },
            {
                "num": "5",
                "question": '"It is discouraged to use frame in web development" Explain the reasons.',
                "marks": "5",
                "answer": """<b>Reasons Why Frames Are Discouraged in Web Development:</b><br/><br/>
<b>1. Deprecated in HTML5:</b><br/>
The &lt;frame&gt; and &lt;frameset&gt; tags have been removed from the HTML5 specification. Modern browsers still support them for backward compatibility, but they are considered obsolete. The &lt;iframe&gt; element is the recommended alternative for embedding content.<br/><br/>
<b>2. Poor Accessibility:</b><br/>
Screen readers and assistive technologies struggle with frames because they treat each frame as a separate document. Users with disabilities may find it difficult to navigate between frames and understand the overall page structure.<br/><br/>
<b>3. SEO (Search Engine Optimization) Issues:</b><br/>
Search engines have difficulty indexing content within frames. Each frame loads a separate HTML document, making it hard for search engines to understand the relationship between the content and to index the complete page properly. This negatively impacts search rankings.<br/><br/>
<b>4. Bookmarking and URL Problems:</b><br/>
When a page uses frames, the browser's address bar shows only the URL of the frameset document, not the individual frames. Users cannot bookmark or share specific content within a frame, and the back/forward navigation buttons may behave unexpectedly.<br/><br/>
<b>5. Mobile Responsiveness:</b><br/>
Frames are not responsive by design. They do not adapt well to different screen sizes, making websites with frames unusable on mobile devices and tablets. Modern responsive design techniques (CSS Flexbox, Grid) provide much better solutions.<br/><br/>
<b>6. Maintenance Difficulty:</b><br/>
Websites built with frames are harder to maintain and update. Navigation menus embedded in separate frames require changes across multiple files. Modern templating systems and server-side includes offer better alternatives.<br/><br/>
<b>7. Usability Issues:</b><br/>
Frames create confusing user experiences. Users cannot easily print the entire page, scroll behavior becomes inconsistent across frames, and the page may display differently across browsers."""
            },
            {
                "num": "6",
                "question": "What is the strength of CSS? What are the various approaches to include CSS document in HTML?",
                "marks": "1+4",
                "answer": """<b>Strength of CSS (Cascading Style Sheets):</b><br/><br/>
<b>1. Separation of Content and Presentation:</b> CSS separates the structure (HTML) from the styling, making code cleaner and easier to maintain.<br/><br/>
<b>2. Reusability:</b> A single CSS file can style multiple HTML pages, ensuring consistency across an entire website.<br/><br/>
<b>3. Consistent Design:</b> Changes made to the CSS file are automatically applied to all linked pages, ensuring uniform appearance.<br/><br/>
<b>4. Faster Page Loading:</b> External CSS files are cached by browsers, reducing load times for subsequent pages.<br/><br/>
<b>5. Responsive Design:</b> CSS media queries enable websites to adapt to different screen sizes and devices.<br/><br/>
<b>6. Enhanced Accessibility:</b> CSS allows developers to create accessible designs that work with screen readers and assistive technologies.<br/><br/>
<b>7. Print-Friendly Pages:</b> CSS can define separate styles for printing, hiding unnecessary elements and optimizing layout.<br/><br/>
<b>8. Advanced Visual Effects:</b> CSS supports animations, transitions, gradients, shadows, and transforms without requiring JavaScript or images.<br/><br/>
<b>Various Approaches to Include CSS in HTML:</b><br/><br/>
<b>1. Inline CSS:</b> Styles are applied directly to individual HTML elements using the style attribute.<br/>
&lt;p style="color: blue; font-size: 16px;"&gt;This is a blue paragraph.&lt;/p&gt;<br/><br/>
<b>2. Internal (Embedded) CSS:</b> Styles are defined within the &lt;style&gt; tag in the &lt;head&gt; section of the HTML document.<br/>
&lt;head&gt;<br/>
&nbsp;&nbsp;&lt;style&gt;<br/>
&nbsp;&nbsp;&nbsp;&nbsp;body { background-color: lightgray; }<br/>
&nbsp;&nbsp;&nbsp;&nbsp;h1 { color: navy; }<br/>
&nbsp;&nbsp;&lt;/style&gt;<br/>
&lt;/head&gt;<br/><br/>
<b>3. External CSS:</b> Styles are written in a separate .css file and linked to the HTML document using the &lt;link&gt; tag. This is the recommended approach.<br/>
&lt;head&gt;<br/>
&nbsp;&nbsp;&lt;link rel="stylesheet" type="text/css" href="styles.css"&gt;<br/>
&lt;/head&gt;<br/><br/>
<b>4. @import Rule:</b> CSS files can import other CSS files using the @import rule within a &lt;style&gt; tag or external CSS file.<br/>
&lt;style&gt;<br/>
&nbsp;&nbsp;@import url("external.css");<br/>
&lt;/style&gt;"""
            },
            {
                "num": "7",
                "question": "What is cookie? Explain how you set and remove values stored in cookie with suitable example.",
                "marks": "1+4",
                "answer": """<b>Cookie:</b><br/>
A cookie is a small piece of data (text file) stored on the user's computer by a web browser at the request of a web server. Cookies are used to remember user preferences, login sessions, shopping cart items, and track user behavior. Each cookie has a name, value, expiration date, domain, and path. The maximum size of a cookie is approximately 4 KB.<br/><br/>
<b>Setting and Removing Cookies:</b><br/><br/>
Cookies can be created, read, and deleted using JavaScript or server-side scripts. Here is an example using JavaScript:<br/><br/>
<pre>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Cookie Example&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h2&gt;Cookie Demo&lt;/h2&gt;
    &lt;button onclick="setCookie()"&gt;Set Cookie&lt;/button&gt;
    &lt;button onclick="getCookie()"&gt;Get Cookie&lt;/button&gt;
    &lt;button onclick="removeCookie()"&gt;Remove Cookie&lt;/button&gt;
    &lt;p id="output"&gt;&lt;/p&gt;

    &lt;script&gt;
        // Function to set a cookie
        function setCookie() {
            var username = "JohnDoe";
            var expires = new Date();
            expires.setTime(expires.getTime() + (7 * 24 * 60 * 60 * 1000)); // 7 days
            document.cookie = "username=" + username + ";expires=" + expires.toUTCString() + ";path=/";
            document.getElementById("output").innerHTML = "Cookie set successfully!";
        }

        // Function to get a cookie
        function getCookie() {
            var name = "username=";
            var decodedCookie = decodeURIComponent(document.cookie);
            var cookieArray = decodedCookie.split(';');
            for(var i = 0; i &lt; cookieArray.length; i++) {
                var c = cookieArray[i].trim();
                if (c.indexOf(name) == 0) {
                    document.getElementById("output").innerHTML = 
                        "Cookie value: " + c.substring(name.length, c.length);
                    return;
                }
            }
            document.getElementById("output").innerHTML = "Cookie not found!";
        }

        // Function to remove/delete a cookie
        function removeCookie() {
            document.cookie = "username=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;";
            document.getElementById("output").innerHTML = "Cookie removed successfully!";
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;</pre><br/>
<b>Explanation:</b><br/>
<b>Setting a Cookie:</b> Use <b>document.cookie</b> with name=value pair, expiration date, and path. The expiration date determines how long the cookie persists.<br/><br/>
<b>Reading a Cookie:</b> Access <b>document.cookie</b> which returns all cookies as a semicolon-separated string. Parse the string to extract the desired cookie value.<br/><br/>
<b>Removing a Cookie:</b> Set the cookie's expiration date to a past date (e.g., January 1, 1970). The browser automatically deletes expired cookies."""
            },
            {
                "num": "8",
                "question": "Write HTML tags to generate a form with: Student Information, First Name, Last Name, Gender (radio), Subject (checkboxes: C, JAVA, PHP), Comment (textarea).",
                "marks": "5",
                "answer": """<b>HTML Code for Student Information Form:</b><br/>
<pre>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Student Information&lt;/title&gt;
    &lt;style&gt;
        body { font-family: Arial, sans-serif; margin: 20px; }
        form { width: 400px; padding: 20px; border: 1px solid #ccc; border-radius: 5px; }
        label { display: inline-block; width: 100px; margin-top: 10px; }
        input[type="text"], textarea { width: 250px; padding: 5px; margin-top: 5px; }
        .gender, .subjects { margin-top: 10px; }
        input[type="submit"] { margin-top: 15px; padding: 8px 20px; background-color: #4CAF50; color: white; border: none; cursor: pointer; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;form action="/submit" method="post"&gt;
        &lt;h2&gt;Student Information&lt;/h2&gt;
        
        &lt;label for="fname"&gt;First Name:&lt;/label&gt;
        &lt;input type="text" id="fname" name="firstname" placeholder="Enter first name"&gt;&lt;br/&gt;
        
        &lt;label for="lname"&gt;Last Name:&lt;/label&gt;
        &lt;input type="text" id="lname" name="lastname" placeholder="Enter last name"&gt;&lt;br/&gt;
        
        &lt;div class="gender"&gt;
            &lt;label&gt;Gender:&lt;/label&gt;
            &lt;input type="radio" id="male" name="gender" value="male"&gt;
            &lt;label for="male"&gt;Male&lt;/label&gt;
            &lt;input type="radio" id="female" name="gender" value="female"&gt;
            &lt;label for="female"&gt;Female&lt;/label&gt;
            &lt;input type="radio" id="other" name="gender" value="other"&gt;
            &lt;label for="other"&gt;Other&lt;/label&gt;
        &lt;/div&gt;
        
        &lt;div class="subjects"&gt;
            &lt;label&gt;Subject:&lt;/label&gt;&lt;br/&gt;
            &lt;input type="checkbox" id="c" name="subject" value="C"&gt;
            &lt;label for="c"&gt;C&lt;/label&gt;&lt;br/&gt;
            &lt;input type="checkbox" id="java" name="subject" value="JAVA"&gt;
            &lt;label for="java"&gt;JAVA&lt;/label&gt;&lt;br/&gt;
            &lt;input type="checkbox" id="php" name="subject" value="PHP"&gt;
            &lt;label for="php"&gt;PHP&lt;/label&gt;
        &lt;/div&gt;
        
        &lt;label for="comment"&gt;Comment:&lt;/label&gt;&lt;br/&gt;
        &lt;textarea id="comment" name="comment" rows="4" cols="35" placeholder="Enter your comments here..."&gt;&lt;/textarea&gt;&lt;br/&gt;
        
        &lt;input type="submit" value="Submit"&gt;
    &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;</pre>"""
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Is XML replacement for HTML? Explain different types of tier technology with suitable diagram.",
                "marks": "2+8",
                "answer": """<b>Is XML a Replacement for HTML?</b><br/><br/>
<b>No, XML is NOT a replacement for HTML.</b> XML and HTML were designed with different goals and serve different purposes:<br/><br/>
<b>HTML (HyperText Markup Language):</b><br/>
• Designed to display data and focus on how data looks.<br/>
• Predefined tags (&lt;p&gt;, &lt;div&gt;, &lt;table&gt;, etc.) that browsers understand.<br/>
• Used to create web pages and define their structure and presentation.<br/>
• Tags are primarily for formatting and layout.<br/><br/>
<b>XML (Extensible Markup Language):</b><br/>
• Designed to carry and store data, focusing on what data is.<br/>
• No predefined tags; users create their own tags to describe data.<br/>
• Used for data interchange between systems and platforms.<br/>
• Self-descriptive and platform-independent.<br/><br/>
<b>Relationship:</b><br/>
XML complements HTML. XML is used to transport and store data, while HTML is used to format and display data. XHTML combines both by using XML syntax rules with HTML tags.<br/><br/>
<b>Three-Tier Architecture:</b><br/><br/>
Three-tier architecture is a client-server architecture that separates an application into three logical and physical computing tiers: Presentation Tier, Application Tier, and Data Tier.<br/><br/>
<b>1. Presentation Tier (Client Tier):</b><br/>
This is the top-most level of the application. It is the user interface and communication layer where the end-user interacts with the application. It displays information to the user and collects input.<br/>
<b>Technologies:</b> HTML, CSS, JavaScript, React, Angular<br/>
<b>Function:</b> Display data, handle user input, send requests to application tier.<br/><br/>
<b>2. Application Tier (Logic/Business Tier):</b><br/>
This middle tier coordinates the application, processes commands, makes logical decisions, and performs calculations. It acts as a bridge between the presentation and data tiers.<br/>
<b>Technologies:</b> PHP, Python, Java, Node.js, ASP.NET<br/>
<b>Function:</b> Process business logic, validate data, authenticate users, manage sessions, communicate with database.<br/><br/>
<b>3. Data Tier (Database Tier):</b><br/>
This bottom tier consists of database servers where information is stored and retrieved. It maintains data integrity and handles data persistence.<br/>
<b>Technologies:</b> MySQL, PostgreSQL, MongoDB, Oracle, SQL Server<br/>
<b>Function:</b> Store data, execute queries, manage transactions, ensure data security.<br/><br/>
<b>Diagram:</b><br/>
<pre>
+-------------------+       HTTP Request       +-------------------+       SQL Query       +-------------------+
|   PRESENTATION    |  --------------------&gt;   |    APPLICATION    |  ------------------&gt;  |      DATA TIER    |
|     TIER          |                          |      TIER         |                         |    (Database)     |
|  (Client/Browser) |  &lt;--------------------   |  (Web Server/App) |  &lt;------------------   |  (MySQL/Oracle)   |
|  HTML, CSS, JS    |      HTTP Response       |  PHP/Java/Node    |      Query Result       |                   |
+-------------------+                          +-------------------+                         +-------------------+
        |                                               |                                              |
        |                                               |                                              |
   User Interface                               Business Logic                               Data Storage
</pre><br/>
<b>Advantages of Three-Tier Architecture:</b><br/>
• <b>Scalability:</b> Each tier can be scaled independently.<br/>
• <b>Maintainability:</b> Changes in one tier do not affect others.<br/>
• <b>Security:</b> Data tier is protected behind the application tier.<br/>
• <b>Reusability:</b> Business logic can be reused across different interfaces.<br/>
• <b>Flexibility:</b> Different technologies can be used for each tier."""
            },
            {
                "num": "10",
                "question": "Write a server-side script to display all the records stored in student table which resides under database called TU. The structure of student table is (id, name, address).",
                "marks": "10",
                "answer": """<b>Server-Side Script using PHP with MySQLi:</b><br/><br/>
The following PHP script connects to the MySQL database named "TU", retrieves all records from the "student" table, and displays them in an HTML table format.<br/><br/>
<pre>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Student Records - TU Database&lt;/title&gt;
    &lt;style&gt;
        table { border-collapse: collapse; width: 60%; margin: 20px auto; }
        th, td { border: 1px solid #333; padding: 10px; text-align: left; }
        th { background-color: #4CAF50; color: white; }
        tr:nth-child(even) { background-color: #f2f2f2; }
        h2 { text-align: center; color: #333; }
        .error { color: red; text-align: center; }
        .success { color: green; text-align: center; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h2&gt;Student Records from TU Database&lt;/h2&gt;

    &lt;?php
    // Database configuration
    $servername = "localhost";
    $username = "root";
    $password = "";
    $database = "TU";

    // Create connection using MySQLi
    $conn = new mysqli($servername, $username, $password, $database);

    // Check connection
    if ($conn-&gt;connect_error) {
        die("&lt;p class='error'&gt;Connection failed: " . $conn-&gt;connect_error . "&lt;/p&gt;");
    }

    // SQL query to select all records from student table
    $sql = "SELECT id, name, address FROM student";
    $result = $conn-&gt;query($sql);

    // Check if records exist
    if ($result-&gt;num_rows &gt; 0) {
        echo "&lt;table&gt;";
        echo "&lt;tr&gt;&lt;th&gt;ID&lt;/th&gt;&lt;th&gt;Name&lt;/th&gt;&lt;th&gt;Address&lt;/th&gt;&lt;/tr&gt;";
        
        // Output data of each row
        while($row = $result-&gt;fetch_assoc()) {
            echo "&lt;tr&gt;";
            echo "&lt;td&gt;" . $row["id"] . "&lt;/td&gt;";
            echo "&lt;td&gt;" . $row["name"] . "&lt;/td&gt;";
            echo "&lt;td&gt;" . $row["address"] . "&lt;/td&gt;";
            echo "&lt;/tr&gt;";
        }
        echo "&lt;/table&gt;";
        echo "&lt;p class='success'&gt;Total Records: " . $result-&gt;num_rows . "&lt;/p&gt;";
    } else {
        echo "&lt;p class='error'&gt;No records found in the student table.&lt;/p&gt;";
    }

    // Close connection
    $conn-&gt;close();
    ?&gt;

&lt;/body&gt;
&lt;/html&gt;</pre><br/>
<b>Explanation of the Script:</b><br/><br/>
<b>1. Database Connection:</b><br/>
&nbsp;&nbsp;• <b>$conn = new mysqli($servername, $username, $password, $database);</b> creates a new MySQLi connection.<br/>
&nbsp;&nbsp;• <b>connect_error</b> checks if the connection was successful.<br/><br/>
<b>2. Execute Query:</b><br/>
&nbsp;&nbsp;• <b>$sql = "SELECT id, name, address FROM student";</b> defines the SQL query.<br/>
&nbsp;&nbsp;• <b>$conn-&gt;query($sql)</b> executes the query and returns a result set.<br/><br/>
<b>3. Fetch and Display Data:</b><br/>
&nbsp;&nbsp;• <b>$result-&gt;num_rows</b> returns the number of rows in the result set.<br/>
&nbsp;&nbsp;• <b>$result-&gt;fetch_assoc()</b> fetches each row as an associative array.<br/>
&nbsp;&nbsp;• The while loop iterates through all records and displays them in an HTML table.<br/><br/>
<b>4. Close Connection:</b><br/>
&nbsp;&nbsp;• <b>$conn-&gt;close();</b> closes the database connection to free resources.<br/><br/>
<b>Alternative using PDO (PHP Data Objects):</b><br/>
<pre>&lt;?php
try {
    $pdo = new PDO("mysql:host=localhost;dbname=TU", "root", "");
    $pdo-&gt;setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    
    $stmt = $pdo-&gt;query("SELECT id, name, address FROM student");
    $students = $stmt-&gt;fetchAll(PDO::FETCH_ASSOC);
    
    foreach ($students as $row) {
        echo "ID: " . $row['id'] . " | Name: " . $row['name'] . " | Address: " . $row['address'] . "&lt;br/&gt;";
    }
} catch (PDOException $e) {
    echo "Error: " . $e-&gt;getMessage();
}
?&gt;</pre>"""
            },
            {
                "num": "11",
                "question": "Write well-formed XML document and validate with the use of XML schema. The XML should store Employee information with: Name (First Name, Last Name), Contact (Mobile, Landline), Address (City, Street, Tole).",
                "marks": "10",
                "answer": """<b>Well-Formed XML Document (employee.xml):</b><br/><br/>
<pre>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;Employee xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:noNamespaceSchemaLocation="employee.xsd"&gt;
    &lt;Name&gt;
        &lt;FirstName&gt;Ram&lt;/FirstName&gt;
        &lt;LastName&gt;Sharma&lt;/LastName&gt;
    &lt;/Name&gt;
    &lt;Contact&gt;
        &lt;Mobile&gt;9801234567&lt;/Mobile&gt;
        &lt;Landline&gt;01-4433221&lt;/Landline&gt;
    &lt;/Contact&gt;
    &lt;Address&gt;
        &lt;City&gt;Kathmandu&lt;/City&gt;
        &lt;Street&gt;Baneshwor&lt;/Street&gt;
        &lt;Tole&gt;Minbhawan&lt;/Tole&gt;
    &lt;/Address&gt;
&lt;/Employee&gt;</pre><br/>
<b>XML Schema (employee.xsd):</b><br/><br/>
<pre>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"&gt;

    &lt;!-- Definition of Name element --&gt;
    &lt;xs:complexType name="NameType"&gt;
        &lt;xs:sequence&gt;
            &lt;xs:element name="FirstName" type="xs:string"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;Employee's first name&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
            &lt;/xs:element&gt;
            &lt;xs:element name="LastName" type="xs:string"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;Employee's last name&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
            &lt;/xs:element&gt;
        &lt;/xs:sequence&gt;
    &lt;/xs:complexType&gt;

    &lt;!-- Definition of Contact element --&gt;
    &lt;xs:complexType name="ContactType"&gt;
        &lt;xs:sequence&gt;
            &lt;xs:element name="Mobile" type="xs:string"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;Employee's mobile number&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
            &lt;/xs:element&gt;
            &lt;xs:element name="Landline" type="xs:string"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;Employee's landline number&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
            &lt;/xs:element&gt;
        &lt;/xs:sequence&gt;
    &lt;/xs:complexType&gt;

    &lt;!-- Definition of Address element --&gt;
    &lt;xs:complexType name="AddressType"&gt;
        &lt;xs:sequence&gt;
            &lt;xs:element name="City" type="xs:string"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;City name&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
            &lt;/xs:element&gt;
            &lt;xs:element name="Street" type="xs:string"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;Street name&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
            &lt;/xs:element&gt;
            &lt;xs:element name="Tole" type="xs:string"&gt;
                &lt;xs:annotation&gt;
                    &lt;xs:documentation&gt;Tole/locality name&lt;/xs:documentation&gt;
                &lt;/xs:annotation&gt;
            &lt;/xs:element&gt;
        &lt;/xs:sequence&gt;
    &lt;/xs:complexType&gt;

    &lt;!-- Definition of Employee element --&gt;
    &lt;xs:element name="Employee"&gt;
        &lt;xs:complexType&gt;
            &lt;xs:sequence&gt;
                &lt;xs:element name="Name" type="NameType" /&gt;
                &lt;xs:element name="Contact" type="ContactType" /&gt;
                &lt;xs:element name="Address" type="AddressType" /&gt;
            &lt;/xs:sequence&gt;
        &lt;/xs:complexType&gt;
    &lt;/xs:element&gt;

&lt;/xs:schema&gt;</pre><br/>
<b>Explanation:</b><br/><br/>
<b>1. Well-Formed XML Rules Followed:</b><br/>
&nbsp;&nbsp;• XML declaration is present (&lt;?xml version="1.0" encoding="UTF-8"?&gt;).<br/>
&nbsp;&nbsp;• All elements are properly nested and closed.<br/>
&nbsp;&nbsp;• Element names are case-sensitive and consistently used.<br/>
&nbsp;&nbsp;• Attribute values are quoted.<br/>
&nbsp;&nbsp;• Single root element (&lt;Employee&gt;) contains all other elements.<br/><br/>
<b>2. XML Schema (XSD) Components:</b><br/>
&nbsp;&nbsp;• <b>xs:schema:</b> Root element defining the schema namespace.<br/>
&nbsp;&nbsp;• <b>xs:complexType:</b> Defines complex elements that contain child elements.<br/>
&nbsp;&nbsp;• <b>xs:sequence:</b> Specifies that child elements must appear in the defined order.<br/>
&nbsp;&nbsp;• <b>xs:element:</b> Declares elements with their name and data type.<br/>
&nbsp;&nbsp;• <b>xs:string:</b> Built-in data type for text content.<br/><br/>
<b>3. Schema Validation:</b><br/>
&nbsp;&nbsp;• The XML file references the schema using <b>xsi:noNamespaceSchemaLocation="employee.xsd"</b>.<br/>
&nbsp;&nbsp;• XML validators (like online validators or tools like xmllint) check that:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- All required elements are present (Name, Contact, Address).<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- Elements appear in the correct order.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- Data types match the schema definitions.<br/>
&nbsp;&nbsp;&nbsp;&nbsp;- No extra or undefined elements exist.<br/><br/>
<b>4. Extended Version with Multiple Employees:</b><br/>
<pre>&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;Employees xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
           xsi:noNamespaceSchemaLocation="employees.xsd"&gt;
    &lt;Employee&gt;
        &lt;Name&gt;
            &lt;FirstName&gt;Sita&lt;/FirstName&gt;
            &lt;LastName&gt;Gurung&lt;/LastName&gt;
        &lt;/Name&gt;
        &lt;Contact&gt;
            &lt;Mobile&gt;9812345678&lt;/Mobile&gt;
            &lt;Landline&gt;01-5544332&lt;/Landline&gt;
        &lt;/Contact&gt;
        &lt;Address&gt;
            &lt;City&gt;Pokhara&lt;/City&gt;
            &lt;Street&gt;Lakeside&lt;/Street&gt;
            &lt;Tole&gt;Baidam&lt;/Tole&gt;
        &lt;/Address&gt;
    &lt;/Employee&gt;
&lt;/Employees&gt;</pre><br/>
<b>Corresponding Schema for Multiple Employees:</b><br/>
<pre>&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"&gt;
    &lt;xs:element name="Employees"&gt;
        &lt;xs:complexType&gt;
            &lt;xs:sequence&gt;
                &lt;xs:element name="Employee" maxOccurs="unbounded"&gt;
                    &lt;xs:complexType&gt;
                        &lt;xs:sequence&gt;
                            &lt;xs:element name="Name"&gt;
                                &lt;xs:complexType&gt;
                                    &lt;xs:sequence&gt;
                                        &lt;xs:element name="FirstName" type="xs:string"/&gt;
                                        &lt;xs:element name="LastName" type="xs:string"/&gt;
                                    &lt;/xs:sequence&gt;
                                &lt;/xs:complexType&gt;
                            &lt;/xs:element&gt;
                            &lt;xs:element name="Contact"&gt;
                                &lt;xs:complexType&gt;
                                    &lt;xs:sequence&gt;
                                        &lt;xs:element name="Mobile" type="xs:string"/&gt;
                                        &lt;xs:element name="Landline" type="xs:string"/&gt;
                                    &lt;/xs:sequence&gt;
                                &lt;/xs:complexType&gt;
                            &lt;/xs:element&gt;
                            &lt;xs:element name="Address"&gt;
                                &lt;xs:complexType&gt;
                                    &lt;xs:sequence&gt;
                                        &lt;xs:element name="City" type="xs:string"/&gt;
                                        &lt;xs:element name="Street" type="xs:string"/&gt;
                                        &lt;xs:element name="Tole" type="xs:string"/&gt;
                                    &lt;/xs:sequence&gt;
                                &lt;/xs:complexType&gt;
                            &lt;/xs:element&gt;
                        &lt;/xs:sequence&gt;
                    &lt;/xs:complexType&gt;
                &lt;/xs:element&gt;
            &lt;/xs:sequence&gt;
        &lt;/xs:complexType&gt;
    &lt;/xs:element&gt;
&lt;/xs:schema&gt;</pre>"""
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet("CACS205", "web-technology", "Web Technology", 2019, "semester-3", CACS205_2019)
