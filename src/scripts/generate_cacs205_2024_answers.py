import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS205_2024 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What is CSS? Explain the method of using CSS on the web page.",
                "marks": "2+3",
                "answer": """<b>CSS (Cascading Style Sheets)</b> is a stylesheet language used to describe the presentation and layout of HTML documents. It controls colors, fonts, spacing, positioning, and overall visual appearance, separating content from design.

<b>Methods of Using CSS on a Web Page:</b>

1. <b>Inline CSS:</b> Styles are applied directly to individual HTML elements using the <code>style</code> attribute.
<pre>
&lt;p style="color: blue; font-size: 16px;"&gt;This is inline CSS.&lt;/p&gt;
</pre>
<b>Pros:</b> Quick for single elements. <b>Cons:</b> Hard to maintain, not reusable.

2. <b>Internal (Embedded) CSS:</b> Styles are defined within the <code>&lt;style&gt;</code> tag inside the <code>&lt;head&gt;</code> section of the HTML document.
<pre>
&lt;head&gt;
  &lt;style&gt;
    p { color: blue; font-size: 16px; }
    h1 { background-color: yellow; }
  &lt;/style&gt;
&lt;/head&gt;
</pre>
<b>Pros:</b> Good for single-page styling. <b>Cons:</b> Not shared across multiple pages.

3. <b>External CSS:</b> Styles are written in a separate <code>.css</code> file and linked to HTML using the <code>&lt;link&gt;</code> tag.
<pre>
&lt;!-- HTML File --&gt;
&lt;head&gt;
  &lt;link rel="stylesheet" type="text/css" href="styles.css"&gt;
&lt;/head&gt;

/* styles.css */
p { color: blue; font-size: 16px; }
h1 { background-color: yellow; }
</pre>
<b>Pros:</b> Reusable across multiple pages, easy to maintain, cached by browsers. <b>Cons:</b> Requires an extra HTTP request.

<b>Cascading Priority:</b> Inline &gt; Internal &gt; External (when same selectors are used).""",
            },
            {
                "num": "3",
                "question": "What is XML? Write rules to create XML document with example.",
                "marks": "1+4",
                "answer": """<b>XML (eXtensible Markup Language)</b> is a markup language designed to store and transport data in a self-describing, platform-independent format. Unlike HTML, which is used to display data, XML focuses on what data is. It is both human-readable and machine-readable.

<b>Rules to Create an XML Document:</b><br/>
1. <b>Prolog:</b> Optional XML declaration at the top: <code>&lt;?xml version="1.0" encoding="UTF-8"?&gt;</code><br/>
2. <b>Root Element:</b> Every XML document must have exactly one root element that contains all other elements.<br/>
3. <b>Case Sensitivity:</b> Tags are case-sensitive. Opening and closing tags must match exactly.<br/>
4. <b>Proper Nesting:</b> All elements must be properly nested within each other.<br/>
5. <b>Closing Tags:</b> Every opening tag must have a corresponding closing tag. Empty elements can use self-closing syntax: <code>&lt;element /&gt;</code><br/>
6. <b>Attribute Values:</b> Attribute values must always be enclosed in quotes (single or double).<br/>
7. <b>Valid Names:</b> Element names must start with a letter or underscore; cannot contain spaces.<br/>
8. <b>No Reserved Characters:</b> Special characters like &lt;, &gt;, &amp; must be escaped or placed in CDATA sections.

<b>Example of a Well-Formed XML Document:</b>
<pre>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;library&gt;
  &lt;book id="b001"&gt;
    &lt;title&gt;Web Technology&lt;/title&gt;
    &lt;author&gt;John Smith&lt;/author&gt;
    &lt;price currency="USD"&gt;45.00&lt;/price&gt;
    &lt;year&gt;2024&lt;/year&gt;
  &lt;/book&gt;
  &lt;book id="b002"&gt;
    &lt;title&gt;OOP in Java&lt;/title&gt;
    &lt;author&gt;Jane Doe&lt;/author&gt;
    &lt;price currency="USD"&gt;50.00&lt;/price&gt;
    &lt;year&gt;2023&lt;/year&gt;
  &lt;/book&gt;
&lt;/library&gt;
</pre>""",
            },
            {
                "num": "4",
                "question": "Explain HTML form elements with suitable example.",
                "marks": "2+3",
                "answer": """<b>HTML Form Elements</b> are used to collect user input on a web page. A form is created using the <code>&lt;form&gt;</code> tag and can contain various input elements that allow users to enter text, make selections, and submit data to a server.

<b>Common HTML Form Elements:</b>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Element</b></td><td><b>Description</b></td></tr>
<tr><td>&lt;form&gt;</td><td>Container for all form elements; defines action and method</td></tr>
<tr><td>&lt;input&gt;</td><td>Most versatile element — text, password, radio, checkbox, submit, etc.</td></tr>
<tr><td>&lt;label&gt;</td><td>Defines a label for an input element</td></tr>
<tr><td>&lt;textarea&gt;</td><td>Multi-line text input</td></tr>
<tr><td>&lt;select&gt;</td><td>Dropdown list</td></tr>
<tr><td>&lt;option&gt;</td><td>Items within a select dropdown</td></tr>
<tr><td>&lt;button&gt;</td><td>Clickable button</td></tr>
<tr><td>&lt;fieldset&gt;</td><td>Groups related elements</td></tr>
<tr><td>&lt;legend&gt;</td><td>Caption for a fieldset</td></tr>
</table>

<b>Example — Complete HTML Form:</b>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;Registration Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;h2&gt;Student Registration&lt;/h2&gt;
  &lt;form action="register.php" method="POST"&gt;
    &lt;label for="fname"&gt;First Name:&lt;/label&gt;
    &lt;input type="text" id="fname" name="fname" required&gt;&lt;br/&gt;&lt;br/&gt;

    &lt;label for="pwd"&gt;Password:&lt;/label&gt;
    &lt;input type="password" id="pwd" name="pwd"&gt;&lt;br/&gt;&lt;br/&gt;

    &lt;label&gt;Gender:&lt;/label&gt;
    &lt;input type="radio" name="gender" value="male"&gt; Male
    &lt;input type="radio" name="gender" value="female"&gt; Female&lt;br/&gt;&lt;br/&gt;

    &lt;label&gt;Hobbies:&lt;/label&gt;
    &lt;input type="checkbox" name="hobby" value="reading"&gt; Reading
    &lt;input type="checkbox" name="hobby" value="sports"&gt; Sports&lt;br/&gt;&lt;br/&gt;

    &lt;label for="country"&gt;Country:&lt;/label&gt;
    &lt;select id="country" name="country"&gt;
      &lt;option value="np"&gt;Nepal&lt;/option&gt;
      &lt;option value="in"&gt;India&lt;/option&gt;
      &lt;option value="us"&gt;USA&lt;/option&gt;
    &lt;/select&gt;&lt;br/&gt;&lt;br/&gt;

    &lt;label for="address"&gt;Address:&lt;/label&gt;
    &lt;textarea id="address" name="address" rows="4" cols="30"&gt;&lt;/textarea&gt;&lt;br/&gt;&lt;br/&gt;

    &lt;input type="submit" value="Register"&gt;
    &lt;input type="reset" value="Clear"&gt;
  &lt;/form&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>""",
            },
            {
                "num": "5",
                "question": "What is XPath? Write XSLT code to display your books information (Title, price, ISBN, subject code) store into XML.",
                "marks": "1+4",
                "answer": """<b>XPath (XML Path Language)</b> is a query language used to navigate and select nodes in an XML document. It uses path expressions to identify and locate specific parts of an XML document, similar to how file paths work in an operating system. XPath is used in XSLT, XQuery, and other XML technologies.

<b>Common XPath Expressions:</b><br/>
• <code>/bookstore</code> — Selects the root element bookstore<br/>
• <code>//book</code> — Selects all book elements anywhere in the document<br/>
• <code>/bookstore/book[1]</code> — Selects the first book element<br/>
• <code>//title</code> — Selects all title elements<br/>
• <code>//book[@category='java']</code> — Selects books with category attribute equal to 'java'<br/>
• <code>//book[price&gt;30]</code> — Selects books with price greater than 30

<b>XML File (books.xml):</b>
<pre>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;?xml-stylesheet type="text/xsl" href="books.xsl"?&gt;
&lt;bookstore&gt;
  &lt;book&gt;
    &lt;title&gt;Web Technology&lt;/title&gt;
    &lt;price&gt;500&lt;/price&gt;
    &lt;isbn&gt;978-3-16-148410-0&lt;/isbn&gt;
    &lt;subjectCode&gt;CACS205&lt;/subjectCode&gt;
  &lt;/book&gt;
  &lt;book&gt;
    &lt;title&gt;OOP in Java&lt;/title&gt;
    &lt;price&gt;650&lt;/price&gt;
    &lt;isbn&gt;978-0-13-468599-1&lt;/isbn&gt;
    &lt;subjectCode&gt;CACS204&lt;/subjectCode&gt;
  &lt;/book&gt;
&lt;/bookstore&gt;
</pre>

<b>XSLT File (books.xsl):</b>
<pre>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"&gt;
  &lt;xsl:template match="/"&gt;
    &lt;html&gt;
    &lt;body&gt;
      &lt;h2&gt;Book Information&lt;/h2&gt;
      &lt;table border="1"&gt;
        &lt;tr&gt;
          &lt;th&gt;Title&lt;/th&gt;
          &lt;th&gt;Price&lt;/th&gt;
          &lt;th&gt;ISBN&lt;/th&gt;
          &lt;th&gt;Subject Code&lt;/th&gt;
        &lt;/tr&gt;
        &lt;xsl:for-each select="bookstore/book"&gt;
          &lt;tr&gt;
            &lt;td&gt;&lt;xsl:value-of select="title"/&gt;&lt;/td&gt;
            &lt;td&gt;&lt;xsl:value-of select="price"/&gt;&lt;/td&gt;
            &lt;td&gt;&lt;xsl:value-of select="isbn"/&gt;&lt;/td&gt;
            &lt;td&gt;&lt;xsl:value-of select="subjectCode"/&gt;&lt;/td&gt;
          &lt;/tr&gt;
        &lt;/xsl:for-each&gt;
      &lt;/table&gt;
    &lt;/body&gt;
    &lt;/html&gt;
  &lt;/xsl:template&gt;
&lt;/xsl:stylesheet&gt;
</pre>""",
            },
            {
                "num": "6",
                "question": "Why server side programming is important for web development? Explain with its major features.",
                "marks": "5",
                "answer": """<b>Importance of Server-Side Programming in Web Development:</b><br/>
Server-side programming is essential because it enables dynamic content generation, data processing, and business logic execution on the server before sending responses to clients. Without server-side processing, websites would be limited to static HTML pages that cannot interact with databases, authenticate users, or personalize content.

<b>Key Reasons for Importance:</b><br/>
1. <b>Dynamic Content Generation:</b> Server-side scripts generate HTML dynamically based on user input, database queries, or business rules.<br/>
2. <b>Database Interaction:</b> Enables CRUD (Create, Read, Update, Delete) operations on databases to persist and retrieve data.<br/>
3. <b>Security:</b> Sensitive operations (authentication, payment processing, data validation) occur on the server, hiding implementation details from users.<br/>
4. <b>User Authentication and Authorization:</b> Manages login sessions, access control, and user privileges securely.<br/>
5. <b>Cross-Platform Compatibility:</b> Server logic runs independently of the client's browser or device.

<b>Major Features of Server-Side Programming:</b>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Feature</b></td><td><b>Description</b></td></tr>
<tr><td>Session Management</td><td>Tracks user state across multiple page requests using sessions and cookies</td></tr>
<tr><td>Database Connectivity</td><td>Connects to MySQL, PostgreSQL, MongoDB, etc. using drivers or ORMs</td></tr>
<tr><td>File Handling</td><td>Reads, writes, and manipulates files on the server filesystem</td></tr>
<tr><td>API Development</td><td>Creates RESTful or SOAP APIs for client-server communication</td></tr>
<tr><td>Security Features</td><td>Encryption, input sanitization, CSRF/XSS protection, SSL/TLS support</td></tr>
<tr><td>Template Engines</td><td>Separates presentation logic from business logic (e.g., JSP, Blade, EJS)</td></tr>
<tr><td>Error Handling</td><td>Centralized logging and error reporting for debugging and monitoring</td></tr>
<tr><td>Scalability</td><td>Supports load balancing, caching, and distributed architectures</td></tr>
</table>

<b>Popular Server-Side Technologies:</b> PHP, Node.js, Python (Django/Flask), Java (Spring/Servlets/JSP), ASP.NET, Ruby on Rails.""",
            },
            {
                "num": "7",
                "question": "Why session is important for web development, write a server side script to create, store, retrieve and remove session and cookie.",
                "marks": "2+3",
                "answer": """<b>Importance of Session in Web Development:</b><br/>
HTTP is a stateless protocol, meaning each request from a client to a server is independent and does not retain any memory of previous interactions. <b>Sessions</b> solve this problem by allowing the server to maintain stateful information about a user across multiple requests.

<b>Why Sessions Are Important:</b><br/>
1. <b>User Authentication:</b> Keeps users logged in as they navigate between pages.<br/>
2. <b>Shopping Carts:</b> E-commerce sites use sessions to store cart items temporarily.<br/>
3. <b>Personalization:</b> Remembers user preferences, language settings, and themes.<br/>
4. <b>Security:</b> Stores sensitive data server-side rather than exposing it in cookies.<br/>
5. <b>Tracking:</b> Tracks user activity and progress through multi-step processes.

<b>PHP Server-Side Script for Session and Cookie Management:</b>
<pre>
&lt;?php
// ========== CREATE AND STORE SESSION ==========
session_start();

// Store data in session
$_SESSION['username'] = 'ram_sharma';
$_SESSION['role'] = 'student';
$_SESSION['login_time'] = date('Y-m-d H:i:s');

echo "&lt;h3&gt;Session Created Successfully&lt;/h3&gt;";
echo "Username: " . $_SESSION['username'] . "&lt;br/&gt;";
echo "Role: " . $_SESSION['role'] . "&lt;br/&gt;";
echo "Login Time: " . $_SESSION['login_time'] . "&lt;br/&gt;";

// ========== CREATE AND STORE COOKIE ==========
// setcookie(name, value, expire, path, domain, secure, httponly)
setcookie("user_pref", "dark_mode", time() + (86400 * 30), "/");
setcookie("visit_count", "1", time() + (86400 * 30), "/");

echo "&lt;h3&gt;Cookies Set Successfully&lt;/h3&gt;";

// ========== RETRIEVE SESSION DATA ==========
echo "&lt;h3&gt;Retrieve Session Data&lt;/h3&gt;";
if (isset($_SESSION['username'])) {
    echo "Session Username: " . $_SESSION['username'] . "&lt;br/&gt;";
} else {
    echo "No session data found.&lt;br/&gt;";
}

// ========== RETRIEVE COOKIE DATA ==========
echo "&lt;h3&gt;Retrieve Cookie Data&lt;/h3&gt;";
if (isset($_COOKIE['user_pref'])) {
    echo "Cookie Preference: " . $_COOKIE['user_pref'] . "&lt;br/&gt;";
} else {
    echo "No cookie found.&lt;br/&gt;";
}

// ========== REMOVE SESSION DATA ==========
echo "&lt;h3&gt;Remove Session&lt;/h3&gt;";
// Remove specific session variables
unset($_SESSION['username']);
unset($_SESSION['role']);

// Destroy entire session
session_destroy();
echo "Session destroyed successfully.&lt;br/&gt;";

// ========== REMOVE COOKIE ==========
echo "&lt;h3&gt;Remove Cookie&lt;/h3&gt;";
// Set expiration time to past to delete cookie
setcookie("user_pref", "", time() - 3600, "/");
setcookie("visit_count", "", time() - 3600, "/");
echo "Cookies removed successfully.&lt;br/&gt;";
?&gt;
</pre>

<b>Key Differences:</b><br/>
• <b>Session:</b> Data stored on the server; session ID sent to client via cookie. More secure for sensitive data.<br/>
• <b>Cookie:</b> Data stored on the client's browser. Limited size (~4KB) and can be disabled by users.""",
            },
            {
                "num": "8",
                "question": "Explain multi-tier technology with its advantage and disadvantages.",
                "marks": "2+3",
                "answer": """<b>Multi-Tier Architecture</b> is a client-server architecture in which the presentation, application processing, and data management functions are physically separated into distinct layers or tiers. The most common implementation is the <b>Three-Tier Architecture</b>, consisting of Presentation Tier, Application/Business Logic Tier, and Data Tier.

<b>Types of Multi-Tier Architecture:</b><br/>
1. <b>One-Tier:</b> All layers (UI, logic, data) exist on a single system (e.g., desktop application).<br/>
2. <b>Two-Tier (Client-Server):</b> Client handles presentation and some logic; server manages the database.<br/>
3. <b>Three-Tier:</b> Separate presentation, application logic, and data tiers.<br/>
4. <b>N-Tier:</b> Further breakdown into multiple specialized layers (web server, app server, cache layer, message queue, etc.).

<b>Three-Tier Architecture:</b>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Tier</b></td><td><b>Name</b></td><td><b>Role</b></td><td><b>Examples</b></td></tr>
<tr><td>1st</td><td>Presentation Tier</td><td>User interface and interaction</td><td>HTML, CSS, JavaScript, React</td></tr>
<tr><td>2nd</td><td>Application Tier</td><td>Business logic and processing</td><td>PHP, Java, Python, Node.js</td></tr>
<tr><td>3rd</td><td>Data Tier</td><td>Data storage and retrieval</td><td>MySQL, PostgreSQL, MongoDB</td></tr>
</table>

<b>Advantages of Multi-Tier Technology:</b><br/>
1. <b>Scalability:</b> Each tier can be scaled independently based on demand.<br/>
2. <b>Maintainability:</b> Changes in one tier do not affect others, making updates easier.<br/>
3. <b>Reusability:</b> Business logic can be reused by multiple presentation layers (web, mobile, desktop).<br/>
4. <b>Security:</b> The data tier is isolated from direct client access, reducing attack surface.<br/>
5. <b>Performance:</b> Caching and load balancing can be applied at specific tiers.<br/>
6. <b>Flexibility:</b> Different technologies can be used for each tier based on requirements.<br/>
7. <b>Fault Tolerance:</b> Failure in one tier does not necessarily bring down the entire system.

<b>Disadvantages of Multi-Tier Technology:</b><br/>
1. <b>Complexity:</b> More complex to design, develop, and deploy than monolithic architectures.<br/>
2. <b>Performance Overhead:</b> Network communication between tiers can introduce latency.<br/>
3. <b>Cost:</b> Requires more hardware, software licenses, and infrastructure.<br/>
4. <b>Deployment Challenges:</b> Coordinating deployments across multiple servers is more difficult.<br/>
5. <b>Testing Difficulty:</b> Integration testing becomes more complex with distributed components.<br/>
6. <b>Network Dependency:</b> Heavily reliant on network reliability and bandwidth between tiers.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Write a server side script for implementing login. Your program should take username and password as input and redirect to home page if validated otherwise prints an error try again.",
                "marks": "10",
                "answer": """<b>PHP Server-Side Login Implementation:</b>

<b>login.php — Login Form:</b>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
  &lt;title&gt;Login Page&lt;/title&gt;
  &lt;style&gt;
    body { font-family: Arial; background: #f0f0f0; }
    .login-box { width: 300px; margin: 100px auto; padding: 20px; 
                 background: white; border-radius: 8px; }
    input { width: 100%; padding: 10px; margin: 5px 0; }
    button { width: 100%; padding: 10px; background: #007bff; 
             color: white; border: none; }
    .error { color: red; margin-top: 10px; }
  &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
  &lt;div class="login-box"&gt;
    &lt;h2&gt;User Login&lt;/h2&gt;
    &lt;form method="POST" action="authenticate.php"&gt;
      &lt;input type="text" name="username" placeholder="Username" required&gt;
      &lt;input type="password" name="password" placeholder="Password" required&gt;
      &lt;button type="submit"&gt;Login&lt;/button&gt;
    &lt;/form&gt;
    &lt;?php
      if (isset($_GET['error'])) {
        echo '&lt;p class="error"&gt;Invalid username or password. Please try again.&lt;/p&gt;';
      }
    ?&gt;
  &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

<b>authenticate.php — Validation Script:</b>
<pre>
&lt;?php
session_start();

// Predefined valid credentials (in real apps, check against database)
$valid_username = "admin";
$valid_password = "admin123";  // In production, use hashed passwords

// Retrieve form data
$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';

// Validate credentials
if ($username === $valid_username && $password === $valid_password) {
    // Store user info in session
    $_SESSION['username'] = $username;
    $_SESSION['logged_in'] = true;
    $_SESSION['login_time'] = date('Y-m-d H:i:s');

    // Redirect to home page on successful login
    header("Location: home.php");
    exit();
} else {
    // Redirect back to login with error message
    header("Location: login.php?error=1");
    exit();
}
?&gt;
</pre>

<b>home.php — Home Page (Protected):</b>
<pre>
&lt;?php
session_start();

// Check if user is logged in
if (!isset($_SESSION['logged_in']) || $_SESSION['logged_in'] !== true) {
    header("Location: login.php");
    exit();
}
?&gt;
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;&lt;title&gt;Home&lt;/title&gt;&lt;/head&gt;
&lt;body&gt;
  &lt;h1&gt;Welcome, &lt;?php echo htmlspecialchars($_SESSION['username']); ?&gt;!&lt;/h1&gt;
  &lt;p&gt;You successfully logged in at &lt;?php echo $_SESSION['login_time']; ?&gt;.&lt;/p&gt;
  &lt;a href="logout.php"&gt;Logout&lt;/a&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

<b>logout.php — Logout Script:</b>
<pre>
&lt;?php
session_start();
session_unset();
session_destroy();
header("Location: login.php");
exit();
?&gt;
</pre>

<b>Explanation:</b><br/>
• <b>login.php</b> displays the login form with username and password fields.<br/>
• <b>authenticate.php</b> validates credentials against predefined values (or database in production).<br/>
• On success, it creates a session and redirects to <b>home.php</b> using <code>header("Location: ...")</code>.<br/>
• On failure, it redirects back to login.php with an error flag.<br/>
• <b>home.php</b> verifies the session before displaying content, preventing unauthorized access.<br/>
• <b>logout.php</b> destroys the session and redirects to the login page.""",
            },
            {
                "num": "10",
                "question": 'Compare XML Schema with DTD. Write XML schema to describe student as root element, name as child element with first-name, middle name, last name, city as child elements with its content "KTM","PKR","LPT" and rollno as its attribute.',
                "marks": "3+7",
                "answer": """<b>Comparison of XML Schema (XSD) and DTD:</b>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Feature</b></td><td><b>DTD (Document Type Definition)</b></td><td><b>XML Schema (XSD)</b></td></tr>
<tr><td>Syntax</td><td>Uses non-XML syntax</td><td>Uses XML syntax (valid XML document)</td></tr>
<tr><td>Data Types</td><td>Limited to text strings only (CDATA, PCDATA)</td><td>Rich set of data types (string, int, date, decimal, boolean, etc.)</td></tr>
<tr><td>Namespace Support</td><td>No namespace support</td><td>Full namespace support</td></tr>
<tr><td>Complex Types</td><td>Limited support for complex structures</td><td>Supports complex types, sequences, choices, and groups</td></tr>
<tr><td>Occurrence Constraints</td><td>Only *, +, ? operators</td><td>minOccurs and maxOccurs for precise control</td></tr>
<tr><td>Extensibility</td><td>Not extensible</td><td>Highly extensible with inheritance and derivation</td></tr>
<tr><td>Validation</td><td>Less powerful validation</td><td>Strong and detailed validation capabilities</td></tr>
<tr><td>Learning Curve</td><td>Simpler to learn</td><td>More complex but more powerful</td></tr>
<tr><td>Standard</td><td>Older SGML-based standard</td><td>W3C Recommendation, modern standard</td></tr>
</table>

<b>XML Schema for Student:</b>
<pre>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema"&gt;

  &lt;!-- Define city enumeration --&gt;
  &lt;xs:simpleType name="cityType"&gt;
    &lt;xs:restriction base="xs:string"&gt;
      &lt;xs:enumeration value="KTM"/&gt;
      &lt;xs:enumeration value="PKR"/&gt;
      &lt;xs:enumeration value="LPT"/&gt;
    &lt;/xs:restriction&gt;
  &lt;/xs:simpleType&gt;

  &lt;!-- Define name complex type --&gt;
  &lt;xs:complexType name="nameType"&gt;
    &lt;xs:sequence&gt;
      &lt;xs:element name="first-name" type="xs:string"/&gt;
      &lt;xs:element name="middle-name" type="xs:string"/&gt;
      &lt;xs:element name="last-name" type="xs:string"/&gt;
    &lt;/xs:sequence&gt;
  &lt;/xs:complexType&gt;

  &lt;!-- Define student element --&gt;
  &lt;xs:element name="student"&gt;
    &lt;xs:complexType&gt;
      &lt;xs:sequence&gt;
        &lt;xs:element name="name" type="nameType"/&gt;
        &lt;xs:element name="city" type="cityType"/&gt;
      &lt;/xs:sequence&gt;
      &lt;xs:attribute name="rollno" type="xs:string" use="required"/&gt;
    &lt;/xs:complexType&gt;
  &lt;/xs:element&gt;

&lt;/xs:schema&gt;
</pre>

<b>Valid XML Instance Document:</b>
<pre>
&lt;?xml version="1.0" encoding="UTF-8"?&gt;
&lt;student xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:noNamespaceSchemaLocation="student.xsd"
         rollno="BCA101"&gt;
  &lt;name&gt;
    &lt;first-name&gt;Ram&lt;/first-name&gt;
    &lt;middle-name&gt;Prasad&lt;/middle-name&gt;
    &lt;last-name&gt;Sharma&lt;/last-name&gt;
  &lt;/name&gt;
  &lt;city&gt;KTM&lt;/city&gt;
&lt;/student&gt;
</pre>

<b>Explanation:</b><br/>
• <code>cityType</code> restricts city values to "KTM", "PKR", or "LPT" using enumeration.<br/>
• <code>nameType</code> is a complexType containing first-name, middle-name, and last-name as a sequence.<br/>
• The <code>student</code> element contains a <code>name</code> element and a <code>city</code> element, plus a required <code>rollno</code> attribute.<br/>
• <code>use="required"</code> ensures rollno must be present in every student element.""",
            },
            {
                "num": "11",
                "question": "Create web page with following details. a) Create basic structure [2] b) Add header section to the top of page which contain logo and search bar. [2] c) Create two column layout of (25%,75%) width and put unordered list into first one and image gallery into second one. [2] d) Add footer section, which includes address of company and copyright information. [2] e) Also add some basic CSS using external stylesheet.[2]",
                "marks": "2+2+2+2+2",
                "answer": """<b>index.html:</b>
<pre>
&lt;!DOCTYPE html&gt;
&lt;html lang="en"&gt;
&lt;head&gt;
  &lt;meta charset="UTF-8"&gt;
  &lt;meta name="viewport" content="width=device-width, initial-scale=1.0"&gt;
  &lt;title&gt;My Company&lt;/title&gt;
  &lt;link rel="stylesheet" href="style.css"&gt;
&lt;/head&gt;
&lt;body&gt;

  &lt;!-- Header Section --&gt;
  &lt;header&gt;
    &lt;div class="logo"&gt;MyCompany&lt;/div&gt;
    &lt;div class="search-bar"&gt;
      &lt;input type="text" placeholder="Search..."&gt;
      &lt;button&gt;Search&lt;/button&gt;
    &lt;/div&gt;
  &lt;/header&gt;

  &lt;!-- Main Content: Two Column Layout --&gt;
  &lt;div class="main-container"&gt;
    &lt;aside class="sidebar"&gt;
      &lt;h3&gt;Navigation&lt;/h3&gt;
      &lt;ul&gt;
        &lt;li&gt;&lt;a href="#"&gt;Home&lt;/a&gt;&lt;/li&gt;
        &lt;li&gt;&lt;a href="#"&gt;About Us&lt;/a&gt;&lt;/li&gt;
        &lt;li&gt;&lt;a href="#"&gt;Services&lt;/a&gt;&lt;/li&gt;
        &lt;li&gt;&lt;a href="#"&gt;Portfolio&lt;/a&gt;&lt;/li&gt;
        &lt;li&gt;&lt;a href="#"&gt;Contact&lt;/a&gt;&lt;/li&gt;
      &lt;/ul&gt;
    &lt;/aside&gt;

    &lt;section class="content"&gt;
      &lt;h2&gt;Image Gallery&lt;/h2&gt;
      &lt;div class="gallery"&gt;
        &lt;img src="image1.jpg" alt="Image 1"&gt;
        &lt;img src="image2.jpg" alt="Image 2"&gt;
        &lt;img src="image3.jpg" alt="Image 3"&gt;
        &lt;img src="image4.jpg" alt="Image 4"&gt;
      &lt;/div&gt;
    &lt;/section&gt;
  &lt;/div&gt;

  &lt;!-- Footer Section --&gt;
  &lt;footer&gt;
    &lt;div class="address"&gt;
      &lt;p&gt;&lt;strong&gt;MyCompany Pvt. Ltd.&lt;/strong&gt;&lt;/p&gt;
      &lt;p&gt;123 Business Street, Kathmandu, Nepal&lt;/p&gt;
      &lt;p&gt;Phone: +977-1-1234567 | Email: info@mycompany.com&lt;/p&gt;
    &lt;/div&gt;
    &lt;div class="copyright"&gt;
      &lt;p&gt;&amp;copy; 2024 MyCompany. All rights reserved.&lt;/p&gt;
    &lt;/div&gt;
  &lt;/footer&gt;

&lt;/body&gt;
&lt;/html&gt;
</pre>

<b>style.css (External Stylesheet):</b>
<pre>
/* Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  background-color: #f4f4f4;
}

/* Header Styles */
header {
  background-color: #333;
  color: white;
  padding: 15px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 24px;
  font-weight: bold;
}

.search-bar input {
  padding: 8px;
  width: 200px;
  border: none;
  border-radius: 4px 0 0 4px;
}

.search-bar button {
  padding: 8px 15px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
}

/* Main Container: Two Column Layout */
.main-container {
  display: flex;
  min-height: 400px;
  margin: 20px;
}

.sidebar {
  width: 25%;
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0,0,0,0.1);
}

.sidebar h3 {
  margin-bottom: 10px;
  color: #333;
}

.sidebar ul {
  list-style-type: disc;
  padding-left: 20px;
}

.sidebar ul li {
  margin: 8px 0;
}

.sidebar ul li a {
  text-decoration: none;
  color: #007bff;
}

.sidebar ul li a:hover {
  text-decoration: underline;
}

.content {
  width: 75%;
  padding: 20px;
  background-color: #fff;
  margin-left: 20px;
  border-radius: 5px;
  box-shadow: 0 0 5px rgba(0,0,0,0.1);
}

.content h2 {
  margin-bottom: 15px;
  color: #333;
}

.gallery {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 15px;
}

.gallery img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 5px;
  border: 1px solid #ddd;
}

/* Footer Styles */
footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 20px;
  margin-top: 20px;
}

.address p {
  margin: 5px 0;
}

.copyright {
  margin-top: 10px;
  font-size: 14px;
  color: #ccc;
}
</pre>

<b>Explanation:</b><br/>
• <b>Basic Structure (a):</b> Proper DOCTYPE, html, head, and body tags with meta charset and viewport for responsiveness.<br/>
• <b>Header (b):</b> Contains a logo div and a search bar with input field and button.<br/>
• <b>Two-Column Layout (c):</b> Uses CSS Flexbox. Sidebar is 25% with unordered list; Content is 75% with image gallery using CSS Grid.<br/>
• <b>Footer (d):</b> Contains company address and copyright information.<br/>
• <b>External CSS (e):</b> All styling is in <code>style.css</code>, linked via <code>&lt;link&gt;</code> tag in the head section.""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet("CACS205", "web-technology", "Web Technology", 2024, "semester-3", CACS205_2024)
    print("Answer sheet generation complete for CACS205!")
