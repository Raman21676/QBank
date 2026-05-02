#!/usr/bin/env python3
"""Generate answer sheets for 2nd semester 2018 core subjects."""

import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

# ========== CACS151: C Programming 2018 ==========
CACS151_2018 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "1. Which of the following doesn't require an & for the input in scanf()?<br/>a) char name[10] &nbsp;&nbsp; b) int name[10] &nbsp;&nbsp; c) float name[10] &nbsp;&nbsp; d) double name[10]<br/><br/>2. What is the memory size of float data type in C?<br/>a) 4 Bytes &nbsp;&nbsp; b) 8 Bytes &nbsp;&nbsp; c) Depends on system/compiler &nbsp;&nbsp; d) Cannot be determined<br/><br/>3. What will be the output of the following C code?<br/><pre>int x=3,y;\ny=(++x)+(x++);\nprintf(\"%d\",y);</pre><br/>a) 6 &nbsp;&nbsp; b) 8 &nbsp;&nbsp; c) 7 &nbsp;&nbsp; d) 9<br/><br/>4. Which keyword is used to come out of a loop only for that iteration?<br/>a) break &nbsp;&nbsp; b) continue &nbsp;&nbsp; c) return &nbsp;&nbsp; d) void<br/><br/>5. Bitwise operators can operate upon?<br/>a) Double and chars &nbsp;&nbsp; b) floats and doubles &nbsp;&nbsp; c) int and floats &nbsp;&nbsp; d) int and chars<br/><br/>6. In C, if you pass an array as an argument to a function, what actually gets passed?<br/>a) Value of elements &nbsp;&nbsp; b) First element &nbsp;&nbsp; c) Address of first element &nbsp;&nbsp; d) Address of last element<br/><br/>7. Which operator is used to access members of structure using structure variable?<br/>a) Address operator (&) &nbsp;&nbsp; b) Dot operator (.) &nbsp;&nbsp; c) Pointer operator (*) &nbsp;&nbsp; d) Arrow operator (->)<br/><br/>8. Which function is used to record input from file?<br/>a) ftell() &nbsp;&nbsp; b) fwrite() &nbsp;&nbsp; c) fprintf() &nbsp;&nbsp; d) fread()<br/><br/>9. Which of the following is a keyword used for a storage class?<br/>a) printf &nbsp;&nbsp; b) goto &nbsp;&nbsp; c) external &nbsp;&nbsp; d) break<br/><br/>10. What will be the size of following union declaration?<br/><pre>union test { int x; char y; float z; }</pre><br/>a) 8 bytes &nbsp;&nbsp; b) 13 bytes &nbsp;&nbsp; c) 1 byte &nbsp;&nbsp; d) 4 bytes",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>1) a) char name[10]</b> — Array names are pointers to the first element, so they don't need &. For int/float/double arrays, each element needs & when reading individual elements.<br/><br/>
<b>2) a) 4 Bytes</b> — In standard C, float typically occupies 4 bytes (32 bits) with precision of about 6-7 decimal digits.<br/><br/>
<b>3) b) 8</b> — ++x (pre-increment) makes x=4, then x++ (post-increment) uses x=4 and makes x=5. So y = 4 + 4 = 8.<br/><br/>
<b>4) b) continue</b> — continue skips the current iteration and moves to the next iteration. break exits the loop entirely.<br/><br/>
<b>5) d) int and chars</b> — Bitwise operators (&, |, ^, ~, &lt;&lt;, &gt;&gt;) work on integer types (int, char, short, long). They cannot operate on float or double.<br/><br/>
<b>6) c) The address of first element in an array</b> — Arrays decay to pointers when passed to functions. The function receives the base address, not the values.<br/><br/>
<b>7) b) Dot operator (.)</b> — The dot operator accesses structure members through a structure variable. Arrow operator (->) is used with structure pointers.<br/><br/>
<b>8) d) fread()</b> — fread() reads binary data from a file. fwrite() writes binary data. fprintf() writes formatted text. ftell() returns file position.<br/><br/>
<b>9) c) external</b> — extern is a storage class keyword (though misspelled as \"external\" in options). auto, static, register, and extern are C storage classes.<br/><br/>
<b>10) d) 4 bytes</b> — Union size equals the size of its largest member. Here float z = 4 bytes (assuming 32-bit system), so union size = 4 bytes.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "11",
                "question": "What is software process model? Differentiate between cohesion and coupling in programming. [1+4]",
                "marks": "5",
                "answer": """<b>Software Process Model:</b><br/>
A software process model is a structured set of activities required to develop a software system. It defines the order of activities, their inputs/outputs, and the workflow. Common models include Waterfall, Agile, Spiral, and V-Model.<br/><br/>
<b>Cohesion vs Coupling:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Cohesion</b></td><td><b>Coupling</b></td></tr>
<tr><td>Measures how closely related elements within a module are</td><td>Measures the degree of interdependence between modules</td></tr>
<tr><td>Higher cohesion is better</td><td>Lower coupling is better</td></tr>
<tr><td>Types: Functional, Sequential, Communicational, Procedural, Temporal, Logical, Coincidental</td><td>Types: Content, Common, External, Control, Stamp, Data</td></tr>
<tr><td>Goal: Each module should do one thing well</td><td>Goal: Modules should be as independent as possible</td></tr>
</table><br/>
<b>Example:</b> A module that calculates salary (functional cohesion) is better than one that does unrelated tasks (coincidental cohesion). Two modules sharing only necessary data (data coupling) is better than one module controlling another's logic (control coupling).""",
            },
            {
                "num": "12",
                "question": "Define keyword and identifiers. Explain rules for defining valid identifiers. [2+3]",
                "marks": "5",
                "answer": """<b>Keywords:</b><br/>
Keywords are reserved words in C that have predefined meanings and cannot be used as identifiers. They are the building blocks of C syntax. Examples: int, float, if, else, for, while, return, struct, void, static.<br/><br/>
<b>Identifiers:</b><br/>
Identifiers are names given to variables, functions, arrays, structures, and other user-defined elements. They allow programmers to reference data and operations symbolically.<br/><br/>
<b>Rules for Valid Identifiers:</b><br/>
<b>1.</b> Must begin with a letter (a-z, A-Z) or underscore (_).<br/>
<b>2.</b> Can contain letters, digits (0-9), and underscores.<br/>
<b>3.</b> Cannot contain special characters (@, #, $, %, space, etc.).<br/>
<b>4.</b> Cannot be a C keyword (if, int, for, etc.).<br/>
<b>5.</b> C is case-sensitive: \"name\" and \"Name\" are different identifiers.<br/>
<b>6.</b> Maximum length depends on compiler, but first 31 characters are significant in standard C.<br/><br/>
<b>Valid:</b> _count, totalSum, student_name, value2<br/>
<b>Invalid:</b> 2value (starts with digit), student name (contains space), int (keyword), total$sum (special char)""",
            },
            {
                "num": "13",
                "question": "List the operators used in C on the basis of utility. Explain the concept of bitwise operator. [2+3]",
                "marks": "5",
                "answer": """<b>Operators in C by Utility:</b><br/>
<table border='1' cellpadding='3'>
<tr><td><b>Category</b></td><td><b>Operators</b></td></tr>
<tr><td>Arithmetic</td><td>+, -, *, /, %</td></tr>
<tr><td>Relational</td><td>&lt;, &gt;, &lt;=, &gt;=, ==, !=</td></tr>
<tr><td>Logical</td><td>&amp;&amp;, ||, !</td></tr>
<tr><td>Bitwise</td><td>&amp;, |, ^, ~, &lt;&lt;, &gt;&gt;</td></tr>
<tr><td>Assignment</td><td>=, +=, -=, *=, /=, %=</td></tr>
<tr><td>Increment/Decrement</td><td>++, --</td></tr>
<tr><td>Conditional</td><td>?:</td></tr>
<tr><td>Special</td><td>sizeof, &amp;, *, , (comma)</td></tr>
</table><br/>
<b>Bitwise Operators:</b><br/>
Bitwise operators perform operations on individual bits of integer operands.<br/><br/>
<b>& (AND):</b> Sets bit to 1 if both bits are 1.<br/>
<pre>5 & 3 = 101 & 011 = 001 = 1</pre><br/>
<b>| (OR):</b> Sets bit to 1 if at least one bit is 1.<br/>
<pre>5 | 3 = 101 | 011 = 111 = 7</pre><br/>
<b>^ (XOR):</b> Sets bit to 1 if bits are different.<br/>
<pre>5 ^ 3 = 101 ^ 011 = 110 = 6</pre><br/>
<b>~ (NOT):</b> Inverts all bits (one's complement).<br/>
<pre>~5 = ~00000101 = 11111010 = -6 (in 2's complement)</pre><br/>
<b>&lt;&lt; (Left Shift):</b> Shifts bits left, filling with 0.<br/>
<pre>5 &lt;&lt; 1 = 1010 = 10 (equivalent to ×2)</pre><br/>
<b>&gt;&gt; (Right Shift):</b> Shifts bits right.<br/>
<pre>5 &gt;&gt; 1 = 0010 = 2 (equivalent to ÷2)</pre>""",
            },
            {
                "num": "14",
                "question": "Differentiate between while loop and do while loop. Write a C program to find input number is prime or composite. [2+3]",
                "marks": "5",
                "answer": """<b>Difference between while and do-while:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>while loop</b></td><td><b>do-while loop</b></td></tr>
<tr><td>Condition checked before entering loop</td><td>Condition checked after executing loop body</td></tr>
<tr><td>May not execute at all (0 iterations)</td><td>Executes at least once (minimum 1 iteration)</td></tr>
<tr><td>Syntax: while(condition) { }</td><td>Syntax: do { } while(condition);</td></tr>
<tr><td>Entry-controlled loop</td><td>Exit-controlled loop</td></tr>
</table><br/>
<b>C Program to check Prime or Composite:</b><br/>
<pre>#include&lt;stdio.h&gt;

int main() {
    int n, i, flag = 0;
    printf("Enter a number: ");
    scanf("%d", &amp;n);
    
    if(n &lt;= 1) {
        printf("%d is neither prime nor composite\\n", n);
    } else {
        for(i = 2; i &lt;= n/2; i++) {
            if(n % i == 0) {
                flag = 1;
                break;
            }
        }
        if(flag == 0)
            printf("%d is a prime number\\n", n);
        else
            printf("%d is a composite number\\n", n);
    }
    return 0;
}</pre><br/>
<b>Explanation:</b> The program checks divisibility from 2 to n/2. If any divisor is found, the number is composite. Otherwise, it's prime. Numbers ≤ 1 are neither prime nor composite.""",
            },
            {
                "num": "15",
                "question": "What is DMA? Write a program to find the largest and smallest number in a list of N numbers using DMA. [1+4]",
                "marks": "5",
                "answer": """<b>DMA (Dynamic Memory Allocation):</b><br/>
DMA is the process of allocating memory during program execution (runtime) rather than at compile time. It allows programs to request memory as needed and release it when no longer required. C provides functions malloc(), calloc(), realloc(), and free() for DMA, declared in &lt;stdlib.h&gt;.<br/><br/>
<b>Program using DMA to find largest and smallest:</b><br/>
<pre>#include&lt;stdio.h&gt;
#include&lt;stdlib.h&gt;

int main() {
    int n, i, *arr, largest, smallest;
    
    printf("Enter number of elements: ");
    scanf("%d", &amp;n);
    
    // Dynamic memory allocation
    arr = (int*)malloc(n * sizeof(int));
    
    if(arr == NULL) {
        printf("Memory allocation failed!\\n");
        return 1;
    }
    
    printf("Enter %d numbers:\\n", n);
    for(i = 0; i &lt; n; i++) {
        scanf("%d", &amp;arr[i]);
    }
    
    largest = smallest = arr[0];
    for(i = 1; i &lt; n; i++) {
        if(arr[i] &gt; largest)
            largest = arr[i];
        if(arr[i] &lt; smallest)
            smallest = arr[i];
    }
    
    printf("Largest = %d\\n", largest);
    printf("Smallest = %d\\n", smallest);
    
    free(arr); // Deallocate memory
    return 0;
}</pre><br/>
<b>Explanation:</b> malloc() allocates memory for n integers at runtime. The user can enter any number of elements. After processing, free() releases the memory to prevent memory leaks.""",
            },
            {
                "num": "16",
                "question": "What is difference between binary file and text file? Write a C program to write some text \"Welcome to BCA program\" in a file test.txt. [2+3]",
                "marks": "5",
                "answer": """<b>Text File vs Binary File:</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Text File</b></td><td><b>Binary File</b></td></tr>
<tr><td>Stores data as ASCII characters</td><td>Stores data in binary format (0s and 1s)</td></tr>
<tr><td>Human-readable</td><td>Not human-readable</td></tr>
<tr><td>Uses functions: fprintf(), fscanf(), fgets(), fputs()</td><td>Uses functions: fwrite(), fread()</td></tr>
<tr><td>Newline character converted to system-specific format</td><td>No translation, data stored as-is</td></tr>
<tr><td>Slower for numerical data</td><td>Faster and more compact for numerical data</td></tr>
<tr><td>Example: .txt, .csv, .html</td><td>Example: .exe, .bin, .dat, .jpg</td></tr>
</table><br/>
<b>C Program to write text to file:</b><br/>
<pre>#include&lt;stdio.h&gt;

int main() {
    FILE *fp;
    
    fp = fopen("test.txt", "w");
    if(fp == NULL) {
        printf("Error opening file!\\n");
        return 1;
    }
    
    fprintf(fp, "Welcome to BCA program");
    
    fclose(fp);
    printf("Text written successfully!\\n");
    
    return 0;
}</pre><br/>
<b>Explanation:</b> fopen() opens test.txt in write mode (\"w\"). fprintf() writes the string to the file. fclose() closes the file, flushing the buffer to disk. If the file doesn't exist, it's created; if it exists, its contents are overwritten.""",
            },
            {
                "num": "17",
                "question": "Explain any four graphics functions in C. Write a program to draw two concentric circles with center (50, 50) and radii 75 and 125. [2+3]",
                "marks": "5",
                "answer": """<b>Graphics Functions in C (using graphics.h):</b><br/><br/>
<b>1. initgraph():</b> Initializes the graphics system.<br/>
<pre>initgraph(&amp;gd, &amp;gm, "");</pre><br/>
<b>2. setcolor():</b> Sets the current drawing color.<br/>
<pre>setcolor(RED);</pre><br/>
<b>3. circle():</b> Draws a circle with given center and radius.<br/>
<pre>circle(x, y, radius);</pre><br/>
<b>4. line():</b> Draws a line between two points.<br/>
<pre>line(x1, y1, x2, y2);</pre><br/>
Other functions: rectangle(), bar(), putpixel(), outtextxy(), closegraph()<br/><br/>
<b>Program to draw concentric circles:</b><br/>
<pre>#include&lt;graphics.h&gt;
#include&lt;conio.h&gt;

int main() {
    int gd = DETECT, gm;
    
    initgraph(&amp;gd, &amp;gm, "");
    
    // Draw first circle with radius 75
    setcolor(RED);
    circle(50, 50, 75);
    
    // Draw second circle with radius 125
    setcolor(BLUE);
    circle(50, 50, 125);
    
    getch();
    closegraph();
    
    return 0;
}</pre><br/>
<b>Explanation:</b> Both circles share the same center (50, 50) but have different radii (75 and 125), creating concentric circles. The graphics system must be initialized with initgraph() and closed with closegraph(). getch() waits for a key press before closing.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "18",
                "question": "What is one dimensional array? How it is initialized? Write a C program to find the sum of two matrix of order m×n. [1+1+8]",
                "marks": "10",
                "answer": """<b>One Dimensional Array:</b><br/>
A one-dimensional array is a linear collection of elements of the same data type stored in contiguous memory locations. It is accessed using a single index. Declaration: <b>type arrayName[size];</b><br/><br/>
<b>Initialization:</b><br/>
<pre>int arr[5] = {10, 20, 30, 40, 50};
int arr[] = {10, 20, 30}; // Size determined automatically
int arr[5] = {10, 20}; // Remaining elements set to 0</pre><br/>
<b>Program for Matrix Addition:</b><br/>
<pre>#include&lt;stdio.h&gt;

int main() {
    int a[10][10], b[10][10], sum[10][10];
    int m, n, i, j;
    
    printf("Enter rows and columns: ");
    scanf("%d%d", &amp;m, &amp;n);
    
    printf("Enter elements of first matrix:\\n");
    for(i = 0; i &lt; m; i++)
        for(j = 0; j &lt; n; j++)
            scanf("%d", &amp;a[i][j]);
    
    printf("Enter elements of second matrix:\\n");
    for(i = 0; i &lt; m; i++)
        for(j = 0; j &lt; n; j++)
            scanf("%d", &amp;b[i][j]);
    
    // Matrix addition
    for(i = 0; i &lt; m; i++)
        for(j = 0; j &lt; n; j++)
            sum[i][j] = a[i][j] + b[i][j];
    
    printf("Sum of matrices:\\n");
    for(i = 0; i &lt; m; i++) {
        for(j = 0; j &lt; n; j++)
            printf("%d ", sum[i][j]);
        printf("\\n");
    }
    
    return 0;
}</pre><br/>
<b>Explanation:</b> Two matrices are read element by element. Corresponding elements are added and stored in the sum matrix. The result is displayed in matrix format.""",
            },
            {
                "num": "19",
                "question": "Define structure and union? Write a C program using structure that reads the records of 35 students with members roll, name, address and marks and display the record of students who have obtained greater than 250 marks. [2+8]",
                "marks": "10",
                "answer": """<b>Structure:</b><br/>
A structure is a user-defined data type that groups variables of different data types under a single name. Each variable in a structure is called a member. Structures are declared using the <b>struct</b> keyword. The total memory allocated is the sum of all members' sizes.<br/><br/>
<b>Union:</b><br/>
A union is similar to a structure but all members share the same memory location. Only one member can hold a value at a time. The size of a union equals the size of its largest member. Unions are declared using the <b>union</b> keyword.<br/><br/>
<b>Difference:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Structure</td><td>Union</td></tr>
<tr><td>All members have separate memory</td><td>All members share same memory</td></tr>
<tr><td>Size = sum of all members</td><td>Size = size of largest member</td></tr>
<tr><td>All members can hold values simultaneously</td><td>Only one member active at a time</td></tr>
</table><br/>
<b>Program using Structure:</b><br/>
<pre>#include&lt;stdio.h&gt;
#include&lt;string.h&gt;

struct Student {
    int roll;
    char name[50];
    char address[100];
    int marks;
};

int main() {
    struct Student s[35];
    int i, count = 0;
    
    printf("Enter records of 35 students:\\n");
    for(i = 0; i &lt; 35; i++) {
        printf("\\nStudent %d:\\n", i+1);
        printf("Roll: ");
        scanf("%d", &amp;s[i].roll);
        printf("Name: ");
        scanf(" %[^\\n]", s[i].name);
        printf("Address: ");
        scanf(" %[^\\n]", s[i].address);
        printf("Marks: ");
        scanf("%d", &amp;s[i].marks);
    }
    
    printf("\\nStudents with marks &gt; 250:\\n");
    for(i = 0; i &lt; 35; i++) {
        if(s[i].marks &gt; 250) {
            printf("Roll: %d, Name: %s, Address: %s, Marks: %d\\n",
                   s[i].roll, s[i].name, s[i].address, s[i].marks);
            count++;
        }
    }
    
    if(count == 0)
        printf("No student scored more than 250 marks.\\n");
    
    return 0;
}</pre><br/>
<b>Explanation:</b> A structure Student is defined with four members. An array of 35 structures stores student records. The program iterates through all records and displays only those with marks greater than 250.""",
            },
            {
                "num": "20",
                "question": "What is function? List its advantages. Explain the concept of function call by value and function call by reference with example. [1+2+7]",
                "marks": "10",
                "answer": """<b>Function:</b><br/>
A function is a self-contained block of code that performs a specific task. It is defined once and can be called multiple times from different parts of a program. Functions help in modular programming, code reuse, and easier debugging.<br/><br/>
<b>Advantages of Functions:</b><br/>
<b>1. Modularity:</b> Breaks complex problems into smaller, manageable modules.<br/>
<b>2. Code Reusability:</b> Write once, use multiple times.<br/>
<b>3. Easier Debugging:</b> Errors can be isolated to specific functions.<br/>
<b>4. Reduced Code Size:</b> Avoids repetition of code.<br/>
<b>5. Team Collaboration:</b> Different programmers can work on different functions.<br/><br/>
<b>Call by Value:</b><br/>
A copy of the actual argument is passed to the function. Changes made to parameters inside the function do not affect the original variables.<br/><br/>
<b>Call by Reference:</b><br/>
The address (memory location) of the actual argument is passed. Changes made to parameters inside the function directly affect the original variables.<br/><br/>
<b>Example:</b><br/>
<pre>#include&lt;stdio.h&gt;

// Call by value
void swapByValue(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
    printf("Inside swapByValue: a=%d, b=%d\\n", a, b);
}

// Call by reference
void swapByReference(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
    printf("Inside swapByReference: a=%d, b=%d\\n", *a, *b);
}

int main() {
    int x = 10, y = 20;
    
    printf("Original: x=%d, y=%d\\n", x, y);
    
    swapByValue(x, y);
    printf("After call by value: x=%d, y=%d\\n", x, y);
    // x and y remain unchanged
    
    swapByReference(&amp;x, &amp;y);
    printf("After call by reference: x=%d, y=%d\\n", x, y);
    // x and y are swapped
    
    return 0;
}</pre><br/>
<b>Output:</b><br/>
Original: x=10, y=20<br/>
Inside swapByValue: a=20, b=10<br/>
After call by value: x=10, y=20<br/>
Inside swapByReference: a=20, b=10<br/>
After call by reference: x=20, y=10<br/><br/>
<b>Conclusion:</b> Call by value is safer (original data protected) but cannot modify caller's variables. Call by reference is more efficient for large data and allows modification of original variables.""",
            },
        ]
    }
]

print("Generating CACS151 answer sheet...")
generate_answer_sheet("CACS151", "c-programming", "C Programming", 2018, "semester-2", CACS151_2018)
print("✅ CACS151 2018 done!")

# ========== CACS155: Microprocessor & Computer Architecture 2018 ==========
CACS155_2018 = [
    {
        "title": "Group A",
        "instruction": "Attempt ALL the questions. [10 × 1 = 10]",
        "questions": [
            {
                "num": "1",
                "question": "1. How many number of pins are there in 8085 Microprocessor?<br/>a) 16 &nbsp;&nbsp; b) 20 &nbsp;&nbsp; c) 32 &nbsp;&nbsp; d) 40<br/><br/>2. Which one of the following interrupt has the highest priority?<br/>a) RST7.5 &nbsp;&nbsp; b) TRAP &nbsp;&nbsp; c) RST6.5 &nbsp;&nbsp; d) RST5.5<br/><br/>3. How many bytes make a word of 32 bits?<br/>a) One Byte &nbsp;&nbsp; b) Two Bytes &nbsp;&nbsp; c) Three Bytes &nbsp;&nbsp; d) Four Bytes<br/><br/>4. Which one of the following flag has set or reset value on the basis of even or odd number of 1's in result?<br/>a) Zero &nbsp;&nbsp; b) Carry &nbsp;&nbsp; c) Parity &nbsp;&nbsp; d) Sign<br/><br/>5. What is the size of MOV B, A instruction in 8085 Microprocessor?<br/>a) One Word &nbsp;&nbsp; b) Two Word &nbsp;&nbsp; c) Three Word &nbsp;&nbsp; d) Four Word<br/><br/>6. Which one of the following bit(s) specify the direct or indirect address?<br/>a) Address bits &nbsp;&nbsp; b) Opcode Bits &nbsp;&nbsp; c) Mode Bit &nbsp;&nbsp; d) Control Word<br/><br/>7. Which one of the following term is correct for the process of transformation of the instruction code bits to an address in control memory where the routine is located?<br/>a) Mapping &nbsp;&nbsp; b) Pipelining &nbsp;&nbsp; c) Sequencing &nbsp;&nbsp; d) Acknowledging<br/><br/>8. Which one of the following is not a logical and bit manipulation operation?<br/>a) Enable Interrupt &nbsp;&nbsp; b) Increment &nbsp;&nbsp; c) Clear Carry &nbsp;&nbsp; d) Clear<br/><br/>9. Which one of the following is not the pipelining hazard?<br/>a) Data dependency &nbsp;&nbsp; b) Resource conflict &nbsp;&nbsp; c) Branch conflict &nbsp;&nbsp; d) Interrupt Hazard<br/><br/>10. Which one of the following organization of parallel processing is only a theoretical interest since no practical system has been constructed?<br/>a) SISD &nbsp;&nbsp; b) SIMD &nbsp;&nbsp; c) MISD &nbsp;&nbsp; d) MIMD",
                "marks": "10 × 1 = 10",
                "answer": """<b>Answers:</b><br/>
<b>1) d) 40</b> — Intel 8085 is an 8-bit microprocessor with a 40-pin DIP (Dual Inline Package) configuration.<br/><br/>
<b>2) b) TRAP</b> — TRAP is a non-maskable interrupt with the highest priority in 8085. It cannot be disabled and is used for critical conditions like power failure.<br/><br/>
<b>3) d) Four Bytes</b> — 1 byte = 8 bits. Therefore, 32 bits = 32/8 = 4 bytes.<br/><br/>
<b>4) c) Parity</b> — The Parity flag is set if the result has an even number of 1s (even parity), and reset if odd number of 1s (odd parity).<br/><br/>
<b>5) a) One Word</b> — MOV B, A is a 1-byte instruction that copies the contents of accumulator to register B.<br/><br/>
<b>6) c) Mode Bit</b> — The mode bit specifies whether addressing is direct or indirect in microprogrammed control units.<br/><br/>
<b>7) a) Mapping</b> — Mapping is the process that transforms instruction code bits into an address in control memory where the corresponding microprogram routine is stored.<br/><br/>
<b>8) a) Enable Interrupt</b> — EI (Enable Interrupt) is a program control instruction, not a logical or bit manipulation operation. Logical operations include AND, OR, XOR, NOT, etc.<br/><br/>
<b>9) d) Interrupt Hazard</b> — The three main pipeline hazards are: data hazards (data dependency), structural hazards (resource conflict), and control hazards (branch conflict). Interrupt hazard is not a standard pipeline hazard category.<br/><br/>
<b>10) c) MISD</b> — MISD (Multiple Instruction, Single Data) is a theoretical parallel processing architecture where multiple instructions operate on the same data stream simultaneously. No practical MISD system has been constructed.""",
            }
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6 × 5 = 30]",
        "questions": [
            {
                "num": "11",
                "question": "Explain the Bus organization of 8085 Microprocessor.",
                "marks": "5",
                "answer": """<b>Bus Organization of 8085 Microprocessor:</b><br/><br/>
The 8085 microprocessor uses three types of buses to communicate with memory and I/O devices:<br/><br/>
<b>1. Address Bus (16-bit):</b><br/>
• Unidirectional bus (CPU to memory/I/O)<br/>
• A₁₅-A₈ (high-order) and AD₇-AD₀ (low-order, multiplexed)<br/>
• Can address 2¹⁶ = 65,536 (64KB) memory locations<br/>
• Used to specify the source or destination of data<br/><br/>
<b>2. Data Bus (8-bit):</b><br/>
• Bidirectional bus<br/>
• AD₇-AD₀ lines are multiplexed (shared with address bus low byte)<br/>
• ALE (Address Latch Enable) signal demultiplexes them<br/>
• Transfers 8 bits of data at a time between CPU and memory/I/O<br/><br/>
<b>3. Control Bus:</b><br/>
• Carries control and status signals<br/>
• <b>Control Signals:</b> RD̄ (read), WR̄ (write), IO/M̄ (I/O or memory)<br/>
• <b>Status Signals:</b> S₁, S₀ (identify operation type)<br/>
• <b>Other Signals:</b> ALE, READY, RESET IN, HOLD, HLDA<br/><br/>
<b>Bus Timing:</b><br/>
During T1 state: Address is placed on address bus, ALE goes high<br/>
During T2/T3 states: Data transfer occurs on data bus<br/>
This organized bus structure enables efficient communication between all system components.""",
            },
            {
                "num": "12",
                "question": "Explain the opcode fetch machine cycle for MVI A, 32H with timing diagram.",
                "marks": "5",
                "answer": """<b>Opcode Fetch Machine Cycle for MVI A, 32H:</b><br/><br/>
MVI A, 32H is a 2-byte instruction:<br/>
• Byte 1: Opcode (3E H) — MVI A<br/>
• Byte 2: Data (32 H) — immediate operand<br/><br/>
<b>Opcode Fetch Cycle (T1-T4):</b><br/><br/>
<b>T1 State:</b><br/>
• PC contents (address of 3E H) placed on address bus<br/>
• ALE goes HIGH to latch the address<br/>
• IO/M̄ = 0 (memory operation)<br/><br/>
<b>T2 State:</b><br/>
• ALE goes LOW<br/>
• RD̄ goes LOW (read signal active)<br/>
• Memory places opcode 3E H on data bus<br/><br/>
<b>T3 State:</b><br/>
• Opcode 3E H is read into instruction register<br/>
• RD̄ goes HIGH<br/>
• PC is incremented by 1<br/><br/>
<b>T4 State:</b><br/>
• Opcode is decoded<br/>
• CPU recognizes it as MVI A (2-byte instruction)<br/><br/>
<b>Memory Read Cycle for Operand (T1-T3 of next cycle):</b><br/>
Similar to opcode fetch, but reads data byte 32H and transfers it to accumulator.<br/><br/>
<i>[Timing Diagram: CLK, ALE, A₁₅-A₀, AD₇-AD₀, RD̄, WR̄ showing states T1-T4]</i><br/><br/>
<b>Total Machine Cycles:</b> 2 (Opcode Fetch + Memory Read) = 7 T-states""",
            },
            {
                "num": "13",
                "question": "Explain the 8085 Instruction addressing modes with example.",
                "marks": "5",
                "answer": """<b>Addressing Modes of 8085:</b><br/><br/>
<b>1. Immediate Addressing:</b><br/>
Data is specified directly in the instruction.<br/>
<i>Example:</i> MVI A, 32H — loads 32H directly into accumulator<br/>
<i>Example:</i> ADI 05H — adds 05H to accumulator<br/><br/>
<b>2. Register Addressing:</b><br/>
Data is in a register specified in the instruction.<br/>
<i>Example:</i> MOV A, B — copies data from register B to A<br/>
<i>Example:</i> ADD C — adds contents of register C to A<br/><br/>
<b>3. Register Indirect Addressing:</b><br/>
Instruction specifies a register pair that holds the memory address of data.<br/>
<i>Example:</i> MOV A, M — loads data from memory location pointed by HL pair<br/>
<i>Example:</i> LDAX B — loads accumulator from memory pointed by BC pair<br/><br/>
<b>4. Direct Addressing:</b><br/>
Instruction contains the 16-bit memory address directly.<br/>
<i>Example:</i> LDA 2050H — loads accumulator from memory location 2050H<br/>
<i>Example:</i> STA 3050H — stores accumulator to memory location 3050H<br/><br/>
<b>5. Implicit/Implied Addressing:</b><br/>
No operand is specified; operation is internal to CPU.<br/>
<i>Example:</i> CMA — complements accumulator<br/>
<i>Example:</i> RLC — rotates accumulator left<br/><br/>
<b>Summary Table:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>Mode</td><td>Data Location</td><td>Example</td></tr>
<tr><td>Immediate</td><td>In instruction</td><td>MVI A, 32H</td></tr>
<tr><td>Register</td><td>In register</td><td>MOV A, B</td></tr>
<tr><td>Register Indirect</td><td>Memory (addr in reg pair)</td><td>MOV A, M</td></tr>
<tr><td>Direct</td><td>Memory (addr in instruction)</td><td>LDA 2050H</td></tr>
<tr><td>Implicit</td><td>Internal register</td><td>CMA</td></tr>
</table>""",
            },
            {
                "num": "14",
                "question": "Explain the memory hierarchy with diagram.",
                "marks": "5",
                "answer": """<b>Memory Hierarchy:</b><br/><br/>
Memory hierarchy organizes computer memory into levels based on speed, cost, and size. The goal is to provide a balance between fast access and large capacity at reasonable cost.<br/><br/>
<i>[Diagram description: Pyramid structure]</i><br/>
<table border='1' cellpadding='3'>
<tr><td><b>Level</b></td><td><b>Type</b></td><td><b>Speed</b></td><td><b>Size</b></td><td><b>Cost</b></td></tr>
<tr><td>Top</td><td>Registers</td><td>Fastest (1 ns)</td><td>Smallest (bytes)</td><td>Highest</td></tr>
<tr><td></td><td>Cache (L1, L2, L3)</td><td>Very fast (2-10 ns)</td><td>Small (KB-MB)</td><td>Very high</td></tr>
<tr><td></td><td>Main Memory (RAM)</td><td>Fast (50-100 ns)</td><td>Medium (GB)</td><td>Moderate</td></tr>
<tr><td></td><td>Secondary (SSD/HDD)</td><td>Slow (ms)</td><td>Large (TB)</td><td>Low</td></tr>
<tr><td>Bottom</td><td>Offline/Tertiary (Tape)</td><td>Slowest</td><td>Largest</td><td>Lowest</td></tr>
</table><br/>
<b>Principle:</b> As we go down the hierarchy:<br/>
• Speed decreases<br/>
• Capacity increases<br/>
• Cost per bit decreases<br/><br/>
<b>Working Principle:</b><br/>
• Most frequently used data is kept in faster, smaller memories (registers, cache)<br/>
• Less frequently used data resides in slower, larger memories (RAM, disk)<br/>
• Data moves between levels automatically (cache management, virtual memory)<br/><br/>
<b>Locality of Reference:</b><br/>
• <b>Temporal:</b> Recently accessed data is likely to be accessed again<br/>
• <b>Spatial:</b> Data near recently accessed data is likely to be accessed<br/><br/>
This principle makes memory hierarchy effective, giving the illusion of large, fast, cheap memory.""",
            },
            {
                "num": "15",
                "question": "Explain the organization of Microprogrammed Control Unit.",
                "marks": "5",
                "answer": """<b>Microprogrammed Control Unit:</b><br/><br/>
A microprogrammed control unit implements control signals using a stored program (microprogram) in control memory (ROM), rather than hardwired logic. It is more flexible and easier to modify than hardwired control.<br/><br/>
<b>Components:</b><br/><br/>
<b>1. Control Memory (ROM):</b><br/>
• Stores microinstructions (control words)<br/>
• Each machine instruction corresponds to a microprogram (sequence of microinstructions)<br/>
• Typically 1K-4K words of control store<br/><br/>
<b>2. Control Address Register (CAR):</b><br/>
• Holds the address of the next microinstruction to be executed<br/>
• Also called Microprogram Counter (μPC)<br/><br/>
<b>3. Control Data Register (CDR):</b><br/>
• Holds the current microinstruction being executed<br/>
• Also called Pipeline Register or Control Buffer Register<br/><br/>
<b>4. Microinstruction Format:</b><br/>
Contains fields for:<br/>
• <b>Control Field:</b> Specifies which control signals to activate<br/>
• <b>Address Field:</b> Specifies address of next microinstruction<br/>
• <b>Condition Field:</b> Specifies branching conditions (flags, status)<br/><br/>
<b>5. Mapping Logic:</b><br/>
• Converts opcode of machine instruction to starting address of its microprogram in control memory<br/><br/>
<b>Execution Process:</b><br/>
1. Machine instruction fetched and decoded<br/>
2. Mapping logic converts opcode to microprogram address<br/>
3. Microinstructions are fetched from control memory sequentially<br/>
4. Control signals are generated to execute each microoperation<br/>
5. Next address logic determines next microinstruction address<br/><br/>
<b>Advantages:</b> Flexible, easy to modify, supports complex instructions<br/>
<b>Disadvantages:</b> Slower than hardwired control, requires control memory""",
            },
            {
                "num": "16",
                "question": "Define control word. Explain the procedure for generating control word for specific operation.",
                "marks": "5",
                "answer": """<b>Control Word:</b><br/>
A control word is a binary word stored in control memory that specifies the control signals to be activated during a microoperation. Each bit in the control word corresponds to a specific control signal. When a bit is 1, the corresponding control signal is active; when 0, it is inactive.<br/><br/>
<b>Format of Control Word:</b><br/>
<table border='1' cellpadding='3'>
<tr><td>F1</td><td>F2</td><td>F3</td><td>CD</td><td>BR</td><td>AD</td></tr>
<tr><td>3 bits</td><td>3 bits</td><td>3 bits</td><td>2 bits</td><td>2 bits</td><td>7 bits</td></tr>
</table><br/>
• <b>F1, F2, F3:</b> Microoperation fields (select ALU, register, or memory operations)<br/>
• <b>CD:</b> Condition for branching (status bits)<br/>
• <b>BR:</b> Branch field (type of branch: JMP, CALL, RET, etc.)<br/>
• <b>AD:</b> Address field (next microinstruction address)<br/><br/>
<b>Procedure for Generating Control Word:</b><br/><br/>
<b>Step 1:</b> Identify the microoperations required for the specific operation (e.g., ADD, MOV, LOAD).<br/><br/>
<b>Step 2:</b> Determine which control signals need to be activated for each microoperation.<br/>
<i>Example for ADD R1, R2:</i><br/>
• Select R1 as destination → DR ← R1<br/>
• Select R2 as source → SR ← R2<br/>
• ALU performs ADD → ALU_op = ADD<br/>
• Write result to R1 → Write_enable<br/><br/>
<b>Step 3:</b> Encode the control signals into the control word format.<br/>
Each control signal is assigned a bit position in the control word.<br/><br/>
<b>Step 4:</b> Store the control word in control memory at the appropriate address.<br/><br/>
<b>Step 5:</b> Sequence the control words to form a complete microprogram for the instruction.<br/><br/>
<i>Example Control Word for PC ← PC + 1:</i><br/>
• PC_out = 1 (output PC to bus)<br/>
• ALU_add = 1 (ALU adds 1)<br/>
• PC_in = 1 (input result to PC)<br/>
• All other signals = 0<br/><br/>
Control Word = 0010 1000 0001... (binary pattern for active signals)""",
            },
            {
                "num": "17",
                "question": "Define instruction pipeline. Explain the four-segment instruction pipeline with example.",
                "marks": "5",
                "answer": """<b>Instruction Pipeline:</b><br/>
Instruction pipelining is a technique where multiple instructions are overlapped in execution. The processor is divided into stages, and different instructions occupy different stages simultaneously, similar to an assembly line. This increases instruction throughput (number of instructions completed per unit time).<br/><br/>
<b>Four-Segment Instruction Pipeline:</b><br/><br/>
<b>Segment 1: FI (Fetch Instruction)</b><br/>
• Read instruction from memory<br/>
• PC is incremented<br/>
• Instruction placed in instruction register<br/><br/>
<b>Segment 2: DA (Decode Address / Decode Instruction)</b><br/>
• Decode the opcode to determine the operation<br/>
• Decode/register fetch: read register operands<br/>
• Calculate effective address for memory operands<br/><br/>
<b>Segment 3: FO (Fetch Operands)</b><br/>
• Fetch operands from registers or memory<br/>
• For memory operands, perform address calculation and memory read<br/><br/>
<b>Segment 4: EX (Execute)</b><br/>
• ALU performs the operation<br/>
• Store result in destination register or memory<br/>
• Update status flags<br/><br/>
<b>Example Execution:</b><br/>
Consider instructions I1, I2, I3, I4:<br/>
<table border='1' cellpadding='3'>
<tr><td>Clock</td><td>FI</td><td>DA</td><td>FO</td><td>EX</td></tr>
<tr><td>1</td><td>I1</td><td>-</td><td>-</td><td>-</td></tr>
<tr><td>2</td><td>I2</td><td>I1</td><td>-</td><td>-</td></tr>
<tr><td>3</td><td>I3</td><td>I2</td><td>I1</td><td>-</td></tr>
<tr><td>4</td><td>I4</td><td>I3</td><td>I2</td><td>I1</td></tr>
<tr><td>5</td><td>I5</td><td>I4</td><td>I3</td><td>I2</td></tr>
<tr><td>6</td><td>I6</td><td>I5</td><td>I4</td><td>I3</td></tr>
</table><br/>
After initial fill (3 cycles), one instruction completes every cycle. Without pipelining, each instruction would take 4 cycles, so 4 instructions = 16 cycles. With pipelining, 4 instructions = 7 cycles (after fill).""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2 × 10 = 20]",
        "questions": [
            {
                "num": "18",
                "question": "Explain the functional block diagram of 8085 Microprocessor.",
                "marks": "10",
                "answer": """<b>Functional Block Diagram of 8085 Microprocessor:</b><br/><br/>
The 8085 is an 8-bit NMOS microprocessor with the following functional units:<br/><br/>
<i>[Diagram description: Central ALU connected to registers, control unit, and buses]</i><br/><br/>
<b>1. Arithmetic and Logic Unit (ALU):</b><br/>
• Performs arithmetic operations (ADD, SUB, INC, DEC)<br/>
• Performs logical operations (AND, OR, XOR, NOT, Compare)<br/>
• Updates flags (Sign, Zero, Carry, Parity, Auxiliary Carry)<br/>
• 8-bit wide, works with accumulator and temporary register<br/><br/>
<b>2. Registers:</b><br/>
• <b>Accumulator (A):</b> 8-bit, stores result of ALU operations<br/>
• <b>General Purpose Registers:</b> B, C, D, E, H, L (8-bit each)<br/>
• <b>Register Pairs:</b> BC, DE, HL (16-bit each for addressing)<br/>
• <b>Program Counter (PC):</b> 16-bit, holds address of next instruction<br/>
• <b>Stack Pointer (SP):</b> 16-bit, points to top of stack<br/>
• <b>Instruction Register (IR):</b> Holds current instruction<br/>
• <b>Temporary Registers:</b> W, Z, ACT, TMP for internal operations<br/><br/>
<b>3. Flag Register (8-bit):</b><br/>
• S (Sign): Set if MSB of result is 1<br/>
• Z (Zero): Set if result is zero<br/>
• AC (Auxiliary Carry): Carry from bit 3 to bit 4<br/>
• P (Parity): Set if result has even number of 1s<br/>
• CY (Carry): Set if carry/borrow generated<br/><br/>
<b>4. Timing and Control Unit:</b><br/>
• Generates control signals (RD̄, WR̄, ALE, IO/M̄)<br/>
• Manages instruction sequencing and machine cycles<br/>
• Synchronizes operations with clock (3 MHz)<br/><br/>
<b>5. Interrupt Control:</b><br/>
• Manages 5 interrupts: INTR, RST 5.5, 6.5, 7.5, TRAP<br/>
• TRAP is non-maskable with highest priority<br/><br/>
<b>6. Serial I/O Control:</b><br/>
• SID (Serial Input Data) and SOD (Serial Output Data)<br/>
• Enables serial communication<br/><br/>
<b>7. Address Buffer and Address/Data Buffer:</b><br/>
• Address buffer drives 16-bit address bus<br/>
• Address/Data buffer is bidirectional for multiplexed AD₇-AD₀<br/><br/>
All these units work together to fetch, decode, and execute instructions in a coordinated manner.""",
            },
            {
                "num": "19",
                "question": "Explain the design and control logic of Accumulator.",
                "marks": "10",
                "answer": """<b>Accumulator in 8085:</b><br/><br/>
The accumulator (register A) is an 8-bit register that plays a central role in 8085 operations. It is the default source and destination for most ALU operations.<br/><br/>
<b>Design of Accumulator:</b><br/><br/>
<b>1. 8-bit Register:</b><br/>
• Built using 8 D flip-flops<br/>
• Can store one byte of data<br/>
• Connected to internal data bus through tri-state buffers<br/><br/>
<b>2. Input Path:</b><br/>
• Data can be loaded into accumulator from:<br/>
  - Internal data bus (from memory, I/O, or other registers)<br/>
  - ALU output (result of arithmetic/logical operations)<br/>
• Load control signal: A_in (when active, data enters accumulator)<br/><br/>
<b>3. Output Path:</b><br/>
• Accumulator contents can be output to:<br/>
  - Internal data bus (to memory, I/O, or other registers)<br/>
  - ALU input A (for ALU operations)<br/>
• Output control signal: A_out (when active, data leaves accumulator)<br/><br/>
<b>Control Logic of Accumulator:</b><br/><br/>
<b>1. Load Operation (A ← data):</b><br/>
• Control signals: A_in = 1, A_out = 0<br/>
• Data from bus is latched into accumulator on clock edge<br/>
• Used by instructions: MVI A, data; MOV A, reg; LDA addr; IN port<br/><br/>
<b>2. Output Operation (bus ← A):</b><br/>
• Control signals: A_out = 1, A_in = 0<br/>
• Accumulator contents placed on internal bus<br/>
• Used by instructions: MOV reg, A; STA addr; OUT port<br/><br/>
<b>3. ALU Operation (A ← A op data):</b><br/>
• Control signals: A_out = 1 (to ALU), A_in = 1 (from ALU)<br/>
• Both operations may occur in different clock phases<br/>
• Used by: ADD, SUB, ANA, ORA, XRA, CMP instructions<br/><br/>
<b>4. Special Operations:</b><br/>
• <b>Complement:</b> A ← Ā (CMA instruction)<br/>
• <b>Decimal Adjust:</b> A ← BCD adjust (DAA instruction)<br/>
• <b>Rotate:</b> RLC, RRC, RAL, RAR operations<br/><br/>
<b>Timing:</b><br/>
In T-state operations, accumulator input is enabled during write cycles and output during read cycles, synchronized by the internal clock and control unit signals.<br/><br/>
<b>Importance:</b><br/>
The accumulator is essential because:<br/>
• Most arithmetic/logical operations use it implicitly<br/>
• Flag register is updated based on accumulator contents<br/>
• I/O operations transfer data through accumulator""",
            },
            {
                "num": "20",
                "question": "Explain the different data transfer and manipulation instructions with example.",
                "marks": "10",
                "answer": """<b>Data Transfer and Manipulation Instructions in 8085:</b><br/><br/>
<b>A. DATA TRANSFER INSTRUCTIONS:</b><br/><br/>
<b>1. MOV (Move):</b><br/>
Transfers data between registers or between register and memory.<br/>
<i>Example:</i> MOV A, B — copies content of B to A<br/>
<i>Example:</i> MOV M, A — copies A to memory location pointed by HL<br/><br/>
<b>2. MVI (Move Immediate):</b><br/>
Loads 8-bit immediate data into register or memory.<br/>
<i>Example:</i> MVI A, 32H — loads 32H into accumulator<br/>
<i>Example:</i> MVI B, 05H — loads 05H into register B<br/><br/>
<b>3. LDA (Load Accumulator Direct):</b><br/>
Loads accumulator from direct 16-bit memory address.<br/>
<i>Example:</i> LDA 2050H — A ← [2050H]<br/><br/>
<b>4. STA (Store Accumulator Direct):</b><br/>
Stores accumulator to direct 16-bit memory address.<br/>
<i>Example:</i> STA 3050H — [3050H] ← A<br/><br/>
<b>5. LHLD (Load HL Direct):</b><br/>
Loads HL register pair from two consecutive memory locations.<br/>
<i>Example:</i> LHLD 2050H — L ← [2050H], H ← [2051H]<br/><br/>
<b>6. SHLD (Store HL Direct):</b><br/>
Stores HL register pair to two consecutive memory locations.<br/>
<i>Example:</i> SHLD 3050H — [3050H] ← L, [3051H] ← H<br/><br/>
<b>7. LXI (Load Extended Immediate):</b><br/>
Loads 16-bit immediate data into register pair.<br/>
<i>Example:</i> LXI H, 2050H — HL ← 2050H<br/><br/>
<b>8. IN/OUT (Input/Output):</b><br/>
Transfers data between accumulator and I/O port.<br/>
<i>Example:</i> IN 01H — A ← data from port 01H<br/>
<i>Example:</i> OUT 02H — port 02H ← A<br/><br/>
<b>B. DATA MANIPULATION INSTRUCTIONS:</b><br/><br/>
<b>1. Arithmetic Instructions:</b><br/>
• <b>ADD:</b> ADD B — A ← A + B<br/>
• <b>ADI:</b> ADI 05H — A ← A + 05H<br/>
• <b>SUB:</b> SUB C — A ← A - C<br/>
• <b>SUI:</b> SUI 03H — A ← A - 03H<br/>
• <b>INR:</b> INR B — B ← B + 1<br/>
• <b>DCR:</b> DCR C — C ← C - 1<br/>
• <b>DAD:</b> DAD B — HL ← HL + BC<br/><br/>
<b>2. Logical Instructions:</b><br/>
• <b>ANA:</b> ANA B — A ← A AND B (bitwise AND)<br/>
• <b>ANI:</b> ANI 0FH — A ← A AND 0FH (mask upper nibble)<br/>
• <b>ORA:</b> ORA C — A ← A OR C (bitwise OR)<br/>
• <b>XRA:</b> XRA A — A ← A XOR A = 0 (clear accumulator)<br/>
• <b>CMA:</b> CMA — A ← Ā (complement accumulator)<br/>
• <b>CMP:</b> CMP B — Compare A with B (A - B, flags updated)<br/><br/>
<b>3. Rotate Instructions:</b><br/>
• <b>RLC:</b> Rotate accumulator left (MSB → LSB and Carry)<br/>
• <b>RRC:</b> Rotate accumulator right (LSB → MSB and Carry)<br/>
• <b>RAL:</b> Rotate left through carry<br/>
• <b>RAR:</b> Rotate right through carry<br/><br/>
<b>Summary:</b> Data transfer instructions move data without modification, while manipulation instructions perform arithmetic, logical, and shift operations that transform data.""",
            },
        ]
    }
]

print("Generating CACS155 answer sheet...")
generate_answer_sheet("CACS155", "microprocessor-architecture", "Microprocessor & Computer Architecture", 2018, "semester-2", CACS155_2018)
print("✅ CACS155 2018 done!")

print("\n🎉 All 2nd-semester 2018 answer sheets generated successfully!")
