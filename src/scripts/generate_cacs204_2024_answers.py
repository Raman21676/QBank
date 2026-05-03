import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS204_2024 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What is constructor? Explain the role of constructor in Java class by considering a suitable example and also list the type of constructor.",
                "marks": "1+3+1",
                "answer": """A <b>constructor</b> is a special method in Java that is automatically invoked when an object of a class is created. It has the same name as the class and does not have a return type—not even void.

<b>Role of Constructor in Java:</b><br/>
1. <b>Object Initialization:</b> Constructors initialize the instance variables of a class at the time of object creation.<br/>
2. <b>Memory Allocation:</b> They help in allocating memory to the object on the heap.<br/>
3. <b>Default Values:</b> If no constructor is defined, Java provides a default constructor that initializes variables with default values (0, null, false).<br/>
4. <b>Code Reusability:</b> Constructors can call other constructors using <code>this()</code>, promoting code reuse.

<b>Example:</b>
<pre>
class Student {
    int id;
    String name;

    // Parameterized Constructor
    Student(int i, String n) {
        id = i;
        name = n;
    }

    void display() {
        System.out.println("ID: " + id + ", Name: " + name);
    }

    public static void main(String[] args) {
        Student s1 = new Student(101, "Ram");
        s1.display();
    }
}
</pre>

<b>Types of Constructor:</b><br/>
1. <b>Default Constructor:</b> No parameters; provided by Java if none is written.<br/>
2. <b>Parameterized Constructor:</b> Accepts one or more parameters to initialize object with specific values.<br/>
3. <b>Copy Constructor:</b> Copies values from one object to another (not built-in in Java but can be created manually).""",
            },
            {
                "num": "3",
                "question": "Define inheritance. Explain types of inheritance with suitable example.",
                "marks": "1+4",
                "answer": """<b>Inheritance</b> is an Object-Oriented Programming concept where one class (child/subclass) acquires the properties and behaviors (fields and methods) of another class (parent/superclass). It promotes code reusability and establishes an "is-a" relationship.

<b>Types of Inheritance in Java:</b>

1. <b>Single Inheritance:</b> A class inherits from one parent class.
<pre>
class Animal {
    void eat() { System.out.println("Eating..."); }
}
class Dog extends Animal {
    void bark() { System.out.println("Barking..."); }
}
</pre>

2. <b>Multilevel Inheritance:</b> A class inherits from a class which itself inherits from another class.
<pre>
class Animal { void eat() {} }
class Dog extends Animal { void bark() {} }
class Puppy extends Dog { void weep() {} }
</pre>

3. <b>Hierarchical Inheritance:</b> Multiple classes inherit from a single parent class.
<pre>
class Animal { void eat() {} }
class Dog extends Animal { void bark() {} }
class Cat extends Animal { void meow() {} }
</pre>

4. <b>Multiple Inheritance (via Interfaces):</b> A class implements multiple interfaces.
<pre>
interface Flyable { void fly(); }
interface Swimmable { void swim(); }
class Duck implements Flyable, Swimmable {
    public void fly() { System.out.println("Flying"); }
    public void swim() { System.out.println("Swimming"); }
}
</pre>

5. <b>Hybrid Inheritance:</b> A combination of two or more types of inheritance (achieved using interfaces in Java).""",
            },
            {
                "num": "4",
                "question": "Define Package. Explain steps in creation and implementation of package with example.",
                "marks": "1+4",
                "answer": """A <b>package</b> in Java is a namespace that organizes a set of related classes and interfaces. It helps avoid naming conflicts, provides access protection, and makes searching and locating classes easier.

<b>Steps to Create and Implement a Package:</b><br/>
<b>Step 1 — Declare the Package:</b> Use the <code>package</code> keyword at the top of the Java source file.
<pre>
package mypackage;
</pre>

<b>Step 2 — Create Directory Structure:</b> The directory structure must match the package name. For <code>mypackage</code>, create a folder named <code>mypackage</code>.

<b>Step 3 — Place Source File:</b> Save the Java file inside the package directory.
<pre>
// mypackage/Student.java
package mypackage;

public class Student {
    public void display() {
        System.out.println("Hello from mypackage!");
    }
}
</pre>

<b>Step 4 — Compile the Package:</b>
<pre>
javac -d . mypackage/Student.java
</pre>
The <code>-d .</code> option creates the package directory automatically.

<b>Step 5 — Use the Package (Import and Implement):</b>
<pre>
// TestPackage.java
import mypackage.Student;

public class TestPackage {
    public static void main(String[] args) {
        Student s = new Student();
        s.display();
    }
}
</pre>

<b>Compile and Run:</b>
<pre>
javac TestPackage.java
java TestPackage
</pre>

<b>Types of Packages:</b><br/>
• <b>Built-in packages:</b> java.lang, java.util, java.io, etc.<br/>
• <b>User-defined packages:</b> Created by the programmer as shown above.""",
            },
            {
                "num": "5",
                "question": "What is multithreading? How does Java support inter-thread communication? Explain with example.",
                "marks": "1+4",
                "answer": """<b>Multithreading</b> is a process of executing multiple threads simultaneously within a single program. A <b>thread</b> is the smallest unit of processing that can be scheduled by the operating system. Multithreading improves CPU utilization, enables concurrent execution, and makes applications more responsive.

<b>Inter-Thread Communication in Java:</b><br/>
Java supports inter-thread communication using three methods from the <code>Object</code> class:<br/>
• <code>wait()</code> — Causes the current thread to release the lock and wait until another thread invokes notify() or notifyAll().<br/>
• <code>notify()</code> — Wakes up a single thread that is waiting on the object's monitor.<br/>
• <code>notifyAll()</code> — Wakes up all threads waiting on the object's monitor.

These methods must be called from a synchronized context.

<b>Example — Producer-Consumer Problem:</b>
<pre>
class SharedResource {
    boolean flag = false;
    int data;

    synchronized void produce(int value) throws InterruptedException {
        while (flag) { wait(); }
        data = value;
        System.out.println("Produced: " + data);
        flag = true;
        notify();
    }

    synchronized void consume() throws InterruptedException {
        while (!flag) { wait(); }
        System.out.println("Consumed: " + data);
        flag = false;
        notify();
    }
}

class Producer extends Thread {
    SharedResource sr;
    Producer(SharedResource sr) { this.sr = sr; }
    public void run() {
        try { for (int i = 1; i <= 5; i++) sr.produce(i); }
        catch (InterruptedException e) { e.printStackTrace(); }
    }
}

class Consumer extends Thread {
    SharedResource sr;
    Consumer(SharedResource sr) { this.sr = sr; }
    public void run() {
        try { for (int i = 1; i <= 5; i++) sr.consume(); }
        catch (InterruptedException e) { e.printStackTrace(); }
    }
}

public class InterThreadDemo {
    public static void main(String[] args) {
        SharedResource sr = new SharedResource();
        new Producer(sr).start();
        new Consumer(sr).start();
    }
}
</pre>""",
            },
            {
                "num": "6",
                "question": "How to handle multiple catch blocks for a nested try block? Explain with an example.",
                "marks": "5",
                "answer": """In Java, a <b>nested try block</b> is a try block inside another try block. This is useful when different sections of code may throw different exceptions. Each inner or outer try block can have its own set of <b>multiple catch blocks</b> to handle specific exception types. The JVM checks catch blocks from top to bottom and executes the first matching one.

<b>Example — Nested Try with Multiple Catch Blocks:</b>
<pre>
public class NestedTryCatch {
    public static void main(String[] args) {
        try {
            // Outer try block
            int[] arr = {10, 20, 30};
            System.out.println("Outer try begins");

            try {
                // Inner try block
                int result = arr[2] / 0;  // ArithmeticException
                System.out.println(result);
            }
            catch (ArithmeticException e) {
                System.out.println("Inner catch: " + e.getMessage());
            }

            try {
                // Another inner try block
                System.out.println(arr[5]);  // ArrayIndexOutOfBoundsException
            }
            catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Inner catch 2: " + e.getMessage());
            }

            String s = null;
            System.out.println(s.length());  // NullPointerException
        }
        catch (NullPointerException e) {
            System.out.println("Outer catch: " + e.getMessage());
        }
        catch (Exception e) {
            System.out.println("General catch: " + e.getMessage());
        }
        finally {
            System.out.println("Finally block executed");
        }
    }
}
</pre>

<b>Output:</b>
<pre>
Outer try begins
Inner catch: / by zero
Inner catch 2: Index 5 out of bounds for length 3
Outer catch: null
Finally block executed
</pre>

<b>Key Points:</b><br/>
• The inner catch handles exceptions raised in its corresponding inner try.<br/>
• If the inner catch cannot handle the exception, it propagates to the outer catch.<br/>
• Multiple catch blocks should be ordered from most specific to most general.<br/>
• The <code>finally</code> block always executes regardless of exceptions.""",
            },
            {
                "num": "7",
                "question": "What is difference between String and StringBuffer and explain 3 methods of String and StringBuffer class with example.",
                "marks": "2+3",
                "answer": """<b>Difference between String and StringBuffer:</b>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>String</b></td><td><b>StringBuffer</b></td></tr>
<tr><td>Mutability</td><td>Immutable (cannot be changed once created)</td><td>Mutable (can be modified)</td></tr>
<tr><td>Memory</td><td>Creates a new object for every modification</td><td>Modifies the same object, saving memory</td></tr>
<tr><td>Thread Safety</td><td>Thread-safe due to immutability</td><td>Thread-safe (all methods are synchronized)</td></tr>
<tr><td>Performance</td><td>Slower for frequent modifications</td><td>Faster for frequent modifications</td></tr>
<tr><td>Storage</td><td>Stored in String Constant Pool</td><td>Stored in Heap memory</td></tr>
</table>

<b>3 Methods of String Class with Example:</b>
<pre>
String s = "Hello World";

// 1. length() — Returns the number of characters
int len = s.length();  // Output: 11

// 2. substring(int beginIndex, int endIndex) — Extracts a portion
String sub = s.substring(0, 5);  // Output: "Hello"

// 3. equalsIgnoreCase(String another) — Compares ignoring case
boolean result = s.equalsIgnoreCase("hello world");  // Output: true
</pre>

<b>3 Methods of StringBuffer Class with Example:</b>
<pre>
StringBuffer sb = new StringBuffer("Hello");

// 1. append(String str) — Adds text at the end
sb.append(" World");  // sb becomes "Hello World"

// 2. insert(int offset, String str) — Inserts text at specified position
sb.insert(5, ",");  // sb becomes "Hello, World"

// 3. reverse() — Reverses the character sequence
sb.reverse();  // sb becomes "dlroW ,olleH"

System.out.println(sb);
</pre>""",
            },
            {
                "num": "8",
                "question": "Write short notes on: (any two) i. JDBC Driver ii. Access Modifiers iii. JDK, JRE and JVM",
                "marks": "2.5+2.5",
                "answer": """<b>i. JDBC Driver:</b><br/>
JDBC (Java Database Connectivity) Driver is a software component that enables Java applications to interact with databases. It translates Java method calls into database-specific commands.

<b>Types of JDBC Drivers:</b><br/>
1. <b>Type 1 — JDBC-ODBC Bridge:</b> Uses ODBC driver to connect to the database. Platform dependent and slow.<br/>
2. <b>Type 2 — Native-API Driver:</b> Uses database-specific client-side libraries. Faster than Type 1 but requires native code.<br/>
3. <b>Type 3 — Network Protocol Driver:</b> Uses a middleware server to translate JDBC calls into database protocol. Platform independent.<br/>
4. <b>Type 4 — Thin Driver (Pure Java):</b> Directly converts JDBC calls into database protocol. Platform independent and fastest. Most commonly used today.<br/><br/>

<b>ii. Access Modifiers:</b><br/>
Access modifiers in Java control the visibility and accessibility of classes, methods, and variables.

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Modifier</b></td><td><b>Class</b></td><td><b>Package</b></td><td><b>Subclass</b></td><td><b>World</b></td></tr>
<tr><td>public</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr>
<tr><td>protected</td><td>Yes</td><td>Yes</td><td>Yes</td><td>No</td></tr>
<tr><td>default (no modifier)</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td></tr>
<tr><td>private</td><td>Yes</td><td>No</td><td>No</td><td>No</td></tr>
</table>

• <b>public:</b> Accessible everywhere.<br/>
• <b>protected:</b> Accessible within the package and by subclasses.<br/>
• <b>default:</b> Accessible only within the same package.<br/>
• <b>private:</b> Accessible only within the declaring class.<br/><br/>

<b>iii. JDK, JRE and JVM:</b><br/>
<b>JVM (Java Virtual Machine):</b> An abstract machine that provides the runtime environment for Java bytecode. It is platform-dependent and responsible for loading, verifying, and executing bytecode.

<b>JRE (Java Runtime Environment):</b> A software package that provides the libraries, JVM, and other components required to run Java applications. It does not include development tools. End users only need JRE to run Java programs.

<b>JDK (Java Development Kit):</b> A complete software development kit for Java. It includes JRE + development tools such as compiler (javac), debugger (jdb), archiver (jar), and documentation tools (javadoc). Developers need JDK to write and compile Java programs.

<b>Relationship:</b> JDK ⊃ JRE ⊃ JVM""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Define array and multi dimensional array. Write a program to read two m X n matrices, perform multiplication operation and store result in third matrix.",
                "marks": "3+7",
                "answer": """<b>Array:</b> An array is a collection of elements of the same data type stored in contiguous memory locations. It is accessed using an index and provides a way to store multiple values under a single variable name.

<b>Multi-Dimensional Array:</b> A multi-dimensional array is an array of arrays. The most common form is the two-dimensional array, which represents data in rows and columns (like a matrix). In Java, a 2D array is declared as <code>int[][] arr = new int[rows][cols];</code>.

<b>Java Program for Matrix Multiplication:</b>
<pre>
import java.util.Scanner;

public class MatrixMultiplication {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of rows (m): ");
        int m = sc.nextInt();
        System.out.print("Enter number of columns (n): ");
        int n = sc.nextInt();

        int[][] matrix1 = new int[m][n];
        int[][] matrix2 = new int[m][n];
        int[][] result = new int[m][n];

        System.out.println("Enter elements of first matrix:");
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                matrix1[i][j] = sc.nextInt();

        System.out.println("Enter elements of second matrix:");
        for (int i = 0; i < m; i++)
            for (int j = 0; j < n; j++)
                matrix2[i][j] = sc.nextInt();

        // Matrix multiplication
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result[i][j] = 0;
                for (int k = 0; k < n; k++) {
                    result[i][j] += matrix1[i][k] * matrix2[k][j];
                }
            }
        }

        System.out.println("Resultant Matrix:");
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(result[i][j] + "\t");
            }
            System.out.println();
        }
        sc.close();
    }
}
</pre>

<b>Note:</b> For proper matrix multiplication, the number of columns in the first matrix should equal the number of rows in the second matrix. The program above assumes square matrices of size m×n for simplicity. For general multiplication (m×n and n×p), adjust dimensions accordingly.""",
            },
            {
                "num": "10",
                "question": 'Write a program to create the following simple GUI based application. If user press the Submit button, your program should store the information in a file named "exam.txt" only when he accepts the terms and condition otherwise it should display a message "please accept the terms and condition first".',
                "marks": "6+3+1",
                "answer": """<b>Java GUI Program using Swing:</b>
<pre>
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;

public class ExamForm extends JFrame implements ActionListener {
    JTextField nameField, emailField;
    JCheckBox termsCheck;
    JButton submitButton;
    JLabel messageLabel;

    public ExamForm() {
        setTitle("Exam Registration Form");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new GridLayout(6, 2, 10, 10));

        // Name
        add(new JLabel("Name:"));
        nameField = new JTextField();
        add(nameField);

        // Email
        add(new JLabel("Email:"));
        emailField = new JTextField();
        add(emailField);

        // Terms checkbox
        termsCheck = new JCheckBox("I accept the terms and conditions");
        add(termsCheck);
        add(new JLabel(""));

        // Submit button
        submitButton = new JButton("Submit");
        submitButton.addActionListener(this);
        add(submitButton);

        // Message label
        messageLabel = new JLabel("");
        messageLabel.setForeground(Color.RED);
        add(messageLabel);

        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == submitButton) {
            if (!termsCheck.isSelected()) {
                messageLabel.setText("please accept the terms and condition first");
            } else {
                String name = nameField.getText();
                String email = emailField.getText();
                try {
                    FileWriter fw = new FileWriter("exam.txt", true);
                    BufferedWriter bw = new BufferedWriter(fw);
                    bw.write("Name: " + name + ", Email: " + email);
                    bw.newLine();
                    bw.close();
                    messageLabel.setForeground(Color.GREEN);
                    messageLabel.setText("Information saved successfully!");
                } catch (IOException ex) {
                    messageLabel.setText("Error writing to file: " + ex.getMessage());
                }
            }
        }
    }

    public static void main(String[] args) {
        new ExamForm();
    }
}
</pre>

<b>Explanation:</b><br/>
• The form uses <code>JTextField</code> for name and email input.<br/>
• <code>JCheckBox</code> allows the user to accept terms and conditions.<br/>
• When Submit is clicked, <code>actionPerformed()</code> checks if the checkbox is selected.<br/>
• If not selected, it displays "please accept the terms and condition first".<br/>
• If selected, it writes the information to <code>exam.txt</code> using <code>FileWriter</code> and <code>BufferedWriter</code>.<br/>
• The file is opened in append mode (<code>true</code>) so new entries are added without overwriting existing data.""",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet("CACS204", "oop-java", "OOP in Java", 2024, "semester-3", CACS204_2024)
    print("Answer sheet generation complete for CACS204!")
