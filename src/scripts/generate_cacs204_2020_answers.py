#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS204_2020 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "2",
                "question": "Define OOP. Write the characteristics of OOP Language.",
                "marks": "5",
                "answer": """<b>Object-Oriented Programming (OOP):</b><br/>
OOP is a programming paradigm that organizes software design around data (objects) rather than functions and logic. An object is an instance of a class that contains data (attributes) and methods (behaviors).<br/><br/>
<b>Characteristics of OOP Language:</b><br/>
<b>1. Class:</b> A blueprint or template that defines the properties and behaviors of objects.<br/>
<b>2. Object:</b> An instance of a class that encapsulates data and methods.<br/>
<b>3. Encapsulation:</b> Wrapping data and methods together into a single unit (class) and hiding internal details from the outside world.<br/>
<b>4. Inheritance:</b> The mechanism by which one class acquires the properties and methods of another class, promoting code reusability.<br/>
<b>5. Polymorphism:</b> The ability to take multiple forms. It allows methods to perform different operations based on the object that invokes them (method overriding and overloading).<br/>
<b>6. Abstraction:</b> Hiding complex implementation details and showing only essential features to the user."""
            },
            {
                "num": "3",
                "question": "Explain the operators available in Java programming.",
                "marks": "5",
                "answer": """<b>Operators in Java:</b><br/><br/>
<b>1. Arithmetic Operators:</b> + (addition), - (subtraction), * (multiplication), / (division), % (modulus)<br/>
<b>2. Relational Operators:</b> == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to)<br/>
<b>3. Logical Operators:</b> && (logical AND), || (logical OR), ! (logical NOT)<br/>
<b>4. Assignment Operators:</b> = (simple assignment), +=, -=, *=, /=, %= (compound assignment)<br/>
<b>5. Increment/Decrement Operators:</b> ++ (increment by 1), -- (decrement by 1)<br/>
<b>6. Bitwise Operators:</b> & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift), >>> (unsigned right shift)<br/>
<b>7. Conditional (Ternary) Operator:</b> condition ? expression1 : expression2<br/>
<b>8. Instanceof Operator:</b> Checks whether an object is an instance of a particular class."""
            },
            {
                "num": "4",
                "question": "Define loop. Write a java program to print first n prime numbers.",
                "marks": "5",
                "answer": """<b>Loop:</b><br/>
A loop is a control structure that allows a block of code to be executed repeatedly based on a condition. Java provides three types of loops: for, while, and do-while.<br/><br/>
<b>Program to print first n prime numbers:</b><br/>
<pre>import java.util.Scanner;

public class PrimeNumbers {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = sc.nextInt();
        int count = 0;
        int num = 2;
        
        while (count < n) {
            boolean isPrime = true;
            for (int i = 2; i <= num / 2; i++) {
                if (num % i == 0) {
                    isPrime = false;
                    break;
                }
            }
            if (isPrime) {
                System.out.print(num + " ");
                count++;
            }
            num++;
        }
    }
}</pre>"""
            },
            {
                "num": "5",
                "question": "Differentiate between abstract class and interface with suitable example.",
                "marks": "5",
                "answer": """<b>Abstract Class vs Interface:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Abstract Class</b></td><td><b>Interface</b></td></tr>
<tr><td>Declared with abstract keyword</td><td>Declared with interface keyword</td></tr>
<tr><td>Can have both abstract and concrete methods</td><td>Can only have abstract methods (before Java 8); default/static methods allowed since Java 8</td></tr>
<tr><td>Can have instance variables</td><td>Variables are public, static, and final by default</td></tr>
<tr><td>Supports constructors</td><td>No constructors</td></tr>
<tr><td>A class can extend only one abstract class</td><td>A class can implement multiple interfaces</td></tr>
<tr><td>Used when classes share common code</td><td>Used to define a contract for classes</td></tr>
</table><br/>
<b>Example:</b><br/>
<pre>abstract class Animal {
    abstract void sound();
    void sleep() { System.out.println("Sleeping"); }
}

interface Drawable {
    void draw();
}</pre>"""
            },
            {
                "num": "6",
                "question": "Define access modifier. Explain access modifiers in java with example.",
                "marks": "5",
                "answer": """<b>Access Modifier:</b><br/>
Access modifiers in Java define the visibility or accessibility of classes, methods, and variables. They control which parts of the program can access a particular member.<br/><br/>
<b>Types of Access Modifiers in Java:</b><br/>
<b>1. private:</b> Accessible only within the same class. Most restrictive.<br/>
<b>2. default (no modifier):</b> Accessible within the same package.<br/>
<b>3. protected:</b> Accessible within the same package and by subclasses in other packages.<br/>
<b>4. public:</b> Accessible from anywhere. Least restrictive.<br/><br/>
<b>Example:</b><br/>
<pre>public class Demo {
    public int a = 10;       // accessible everywhere
    private int b = 20;      // accessible only in Demo
    protected int c = 30;    // accessible in package + subclasses
    int d = 40;              // default - accessible in package only
}</pre>"""
            },
            {
                "num": "7",
                "question": "Define exception. Explain exception handling mechanism in java with example.",
                "marks": "6",
                "answer": """<b>Exception:</b><br/>
An exception is an event that disrupts the normal flow of program execution. It is an object that is thrown at runtime when an error occurs.<br/><br/>
<b>Exception Handling Mechanism in Java:</b><br/>
Java uses the following keywords for exception handling:<br/>
<b>1. try:</b> Block of code that might throw an exception.<br/>
<b>2. catch:</b> Block that handles the exception thrown in the try block.<br/>
<b>3. finally:</b> Block that always executes, regardless of whether an exception occurred.<br/>
<b>4. throw:</b> Used to explicitly throw an exception.<br/>
<b>5. throws:</b> Declares exceptions that a method might throw.<br/><br/>
<b>Example:</b><br/>
<pre>public class ExceptionDemo {
    public static void main(String[] args) {
        try {
            int a = 10, b = 0;
            int result = a / b;
        } catch (ArithmeticException e) {
            System.out.println("Cannot divide by zero: " + e.getMessage());
        } finally {
            System.out.println("Finally block executed");
        }
    }
}</pre>"""
            },
            {
                "num": "8",
                "question": "Write short note on (Any Two):<br/>a) final keyword<br/>b) Collection class<br/>c) JDBC",
                "marks": "5",
                "answer": """<b>a) final keyword:</b><br/>
The final keyword in Java is used to restrict modification:<br/>
• <b>final variable:</b> Cannot be changed once initialized (constant).<br/>
• <b>final method:</b> Cannot be overridden by subclasses.<br/>
• <b>final class:</b> Cannot be extended (inherited).<br/><br/>
<b>b) Collection class:</b><br/>
The Collection framework in Java provides a set of interfaces and classes to store and manipulate groups of objects:<br/>
• <b>List:</b> Ordered, allows duplicates (ArrayList, LinkedList)<br/>
• <b>Set:</b> Unordered, no duplicates (HashSet, TreeSet)<br/>
• <b>Map:</b> Key-value pairs (HashMap, TreeMap)<br/>
• <b>Queue:</b> FIFO structure (PriorityQueue, LinkedList)<br/><br/>
<b>c) JDBC (Java Database Connectivity):</b><br/>
JDBC is a Java API that enables Java programs to interact with databases:<br/>
• <b>DriverManager:</b> Manages database drivers<br/>
• <b>Connection:</b> Establishes connection to database<br/>
• <b>Statement:</b> Executes SQL queries<br/>
• <b>ResultSet:</b> Stores query results<br/>
<b>Steps:</b> Load driver → Create connection → Create statement → Execute query → Process results → Close connection"""
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "9",
                "question": "a) Write a program to create and use java package.<br/>b) Define thread. Explain the life cycle of thread.",
                "marks": "10",
                "answer": """<b>a) Program to create and use Java package:</b><br/>
<pre>// File: MyPackage.java
package mypack;

public class MyPackage {
    public void display() {
        System.out.println("Hello from mypack!");
    }
}

// File: TestPackage.java
import mypack.MyPackage;

public class TestPackage {
    public static void main(String[] args) {
        MyPackage obj = new MyPackage();
        obj.display();
    }
}</pre><br/>
<b>b) Thread:</b><br/>
A thread is the smallest unit of execution within a process. Java supports multithreading, allowing multiple threads to run concurrently.<br/><br/>
<b>Life Cycle of a Thread:</b><br/>
<b>1. New:</b> Thread is created but not started.<br/>
<b>2. Runnable:</b> Thread is ready to run, waiting for CPU time.<br/>
<b>3. Running:</b> Thread is currently executing.<br/>
<b>4. Blocked/Waiting:</b> Thread is temporarily inactive (waiting for a resource or another thread).<br/>
<b>5. Terminated:</b> Thread has completed execution or been stopped."""
            },
            {
                "num": "10",
                "question": "a) Write a program to sort name of any five cities in ascending order.<br/>b) Define polymorphism. How do we achieve polymorphism in java explain with example?",
                "marks": "10",
                "answer": """<b>a) Program to sort names of five cities:</b><br/>
<pre>import java.util.Arrays;
import java.util.Scanner;

public class SortCities {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String[] cities = new String[5];
        
        System.out.println("Enter 5 city names:");
        for (int i = 0; i < 5; i++) {
            cities[i] = sc.nextLine();
        }
        
        Arrays.sort(cities);
        
        System.out.println("Cities in ascending order:");
        for (String city : cities) {
            System.out.println(city);
        }
    }
}</pre><br/>
<b>b) Polymorphism:</b><br/>
Polymorphism means "many forms." It allows objects of different classes to be treated as objects of a common superclass, and a single method can behave differently based on the object that calls it.<br/><br/>
<b>Types of Polymorphism in Java:</b><br/>
<b>1. Compile-time (Method Overloading):</b> Same method name with different parameters.<br/>
<pre>class MathOp {
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
}</pre><br/>
<b>2. Runtime (Method Overriding):</b> Subclass provides a specific implementation of a method declared in the parent class.<br/>
<pre>class Animal { void sound() { System.out.println("Animal sound"); } }
class Dog extends Animal { void sound() { System.out.println("Bark"); } }</pre>"""
            },
            {
                "num": "11",
                "question": "a) Differentiate between java AWT and java Swing. Explain the different types layout managers in java GUI programming.<br/>b) Write a java GUI program to calculate square of entered number.",
                "marks": "10",
                "answer": """<b>a) AWT vs Swing:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>AWT</b></td><td><b>Swing</b></td></tr>
<tr><td>Platform-dependent (heavyweight)</td><td>Platform-independent (lightweight)</td></tr>
<tr><td>Uses native OS components</td><td>Uses pure Java components</td></tr>
<tr><td>Package: java.awt</td><td>Package: javax.swing</td></tr>
<tr><td>Less components and features</td><td>More components and richer features</td></tr>
<tr><td>Not customizable</td><td>Highly customizable (look and feel)</td></tr>
</table><br/>
<b>Layout Managers in Java GUI:</b><br/>
<b>1. FlowLayout:</b> Components arranged left-to-right, top-to-bottom.<br/>
<b>2. BorderLayout:</b> Components placed in NORTH, SOUTH, EAST, WEST, CENTER.<br/>
<b>3. GridLayout:</b> Components arranged in a grid of rows and columns.<br/>
<b>4. GridBagLayout:</b> Flexible grid layout with varying component sizes.<br/>
<b>5. CardLayout:</b> Multiple panels stacked like a deck of cards.<br/>
<b>6. BoxLayout:</b> Components arranged vertically or horizontally in a box.<br/><br/>
<b>b) Java GUI program to calculate square:</b><br/>
<pre>import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SquareCalculator extends JFrame {
    JTextField numField, resultField;
    JButton calcBtn;
    
    public SquareCalculator() {
        setTitle("Square Calculator");
        setSize(300, 150);
        setLayout(new GridLayout(3, 2));
        
        add(new JLabel("Enter any number:"));
        numField = new JTextField();
        add(numField);
        
        calcBtn = new JButton("Calculate");
        add(calcBtn);
        
        add(new JLabel("Square of entered number:"));
        resultField = new JTextField();
        resultField.setEditable(false);
        add(resultField);
        
        calcBtn.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                double num = Double.parseDouble(numField.getText());
                resultField.setText(String.valueOf(num * num));
            }
        });
        
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
    
    public static void main(String[] args) {
        new SquareCalculator();
    }
}</pre>"""
            },
        ]
    }
]

print("Generating CACS204 2020 answer sheet...")
generate_answer_sheet("CACS204", "oop-java", "OOP in Java", 2020, "semester-3", CACS204_2020)
print("✅ CACS204 2020 done!")
