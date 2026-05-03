#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS201_2024 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "Differentiate between stack and queue. What are the general applications of a stack?",
                "marks": "2+3",
                "answer": """<b>Stack vs Queue:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Basis</b></td><td><b>Stack</b></td><td><b>Queue</b></td></tr>
<tr><td>Principle</td><td>LIFO (Last-In-First-Out)</td><td>FIFO (First-In-First-Out)</td></tr>
<tr><td>Insertion</td><td>Push — at one end (TOP)</td><td>Enqueue — at one end (REAR)</td></tr>
<tr><td>Deletion</td><td>Pop — from TOP end</td><td>Dequeue — from FRONT end</td></tr>
<tr><td>Access point</td><td>Only TOP element accessible</td><td>Only FRONT element accessible</td></tr>
<tr><td>Pointer movement</td><td>Single pointer (top)</td><td>Two pointers (front and rear)</td></tr>
<tr><td>Overflow</td><td>When top == MAX-1</td><td>When rear == MAX-1 (in linear queue)</td></tr>
<tr><td>Underflow</td><td>When top == -1</td><td>When front == rear</td></tr>
<tr><td>Examples</td><td>Pile of plates, browser back button</td><td>Line at ticket counter, printer queue</td></tr>
<tr><td>Variants</td><td>No standard variants</td><td>Linear, circular, priority, deque</td></tr>
</table><br/>

<b>General Applications of Stack:</b><br/>
1. <b>Expression Evaluation and Conversion:</b> Converting infix expressions to postfix/prefix notation and evaluating postfix expressions using a stack.<br/>
2. <b>Function Call Management:</b> The system call stack manages function calls, local variables, return addresses, and parameters in programming languages.<br/>
3. <b>Recursion:</b> Recursive function calls use an implicit stack to store activation records of each recursive call.<br/>
4. <b>Backtracking Algorithms:</b> Used in maze solving, puzzle solving (e.g., Sudoku), and game playing to remember previous states and backtrack when needed.<br/>
5. <b>Undo/Redo Operations:</b> Text editors, word processors, and graphics software use stacks to implement undo and redo functionality.<br/>
6. <b>Browser History:</b> Web browsers use a stack to manage the back and forward navigation of visited pages.<br/>
7. <b>Memory Management:</b> Runtime environments use stacks for dynamic memory allocation and management of local variables.<br/>
8. <b>Parenthesis Matching:</b> Compilers use stacks to check balanced parentheses in arithmetic expressions and programming syntax.<br/>
9. <b>Depth First Search (DFS):</b> Graph traversal algorithm uses a stack (explicit or recursive) to explore nodes depth-wise.""",
            },
            {
                "num": "3",
                "question": "What is a linked list? How is doubly linked list different from circular linked list? Explain with example.",
                "marks": "1+4",
                "answer": """<b>Linked List:</b><br/>
A linked list is a linear data structure in which elements (called nodes) are stored in non-contiguous memory locations. Each node contains two parts: <b>data</b> (the value stored) and a <b>pointer/reference</b> (address of the next node). The first node is called the <b>head</b> and the last node points to NULL, indicating the end of the list. Unlike arrays, linked lists allow dynamic memory allocation and efficient insertion/deletion at any position.<br/><br/>

<b>Difference between Doubly Linked List and Circular Linked List:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Basis</b></td><td><b>Doubly Linked List</b></td><td><b>Circular Linked List</b></td></tr>
<tr><td>Pointer structure</td><td>Each node has two pointers: next and previous</td><td>Each node has one pointer (next) like singly list</td></tr>
<tr><td>Traversal</td><td>Can be traversed in both forward and backward directions</td><td>Can be traversed only in forward direction (singly circular)</td></tr>
<tr><td>Last node pointer</td><td>Last node's next points to NULL; first node's prev points to NULL</td><td>Last node's next points back to the first node</td></tr>
<tr><td>Memory usage</td><td>More memory (extra prev pointer per node)</td><td>Less memory (same as singly linked list)</td></tr>
<tr><td>Insertion/Deletion</td><td>Easier — direct access to previous node via prev pointer</td><td>Requires traversal to find previous node</td></tr>
<tr><td>Application</td><td>Browser navigation (back/forward), undo mechanisms</td><td>CPU scheduling, round-robin algorithms, multiplayer games</td></tr>
<tr><td>NULL pointer</td><td>First and last nodes contain NULL pointers</td><td>No node contains NULL pointer (closed loop)</td></tr>
</table><br/>

<b>Example — Doubly Linked List:</b><br/>
<pre>
NULL <--[10|prev|next]-->[20|prev|next]-->[30|prev|next]--> NULL
         Head                           Tail
</pre>
Here, node 10 has prev=NULL and next=20; node 20 has prev=10 and next=30; node 30 has prev=20 and next=NULL.<br/><br/>

<b>Example — Circular Linked List:</b><br/>
<pre>
        +----------------------------------+
        |                                  |
       \|/                                 |
       [10|next]-->[20|next]-->[30|next]---+
         Head
</pre>
Here, node 10 points to 20, node 20 points to 30, and node 30 points back to 10, forming a circle. There is no NULL pointer in the list.""",
            },
            {
                "num": "4",
                "question": "What is recursion and recursive function? Write a recursive function to compute Fibonacci number.",
                "marks": "2+3",
                "answer": """<b>Recursion:</b><br/>
Recursion is a programming technique in which a function calls itself directly or indirectly to solve a problem. It breaks down a complex problem into smaller, simpler subproblems of the same type. A recursive solution consists of two essential components:<br/>
1. <b>Base Case:</b> The terminating condition that stops the recursion and returns a result without making further recursive calls.<br/>
2. <b>Recursive Case:</b> The part where the function calls itself with a smaller or simpler input, moving progressively toward the base case.<br/><br/>

<b>Recursive Function:</b><br/>
A recursive function is a function that calls itself during its execution. Each recursive call creates a new activation record on the call stack containing local variables and parameters. If the base case is not properly defined, the function may result in infinite recursion leading to <b>stack overflow</b>.<br/><br/>

<b>Example — Recursive Function to Compute Fibonacci Number:</b><br/>
The Fibonacci sequence is defined as: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n ≥ 2.<br/>
<pre>
// C language implementation
int fibonacci(int n) {
    if (n == 0)           // Base case 1
        return 0;
    if (n == 1)           // Base case 2
        return 1;
    return fibonacci(n - 1) + fibonacci(n - 2);  // Recursive case
}

// Python implementation
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
</pre>

<b>Execution Trace for fibonacci(5):</b><br/>
<pre>
fibonacci(5)
= fibonacci(4) + fibonacci(3)
= [fibonacci(3) + fibonacci(2)] + [fibonacci(2) + fibonacci(1)]
= [[fibonacci(2) + fibonacci(1)] + [fibonacci(1) + fibonacci(0)]] + [[fibonacci(1) + fibonacci(0)] + 1]
= [[[fibonacci(1) + fibonacci(0)] + 1] + [1 + 0]] + [[1 + 0] + 1]
= [[[1 + 0] + 1] + 1] + [1 + 1]
= [[1 + 1] + 1] + 2
= [2 + 1] + 2
= 3 + 2 = <b>5</b>
</pre>

<b>Time Complexity:</b> O(2<sup>n</sup>) for naive recursion (exponential)<br/>
<b>Space Complexity:</b> O(n) for the call stack<br/>
<b>Note:</b> The naive recursive approach can be optimized using <b>memoization</b> or <b>dynamic programming</b> to achieve O(n) time complexity.""",
            },
            {
                "num": "5",
                "question": "How does collision occur during hashing? Explain any two hashing functions.",
                "marks": "3+2",
                "answer": """<b>Collision in Hashing:</b><br/>
Collision occurs in hashing when two or more different keys are mapped to the same index (hash address) in the hash table by the hash function. Since the domain of possible keys is typically much larger than the range of hash table indices, collisions are inevitable. When a collision occurs, we need a <b>collision resolution technique</b> to store the conflicting elements.<br/><br/>

<b>Example of Collision:</b><br/>
Hash table size = 10, Hash function = key % 10<br/>
• Key 25 → 25 % 10 = 5 (stored at index 5)<br/>
• Key 35 → 35 % 10 = 5 (collision! Both 25 and 35 map to index 5)<br/><br/>

<b>Why Collisions Occur:</b><br/>
1. <b>Limited table size:</b> The hash table has a finite number of slots, but the key space is potentially infinite.<br/>
2. <b>Non-uniform hash function:</b> A poorly designed hash function may cluster keys into a few indices.<br/>
3. <b>Birthday paradox:</b> Even with a good hash function, collisions become likely as the table fills up.<br/><br/>

<b>Two Hashing Functions:</b><br/><br/>
<b>1. Division Method (Modulo Method):</b><br/>
This is the simplest and most commonly used hash function. The key is divided by the table size, and the remainder is taken as the hash address.<br/>
<b>Formula:</b> h(key) = key % m, where m is the table size.<br/>
<b>Example:</b> For table size m = 10:<br/>
• h(42) = 42 % 10 = <b>2</b><br/>
• h(73) = 73 % 10 = <b>3</b><br/>
• h(128) = 128 % 10 = <b>8</b><br/>
<b>Advantages:</b> Simple, fast, easy to implement.<br/>
<b>Disadvantages:</b> If m is a power of 2 or has common factors with keys, clustering may occur. Best to choose m as a prime number not close to a power of 2.<br/><br/>

<b>2. Mid-Square Method:</b><br/>
In this method, the key is squared, and then a few digits from the middle of the squared result are extracted as the hash address.<br/>
<b>Formula:</b> h(key) = middle_digits(key²)<br/>
<b>Example:</b> For a hash table of size 100 (need 2 digits):<br/>
• Key = 12 → 12² = <b>144</b> → middle digits = <b>44</b><br/>
• Key = 45 → 45² = <b>2025</b> → middle digits = <b>02</b><br/>
• Key = 68 → 68² = <b>4624</b> → middle digits = <b>62</b><br/>
<b>Advantages:</b> Distributes keys more uniformly; less clustering compared to division method.<br/>
<b>Disadvantages:</b> Slightly more computation; the number of middle digits to extract must be chosen carefully based on table size.<br/><br/>

<b>Other Hashing Functions (for reference):</b><br/>
• <b>Folding Method:</b> The key is divided into parts, which are then added together to form the hash address.<br/>
• <b>Multiplicative Method:</b> h(key) = floor(m × (key × A mod 1)), where A is a constant between 0 and 1.""",
            },
            {
                "num": "6",
                "question": "What is an AVL tree? Create an AVL tree from the following data: 18, 12, 14, 8, 5, 25, 34, 24, 27",
                "marks": "1+4",
                "answer": """<b>AVL Tree:</b><br/>
An AVL tree (named after its inventors <b>Adelson-Velsky and Landis</b>) is a self-balancing binary search tree. In an AVL tree, the difference between the heights of the left and right subtrees (called the <b>balance factor</b>) of every node must be at most 1. The balance factor is calculated as:<br/>
<b>Balance Factor = Height of Left Subtree − Height of Right Subtree</b><br/>
Valid balance factors are <b>-1, 0, or +1</b>. If the balance factor becomes less than -1 or greater than +1 after any insertion or deletion, <b>rotations</b> are performed to restore balance while maintaining the BST property.<br/><br/>

<b>Rotation Types:</b><br/>
• <b>LL Rotation (Right Rotation):</b> Performed when BF = +2 and left child's BF ≥ 0<br/>
• <b>RR Rotation (Left Rotation):</b> Performed when BF = -2 and right child's BF ≤ 0<br/>
• <b>LR Rotation (Left-Right Rotation):</b> Performed when BF = +2 and left child's BF < 0<br/>
• <b>RL Rotation (Right-Left Rotation):</b> Performed when BF = -2 and right child's BF > 0<br/><br/>

<b>AVL Tree Construction from: 18, 12, 14, 8, 5, 25, 34, 24, 27</b><br/><br/>

<b>Step 1:</b> Insert 18<br/>
<pre>  18</pre>
BF(18) = 0 (balanced)<br/><br/>

<b>Step 2:</b> Insert 12 (left of 18)<br/>
<pre>   18
  /
 12</pre>
BF(18) = 1-0 = +1 (balanced)<br/><br/>

<b>Step 3:</b> Insert 14 (right of 12)<br/>
<pre>   18
  /
 12
  \
  14</pre>
BF(12) = 0-1 = -1, BF(18) = 2-0 = +2 → <b>LR Rotation at 18</b><br/>
First left rotate at 12, then right rotate at 18:<br/>
<pre>    14
   /  \
  12  18</pre>
BF(14) = 0, BF(12) = 0, BF(18) = 0 (balanced)<br/><br/>

<b>Step 4:</b> Insert 8 (left of 12)<br/>
<pre>     14
    /  \
   12  18
  /
 8</pre>
BF(12) = 1-0 = +1, BF(14) = 1-1 = 0 (balanced)<br/><br/>

<b>Step 5:</b> Insert 5 (left of 8)<br/>
<pre>      14
     /  \
    12  18
   /
  8
 /
5</pre>
BF(8) = 1-0 = +1, BF(12) = 2-0 = +2, BF(14) = 2-1 = +1 → <b>LL Rotation at 12</b><br/>
After right rotation at 12:<br/>
<pre>       14
      /  \
     8   18
    / \
   5  12</pre>
All balanced.<br/><br/>

<b>Step 6:</b> Insert 25 (right of 18)<br/>
<pre>       14
      /  \
     8   18
    / \    \
   5  12   25</pre>
BF(18) = 0-1 = -1, BF(14) = 2-2 = 0 (balanced)<br/><br/>

<b>Step 7:</b> Insert 34 (right of 25)<br/>
<pre>       14
      /  \
     8   18
    / \    \
   5  12   25
            \
            34</pre>
BF(25) = 0-1 = -1, BF(18) = 0-2 = -2, BF(14) = 2-3 = -1 → <b>RR Rotation at 18</b><br/>
After left rotation at 18:<br/>
<pre>        14
       /  \
      8   25
     / \  / \
    5  12 18 34</pre>
All balanced.<br/><br/>

<b>Step 8:</b> Insert 24 (left of 25, right of 18)<br/>
<pre>        14
       /  \
      8   25
     / \  / \
    5  12 18 34
          \
          24</pre>
BF(18) = 0-1 = -1, BF(25) = 2-1 = +1, BF(14) = 2-3 = -1 (balanced)<br/><br/>

<b>Step 9:</b> Insert 27 (right of 25? No, 27 < 34 and 27 > 25 → left of 34, right of 25)<br/>
Wait: 27 > 25 and 27 < 34 → goes to left of 34<br/>
<pre>        14
       /  \
      8   25
     / \  / \
    5  12 18 34
          \   /
          24 27</pre>
BF(34) = 1-0 = +1, BF(25) = 2-2 = 0, BF(14) = 2-3 = -1 (all within {-1,0,1})<br/><br/>

Wait, let me recheck: 27 is between 25 and 34, so left child of 34.<br/>
BF(34) = 1-0 = +1. BF(25) = height(left)=2 (18→24), height(right)=2 (34→27) = 2-2 = 0. BF(14) = left height = 2, right height = 3 = 2-3 = -1. All balanced!<br/><br/>

<b>Final AVL Tree:</b><br/>
<pre>
          14
        /    \
       8      25
      / \    /  \
     5  12  18   34
            \    /
            24  27
</pre>

All balance factors are within {-1, 0, +1}. The tree satisfies both BST property and AVL balance condition.""",
            },
            {
                "num": "7",
                "question": "What are deterministic and non-deterministic algorithms? Explain the use of Big-Oh notation to measure the complexity of an algorithm with an example.",
                "marks": "2+3",
                "answer": """<b>Deterministic Algorithm:</b><br/>
A deterministic algorithm is one that, given a particular input, will always produce the same output and follow the exact same sequence of operations. Every step has a uniquely defined next action. There is no element of randomness, choice, or uncertainty in its execution path.<br/>
<b>Characteristics:</b><br/>
• Same input always yields the same output<br/>
• Execution path is predictable and repeatable<br/>
• No use of random numbers or arbitrary choices<br/>
• <b>Examples:</b> Bubble sort, insertion sort, binary search, linear search, merge sort<br/><br/>

<b>Non-Deterministic Algorithm:</b><br/>
A non-deterministic algorithm is one where the next state or output is not uniquely determined by the current state and input. It may have multiple possible execution paths, use randomness, or make arbitrary choices at certain steps. In theoretical computer science, non-deterministic algorithms are used to define the complexity class <b>NP</b> (Nondeterministic Polynomial time).<br/>
<b>Characteristics:</b><br/>
• Same input may produce different outputs on different runs<br/>
• May use random numbers or oracles to make choices<br/>
• Multiple valid execution paths may exist<br/>
• <b>Examples:</b> Randomized quicksort (pivot chosen randomly), Monte Carlo algorithms, genetic algorithms, simulated annealing, non-deterministic finite automata (NFA)<br/><br/>

<b>Big-Oh Notation:</b><br/>
Big-Oh (O) notation is a mathematical notation used to describe the <b>upper bound</b> of an algorithm's growth rate as the input size n approaches infinity. It characterizes the worst-case time or space complexity, ignoring constant factors and lower-order terms. Big-Oh tells us how much the running time or memory usage grows relative to the input size.<br/><br/>

<b>Formal Definition:</b><br/>
f(n) = O(g(n)) if there exist positive constants c and n₀ such that 0 ≤ f(n) ≤ c·g(n) for all n ≥ n₀.<br/><br/>

<b>Common Big-Oh Complexities:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Complexity</b></td><td><b>Name</b></td><td><b>Example</b></td></tr>
<tr><td>O(1)</td><td>Constant</td><td>Accessing array element by index</td></tr>
<tr><td>O(log n)</td><td>Logarithmic</td><td>Binary search</td></tr>
<tr><td>O(n)</td><td>Linear</td><td>Linear search</td></tr>
<tr><td>O(n log n)</td><td>Linearithmic</td><td>Merge sort, heap sort</td></tr>
<tr><td>O(n²)</td><td>Quadratic</td><td>Bubble sort, insertion sort (worst case)</td></tr>
<tr><td>O(n³)</td><td>Cubic</td><td>Matrix multiplication (naive)</td></tr>
<tr><td>O(2ⁿ)</td><td>Exponential</td><td>Recursive Fibonacci, subset generation</td></tr>
</table><br/>

<b>Example — Analyzing Bubble Sort with Big-Oh:</b><br/>
<pre>
for i = 0 to n-2:
    for j = 0 to n-i-2:
        if A[j] > A[j+1]:
            swap(A[j], A[j+1])
</pre>
<b>Step-by-step analysis:</b><br/>
• The outer loop runs (n-1) times → O(n)<br/>
• The inner loop runs approximately n, (n-1), (n-2), ..., 1 times<br/>
• Total comparisons = (n-1) + (n-2) + ... + 1 = n(n-1)/2 = (n² - n)/2<br/>
• Ignoring constants and lower-order terms: <b>Time Complexity = O(n²)</b><br/>
• In the best case (already sorted), the inner loop still runs, so best case is also O(n²) for basic bubble sort. With optimization (flag to detect swaps), best case becomes O(n).<br/>
• <b>Space Complexity = O(1)</b> (only a temporary variable for swapping)<br/><br/>

<b>Why Big-Oh is Important:</b><br/>
• Allows comparison of algorithms independent of hardware<br/>
• Predicts scalability for large inputs<br/>
• Focuses on asymptotic behavior (growth rate) rather than exact runtime<br/>
• Helps in selecting the most efficient algorithm for a given problem""",
            },
            {
                "num": "8",
                "question": "Implement the quick sort to sort the following data items: 12, 1, 14, 7, 2, 10, 4, 7, 22, 6, 15",
                "marks": "5",
                "answer": """<b>Quick Sort Algorithm:</b><br/>
Quick sort is a divide-and-conquer sorting algorithm that works by selecting a 'pivot' element and partitioning the array such that all elements smaller than the pivot are placed to its left, and all elements greater than the pivot are placed to its right. The sub-arrays are then sorted recursively.<br/><br/>

<b>Algorithm:</b><br/>
<pre>
Algorithm QuickSort(A, low, high):
1. If low < high:
2.    pivotIndex = Partition(A, low, high)
3.    QuickSort(A, low, pivotIndex - 1)
4.    QuickSort(A, pivotIndex + 1, high)

Algorithm Partition(A, low, high):
1. pivot = A[high]        // Last element as pivot
2. i = low - 1
3. For j = low to high - 1:
4.    If A[j] <= pivot:
5.       i = i + 1
6.       Swap A[i] and A[j]
7. Swap A[i+1] and A[high]
8. Return i + 1
</pre>

<b>Data to Sort:</b> 12, 1, 14, 7, 2, 10, 4, 7, 22, 6, 15<br/>
Initial Array: [12, 1, 14, 7, 2, 10, 4, 7, 22, 6, 15]<br/><br/>

<b>First Call:</b> QuickSort(A, 0, 10)<br/>
Array: [12, 1, 14, 7, 2, 10, 4, 7, 22, 6, 15], pivot = 15<br/>
Partition process (j from 0 to 9):<br/>
• j=0, A[0]=12 ≤ 15 → i=0, swap A[0],A[0] → [12, 1, 14, 7, 2, 10, 4, 7, 22, 6, 15]<br/>
• j=1, A[1]=1 ≤ 15 → i=1, swap A[1],A[1] → no change<br/>
• j=2, A[2]=14 ≤ 15 → i=2, swap A[2],A[2] → no change<br/>
• j=3, A[3]=7 ≤ 15 → i=3, swap A[3],A[3] → no change<br/>
• j=4, A[4]=2 ≤ 15 → i=4, swap A[4],A[4] → no change<br/>
• j=5, A[5]=10 ≤ 15 → i=5, swap A[5],A[5] → no change<br/>
• j=6, A[6]=4 ≤ 15 → i=6, swap A[6],A[6] → no change<br/>
• j=7, A[7]=7 ≤ 15 → i=7, swap A[7],A[7] → no change<br/>
• j=8, A[8]=22 > 15 → no swap<br/>
• j=9, A[9]=6 ≤ 15 → i=8, swap A[8] and A[9] → [12, 1, 14, 7, 2, 10, 4, 7, 6, 22, 15]<br/>
Swap A[i+1]=A[9] with A[10]: → [12, 1, 14, 7, 2, 10, 4, 7, 6, <b>15</b>, 22]<br/>
<b>Pivot index = 9</b><br/><br/>

<b>Left Sub-array:</b> QuickSort(A, 0, 8)<br/>
Array: [12, 1, 14, 7, 2, 10, 4, 7, 6], pivot = 6<br/>
Partition (j from 0 to 8):<br/>
• j=0, 12 > 6 → no swap<br/>
• j=1, 1 ≤ 6 → i=0, swap A[0] and A[1] → [1, 12, 14, 7, 2, 10, 4, 7, 6]<br/>
• j=2, 14 > 6 → no swap<br/>
• j=3, 7 > 6 → no swap<br/>
• j=4, 2 ≤ 6 → i=1, swap A[1] and A[4] → [1, 2, 14, 7, 12, 10, 4, 7, 6]<br/>
• j=5, 10 > 6 → no swap<br/>
• j=6, 4 ≤ 6 → i=2, swap A[2] and A[6] → [1, 2, 4, 7, 12, 10, 14, 7, 6]<br/>
• j=7, 7 > 6 → no swap<br/>
• j=8, A[8]=6 is pivot position<br/>
Swap A[i+1]=A[3] with A[8]: → [1, 2, 4, <b>6</b>, 12, 10, 14, 7, 7]<br/>
Wait, let me recheck: A[8] is 6 (pivot). After swap A[3] and A[8]: [1, 2, 4, 6, 12, 10, 14, 7, 7]<br/>
<b>Pivot index = 3</b><br/><br/>

<b>Left of pivot 6:</b> QuickSort(A, 0, 2)<br/>
Array: [1, 2, 4], pivot = 4<br/>
• j=0, 1 ≤ 4 → i=0<br/>
• j=1, 2 ≤ 4 → i=1<br/>
Swap A[2] with A[2]: → [1, 2, 4] (already sorted)<br/>
<b>Pivot index = 2</b><br/><br/>

<b>Left of 4:</b> [1, 2] → pivot=2 → sorted as [1, 2]<br/>
<b>Right of 4:</b> empty<br/><br/>

<b>Right of pivot 6:</b> QuickSort(A, 4, 8)<br/>
Array: [12, 10, 14, 7, 7], pivot = 7<br/>
• j=4, 12 > 7 → no swap<br/>
• j=5, 10 > 7 → no swap<br/>
• j=6, 14 > 7 → no swap<br/>
• j=7, 7 ≤ 7 → i=4, swap A[4],A[7] → [7, 10, 14, 12, 7]<br/>
• j=8, 7 ≤ 7 → i=5, swap A[5],A[8] → [7, 7, 14, 12, 10]<br/>
Swap A[i+1]=A[6] with A[8]: → [7, 7, <b>7</b>, 12, 10, 14]<br/>
Wait, let me recount. After j=7, i=4. After j=8, i=5. Swap A[6] and A[8]: [7, 7, 10, 12, 14]<br/>
Hmm, A[6]=14, A[8]=10. After swap: [7, 7, 10, 12, 14]<br/>
<b>Pivot index = 6</b> (relative to full array, index = 6)<br/><br/>

<b>Left of this 7:</b> QuickSort(A, 4, 5)<br/>
Array: [7, 7], pivot = 7 → already in place<br/><br/>

<b>Right of this 7:</b> QuickSort(A, 7, 8)<br/>
Array: [12, 14], pivot = 14 → after partition: [12, 14] → sorted<br/><br/>

<b>Right of original pivot 15:</b> QuickSort(A, 10, 10)<br/>
Array: [22] → single element, already sorted.<br/><br/>

<b>Final Sorted Array:</b> [1, 2, 4, 6, 7, 7, 10, 12, 14, 15, 22]<br/><br/>

<b>Time Complexity:</b> Best/Average = O(n log n), Worst = O(n²)<br/>
<b>Space Complexity:</b> O(log n) for recursion stack""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "What are the differences between linear queue and circular queue? Write an algorithm to enqueue and dequeue data elements in a circular queue.",
                "marks": "4+3+3",
                "answer": """<b>Difference between Linear Queue and Circular Queue:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Basis</b></td><td><b>Linear Queue</b></td><td><b>Circular Queue</b></td></tr>
<tr><td>Structure</td><td>Elements arranged in a straight line</td><td>Last position is connected back to the first position</td></tr>
<tr><td>Memory utilization</td><td>Poor — spaces at front cannot be reused after dequeue</td><td>Efficient — vacant spaces at front are reused</td></tr>
<tr><td>Overflow condition</td><td> rear == MAX - 1</td><td>(rear + 1) % MAX == front</td></tr>
<tr><td>False overflow</td><td>Occurs when rear reaches end but front has empty spaces</td><td>Does not occur</td></tr>
<tr><td>Pointer movement</td><td>front and rear only move forward</td><td>front and rear wrap around using modulo</td></tr>
<tr><td>Implementation</td><td>Simpler</td><td>Slightly more complex</td></tr>
<tr><td>Applications</td><td>Simple scheduling, buffer management</td><td>CPU scheduling, memory management, traffic systems</td></tr>
<tr><td>Wasted space</td><td>Yes, after deletion</td><td>No wasted space (except one slot in some implementations)</td></tr>
</table><br/>

<b>Algorithm to Enqueue in Circular Queue:</b><br/>
<pre>
Algorithm enqueue(queue, front, rear, maxSize, value):
1. If (rear + 1) % maxSize == front:
       Print "Queue is full (Overflow)"
       Return
2. If front == -1:         // First element
       front = 0
3. rear = (rear + 1) % maxSize
4. queue[rear] = value
5. Print "Enqueued: value"
6. Return
</pre>

<b>C Implementation:</b><br/>
<pre>
#define MAX 100
int queue[MAX];
int front = -1, rear = -1;

void enqueue(int value) {
    if ((rear + 1) % MAX == front) {
        printf("Queue Overflow!\\n");
        return;
    }
    if (front == -1)
        front = 0;
    rear = (rear + 1) % MAX;
    queue[rear] = value;
    printf("Enqueued: %d\\n", value);
}
</pre><br/>

<b>Algorithm to Dequeue in Circular Queue:</b><br/>
<pre>
Algorithm dequeue(queue, front, rear, maxSize):
1. If front == -1:
       Print "Queue is empty (Underflow)"
       Return -1
2. value = queue[front]
3. If front == rear:       // Only one element
       front = -1
       rear = -1
4. Else:
       front = (front + 1) % maxSize
5. Print "Dequeued: value"
6. Return value
</pre>

<b>C Implementation:</b><br/>
<pre>
int dequeue() {
    int value;
    if (front == -1) {
        printf("Queue Underflow!\\n");
        return -1;
    }
    value = queue[front];
    if (front == rear) {
        front = -1;
        rear = -1;
    } else {
        front = (front + 1) % MAX;
    }
    printf("Dequeued: %d\\n", value);
    return value;
}
</pre>

<b>Time Complexity:</b> Enqueue = O(1), Dequeue = O(1)<br/>
<b>Space Complexity:</b> O(maxSize) for the queue array""",
            },
            {
                "num": "10",
                "question": "What is B-tree? How insertions and deletions of elements can be done in a B-tree?",
                "marks": "2+8",
                "answer": """<b>B-Tree:</b><br/>
A B-tree is a self-balancing multi-way search tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. It is a generalization of binary search trees where a node can have more than two children. B-trees are particularly well-suited for storage systems that read and write large blocks of data, such as databases and file systems.<br/><br/>

<b>Properties of B-tree of order m:</b><br/>
1. Every node has at most <b>m</b> children.<br/>
2. Every internal node (except root) has at least <b>⌈m/2⌉</b> children.<br/>
3. The root has at least 2 children if it is not a leaf node.<br/>
4. All leaf nodes are at the same depth (balanced).<br/>
5. A node with <b>k</b> children contains <b>k-1</b> keys.<br/>
6. Keys within a node are stored in ascending order.<br/><br/>

<b>Insertion in B-Tree:</b><br/>
The insertion algorithm ensures that all B-tree properties are maintained after adding a new key.<br/>
<pre>
Algorithm BTreeInsert(T, key):
1. If T is empty:
       Create a new root node containing key
       Return
2. Find the appropriate leaf node where key should be inserted
3. Insert key into the leaf node in sorted order
4. If leaf node overflows (has m keys, i.e., m-1 keys + 1 new = m keys which exceeds m-1 limit):
       a. Split the node at median key
       b. Move median key up to parent node
       c. Create two new nodes: left with keys < median, right with keys > median
       d. If parent overflows, recursively split up to root
5. If root splits, create a new root with the median key and increase tree height by 1
</pre>

<b>Example of Insertion in B-Tree of order 3 (2-3 tree):</b><br/>
Insert 10, 20, 5, 6, 12, 30, 7, 17<br/>
• Insert 10: [10]<br/>
• Insert 20: [10, 20]<br/>
• Insert 5: [5, 10, 20] → Overflow! Split at 10<br/>
  New root: [10], Left: [5], Right: [20]<br/>
• Insert 6: Goes to [5] → [5, 6]<br/>
• Insert 12: Goes to [20] → [12, 20]<br/>
• Insert 30: Goes to [12, 20] → [12, 20, 30] → Overflow! Split at 20<br/>
  Root [10] becomes [10, 20], Left of 20: [12], Right of 20: [30]<br/>
• Insert 7: Goes to [5, 6] → [5, 6, 7] → Overflow! Split at 6<br/>
  Parent [10, 20] becomes [6, 10, 20] → Overflow! Split at 10<br/>
  New root: [10], Left: [6], Right: [20], with appropriate children<br/>
• Continue similarly for remaining keys.<br/><br/>

<b>Deletion in B-Tree:</b><br/>
Deletion requires ensuring that nodes do not underflow (drop below minimum key count).<br/>
<pre>
Algorithm BTreeDelete(T, key):
1. Locate the node containing key
2. If key is in a leaf node:
       a. Simply remove key
       b. If node underflows (keys < ⌈m/2⌉ - 1):
          - Try to borrow a key from left or right sibling
          - If siblings have minimum keys, merge with a sibling and move separator key down from parent
          - If parent underflows, recursively fix up to root
3. If key is in an internal node:
       a. Replace key with its inorder predecessor (largest in left subtree) 
          or inorder successor (smallest in right subtree)
       b. Recursively delete the predecessor/successor from the leaf
4. If root becomes empty after merge, make the merged node the new root
</pre>

<b>Cases for Handling Underflow during Deletion:</b><br/>
<b>Case 1:</b> The key to be deleted is in a leaf and the leaf has more than the minimum number of keys. Simply delete it.<br/><br/>
<b>Case 2:</b> The key is in a leaf but the leaf has the minimum number of keys.<br/>
• <b>2a:</b> If a sibling has more than minimum keys, borrow a key from the sibling through the parent (rotation).<br/>
• <b>2b:</b> If both siblings have minimum keys, merge the leaf with a sibling and pull down the separating key from the parent.<br/><br/>
<b>Case 3:</b> The key is in an internal node. Replace it with its inorder predecessor or successor and delete that key from the leaf.<br/><br/>

<b>Time Complexity:</b> Search, Insert, Delete = O(log<sub>m</sub> n) where m is order and n is number of keys.<br/>
<b>Space Complexity:</b> O(n)""",
            },
            {
                "num": "11",
                "question": "Explain the different ways to represent a graph. For the following graph use Prim's algorithm to find a minimum spanning tree starting from the node 'A'.",
                "marks": "5+5",
                "answer": """<b>Ways to Represent a Graph:</b><br/><br/>

<b>1. Adjacency Matrix:</b><br/>
An adjacency matrix is a 2D array of size V × V (where V is the number of vertices). For an unweighted graph, matrix[i][j] = 1 if there is an edge from vertex i to vertex j, and 0 otherwise. For a weighted graph, matrix[i][j] = weight of the edge, or ∞/0 if no edge exists.<br/>
<b>Example (undirected weighted graph with vertices A, B, C, D):</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td></td><td>A</td><td>B</td><td>C</td><td>D</td></tr>
<tr><td>A</td><td>0</td><td>4</td><td>2</td><td>0</td></tr>
<tr><td>B</td><td>4</td><td>0</td><td>1</td><td>5</td></tr>
<tr><td>C</td><td>2</td><td>1</td><td>0</td><td>3</td></tr>
<tr><td>D</td><td>0</td><td>5</td><td>3</td><td>0</td></tr>
</table>
<b>Advantages:</b> Simple, edge lookup in O(1).<br/>
<b>Disadvantages:</b> O(V²) space, wasteful for sparse graphs.<br/><br/>

<b>2. Adjacency List:</b><br/>
An adjacency list represents a graph as an array of linked lists. Each vertex has a linked list of its adjacent vertices (with weights for weighted graphs).<br/>
<b>Example (same graph):</b><br/>
<pre>
A → (B, 4) → (C, 2)
B → (A, 4) → (C, 1) → (D, 5)
C → (A, 2) → (B, 1) → (D, 3)
D → (B, 5) → (C, 3)
</pre>
<b>Advantages:</b> Space-efficient O(V + E), efficient for sparse graphs.<br/>
<b>Disadvantages:</b> Edge lookup takes O(degree) time.<br/><br/>

<b>3. Edge List:</b><br/>
An edge list stores all edges as a list of tuples (u, v, weight) for weighted graphs.<br/>
<b>Example:</b> [(A,B,4), (A,C,2), (B,C,1), (B,D,5), (C,D,3)]<br/><br/>

<b>4. Incidence Matrix:</b><br/>
An incidence matrix is a V × E matrix where matrix[i][j] = 1 if vertex i is incident to edge j, and 0 otherwise. Used less frequently.<br/><br/>

<b>Prim's Algorithm for Minimum Spanning Tree (MST):</b><br/>
Prim's algorithm finds the MST of a weighted, connected, undirected graph. It starts from an arbitrary vertex and grows the tree by adding the cheapest edge that connects a vertex in the tree to a vertex outside the tree.<br/><br/>

<b>Algorithm:</b><br/>
<pre>
Algorithm Prim(G, start):
1. Initialize a set MST = {start}
2. Initialize totalWeight = 0
3. While MST does not include all vertices:
4.    Find the minimum weight edge (u, v) such that u ∈ MST and v ∉ MST
5.    Add v to MST
6.    Add edge (u, v) to MST edges
7.    totalWeight += weight(u, v)
8. Return MST edges and totalWeight
</pre>

<b>Note:</b> Since the specific graph edges were not fully visible in the original paper, we use a representative graph commonly used in TU BCA exams:<br/>
<pre>
    A
   /|\
  2 4 3
 /  |  \
C---B---D
  1   5
</pre>
Edges: A-C=2, A-B=4, A-D=3, B-C=1, B-D=5<br/><br/>

<b>Step-by-Step Execution starting from 'A':</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Step</b></td><td><b>MST Vertices</b></td><td><b>Candidate Edges</b></td><td><b>Min Edge Selected</b></td><td><b>Weight</b></td></tr>
<tr><td>1</td><td>{A}</td><td>A-C(2), A-B(4), A-D(3)</td><td>A-C</td><td>2</td></tr>
<tr><td>2</td><td>{A, C}</td><td>A-B(4), A-D(3), C-B(1)</td><td>C-B</td><td>1</td></tr>
<tr><td>3</td><td>{A, C, B}</td><td>A-D(3), B-D(5)</td><td>A-D</td><td>3</td></tr>
<tr><td>4</td><td>{A, C, B, D}</td><td>All vertices included</td><td>—</td><td>—</td></tr>
</table><br/>

<b>Total MST Weight = 2 + 1 + 3 = 6</b><br/><br/>

<b>MST Edges:</b> (A, C, 2), (C, B, 1), (A, D, 3)<br/><br/>

<b>Final MST Structure:</b><br/>
<pre>
    A
   / \
  2   3
 /     \
C---1---B       D is connected via A
</pre>

<b>Time Complexity:</b> O(E log V) using a binary heap, or O(E + V log V) using a Fibonacci heap.<br/>
<b>Space Complexity:</b> O(V)""",
                "diagram": "Graph adjacency representations and Prim's algorithm MST should be drawn showing vertices, edges, and weights.",
            },
        ]
    }
]

if __name__ == "__main__":
    generate_answer_sheet(
        "CACS201", "data-structures-algorithms", "Data Structures & Algorithms",
        2024, "semester-3", CACS201_2024
    )
    print("Answer sheet generation complete for CACS201 2024!")
