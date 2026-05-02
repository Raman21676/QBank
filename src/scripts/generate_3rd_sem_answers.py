#!/usr/bin/env python3
"""Generate answer sheets for 3rd semester subjects with clean text extraction."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

# ============== OOP in Java 2019 (CACS 204) ==============

OOP_JAVA_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "i) Which one of the following is not a valid java operator?<br/>a) ● (Dot) &nbsp;&nbsp; b) >>> &nbsp;&nbsp; c) instanceof &nbsp;&nbsp; d) system<br/><br/>ii) Which one of the following keyword is not used in exception handling?<br/>a) throws &nbsp;&nbsp; b) throw &nbsp;&nbsp; c) try &nbsp;&nbsp; d) tries<br/><br/>iii) Which one of the following is not a valid jumping statement in Java?<br/>a) continue &nbsp;&nbsp; b) break &nbsp;&nbsp; c) goto &nbsp;&nbsp; d) return<br/><br/>iv) Which one of the following access specifier is appropriate for members of superclass to access only from subclass?<br/>a) private &nbsp;&nbsp; b) protected &nbsp;&nbsp; c) public &nbsp;&nbsp; d) default<br/><br/>v) Which one of the following is not a collection class defined in java?<br/>a) Linked List &nbsp;&nbsp; b) Hash Set &nbsp;&nbsp; c) Tree Set &nbsp;&nbsp; d) Graph Set<br/><br/>vi) Which one of the following inheritance uses interface?<br/>a) single inheritance &nbsp;&nbsp; b) multi-level inheritance &nbsp;&nbsp; c) multiple inheritance &nbsp;&nbsp; d) hierarchical inheritance<br/><br/>vii) Which one of the following method is called only once during the run time of your applet?<br/>a) stop() &nbsp;&nbsp; b) paint() &nbsp;&nbsp; c) init() &nbsp;&nbsp; d) start()<br/><br/>viii) Which of these method of class String is used to compare two String objects for their equality?<br/>a) equals() &nbsp;&nbsp; b) Equals() &nbsp;&nbsp; c) is Equal() &nbsp;&nbsp; d) Is Equal()<br/><br/>ix) What is the default value of priority variable MIN_PRIORITY and MAX_PRIORITY?<br/>a) 0 & 63 &nbsp;&nbsp; b) 1 & 10 &nbsp;&nbsp; c) 0 & 1 &nbsp;&nbsp; d) 1 & 32<br/><br/>x) Which one of the following is not java swing menu control?<br/>a) Menu Bar &nbsp;&nbsp; b) Menu &nbsp;&nbsp; c) Menu Item &nbsp;&nbsp; d) Menu Scroll",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>i) d) system</b> — system is not an operator; it is a class (System) in java.lang package. The valid operators are dot (.), unsigned right shift (>>>), and instanceof.<br/><br/>
<b>ii) d) tries</b> — The keywords used in exception handling are try, catch, finally, throw, and throws. "tries" is not a Java keyword.<br/><br/>
<b>iii) c) goto</b> — goto is a reserved keyword in Java but it is not used as a valid jumping statement. Java uses break, continue, and return for control flow.<br/><br/>
<b>iv) b) protected</b> — The protected access specifier allows members to be accessed within the same package and by subclasses (even in different packages).<br/><br/>
<b>v) d) Graph Set</b> — LinkedList, HashSet, and TreeSet are all valid collection classes in java.util package. Graph Set does not exist.<br/><br/>
<b>vi) c) multiple inheritance</b> — Java does not support multiple inheritance of classes, but it achieves multiple inheritance through interfaces.<br/><br/>
<b>vii) c) init()</b> — The init() method is called once when the applet is first loaded. start() and stop() can be called multiple times, and paint() is called whenever the applet needs to be redrawn.<br/><br/>
<b>viii) a) equals()</b> — The equals() method (case-sensitive, lowercase) of the String class compares the actual content of two String objects for equality.<br/><br/>
<b>ix) b) 1 & 10</b> — In Java, Thread.MIN_PRIORITY = 1 and Thread.MAX_PRIORITY = 10. The default normal priority is 5 (NORM_PRIORITY).<br/><br/>
<b>x) d) Menu Scroll</b> — JMenuBar, JMenu, and JMenuItem are valid Swing menu components. Menu Scroll is not a standard Swing menu control.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "2",
                "question": "Define OOP. Explain features of Object Oriented Programming Language. [1 + 4]",
                "marks": "5",
                "answer": """<b>Definition of OOP:</b><br/>
Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data (objects) rather than functions and logic. An object is an instance of a class that contains both data (attributes) and methods (behaviors).<br/><br/>
<b>Features of OOP:</b><br/>
<b>1. Encapsulation:</b> Wrapping data and methods into a single unit (class) and restricting direct access to some components using access modifiers (private, protected, public). This protects data integrity.<br/><br/>
<b>2. Inheritance:</b> The mechanism by which one class (subclass/child) acquires the properties and behaviors of another class (superclass/parent). It promotes code reusability. Java supports single, multi-level, hierarchical, and hybrid inheritance.<br/><br/>
<b>3. Polymorphism:</b> The ability to take multiple forms. In Java, it is achieved through method overloading (compile-time polymorphism) and method overriding (runtime polymorphism).<br/><br/>
<b>4. Abstraction:</b> Hiding implementation details and showing only functionality. Achieved using abstract classes and interfaces.<br/><br/>
<b>5. Class and Object:</b> A class is a blueprint/template, while an object is a real-world entity created from that class.""",
            },
            {
                "num": "3",
                "question": "Explain different types of looping statements used in java. [5]",
                "marks": "5",
                "answer": """<b>Looping Statements in Java:</b><br/><br/>
<b>1. for loop:</b> Used when the number of iterations is known beforehand.<br/>
<pre>for(int i=0; i&lt;5; i++) {
    System.out.println(i);
}</pre><br/>
<b>2. while loop:</b> Used when the number of iterations is not known and depends on a condition. The condition is checked before entering the loop.<br/>
<pre>int i = 0;
while(i &lt; 5) {
    System.out.println(i);
    i++;
}</pre><br/>
<b>3. do-while loop:</b> Similar to while, but the condition is checked after executing the loop body. It guarantees at least one execution.<br/>
<pre>int i = 0;
do {
    System.out.println(i);
    i++;
} while(i &lt; 5);</pre><br/>
<b>4. Enhanced for loop (for-each):</b> Used to iterate over arrays or collections without using an index variable.<br/>
<pre>int[] arr = {1, 2, 3, 4, 5};
for(int num : arr) {
    System.out.println(num);
}</pre><br/>
<b>5. Nested loops:</b> A loop inside another loop. Useful for working with multi-dimensional arrays and patterns.""",
            },
            {
                "num": "4",
                "question": "Define Abstract Class. Explain different types of Access controls available in java. [1 + 4]",
                "marks": "5",
                "answer": """<b>Abstract Class:</b><br/>
An abstract class is a class that cannot be instantiated directly. It is declared using the <b>abstract</b> keyword and may contain both abstract methods (without body) and concrete methods (with body). It serves as a base class for subclasses to extend and implement the abstract methods.<br/>
<pre>abstract class Animal {
    abstract void makeSound();
    void sleep() { System.out.println("Sleeping..."); }
}</pre><br/>
<b>Access Controls (Access Modifiers) in Java:</b><br/><br/>
<b>1. private:</b> Accessible only within the same class. Used for encapsulation.<br/><br/>
<b>2. default (package-private):</b> Accessible only within the same package. No keyword is used.<br/><br/>
<b>3. protected:</b> Accessible within the same package and by subclasses in different packages.<br/><br/>
<b>4. public:</b> Accessible from anywhere — any class, any package.<br/><br/>
<table border='1' cellpadding='4'>
<tr><td>Modifier</td><td>Class</td><td>Package</td><td>Subclass</td><td>World</td></tr>
<tr><td>public</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>protected</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr>
<tr><td>default</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr>
<tr><td>private</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr>
</table>""",
            },
            {
                "num": "5",
                "question": "How polymorphism is achieved in Java? Explain with example. [1 + 4]",
                "marks": "5",
                "answer": """<b>Polymorphism in Java:</b><br/>
Polymorphism means "many forms." It allows objects of different classes to be treated as objects of a common superclass. In Java, polymorphism is achieved in two ways:<br/><br/>
<b>1. Compile-time Polymorphism (Method Overloading):</b><br/>
Multiple methods in the same class have the same name but different parameter lists (different number, type, or order of parameters).<br/>
<pre>class Calculator {
    int add(int a, int b) { return a + b; }
    int add(int a, int b, int c) { return a + b + c; }
    double add(double a, double b) { return a + b; }
}
Calculator c = new Calculator();
c.add(2, 3);       // calls first method
c.add(2, 3, 4);    // calls second method
c.add(2.5, 3.5);   // calls third method</pre><br/>
<b>2. Runtime Polymorphism (Method Overriding):</b><br/>
A subclass provides a specific implementation of a method that is already defined in its superclass. The JVM determines which method to call at runtime based on the actual object's class.<br/>
<pre>class Animal {
    void makeSound() { System.out.println("Animal sound"); }
}
class Dog extends Animal {
    void makeSound() { System.out.println("Bark"); }
}
Animal a = new Dog();
a.makeSound(); // Output: Bark (runtime binding)</pre>""",
            },
            {
                "num": "6",
                "question": "Define Exception Handling. Write a program to illustrate the use of exception handling. [1 + 4]",
                "marks": "5",
                "answer": """<b>Exception Handling:</b><br/>
Exception handling is a mechanism in Java to handle runtime errors (exceptions) gracefully without crashing the program. It uses try, catch, finally, throw, and throws keywords to manage exceptional conditions.<br/><br/>
<b>Program illustrating Exception Handling:</b><br/>
<pre>import java.util.Scanner;

public class ExceptionDemo {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {
            System.out.print("Enter first number: ");
            int a = sc.nextInt();
            System.out.print("Enter second number: ");
            int b = sc.nextInt();
            int result = a / b;
            System.out.println("Result: " + result);
        } catch (ArithmeticException e) {
            System.out.println("Error: Division by zero is not allowed!");
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            System.out.println("Execution completed.");
            sc.close();
        }
    }
}</pre><br/>
<b>Explanation:</b><br/>
• <b>try:</b> Contains code that might throw an exception.<br/>
• <b>catch:</b> Handles specific exceptions (ArithmeticException for division by zero).<br/>
• <b>finally:</b> Always executes, used for cleanup (closing resources).<br/>
• <b>throw:</b> Used to explicitly throw an exception.<br/>
• <b>throws:</b> Declares exceptions that a method might throw.""",
            },
            {
                "num": "7",
                "question": "Define the use of static keyword. Write any four String methods used in java with example. [1 + 4]",
                "marks": "5",
                "answer": """<b>static Keyword in Java:</b><br/>
The <b>static</b> keyword is used to create members (variables and methods) that belong to the class itself rather than to any specific instance (object). Static members are shared across all instances of the class and can be accessed without creating an object.<br/><br/>
<b>Uses of static:</b><br/>
• <b>static variable:</b> A single copy shared by all objects (class variable).<br/>
• <b>static method:</b> Can be called without creating an object. Can access only static members directly.<br/>
• <b>static block:</b> Executed once when the class is loaded, used for initialization.<br/>
• <b>static class:</b> Only nested classes can be static.<br/><br/>
<pre>class Student {
    static int count = 0; // static variable
    Student() { count++; }
    static void showCount() { // static method
        System.out.println("Total students: " + count);
    }
}</pre><br/>
<b>Four String Methods with Examples:</b><br/><br/>
<b>1. length():</b> Returns the number of characters in the string.<br/>
<pre>String s = "Hello";
int len = s.length(); // len = 5</pre><br/>
<b>2. charAt(int index):</b> Returns the character at the specified index.<br/>
<pre>String s = "Java";
char c = s.charAt(0); // c = 'J'</pre><br/>
<b>3. substring(int beginIndex, int endIndex):</b> Returns a portion of the string.<br/>
<pre>String s = "Programming";
String sub = s.substring(0, 4); // sub = "Prog"</pre><br/>
<b>4. equals(String str):</b> Compares two strings for content equality.<br/>
<pre>String s1 = "Java";
String s2 = "Java";
boolean result = s1.equals(s2); // result = true</pre>""",
            },
            {
                "num": "8",
                "question": "Define super, final and this keyword in java. Explain the concept of MVC in brief. [1+1+1+2]",
                "marks": "5",
                "answer": """<b>super Keyword:</b><br/>
The <b>super</b> keyword is used to refer to the immediate parent class object. It is used to:<br/>
• Call the parent class constructor: <b>super();</b><br/>
• Access parent class methods: <b>super.methodName();</b><br/>
• Access parent class variables: <b>super.variableName;</b><br/><br/>
<b>final Keyword:</b><br/>
The <b>final</b> keyword is used to restrict modification:<br/>
• <b>final variable:</b> Cannot be changed after initialization (constant).<br/>
• <b>final method:</b> Cannot be overridden by subclasses.<br/>
• <b>final class:</b> Cannot be extended (inherited).<br/><br/>
<b>this Keyword:</b><br/>
The <b>this</b> keyword refers to the current object instance. It is used to:<br/>
• Differentiate instance variables from local variables with the same name.<br/>
• Call another constructor in the same class: <b>this();</b><br/>
• Pass the current object as a parameter.<br/><br/>
<b>MVC (Model-View-Controller) Architecture:</b><br/>
MVC is a software design pattern that separates an application into three interconnected components:<br/><br/>
<b>1. Model:</b> Represents the data and business logic. It manages the application's data, rules, and logic. When data changes, it notifies the View.<br/><br/>
<b>2. View:</b> Represents the user interface (UI). It displays data from the Model to the user and sends user commands to the Controller.<br/><br/>
<b>3. Controller:</b> Acts as an intermediary between Model and View. It receives user input from the View, processes it (using Model), and updates the View accordingly.<br/><br/>
<b>Benefits:</b> Separation of concerns, easier maintenance, parallel development, and code reusability.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "9",
                "question": "a) Define multithreading. Write a java program to show the inter-thread communication. [1+4]<br/>b) Define Stream. Write a program in java to copy the content from one file to another. [1+4]",
                "marks": "10",
                "answer": """<b>a) Multithreading:</b><br/>
Multithreading is a Java feature that allows concurrent execution of two or more parts of a program (threads) for maximum utilization of CPU. A thread is a lightweight sub-process and the smallest unit of processing.<br/><br/>
<b>Program for Inter-thread Communication:</b><br/>
<pre>class SharedResource {
    boolean flag = false;
    synchronized void produce() throws InterruptedException {
        if(flag) wait();
        System.out.println("Producing...");
        flag = true;
        notify();
    }
    synchronized void consume() throws InterruptedException {
        if(!flag) wait();
        System.out.println("Consuming...");
        flag = false;
        notify();
    }
}

class Producer extends Thread {
    SharedResource r;
    Producer(SharedResource r) { this.r = r; }
    public void run() {
        try { for(int i=0; i&lt;5; i++) r.produce(); }
        catch(InterruptedException e) { e.printStackTrace(); }
    }
}

class Consumer extends Thread {
    SharedResource r;
    Consumer(SharedResource r) { this.r = r; }
    public void run() {
        try { for(int i=0; i&lt;5; i++) r.consume(); }
        catch(InterruptedException e) { e.printStackTrace(); }
    }
}

public class InterThreadDemo {
    public static void main(String[] args) {
        SharedResource r = new SharedResource();
        new Producer(r).start();
        new Consumer(r).start();
    }
}</pre><br/>
<b>Explanation:</b> wait() makes the thread wait until notified. notify() wakes up a waiting thread. This achieves inter-thread communication (producer-consumer pattern).<br/><br/>
<b>b) Stream:</b><br/>
A Stream in Java is a sequence of data (bytes or characters) that flows from a source to a destination. Java I/O streams are used for reading from and writing to files, network sockets, and other I/O devices.<br/><br/>
<b>Program to copy content from one file to another:</b><br/>
<pre>import java.io.*;

public class FileCopy {
    public static void main(String[] args) {
        try {
            FileInputStream fis = new FileInputStream("source.txt");
            FileOutputStream fos = new FileOutputStream("destination.txt");
            int ch;
            while((ch = fis.read()) != -1) {
                fos.write(ch);
            }
            System.out.println("File copied successfully!");
            fis.close();
            fos.close();
        } catch(IOException e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}</pre><br/>
<b>Explanation:</b> FileInputStream reads bytes from the source file. FileOutputStream writes bytes to the destination file. The while loop reads one byte at a time until EOF (-1) is reached.""",
            },
            {
                "num": "10",
                "question": "a) Define Collection Class. Explain different Wrapper classes in java. [1 + 4]<br/>b) Define AWT. Explain different types of Layout Managers in java. [1 + 4]",
                "marks": "10",
                "answer": """<b>a) Collection Class:</b><br/>
A Collection in Java is a framework that provides an architecture to store and manipulate a group of objects. It includes interfaces (List, Set, Queue, Map) and classes (ArrayList, LinkedList, HashSet, TreeSet, HashMap, etc.). Collections provide methods for searching, sorting, insertion, manipulation, and deletion of data.<br/><br/>
<b>Wrapper Classes in Java:</b><br/>
Wrapper classes convert primitive data types into objects. Each primitive type has a corresponding wrapper class:<br/>
<table border='1' cellpadding='4'>
<tr><td>Primitive</td><td>Wrapper Class</td></tr>
<tr><td>byte</td><td>Byte</td></tr>
<tr><td>short</td><td>Short</td></tr>
<tr><td>int</td><td>Integer</td></tr>
<tr><td>long</td><td>Long</td></tr>
<tr><td>float</td><td>Float</td></tr>
<tr><td>double</td><td>Double</td></tr>
<tr><td>char</td><td>Character</td></tr>
<tr><td>boolean</td><td>Boolean</td></tr>
</table><br/>
<b>Need for Wrapper Classes:</b><br/>
• Collections (ArrayList, HashSet) can store only objects, not primitives.<br/>
• Wrapper classes provide useful methods (parseInt(), toString(), compareTo()).<br/>
• Autoboxing (primitive → object) and Unboxing (object → primitive) are automatic in Java.<br/><br/>
<b>b) AWT (Abstract Window Toolkit):</b><br/>
AWT is Java's original platform-dependent GUI (Graphical User Interface) toolkit. It contains classes for creating windows, buttons, text fields, menus, and other UI components. AWT components are heavyweight because they use native OS resources.<br/><br/>
<b>Layout Managers in Java AWT:</b><br/><br/>
<b>1. FlowLayout:</b> Arranges components in a left-to-right, top-to-bottom flow (like lines of text in a paragraph). Default for Panel.<br/><br/>
<b>2. BorderLayout:</b> Divides the container into five regions: NORTH, SOUTH, EAST, WEST, and CENTER. Default for Frame and Dialog.<br/><br/>
<b>3. GridLayout:</b> Arranges components in a rectangular grid (rows × columns). All cells have equal size.<br/><br/>
<b>4. CardLayout:</b> Treats each component as a card. Only one card is visible at a time, useful for wizards or tabbed interfaces.<br/><br/>
<b>5. GridBagLayout:</b> Most flexible layout manager. Components can span multiple rows/columns and have different sizes. Uses GridBagConstraints for positioning.""",
            },
            {
                "num": "11",
                "question": "a) List and explain any five swing controls with their uses. [5]<br/>b) Define JDBC. Write a program to display all records from a table of database. [1 + 4]",
                "marks": "10",
                "answer": """<b>a) Five Swing Controls with Uses:</b><br/><br/>
<b>1. JButton:</b> A push button that triggers an action when clicked. Used for submitting forms, confirming actions, etc.<br/>
<pre>JButton btn = new JButton("Click Me");</pre><br/>
<b>2. JTextField:</b> A single-line text input field. Used for entering short text like names, passwords, search queries.<br/>
<pre>JTextField tf = new JTextField(20);</pre><br/>
<b>3. JComboBox:</b> A dropdown list that allows selecting one item from a list. Used for selecting country, gender, department, etc.<br/>
<pre>String[] items = {"Nepal", "India", "China"};
JComboBox cb = new JComboBox(items);</pre><br/>
<b>4. JTable:</b> Displays data in rows and columns (tabular format). Used for showing database records, spreadsheets, etc.<br/>
<pre>String[][] data = {{"1","Ram"}, {"2","Sita"}};
String[] cols = {"ID","Name"};
JTable table = new JTable(data, cols);</pre><br/>
<b>5. JRadioButton:</b> A selectable button where only one option can be selected from a group. Used for single-choice questions, gender selection, etc.<br/>
<pre>JRadioButton male = new JRadioButton("Male");
JRadioButton female = new JRadioButton("Female");
ButtonGroup bg = new ButtonGroup();
bg.add(male); bg.add(female);</pre><br/>
<b>b) JDBC (Java Database Connectivity):</b><br/>
JDBC is a Java API that enables Java applications to interact with relational databases. It provides methods to connect to a database, execute SQL queries, and retrieve results.<br/><br/>
<b>Steps to use JDBC:</b><br/>
1. Load the JDBC driver: <b>Class.forName("com.mysql.cj.jdbc.Driver");</b><br/>
2. Establish connection: <b>DriverManager.getConnection(url, user, password);</b><br/>
3. Create Statement: <b>stmt = conn.createStatement();</b><br/>
4. Execute query: <b>ResultSet rs = stmt.executeQuery("SELECT * FROM table");</b><br/>
5. Process results and close resources.<br/><br/>
<b>Program to display all records:</b><br/>
<pre>import java.sql.*;

public class JDBCDemo {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/college", "root", "password");
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT * FROM students");
            
            System.out.println("ID\tName\tAge");
            while(rs.next()) {
                System.out.println(rs.getInt("id") + "\t" + 
                                   rs.getString("name") + "\t" + 
                                   rs.getInt("age"));
            }
            rs.close();
            stmt.close();
            conn.close();
        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}</pre>""",
            },
        ]
    }
]


# ============== Probability & Statistics 2019 (CAST 202) ==============

PROB_STATS_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "i) How many types of data on the basis of sources of data collection?<br/>a) 1 &nbsp;&nbsp; b) 2 &nbsp;&nbsp; c) 3 &nbsp;&nbsp; d) 4<br/><br/>ii) Which is more appropriate central tendency to find the average of profit?<br/>a) Arithmetic mean &nbsp;&nbsp; b) Median &nbsp;&nbsp; c) Mode &nbsp;&nbsp; d) All<br/><br/>iii) What is the range of Correlation?<br/>a) 0 to ∞ &nbsp;&nbsp; b) -∞ to ∞ &nbsp;&nbsp; c) -1 to 1 &nbsp;&nbsp; d) 0 to 1<br/><br/>iv) If r=0.2 then coefficient of determination implies that<br/>a) 20% of total variation in dependent variable has been explained by independent variable.<br/>b) 40% of total variation...<br/>c) 2% of total variation...<br/>d) 4% of total variation...<br/><br/>v) What is the minimum value of Probability?<br/>a) 1 &nbsp;&nbsp; b) 100 &nbsp;&nbsp; c) 0 &nbsp;&nbsp; d) None of above<br/><br/>vi) In case of Normal distribution<br/>a) Mean > Median &nbsp;&nbsp; b) Mean = Median &nbsp;&nbsp; c) Mean ≤ Median &nbsp;&nbsp; d) Mean ≥ Median<br/><br/>vii) The regression line of X on Y and Y on X are intersect at the point<br/>a) (µ,0) &nbsp;&nbsp; b) (a,b) &nbsp;&nbsp; c) (X,Y) &nbsp;&nbsp; d) (X̄,Ȳ)<br/><br/>viii) In case of systematic sampling<br/>a) sample mean is biased estimator population mean.<br/>b) sample mean is unbiased estimator population mean.<br/>c) sample mean can't estimate population mean.<br/>d) sample mean may equal to population mean.<br/><br/>ix) Mean of Chi-Square distribution with n degrees of freedom is<br/>a) 1 &nbsp;&nbsp; b) 0 &nbsp;&nbsp; c) 2n &nbsp;&nbsp; d) n<br/><br/>x) How do you obtain degree of freedom in one-way ANOVA?<br/>a) (k, n-1) &nbsp;&nbsp; b) (k, n-k) &nbsp;&nbsp; c) (k-1, n-1) &nbsp;&nbsp; d) (k-1, n-k)",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>i) b) 2</b> — On the basis of sources, data is classified into two types: Primary data (collected directly by the investigator) and Secondary data (collected by someone else and used by another).<br/><br/>
<b>ii) c) Mode</b> — Mode is the most appropriate measure of central tendency for finding the average profit because profit data often has extreme values (outliers) and mode represents the most frequently occurring value.<br/><br/>
<b>iii) c) -1 to 1</b> — The correlation coefficient (r) always lies between -1 and +1 inclusive. -1 indicates perfect negative correlation, +1 indicates perfect positive correlation, and 0 indicates no correlation.<br/><br/>
<b>iv) d) 4%</b> — Coefficient of determination = r² = (0.2)² = 0.04 = 4%. It means 4% of the total variation in the dependent variable is explained by the independent variable.<br/><br/>
<b>v) c) 0</b> — The minimum value of probability is 0 (impossible event) and the maximum value is 1 (certain event). Probability always lies between 0 and 1.<br/><br/>
<b>vi) b) Mean = Median</b> — In a normal distribution, the mean, median, and mode are all equal and located at the center of the distribution. The curve is perfectly symmetric.<br/><br/>
<b>vii) d) (X̄, Ȳ)</b> — The two regression lines (X on Y and Y on X) always intersect at the point of means (X̄, Ȳ), which is the mean of X and mean of Y.<br/><br/>
<b>viii) b) sample mean is unbiased estimator population mean.</b> — In systematic sampling, the sample mean is an unbiased estimator of the population mean, provided the population is randomly ordered.<br/><br/>
<b>ix) d) n</b> — For a Chi-Square distribution with n degrees of freedom, the mean is n and the variance is 2n.<br/><br/>
<b>x) d) (k-1, n-k)</b> — In one-way ANOVA, degrees of freedom for treatment (between groups) = k-1, and degrees of freedom for error (within groups) = n-k, where k = number of groups and n = total number of observations.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "2",
                "question": "Describe scope and limitation of Statistics. [5]",
                "marks": "5",
                "answer": """<b>Scope of Statistics:</b><br/><br/>
<b>1. Business and Economics:</b> Statistics is extensively used in business for demand forecasting, market research, quality control, pricing decisions, and sales analysis. In economics, it helps in calculating GDP, inflation rates, unemployment rates, and economic planning.<br/><br/>
<b>2. Government and Administration:</b> Governments use statistics for census, budget preparation, policy formulation, public health planning, and resource allocation.<br/><br/>
<b>3. Natural and Social Sciences:</b> In biology (biostatistics), medicine (clinical trials), psychology (behavioral studies), sociology (surveys), and education (test scoring).<br/><br/>
<b>4. Research:</b> Statistical methods are essential for designing experiments, analyzing data, testing hypotheses, and drawing valid conclusions in all fields of research.<br/><br/>
<b>5. Banking and Finance:</b> Risk assessment, portfolio management, credit scoring, insurance premium calculation, and stock market analysis.<br/><br/>
<b>Limitations of Statistics:</b><br/><br/>
<b>1. Deals with aggregates only:</b> Statistics cannot study individual cases. It studies groups, not single observations.<br/><br/>
<b>2. Homogeneous data required:</b> Statistical methods are applicable only to homogeneous (similar) data. Heterogeneous data must be separated before analysis.<br/><br/>
<b>3. Results are true on average:</b> Statistical laws are not exact like mathematical laws. They are true on average and under certain conditions.<br/><br/>
<b>4. Can be misused:</b> Statistics can be manipulated to support false conclusions. Misleading graphs, selective data, and biased sampling can distort reality.<br/><br/>
<b>5. Does not study qualitative phenomena:</b> Statistics primarily deals with numerical data. Qualitative aspects like beauty, honesty, and intelligence cannot be directly measured statistically.""",
            },
            {
                "num": "3",
                "question": "Determine average wages from following data:<br/><table border='1' cellpadding='3'><tr><td>Wages</td><td>25-30</td><td>30-35</td><td>35-40</td><td>40-45</td><td>45-50</td><td>50-55</td><td>55-60</td><td>60-65</td><td>65-70</td></tr><tr><td>No. of Worker</td><td>10</td><td>13</td><td>18</td><td>21</td><td>24</td><td>28</td><td>20</td><td>11</td><td>8</td></tr></table>",
                "marks": "5",
                "answer": """<b>Solution:</b> We calculate the mean using the assumed mean method.<br/><br/>
<table border='1' cellpadding='3'>
<tr><td>Wages</td><td>f</td><td>Mid (x)</td><td>d=(x-47.5)/5</td><td>fd</td></tr>
<tr><td>25-30</td><td>10</td><td>27.5</td><td>-4</td><td>-40</td></tr>
<tr><td>30-35</td><td>13</td><td>32.5</td><td>-3</td><td>-39</td></tr>
<tr><td>35-40</td><td>18</td><td>37.5</td><td>-2</td><td>-36</td></tr>
<tr><td>40-45</td><td>21</td><td>42.5</td><td>-1</td><td>-21</td></tr>
<tr><td>45-50</td><td>24</td><td>47.5</td><td>0</td><td>0</td></tr>
<tr><td>50-55</td><td>28</td><td>52.5</td><td>1</td><td>28</td></tr>
<tr><td>55-60</td><td>20</td><td>57.5</td><td>2</td><td>40</td></tr>
<tr><td>60-65</td><td>11</td><td>62.5</td><td>3</td><td>33</td></tr>
<tr><td>65-70</td><td>8</td><td>67.5</td><td>4</td><td>32</td></tr>
<tr><td><b>Total</b></td><td><b>N=153</b></td><td></td><td></td><td><b>Σfd=-3</b></td></tr>
</table><br/>
Assumed mean A = 47.5, class width h = 5<br/>
Mean = A + (Σfd/N) × h = 47.5 + (-3/153) × 5 = 47.5 - 0.098 = <b>47.40</b><br/><br/>
<b>Average wages = Rs. 47.40</b>""",
            },
            {
                "num": "4",
                "question": "Calculate Karl Pearson's correlation coefficient from the following data:<br/><table border='1' cellpadding='3'><tr><td>Sales</td><td>43</td><td>41</td><td>36</td><td>34</td><td>50</td></tr><tr><td>Expenses</td><td>10</td><td>22</td><td>13</td><td>19</td><td>17</td></tr></table>",
                "marks": "5",
                "answer": """<b>Solution:</b><br/><br/>
<table border='1' cellpadding='3'>
<tr><td>Sales (X)</td><td>Expenses (Y)</td><td>x=X-X̄</td><td>y=Y-Ȳ</td><td>x²</td><td>y²</td><td>xy</td></tr>
<tr><td>43</td><td>10</td><td>3.8</td><td>-6.2</td><td>14.44</td><td>38.44</td><td>-23.56</td></tr>
<tr><td>41</td><td>22</td><td>1.8</td><td>5.8</td><td>3.24</td><td>33.64</td><td>10.44</td></tr>
<tr><td>36</td><td>13</td><td>-3.2</td><td>-3.2</td><td>10.24</td><td>10.24</td><td>10.24</td></tr>
<tr><td>34</td><td>19</td><td>-5.2</td><td>2.8</td><td>27.04</td><td>7.84</td><td>-14.56</td></tr>
<tr><td>50</td><td>17</td><td>10.8</td><td>0.8</td><td>116.64</td><td>0.64</td><td>8.64</td></tr>
<tr><td><b>ΣX=204</b></td><td><b>ΣY=81</b></td><td></td><td></td><td><b>Σx²=171.6</b></td><td><b>Σy²=90.8</b></td><td><b>Σxy=-8.8</b></td></tr>
</table><br/>
X̄ = 204/5 = 40.8, Ȳ = 81/5 = 16.2<br/><br/>
r = Σxy / √(Σx² × Σy²) = -8.8 / √(171.6 × 90.8) = -8.8 / √15581.28 = -8.8 / 124.825 = <b>-0.0705</b><br/><br/>
<b>Karl Pearson's r ≈ -0.07 (very weak negative correlation)</b><br/>
This indicates almost no linear relationship between Sales and Expenses.""",
            },
            {
                "num": "5",
                "question": "Estimate the marks in JAVA when the marks in Statistics is 65 by using following data:<br/><table border='1' cellpadding='3'><tr><td>Marks in Statistics</td><td>57</td><td>58</td><td>59</td><td>59</td><td>60</td><td>61</td><td>62</td><td>64</td></tr><tr><td>Marks in JAVA</td><td>77</td><td>78</td><td>75</td><td>78</td><td>82</td><td>82</td><td>79</td><td>81</td></tr></table>",
                "marks": "5",
                "answer": """<b>Solution:</b> We need to find the regression equation of Y (JAVA) on X (Statistics).<br/><br/>
<table border='1' cellpadding='3'>
<tr><td>X</td><td>Y</td><td>x=X-60</td><td>y=Y-79</td><td>x²</td><td>y²</td><td>xy</td></tr>
<tr><td>57</td><td>77</td><td>-3</td><td>-2</td><td>9</td><td>4</td><td>6</td></tr>
<tr><td>58</td><td>78</td><td>-2</td><td>-1</td><td>4</td><td>1</td><td>2</td></tr>
<tr><td>59</td><td>75</td><td>-1</td><td>-4</td><td>1</td><td>16</td><td>4</td></tr>
<tr><td>59</td><td>78</td><td>-1</td><td>-1</td><td>1</td><td>1</td><td>1</td></tr>
<tr><td>60</td><td>82</td><td>0</td><td>3</td><td>0</td><td>9</td><td>0</td></tr>
<tr><td>61</td><td>82</td><td>1</td><td>3</td><td>1</td><td>9</td><td>3</td></tr>
<tr><td>62</td><td>79</td><td>2</td><td>0</td><td>4</td><td>0</td><td>0</td></tr>
<tr><td>64</td><td>81</td><td>4</td><td>2</td><td>16</td><td>4</td><td>8</td></tr>
<tr><td><b>ΣX=480</b></td><td><b>ΣY=632</b></td><td></td><td></td><td><b>Σx²=36</b></td><td><b>Σy²=44</b></td><td><b>Σxy=24</b></td></tr>
</table><br/>
X̄ = 480/8 = 60, Ȳ = 632/8 = 79<br/><br/>
Regression coefficient b_yx = Σxy/Σx² = 24/36 = 0.667<br/><br/>
Regression equation: Y - Ȳ = b_yx(X - X̄)<br/>
Y - 79 = 0.667(X - 60)<br/>
Y = 0.667X - 40 + 79<br/>
Y = 0.667X + 39<br/><br/>
When X = 65:<br/>
Y = 0.667(65) + 39 = 43.355 + 39 = <b>82.355 ≈ 82</b><br/><br/>
<b>Estimated marks in JAVA when Statistics = 65 is approximately 82 marks.</b>""",
            },
            {
                "num": "6",
                "question": "Fit Binomial Distribution from the following data where p = 0.5:<br/><table border='1' cellpadding='3'><tr><td>No. of heads</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>Frequency</td><td>28</td><td>62</td><td>46</td><td>20</td><td>4</td></tr></table>",
                "marks": "5",
                "answer": """<b>Solution:</b><br/><br/>
Given: p = 0.5, q = 1 - p = 0.5<br/>
N = Total frequency = 28 + 62 + 46 + 20 + 4 = 160<br/>
n = 4 (maximum number of heads)<br/><br/>
The binomial probabilities are calculated using P(X=r) = ⁿCᵣ pʳ qⁿ⁻ʳ<br/><br/>
<b>P(X=0)</b> = ⁴C₀ (0.5)⁰(0.5)⁴ = 1 × 1 × 0.0625 = 0.0625<br/>
Expected frequency = 160 × 0.0625 = <b>10</b><br/><br/>
<b>P(X=1)</b> = ⁴C₁ (0.5)¹(0.5)³ = 4 × 0.5 × 0.125 = 0.25<br/>
Expected frequency = 160 × 0.25 = <b>40</b><br/><br/>
<b>P(X=2)</b> = ⁴C₂ (0.5)²(0.5)² = 6 × 0.25 × 0.25 = 0.375<br/>
Expected frequency = 160 × 0.375 = <b>60</b><br/><br/>
<b>P(X=3)</b> = ⁴C₃ (0.5)³(0.5)¹ = 4 × 0.125 × 0.5 = 0.25<br/>
Expected frequency = 160 × 0.25 = <b>40</b><br/><br/>
<b>P(X=4)</b> = ⁴C₄ (0.5)⁴(0.5)⁰ = 1 × 0.0625 × 1 = 0.0625<br/>
Expected frequency = 160 × 0.0625 = <b>10</b><br/><br/>
<table border='1' cellpadding='3'>
<tr><td>No. of heads (x)</td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>Total</td></tr>
<tr><td>Observed (f)</td><td>28</td><td>62</td><td>46</td><td>20</td><td>4</td><td>160</td></tr>
<tr><td>Expected</td><td>10</td><td>40</td><td>60</td><td>40</td><td>10</td><td>160</td></tr>
</table><br/>
The fitted binomial distribution shows the expected frequencies under the theoretical binomial model with p=0.5.""",
            },
            {
                "num": "7",
                "question": "How do you determine sample size in sampling? Explain briefly. [5]",
                "marks": "5",
                "answer": """<b>Determination of Sample Size:</b><br/><br/>
Sample size is the number of observations or individuals included in a sample. It is crucial for obtaining reliable and valid results. The sample size depends on several factors:<br/><br/>
<b>1. Population Size (N):</b> For very large populations, the sample size formula becomes independent of N. For small populations, finite population correction is applied.<br/><br/>
<b>2. Margin of Error (E):</b> The maximum acceptable difference between sample statistic and population parameter. Smaller margin requires larger sample size.<br/><br/>
<b>3. Confidence Level:</b> Common levels are 90%, 95%, and 99%. Higher confidence requires larger sample size. Z-values: 90% → 1.645, 95% → 1.96, 99% → 2.576.<br/><br/>
<b>4. Population Standard Deviation (σ):</b> Higher variability requires larger sample size.<br/><br/>
<b>Formulas:</b><br/>
For estimating mean: n = (Z² × σ²) / E²<br/>
For estimating proportion: n = (Z² × p × q) / E²<br/><br/>
Where:<br/>
• Z = critical value from standard normal distribution<br/>
• σ = population standard deviation (or sample estimate)<br/>
• E = margin of error<br/>
• p = estimated proportion, q = 1-p<br/><br/>
<b>Example:</b> To estimate average income with 95% confidence, margin of error = Rs. 100, and σ = Rs. 500:<br/>
n = (1.96² × 500²) / 100² = (3.8416 × 250000) / 10000 = 960400 / 10000 = 96.04 ≈ <b>97</b><br/><br/>
<b>Practical Considerations:</b><br/>
• Budget constraints may limit sample size<br/>
• Response rate should be considered (increase sample size accordingly)<br/>
• For stratified sampling, allocate samples proportionally to strata sizes""",
            },
            {
                "num": "8",
                "question": "Write short notes on simple random sampling. [5]",
                "marks": "5",
                "answer": """<b>Simple Random Sampling (SRS):</b><br/><br/>
Simple Random Sampling is a probability sampling technique where every member of the population has an equal and independent chance of being selected in the sample. It is the most basic and fundamental sampling method.<br/><br/>
<b>Methods of Selection:</b><br/><br/>
<b>1. Lottery Method:</b> Each member of the population is assigned a number, numbers are written on identical slips, mixed thoroughly, and the required number of slips are drawn blindly.<br/><br/>
<b>2. Random Number Table:</b> Using published tables of random digits (like Tippett's table, Fisher-Yates table) to select sample members.<br/><br/>
<b>3. Computer-Generated Random Numbers:</b> Using software functions like RAND() in Excel or random module in Python to generate random numbers.<br/><br/>
<b>Advantages:</b><br/>
• Free from personal bias and subjectivity<br/>
• Easy to understand and implement<br/>
• Every unit has equal chance of selection<br/>
• Sample is representative if population is homogeneous<br/>
• Statistical theory is well-developed for inference<br/><br/>
<b>Disadvantages:</b><br/>
• Requires complete list of population (sampling frame)<br/>
• May not represent subgroups well if population is heterogeneous<br/>
• Can be expensive and time-consuming for large, dispersed populations<br/>
• Sample may be geographically scattered, increasing survey costs<br/><br/>
<b>When to use:</b> SRS is most suitable when the population is small, homogeneous, and a complete sampling frame is available.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "9",
                "question": "Student's age in the regular daytime BCA program and the morning time BCA program of a campus are described by two samples. If the homogeneity in age of the class is positive factor in learning make suggestion, with reason, which of two groups will be easier to teach?<br/><table border='1' cellpadding='3'><tr><td colspan='2'>Regular BCA program</td><td colspan='2'>Morning BCA program</td></tr><tr><td>Age</td><td>No. of Students</td><td>Age</td><td>No. of Students</td></tr><tr><td>23</td><td>9</td><td>27</td><td>10</td></tr><tr><td>29</td><td>2</td><td>31</td><td>8</td></tr><tr><td>28</td><td>5</td><td>30</td><td>5</td></tr><tr><td>22</td><td>10</td><td>29</td><td>4</td></tr><tr><td>30</td><td>1</td><td>28</td><td>6</td></tr><tr><td>21</td><td>4</td><td>33</td><td>5</td></tr><tr><td>25</td><td>11</td><td>34</td><td>5</td></tr><tr><td>26</td><td>6</td><td>35</td><td>11</td></tr><tr><td>27</td><td>3</td><td>36</td><td>2</td></tr><tr><td>24</td><td>9</td><td>32</td><td>4</td></tr><tr><td>Total</td><td>60</td><td>Total</td><td>60</td></tr></table>",
                "marks": "10",
                "answer": """<b>Solution:</b> We compare homogeneity using Coefficient of Variation (CV). Lower CV means more homogeneous.<br/><br/>
<b>For Regular BCA Program:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Age (X)</td><td>f</td><td>fX</td><td>X²</td><td>fX²</td></tr>
<tr><td>21</td><td>4</td><td>84</td><td>441</td><td>1764</td></tr>
<tr><td>22</td><td>10</td><td>220</td><td>484</td><td>4840</td></tr>
<tr><td>23</td><td>9</td><td>207</td><td>529</td><td>4761</td></tr>
<tr><td>24</td><td>9</td><td>216</td><td>576</td><td>5184</td></tr>
<tr><td>25</td><td>11</td><td>275</td><td>625</td><td>6875</td></tr>
<tr><td>26</td><td>6</td><td>156</td><td>676</td><td>4056</td></tr>
<tr><td>27</td><td>3</td><td>81</td><td>729</td><td>2187</td></tr>
<tr><td>28</td><td>5</td><td>140</td><td>784</td><td>3920</td></tr>
<tr><td>29</td><td>2</td><td>58</td><td>841</td><td>1682</td></tr>
<tr><td>30</td><td>1</td><td>30</td><td>900</td><td>900</td></tr>
<tr><td><b>Total</b></td><td><b>60</b></td><td><b>1467</b></td><td></td><td><b>36169</b></td></tr>
</table><br/>
Mean = 1467/60 = 24.45<br/>
Variance = (36169/60) - (24.45)² = 602.817 - 597.803 = 5.014<br/>
SD = √5.014 = 2.24<br/>
CV = (2.24/24.45) × 100 = <b>9.16%</b><br/><br/>
<b>For Morning BCA Program:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Age (Y)</td><td>f</td><td>fY</td><td>Y²</td><td>fY²</td></tr>
<tr><td>27</td><td>10</td><td>270</td><td>729</td><td>7290</td></tr>
<tr><td>28</td><td>6</td><td>168</td><td>784</td><td>4704</td></tr>
<tr><td>29</td><td>4</td><td>116</td><td>841</td><td>3364</td></tr>
<tr><td>30</td><td>5</td><td>150</td><td>900</td><td>4500</td></tr>
<tr><td>31</td><td>8</td><td>248</td><td>961</td><td>7688</td></tr>
<tr><td>32</td><td>4</td><td>128</td><td>1024</td><td>4096</td></tr>
<tr><td>33</td><td>5</td><td>165</td><td>1089</td><td>5445</td></tr>
<tr><td>34</td><td>5</td><td>170</td><td>1156</td><td>5780</td></tr>
<tr><td>35</td><td>11</td><td>385</td><td>1225</td><td>13475</td></tr>
<tr><td>36</td><td>2</td><td>72</td><td>1296</td><td>2592</td></tr>
<tr><td><b>Total</b></td><td><b>60</b></td><td><b>1872</b></td><td></td><td><b>58934</b></td></tr>
</table><br/>
Mean = 1872/60 = 31.2<br/>
Variance = (58934/60) - (31.2)² = 982.233 - 973.44 = 8.793<br/>
SD = √8.793 = 2.965<br/>
CV = (2.965/31.2) × 100 = <b>9.50%</b><br/><br/>
<b>Conclusion:</b><br/>
The Regular BCA program has CV = 9.16%, while Morning BCA has CV = 9.50%. Since the Regular BCA program has a lower coefficient of variation, it is <b>more homogeneous</b> in age.<br/><br/>
<b>Suggestion:</b> The <b>Regular BCA program</b> will be easier to teach because the students' ages are more uniform (less variation). Homogeneous age groups tend to have similar learning paces, prior knowledge levels, and cognitive development, making it easier for instructors to design and deliver lessons effectively.""",
            },
            {
                "num": "10",
                "question": "Given a normal distribution with mean 200 and s.d. 20, find the probability that<br/>i) P(X>180) &nbsp;&nbsp; ii) P(X<220)<br/>iii) P(160<X<240) &nbsp;&nbsp; iv) P(X>220)<br/>v) P(X<180 or X>220) &nbsp;&nbsp; vi) 10% of the values are less than what values of X?",
                "marks": "10",
                "answer": """<b>Solution:</b> Given: μ = 200, σ = 20<br/>
We use Z = (X - μ) / σ<br/><br/>
<b>i) P(X > 180):</b><br/>
Z = (180 - 200) / 20 = -1<br/>
P(X > 180) = P(Z > -1) = P(Z < 1) = <b>0.8413 or 84.13%</b><br/><br/>
<b>ii) P(X < 220):</b><br/>
Z = (220 - 200) / 20 = 1<br/>
P(X < 220) = P(Z < 1) = <b>0.8413 or 84.13%</b><br/><br/>
<b>iii) P(160 < X < 240):</b><br/>
Z₁ = (160 - 200) / 20 = -2<br/>
Z₂ = (240 - 200) / 20 = 2<br/>
P(-2 < Z < 2) = P(Z < 2) - P(Z < -2) = 0.9772 - 0.0228 = <b>0.9544 or 95.44%</b><br/><br/>
<b>iv) P(X > 220):</b><br/>
Z = (220 - 200) / 20 = 1<br/>
P(X > 220) = P(Z > 1) = 1 - P(Z < 1) = 1 - 0.8413 = <b>0.1587 or 15.87%</b><br/><br/>
<b>v) P(X < 180 or X > 220):</b><br/>
P(X < 180) = P(Z < -1) = 0.1587<br/>
P(X > 220) = 0.1587 (from iv)<br/>
Since these are mutually exclusive: P(X < 180 or X > 220) = 0.1587 + 0.1587 = <b>0.3174 or 31.74%</b><br/><br/>
Alternatively: 1 - P(180 < X < 220) = 1 - [P(Z < 1) - P(Z < -1)] = 1 - [0.8413 - 0.1587] = 1 - 0.6826 = 0.3174<br/><br/>
<b>vi) Find X such that P(X < x) = 10% = 0.10:</b><br/>
From Z-table, P(Z < -1.28) ≈ 0.10<br/>
Z = (X - 200) / 20 = -1.28<br/>
X = 200 + (-1.28 × 20) = 200 - 25.6 = <b>174.4</b><br/><br/>
<b>10% of the values are less than 174.4.</b>""",
            },
            {
                "num": "11",
                "question": "The labor productivity indexes of Nepal are recorded as below:<br/><table border='1' cellpadding='3'><tr><td>Sector</td><td colspan='3'>Year</td></tr><tr><td></td><td>2015</td><td>2016</td><td>2017</td></tr><tr><td>Agriculture</td><td>100</td><td>125</td><td>138</td></tr><tr><td>Manufacturing</td><td>100</td><td>60</td><td>53</td></tr><tr><td>Community and Social service</td><td>100</td><td>89</td><td>80</td></tr></table>Does the labor productivity index vary due to the;<br/>i) difference in the sector &nbsp;&nbsp; ii) difference in the time period?",
                "marks": "10",
                "answer": """<b>Solution:</b> This is a Two-Way ANOVA problem.<br/><br/>
<b>Step 1: Calculate row totals, column totals, and grand total</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Sector</td><td>2015</td><td>2016</td><td>2017</td><td>Row Total (Rᵢ)</td></tr>
<tr><td>Agriculture</td><td>100</td><td>125</td><td>138</td><td>363</td></tr>
<tr><td>Manufacturing</td><td>100</td><td>60</td><td>53</td><td>213</td></tr>
<tr><td>Community & Social</td><td>100</td><td>89</td><td>80</td><td>269</td></tr>
<tr><td>Col Total (Cⱼ)</td><td>300</td><td>274</td><td>271</td><td><b>G=845</b></td></tr>
</table><br/>
N = 9, k = 3 sectors, h = 3 years<br/><br/>
<b>Step 2: Calculate Correction Factor (CF)</b><br/>
CF = G²/N = 845²/9 = 714025/9 = 79336.11<br/><br/>
<b>Step 3: Calculate Total Sum of Squares (TSS)</b><br/>
TSS = ΣX² - CF = (100²+125²+138²+100²+60²+53²+100²+89²+80²) - 79336.11<br/>
= (10000+15625+19044+10000+3600+2809+10000+7921+6400) - 79336.11<br/>
= 85399 - 79336.11 = <b>6062.89</b><br/><br/>
<b>Step 4: Calculate Sum of Squares between Sectors (SSS)</b><br/>
SSS = (ΣRᵢ²/h) - CF = (363²+213²+269²)/3 - 79336.11<br/>
= (131769+45369+72361)/3 - 79336.11<br/>
= 249499/3 - 79336.11 = 83166.33 - 79336.11 = <b>3830.22</b><br/><br/>
<b>Step 5: Calculate Sum of Squares between Years (SSY)</b><br/>
SSY = (ΣCⱼ²/k) - CF = (300²+274²+271²)/3 - 79336.11<br/>
= (90000+75076+73441)/3 - 79336.11<br/>
= 238517/3 - 79336.11 = 79505.67 - 79336.11 = <b>169.56</b><br/><br/>
<b>Step 6: Calculate Error Sum of Squares (SSE)</b><br/>
SSE = TSS - SSS - SSY = 6062.89 - 3830.22 - 169.56 = <b>2063.11</b><br/><br/>
<b>Step 7: ANOVA Table</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Source</td><td>SS</td><td>df</td><td>MSS</td><td>F</td></tr>
<tr><td>Sectors</td><td>3830.22</td><td>2</td><td>1915.11</td><td>1.86</td></tr>
<tr><td>Years</td><td>169.56</td><td>2</td><td>84.78</td><td>0.08</td></tr>
<tr><td>Error</td><td>2063.11</td><td>4</td><td>515.78</td><td></td></tr>
<tr><td>Total</td><td>6062.89</td><td>8</td><td></td><td></td></tr>
</table><br/>
<b>Step 8: Compare with F-critical</b><br/>
F-critical (2,4) at 5% = 6.94<br/><br/>
<b>For Sectors:</b> F = 1.86 < 6.94 → <b>Not significant</b><br/>
<b>For Years:</b> F = 0.08 < 6.94 → <b>Not significant</b><br/><br/>
<b>Conclusion:</b><br/>
i) <b>No</b>, the labor productivity index does not vary significantly due to difference in sectors (F = 1.86 < 6.94).<br/>
ii) <b>No</b>, the labor productivity index does not vary significantly due to difference in time periods (F = 0.08 < 6.94).<br/><br/>
Note: The small sample size and limited data may contribute to the non-significant results.""",
            },
        ]
    }
]


if __name__ == "__main__":
    print("Generating OOP in Java 2019 answer sheet...")
    generate_answer_sheet("CACS204", "oop-java", "OOP in Java", 2019, "semester-3", OOP_JAVA_2019)
    print("✅ OOP in Java 2019 answer sheet generated!\n")
    
    print("Generating Probability & Statistics 2019 answer sheet...")
    generate_answer_sheet("CAST202", "probability-statistics", "Probability & Statistics", 2019, "semester-3", PROB_STATS_2019)
    print("✅ Probability & Statistics 2019 answer sheet generated!\n")
    
    print("🎉 All 3rd-semester 2019 answer sheets generated successfully!")
