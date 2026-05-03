#!/usr/bin/env python3
import sys
sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS201_2019 = [
    {
        "title": "Group A",
        "instruction": "Attempt all questions. [10×1=10]",
        "questions": [
            {
                "num": "1",
                "question": "Tick the correct answer for the following MCQs:",
                "marks": "10×1",
                "answer": """<b>i) What is the measurement for time complexity of an algorithm?</b><br/>
<b>Ans: c) Counting number of key operations</b><br/>
Time complexity is measured by counting the number of fundamental operations (comparisons, assignments, arithmetic operations) performed by an algorithm as a function of input size n. It describes how runtime grows with input size, typically expressed using Big-O notation.<br/><br/>

<b>ii) Result of postfix evaluation: 5 7 4 – * 8 4 / + ?</b><br/>
<b>Ans: d) 17</b><br/>
Evaluation using stack:<br/>
• Push 5, 7, 4<br/>
• Encounter '-': pop 4, 7 → 7-4 = 3. Push 3<br/>
• Encounter '*': pop 3, 5 → 5*3 = 15. Push 15<br/>
• Push 8, 4<br/>
• Encounter '/': pop 4, 8 → 8/4 = 2. Push 2<br/>
• Encounter '+': pop 2, 15 → 15+2 = <b>17</b><br/><br/>

<b>iii) Recursive formula for post order traversal of binary tree?</b><br/>
<b>Ans: c) Left-Right-Root</b><br/>
Post-order traversal visits: left subtree → right subtree → root node. The recursive formula is: PostOrder(node) = PostOrder(node.left) + PostOrder(node.right) + Visit(node).<br/><br/>

<b>iv) Number of disk movements in TOH with 4 disks?</b><br/>
<b>Ans: d) 15</b><br/>
Tower of Hanoi requires 2<sup>n</sup> - 1 disk movements for n disks. For n = 4: 2<sup>4</sup> - 1 = 16 - 1 = <b>15 movements</b>.<br/><br/>

<b>v) Big-Oh of best case complexity of insertion sort?</b><br/>
<b>Ans: a) O(n)</b><br/>
In the best case (already sorted array), insertion sort makes n-1 comparisons and 0 swaps. Each element is compared once with its predecessor, giving linear time complexity O(n).<br/><br/>

<b>vi) How does rear index incremented in circular queue?</b><br/>
<b>Ans: b) rear=(rear+1)%SIZE</b><br/>
In a circular queue, the modulo operator wraps the rear pointer around to the beginning when it reaches the end of the array, enabling efficient reuse of vacant positions at the front.<br/><br/>

<b>vii) Variation of linked list where none of the node contains NULL pointer?</b><br/>
<b>Ans: c) Circular</b><br/>
In a circular linked list, the last node's next pointer points back to the first node instead of NULL. Thus, no node contains a NULL pointer, creating a closed loop structure.<br/><br/>

<b>viii) Data structure used in DFS of graph?</b><br/>
<b>Ans: a) Stack</b><br/>
Depth First Search (DFS) uses a stack (explicit or implicit via recursion) to explore vertices. It goes as deep as possible along each branch before backtracking.<br/><br/>

<b>ix) True for B-Tree of order M?</b><br/>
<b>Ans: d) All non-leaf nodes with M-1 keys must have M number of children</b><br/>
In a B-Tree of order M, every non-leaf node with k keys must have exactly k+1 children. If a non-leaf node has M-1 keys, it must have M children. All leaves are at the same depth.<br/><br/>

<b>x) Which is not a hash function?</b><br/>
<b>Ans: c) Chaining</b><br/>
Chaining is a collision resolution technique, not a hash function. Hash functions include division method, mid-square method, folding method, and multiplicative method. Chaining handles collisions by storing colliding elements in linked lists at each hash table index.""",
            },
        ]
    },
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What is Data Structure? Show the status of stack converting following infix expression to postfix P + Q – (R*S/T+U)-V*W",
                "marks": "1+4",
                "answer": """<b>Data Structure:</b><br/>
A data structure is a specialized format for organizing, storing, and managing data so that it can be accessed and modified efficiently. It defines the relationship between data elements and the operations that can be performed on them. Examples include arrays, stacks, queues, linked lists, trees, and graphs. The choice of data structure affects program efficiency in terms of time and space complexity.<br/><br/>

<b>Infix to Postfix Conversion: P + Q – (R*S/T+U)-V*W</b><br/>
Operator precedence: * and / (higher), + and - (lower), parentheses override.<br/>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Symbol</b></td><td><b>Stack</b></td><td><b>Postfix Expression</b></td></tr>
<tr><td>P</td><td>Empty</td><td>P</td></tr>
<tr><td>+</td><td>+</td><td>P</td></tr>
<tr><td>Q</td><td>+</td><td>P Q</td></tr>
<tr><td>-</td><td>-</td><td>P Q +</td></tr>
<tr><td>(</td><td>- (</td><td>P Q +</td></tr>
<tr><td>R</td><td>- (</td><td>P Q + R</td></tr>
<tr><td>*</td><td>- ( *</td><td>P Q + R</td></tr>
<tr><td>S</td><td>- ( *</td><td>P Q + R S</td></tr>
<tr><td>/</td><td>- ( /</td><td>P Q + R S *</td></tr>
<tr><td>T</td><td>- ( /</td><td>P Q + R S * T</td></tr>
<tr><td>+</td><td>- ( +</td><td>P Q + R S * T /</td></tr>
<tr><td>U</td><td>- ( +</td><td>P Q + R S * T / U</td></tr>
<tr><td>)</td><td>-</td><td>P Q + R S * T / U +</td></tr>
<tr><td>-</td><td>-</td><td>P Q + R S * T / U + -</td></tr>
<tr><td>V</td><td>-</td><td>P Q + R S * T / U + - V</td></tr>
<tr><td>*</td><td>- *</td><td>P Q + R S * T / U + - V</td></tr>
<tr><td>W</td><td>- *</td><td>P Q + R S * T / U + - V W</td></tr>
<tr><td>End</td><td>Empty</td><td>P Q + R S * T / U + - V W * -</td></tr>
</table>

<b>Final Postfix Expression:</b> P Q + R S * T / U + - V W * -""",
            },
            {
                "num": "3",
                "question": "Write binary search. Consider hash table of size 10; insert keys 62, 37, 36, 44, 67, 91, 107 using linear probing.",
                "marks": "2.5+2.5",
                "answer": """<b>Binary Search Algorithm:</b><br/>
Binary search is an efficient searching algorithm that works on sorted arrays by repeatedly dividing the search interval in half.<br/>

<pre>
Algorithm BinarySearch(A, n, key):
1. Set low = 0, high = n - 1
2. While low <= high do:
   a. mid = (low + high) / 2
   b. If A[mid] == key:
         Return mid  // Element found
   c. Else If key < A[mid]:
         high = mid - 1
   d. Else:
         low = mid + 1
3. Return -1  // Element not found
</pre>

<b>Time Complexity:</b> O(log n) for average and worst case, O(1) for best case.<br/>
<b>Space Complexity:</b> O(1) for iterative, O(log n) for recursive.<br/>
<b>Requirement:</b> Array must be sorted.<br/><br/>

<b>Hash Table Insertion using Linear Probing:</b><br/>
Hash function: h(key) = key % 10 (table size = 10)<br/>
Linear probing: if collision, try (h(key) + i) % 10 for i = 1, 2, 3...<br/>

<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Key</b></td><td><b>h(key) = key % 10</b></td><td><b>Position</b></td><td><b>Collision?</b></td></tr>
<tr><td>62</td><td>62 % 10 = 2</td><td>2</td><td>No</td></tr>
<tr><td>37</td><td>37 % 10 = 7</td><td>7</td><td>No</td></tr>
<tr><td>36</td><td>36 % 10 = 6</td><td>6</td><td>No</td></tr>
<tr><td>44</td><td>44 % 10 = 4</td><td>4</td><td>No</td></tr>
<tr><td>67</td><td>67 % 10 = 7</td><td>7 occupied</td><td>Yes</td></tr>
<tr><td></td><td>(7+1) % 10 = 8</td><td>8</td><td>No</td></tr>
<tr><td>91</td><td>91 % 10 = 1</td><td>1</td><td>No</td></tr>
<tr><td>107</td><td>107 % 10 = 7</td><td>7 occupied</td><td>Yes</td></tr>
<tr><td></td><td>(7+1) % 10 = 8 occupied</td><td></td><td>Yes</td></tr>
<tr><td></td><td>(7+2) % 10 = 9</td><td>9</td><td>No</td></tr>
</table>

<b>Final Hash Table:</b>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Index</b></td><td>0</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr>
<tr><td><b>Key</b></td><td>-</td><td>91</td><td>62</td><td>-</td><td>44</td><td>-</td><td>36</td><td>37</td><td>67</td><td>107</td></tr>
</table>""",
            },
            {
                "num": "4",
                "question": "What are deterministic and non-deterministic algorithms? Explain greedy algorithm.",
                "marks": "2.5+2.5",
                "answer": """<b>Deterministic Algorithm:</b><br/>
A deterministic algorithm is one that, given a particular input, will always produce the same output and follow the same sequence of steps. Every step has a uniquely defined next action. There is no element of randomness or choice in the execution path.<br/>
<b>Characteristics:</b><br/>
• Same input always yields same output<br/>
• Execution path is predictable and repeatable<br/>
• Examples: Bubble sort, Binary search, Linear search<br/><br/>

<b>Non-Deterministic Algorithm:</b><br/>
A non-deterministic algorithm is one where the next state or output is not uniquely determined by the current state and input. It may have multiple possible execution paths, use randomness, or make arbitrary choices at certain steps.<br/>
<b>Characteristics:</b><br/>
• Same input may produce different outputs on different runs<br/>
• May use random numbers or oracles to make choices<br/>
• Examples: Randomized quicksort, Monte Carlo algorithms, genetic algorithms, simulated annealing<br/>
• In theoretical computer science, non-deterministic algorithms are used to define the complexity class NP<br/><br/>

<b>Greedy Algorithm:</b><br/>
A greedy algorithm is an algorithmic paradigm that builds up a solution piece by piece, always choosing the next piece that offers the most immediate benefit (locally optimal choice) with the hope that these local optimizations will lead to a globally optimal solution.<br/>

<b>Characteristics of Greedy Algorithm:</b><br/>
• Makes the locally optimal choice at each step<br/>
• Never reconsiders or reverses its choices (no backtracking)<br/>
• Simple and efficient when applicable<br/>
• Does not always produce the globally optimal solution<br/>

<b>Components of Greedy Algorithm:</b><br/>
1. <b>Candidate set:</b> The set of potential choices<br/>
2. <b>Selection function:</b> Chooses the best candidate to add to the solution<br/>
3. <b>Feasibility function:</b> Checks if a candidate can contribute to the solution<br/>
4. <b>Objective function:</b> Assigns a value to a solution<br/>
5. <b>Solution function:</b> Indicates when a complete solution is found<br/>

<b>Examples of Greedy Algorithms:</b><br/>
• <b>Dijkstra's algorithm:</b> Finds shortest path in a graph<br/>
• <b>Prim's and Kruskal's algorithms:</b> Find minimum spanning tree<br/>
• <b>Huffman coding:</b> Optimal prefix codes for data compression<br/>
• <b>Fractional knapsack:</b> Selects items with highest value-to-weight ratio<br/>
• <b>Activity selection:</b> Selects maximum number of non-overlapping activities<br/><br/>

<b>Example — Coin Change Problem (Greedy Approach):</b><br/>
To make change for 37 using denominations {25, 10, 5, 1}:<br/>
• Pick 25 (largest ≤ 37), remaining = 12<br/>
• Pick 10 (largest ≤ 12), remaining = 2<br/>
• Pick 1 (largest ≤ 2), remaining = 1<br/>
• Pick 1 (largest ≤ 1), remaining = 0<br/>
Total coins = 4 (optimal for US coin denominations)<br/>
<b>Note:</b> Greedy does NOT always give optimal solution for arbitrary denominations.""",
            },
            {
                "num": "5",
                "question": "Draw a BST from the string DATASTRUCTURE and traverse in post order and pre-order.",
                "marks": "2+1.5+1.5",
                "answer": """<b>Binary Search Tree (BST) Construction from "DATASTRUCTURE":</b><br/>
String: D A T A S T R U C T U R E<br/>
Ignoring duplicates (or handling them as per convention), unique characters in order of appearance: D, A, T, S, R, U, C, E<br/>

<b>Insertion Process:</b><br/>
1. Insert D → D becomes root<br/>
2. Insert A → A < D, so A goes to left of D<br/>
3. Insert T → T > D, so T goes to right of D<br/>
4. Insert A → A already exists (skip or place in left subtree)<br/>
5. Insert S → S < T, S goes to left of T<br/>
6. Insert T → T already exists (skip)<br/>
7. Insert R → R < T, R < S, so R goes to left of S<br/>
8. Insert U → U > T, so U goes to right of T<br/>
9. Insert C → C < D, C > A, so C goes to right of A<br/>
10. Insert T → skip<br/>
11. Insert U → skip<br/>
12. Insert R → skip<br/>
13. Insert E → E < D, E > A, E < C, so E goes to left of C<br/>

<b>Final BST Structure:</b><br/>
<pre>
        D
       / \\
      A   T
       \\  / \\
       C S   U
      / /
     E R
</pre>

<b>Preorder Traversal (Root-Left-Right):</b> D A C E T S R U<br/>
<b>Step by step:</b><br/>
• Visit D (root)<br/>
• Go left to A, visit A<br/>
• Go right to C, visit C<br/>
• Go left to E, visit E<br/>
• Back to C, go right (null)<br/>
• Back to A, go left (null)<br/>
• Back to D, go right to T, visit T<br/>
• Go left to S, visit S<br/>
• Go left to R, visit R<br/>
• Back to S, go right (null)<br/>
• Back to T, go right to U, visit U<br/><br/>

<b>Postorder Traversal (Left-Right-Root):</b> E C A R S U T D<br/>
<b>Step by step:</b><br/>
• From D, go left to A, go right to C, go left to E<br/>
• Visit E (no children)<br/>
• Visit C (right done)<br/>
• Visit A (right done)<br/>
• From D, go right to T, go left to S, go left to R<br/>
• Visit R (no children)<br/>
• Visit S (right done)<br/>
• Go right to U, visit U (no children)<br/>
• Visit T (both subtrees done)<br/>
• Visit D (root, both subtrees done)<br/><br/>

<b>Note:</b> If all characters including duplicates are inserted (with duplicates going to right subtree), the tree would be larger. The standard convention for BST with duplicates places them in the right subtree.""",
            },
            {
                "num": "6",
                "question": "Define circular queue. How does it overcome the limitation of linear queue? Explain.",
                "marks": "1+4",
                "answer": """<b>Circular Queue:</b><br/>
A circular queue is a linear data structure that follows the FIFO (First-In-First-Out) principle, but unlike a linear queue, the last position is connected back to the first position to form a circle. This allows efficient reuse of vacant positions created by dequeue operations at the front.<br/><br/>

<b>Limitations of Linear Queue:</b><br/>
In a linear queue implemented using an array, elements are inserted at the rear and deleted from the front. As dequeue operations occur, the front index moves forward, creating vacant spaces at the beginning of the array. However, the rear can only move forward until it reaches the end of the array. Even though there may be empty spaces at the front, the queue appears full when rear reaches the last index. This condition is called <b>false overflow</b> or <b>queue overflow</b>.<br/><br/>

<b>Example of Linear Queue Problem:</b><br/>
Array size = 5<br/>
• Insert A, B, C, D, E → rear = 4 (full)<br/>
• Delete A, B → front = 2 (positions 0, 1 are vacant)<br/>
• Try to insert F → rear cannot move beyond 4, even though 2 spaces are empty!<br/><br/>

<b>How Circular Queue Overcomes This Limitation:</b><br/>
In a circular queue, when the rear reaches the end of the array, it wraps around to the beginning using modulo arithmetic:<br/>
• <b>Enqueue:</b> rear = (rear + 1) % SIZE<br/>
• <b>Dequeue:</b> front = (front + 1) % SIZE<br/>

This creates a circular arrangement where vacant positions at the front can be reused by new elements coming in at the rear. The queue is considered full when (rear + 1) % SIZE == front.<br/><br/>

<b>Operations in Circular Queue:</b><br/>
<pre>
// Insertion
if ((rear + 1) % SIZE == front):
    print("Queue is full")
else:
    rear = (rear + 1) % SIZE
    queue[rear] = element

// Deletion
if (front == rear):
    print("Queue is empty")
else:
    front = (front + 1) % SIZE
    element = queue[front]
</pre>

<b>Advantages of Circular Queue:</b><br/>
• Eliminates false overflow problem<br/>
• Efficient memory utilization — all array positions can be used<br/>
• No need to shift elements after dequeue<br/>
• Both enqueue and dequeue operations take O(1) time<br/>
• Ideal for CPU scheduling, memory management, and traffic systems""",
            },
            {
                "num": "7",
                "question": "What is singly linked list? Write algorithm to add node at beginning and end.",
                "marks": "1+2+2",
                "answer": """<b>Singly Linked List:</b><br/>
A singly linked list is a linear data structure consisting of a sequence of nodes where each node contains two parts: (1) <b>data</b> — the value stored in the node, and (2) <b>next pointer</b> — a reference to the next node in the sequence. The last node's next pointer is NULL, indicating the end of the list. The list is accessed through a head pointer that points to the first node.<br/><br/>

<b>Structure of a Node:</b><br/>
<pre>
struct Node {
    int data;
    struct Node* next;
};
</pre>

<b>Algorithm to Add Node at the Beginning:</b><br/>
<pre>
Algorithm insertAtBeginning(head, value):
1. Create a new node newNode
2. Set newNode->data = value
3. Set newNode->next = head
4. Set head = newNode
5. Return head
</pre>

<b>C Implementation:</b><br/>
<pre>
struct Node* insertAtBeginning(struct Node* head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = value;
    newNode->next = head;
    head = newNode;
    return head;
}
</pre>

<b>Example:</b> If list is 10 → 20 → 30 and we insert 5 at beginning:<br/>
New list: 5 → 10 → 20 → 30<br/><br/>

<b>Algorithm to Add Node at the End:</b><br/>
<pre>
Algorithm insertAtEnd(head, value):
1. Create a new node newNode
2. Set newNode->data = value
3. Set newNode->next = NULL
4. If head == NULL:
       head = newNode
       Return head
5. Set temp = head
6. While temp->next != NULL:
       temp = temp->next
7. Set temp->next = newNode
8. Return head
</pre>

<b>C Implementation:</b><br/>
<pre>
struct Node* insertAtEnd(struct Node* head, int value) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    struct Node* temp = head;
    newNode->data = value;
    newNode->next = NULL;
    
    if (head == NULL) {
        head = newNode;
        return head;
    }
    
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
    return head;
}
</pre>

<b>Example:</b> If list is 10 → 20 → 30 and we insert 40 at end:<br/>
New list: 10 → 20 → 30 → 40<br/><br/>

<b>Time Complexity:</b><br/>
• Insert at beginning: O(1)<br/>
• Insert at end: O(n) — requires traversal to the last node""",
            },
            {
                "num": "8",
                "question": "Define AVL tree. Construct AVL tree from data set: 4, 6, 12, 9, 5, 2, 13, 8, 3, 7, 11.",
                "marks": "1+4",
                "answer": """<b>AVL Tree:</b><br/>
An AVL tree (named after its inventors Adelson-Velsky and Landis) is a self-balancing binary search tree where the difference between the heights of the left and right subtrees (balance factor) of every node is at most 1. The balance factor of a node is calculated as: height(left subtree) - height(right subtree). Valid balance factors are -1, 0, or +1. If the balance factor becomes less than -1 or greater than +1 after insertion or deletion, rotations are performed to restore balance.<br/><br/>

<b>Balance Factor (BF) = Height of Left Subtree - Height of Right Subtree</b><br/>
• BF = +2 and left child's BF ≥ 0 → Right Rotation (LL)<br/>
• BF = +2 and left child's BF < 0 → Left-Right Rotation (LR)<br/>
• BF = -2 and right child's BF ≤ 0 → Left Rotation (RR)<br/>
• BF = -2 and right child's BF > 0 → Right-Left Rotation (RL)<br/><br/>

<b>AVL Tree Construction Step by Step:</b><br/>
Data set: 4, 6, 12, 9, 5, 2, 13, 8, 3, 7, 11<br/><br/>

<b>Step 1:</b> Insert 4<br/>
<pre>  4</pre>

<b>Step 2:</b> Insert 6 (right of 4)<br/>
<pre>  4
    \\
     6</pre>
BF(4) = 0-1 = -1 (balanced)<br/><br/>

<b>Step 3:</b> Insert 12 (right of 6)<br/>
<pre>  4
    \\
     6
      \\
       12</pre>
BF(4) = 0-2 = -2 → <b>Left Rotate at 4 (RR rotation)</b><br/>
After rotation:<br/>
<pre>   6
  / \\
 4   12</pre><br/>

<b>Step 4:</b> Insert 9 (left of 12)<br/>
<pre>   6
  / \\
 4   12
    /
   9</pre>
BF(12) = 1-0 = +1, BF(6) = 0-1 = -1 (balanced)<br/><br/>

<b>Step 5:</b> Insert 5 (left of 6, right of 4)<br/>
<pre>    6
   / \\
  4   12
   \\  /
    5 9</pre>
BF(4) = 0-1 = -1, BF(6) = 1-1 = 0 (balanced)<br/><br/>

<b>Step 6:</b> Insert 2 (left of 4)<br/>
<pre>     6
    / \\
   4   12
  / \\  /
 2   5 9</pre>
All balanced.<br/><br/>

<b>Step 7:</b> Insert 13 (right of 12)<br/>
<pre>     6
    / \\
   4   12
  / \\  / \\
 2   5 9  13</pre>
All balanced.<br/><br/>

<b>Step 8:</b> Insert 8 (left of 9)<br/>
<pre>     6
    / \\
   4   12
  / \\  / \\
 2   5 9  13
      /
     8</pre>
BF(9) = 1-0 = +1, BF(12) = 2-1 = +1, BF(6) = 1-2 = -1 (balanced)<br/><br/>

<b>Step 9:</b> Insert 3 (right of 2)<br/>
<pre>       6
      / \\
     4   12
    / \\   / \\
   2   5  9  13
    \\     /
     3   8</pre>
BF(2) = 0-1 = -1, BF(4) = 2-1 = +1, BF(6) = 2-2 = 0 (balanced)<br/><br/>

<b>Step 10:</b> Insert 7 (left of 8 or as appropriate)<br/>
Insert 7: 7 < 12, 7 < 9, 7 > 8 → right of 8<br/>
<pre>       6
      / \\
     4    12
    / \\    / \\
   2   5   9  13
    \\      / \\
     3     8
          /
         7</pre>
BF(8) = 1-0 = +1, BF(9) = 2-1 = +1, BF(12) = 2-1 = +1, BF(6) = 2-3 = -1 (balanced)<br/><br/>

<b>Step 11:</b> Insert 11 (right of 9)<br/>
Insert 11: 11 < 12, 11 > 9, 11 > 8 → check: 11 > 9, goes to right of 9<br/>
<pre>        6
       / \\
      4    12
     / \\    / \\
    2   5   9   13
     \\     / \\
      3    8  11
          /
         7</pre>
BF(9) = 2-1 = +1, BF(12) = 2-1 = +1. All nodes balanced.<br/><br/>

<b>Final AVL Tree:</b><br/>
<pre>
         6
       /   \\
      4      12
     / \\     /  \\
    2   5    9    13
     \\      / \\
      3     8  11
           /
          7
</pre>

All balance factors are within {-1, 0, +1}. The tree is balanced.""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "What is stack? List applications. Write algorithm for PUSH and POP operations.",
                "marks": "2+3+5",
                "answer": """<b>Stack:</b><br/>
A stack is a linear data structure that follows the <b>LIFO (Last-In-First-Out)</b> principle. The element inserted last is the first one to be removed. It can be visualized as a pile of plates where you can only add or remove plates from the top. The primary operations on a stack are PUSH (insertion) and POP (deletion), both performed at one end called the <b>TOP</b> of the stack.<br/><br/>

<b>Key Operations:</b><br/>
• <b>PUSH:</b> Adds an element to the top of the stack<br/>
• <b>POP:</b> Removes and returns the top element from the stack<br/>
• <b>PEEK/TOP:</b> Returns the top element without removing it<br/>
• <b>isEmpty:</b> Checks if the stack is empty<br/>
• <b>isFull:</b> Checks if the stack is full (in array implementation)<br/><br/>

<b>Applications of Stack:</b><br/>
1. <b>Expression Evaluation and Conversion:</b> Converting infix to postfix/prefix and evaluating postfix expressions<br/>
2. <b>Function Call Management:</b> Call stack in programming languages manages function calls, local variables, and return addresses<br/>
3. <b>Recursion:</b> Recursive function calls use the system stack to store activation records<br/>
4. <b>Backtracking Algorithms:</b> Used in maze solving, puzzle solving, and game playing to remember previous states<br/>
5. <b>Undo/Redo Operations:</b> Text editors and software applications use stacks to implement undo functionality<br/>
6. <b>Browser History:</b> Back and forward navigation in web browsers<br/>
7. <b>Memory Management:</b> Runtime memory allocation uses call stacks<br/>
8. <b>Parenthesis Checking:</b> Validating balanced parentheses in compilers and expression parsers<br/>
9. <b>Tower of Hanoi:</b> Classic problem solved using recursion/stack<br/>
10. <b>Depth First Search (DFS):</b> Graph traversal algorithm uses stack<br/><br/>

<b>Algorithm for PUSH Operation (Array-based):</b><br/>
<pre>
Algorithm PUSH(stack, top, maxSize, value):
1. If top == maxSize - 1:
       Print "Stack Overflow"
       Return
2. top = top + 1
3. stack[top] = value
4. Print "Element pushed successfully"
5. Return
</pre>

<b>C Implementation of PUSH:</b><br/>
<pre>
#define MAX 100
int stack[MAX];
int top = -1;

void push(int value) {
    if (top == MAX - 1) {
        printf("Stack Overflow!\\n");
        return;
    }
    top++;
    stack[top] = value;
    printf("Pushed: %d\\n", value);
}
</pre>

<b>Algorithm for POP Operation (Array-based):</b><br/>
<pre>
Algorithm POP(stack, top):
1. If top == -1:
       Print "Stack Underflow"
       Return -1  // or error code
2. value = stack[top]
3. top = top - 1
4. Return value
</pre>

<b>C Implementation of POP:</b><br/>
<pre>
int pop() {
    int value;
    if (top == -1) {
        printf("Stack Underflow!\\n");
        return -1;
    }
    value = stack[top];
    top--;
    printf("Popped: %d\\n", value);
    return value;
}
</pre>

<b>Time Complexity:</b> PUSH = O(1), POP = O(1)<br/>
<b>Space Complexity:</b> O(n) where n is the maximum size of the stack""",
            },
            {
                "num": "10",
                "question": "What is heap? Explain quick sort with Big-O notation (best, average, worst) and trace to sort: 8, 10, 5, 12, 14, 5, 7, 13.",
                "marks": "2+2+6",
                "answer": """<b>Heap:</b><br/>
A heap is a specialized tree-based data structure that satisfies the <b>heap property</b>. It is a complete binary tree where each node's value follows a specific ordering relative to its children:<br/>
• <b>Max Heap:</b> The value of each node is greater than or equal to the values of its children. The root contains the maximum element.<br/>
• <b>Min Heap:</b> The value of each node is less than or equal to the values of its children. The root contains the minimum element.<br/>

<b>Properties of Heap:</b><br/>
• It is a complete binary tree (all levels are fully filled except possibly the last, which is filled from left to right)<br/>
• Usually implemented using an array where for node at index i:<br/>
  - Left child at index 2i + 1<br/>
  - Right child at index 2i + 2<br/>
  - Parent at index (i - 1) / 2<br/>
• Heaps are used in heap sort, priority queues, and scheduling algorithms<br/><br/>

<b>Quick Sort:</b><br/>
Quick sort is a divide-and-conquer sorting algorithm that works by selecting a 'pivot' element from the array and partitioning the other elements into two sub-arrays according to whether they are less than or greater than the pivot. The sub-arrays are then sorted recursively.<br/><br/>

<b>Algorithm:</b><br/>
<pre>
Algorithm QuickSort(A, low, high):
1. If low < high:
   a. pivotIndex = Partition(A, low, high)
   b. QuickSort(A, low, pivotIndex - 1)
   c. QuickSort(A, pivotIndex + 1, high)

Algorithm Partition(A, low, high):
1. pivot = A[high]
2. i = low - 1
3. For j = low to high - 1:
      If A[j] <= pivot:
         i = i + 1
         Swap A[i] and A[j]
4. Swap A[i + 1] and A[high]
5. Return i + 1
</pre>

<b>Time Complexity of Quick Sort:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Case</b></td><td><b>Complexity</b></td><td><b>Explanation</b></td></tr>
<tr><td>Best Case</td><td>O(n log n)</td><td>Occurs when pivot divides array into two equal halves at each step</td></tr>
<tr><td>Average Case</td><td>O(n log n)</td><td>Expected performance with random input data</td></tr>
<tr><td>Worst Case</td><td>O(n²)</td><td>Occurs when pivot is always smallest or largest (already sorted/reverse sorted array)</td></tr>
</table>

<b>Space Complexity:</b> O(log n) for recursion stack in best/average case, O(n) in worst case.<br/><br/>

<b>Trace to Sort: 8, 10, 5, 12, 14, 5, 7, 13</b><br/>

<b>First Call:</b> QuickSort(A, 0, 7)<br/>
Array: [8, 10, 5, 12, 14, 5, 7, 13], pivot = 13 (last element)<br/>
Partition process:<br/>
• j=0, A[0]=8 ≤ 13 → i=0, swap A[0] with A[0] → [8, 10, 5, 12, 14, 5, 7, 13]<br/>
• j=1, A[1]=10 ≤ 13 → i=1, swap A[1] with A[1] → [8, 10, 5, 12, 14, 5, 7, 13]<br/>
• j=2, A[2]=5 ≤ 13 → i=2, swap A[2] with A[2] → [8, 10, 5, 12, 14, 5, 7, 13]<br/>
• j=3, A[3]=12 ≤ 13 → i=3, swap A[3] with A[3] → [8, 10, 5, 12, 14, 5, 7, 13]<br/>
• j=4, A[4]=14 > 13 → no swap<br/>
• j=5, A[5]=5 ≤ 13 → i=4, swap A[4] and A[5] → [8, 10, 5, 12, 5, 14, 7, 13]<br/>
• j=6, A[6]=7 ≤ 13 → i=5, swap A[5] and A[6] → [8, 10, 5, 12, 5, 7, 14, 13]<br/>
Swap A[i+1]=A[6] with A[7]: → [8, 10, 5, 12, 5, 7, 13, 14]<br/>
<b>Pivot index = 6</b><br/><br/>

<b>Left Sub-array:</b> QuickSort(A, 0, 5)<br/>
Array: [8, 10, 5, 12, 5, 7], pivot = 7<br/>
• j=0, 8 > 7 → no swap<br/>
• j=1, 10 > 7 → no swap<br/>
• j=2, 5 ≤ 7 → i=0, swap A[0] and A[2] → [5, 10, 8, 12, 5, 7]<br/>
• j=3, 12 > 7 → no swap<br/>
• j=4, 5 ≤ 7 → i=1, swap A[1] and A[4] → [5, 5, 8, 12, 10, 7]<br/>
• j=5, A[5]=7 is pivot position, end loop<br/>
Swap A[i+1]=A[2] with A[5]: → [5, 5, 7, 12, 10, 8]<br/>
<b>Pivot index = 2</b><br/><br/>

<b>Left of 7:</b> QuickSort(A, 0, 1)<br/>
Array: [5, 5], pivot = 5<br/>
• j=0, 5 ≤ 5 → i=0, swap A[0] with A[0] → [5, 5]<br/>
Swap A[1] with A[1]: → [5, 5] (already sorted)<br/><br/>

<b>Right of 7:</b> QuickSort(A, 3, 5)<br/>
Array: [12, 10, 8], pivot = 8<br/>
• j=3, 12 > 8 → no swap<br/>
• j=4, 10 > 8 → no swap<br/>
Swap A[3] with A[5]: → [8, 10, 12]<br/>
<b>Pivot index = 3</b><br/><br/>

<b>Right of 8:</b> QuickSort(A, 4, 5)<br/>
Array: [10, 12], pivot = 12<br/>
• j=4, 10 ≤ 12 → i=4, swap A[4] with A[4] → [10, 12]<br/>
Swap A[5] with A[5] → [10, 12] (already sorted)<br/><br/>

<b>Right of original pivot (13):</b> QuickSort(A, 7, 7)<br/>
Single element [14], already sorted.<br/><br/>

<b>Final Sorted Array:</b> [5, 5, 7, 8, 10, 12, 13, 14]""",
            },
            {
                "num": "11",
                "question": "Define graph and tree. Explain BFS and DFS with examples.",
                "marks": "2+2+6",
                "answer": """<b>Graph:</b><br/>
A graph is a non-linear data structure consisting of a finite set of <b>vertices (nodes)</b> and a set of <b>edges</b> that connect pairs of vertices. Formally, a graph G is defined as G = (V, E) where V is the set of vertices and E is the set of edges. Graphs can be <b>directed</b> (edges have direction) or <b>undirected</b> (edges have no direction). Edges may have <b>weights</b> representing costs, distances, or capacities.<br/>

<b>Types of Graphs:</b><br/>
• <b>Undirected Graph:</b> Edges have no direction; if (u, v) exists, (v, u) also exists<br/>
• <b>Directed Graph (Digraph):</b> Edges have direction; (u, v) ≠ (v, u)<br/>
• <b>Weighted Graph:</b> Each edge has an associated weight/cost<br/>
• <b>Unweighted Graph:</b> All edges are treated equally<br/>
• <b>Cyclic Graph:</b> Contains at least one cycle<br/>
• <b>Acyclic Graph:</b> Contains no cycles (e.g., DAG — Directed Acyclic Graph)<br/>
• <b>Complete Graph:</b> Every pair of distinct vertices is connected by an edge<br/>
• <b>Connected Graph:</b> There is a path between every pair of vertices<br/><br/>

<b>Tree:</b><br/>
A tree is a special type of graph that is <b>connected, acyclic, and undirected</b>. It consists of nodes connected by edges with the following properties:<br/>
• There is exactly one path between any two nodes<br/>
• A tree with n nodes has exactly n-1 edges<br/>
• One node is designated as the <b>root</b><br/>
• Nodes with no children are called <b>leaves</b><br/>
• Nodes with children are called <b>internal nodes</b><br/>

<b>Types of Trees:</b><br/>
• <b>Binary Tree:</b> Each node has at most 2 children<br/>
• <b>Binary Search Tree (BST):</b> Left child < parent < right child<br/>
• <b>AVL Tree:</b> Self-balancing BST<br/>
• <b>B-Tree/B+ Tree:</b> Multi-way search trees used in databases<br/>
• <b>Heap:</b> Complete binary tree with heap property<br/><br/>

<b>Difference between Graph and Tree:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Graph</b></td><td><b>Tree</b></td></tr>
<tr><td>May contain cycles</td><td>Cannot contain cycles</td></tr>
<tr><td>Not necessarily connected</td><td>Always connected</td></tr>
<tr><td>No root node</td><td>Has a root node</td></tr>
<tr><td>Number of edges not fixed</td><td>n nodes have exactly n-1 edges</td></tr>
<tr><td>No parent-child hierarchy</td><td>Parent-child hierarchy exists</td></tr>
<tr><td>More general structure</td><td>Special case of graph</td></tr>
</table><br/>

<b>Breadth First Search (BFS):</b><br/>
BFS is a graph traversal algorithm that explores vertices level by level. It starts from a source vertex, visits all its adjacent vertices, then visits their adjacent vertices, and so on. BFS uses a <b>queue</b> data structure.<br/>

<b>BFS Algorithm:</b><br/>
<pre>
Algorithm BFS(graph, start):
1. Create a queue Q
2. Mark start as visited and enqueue(Q, start)
3. While Q is not empty:
   a. vertex = dequeue(Q)
   b. Process vertex
   c. For each neighbor of vertex:
      If neighbor is not visited:
         Mark neighbor as visited
         enqueue(Q, neighbor)
</pre>

<b>Example of BFS:</b><br/>
Consider the following undirected graph:<br/>
<pre>
    0
   / \\
  1---2
  |   |
  3---4
</pre>
Starting from vertex 0:<br/>
• Visit 0, enqueue 0 → Queue: [0]<br/>
• Dequeue 0, enqueue neighbors 1, 2 → Queue: [1, 2]<br/>
• Dequeue 1, enqueue neighbors 3 (2 already visited) → Queue: [2, 3]<br/>
• Dequeue 2, enqueue neighbors 4 (1 already visited) → Queue: [3, 4]<br/>
• Dequeue 3, no new neighbors → Queue: [4]<br/>
• Dequeue 4, no new neighbors → Queue: []<br/>
<b>BFS Order:</b> 0, 1, 2, 3, 4<br/><br/>

<b>Depth First Search (DFS):</b><br/>
DFS is a graph traversal algorithm that explores as far as possible along each branch before backtracking. It goes deep into the graph before exploring neighbors at the same level. DFS uses a <b>stack</b> (explicit or implicit via recursion).<br/>

<b>DFS Algorithm (Recursive):</b><br/>
<pre>
Algorithm DFS(graph, vertex):
1. Mark vertex as visited
2. Process vertex
3. For each neighbor of vertex:
   If neighbor is not visited:
      DFS(graph, neighbor)
</pre>

<b>DFS Algorithm (Iterative using Stack):</b><br/>
<pre>
Algorithm DFS(graph, start):
1. Create a stack S
2. Mark start as visited and push(S, start)
3. While S is not empty:
   a. vertex = pop(S)
   b. Process vertex
   c. For each neighbor of vertex:
      If neighbor is not visited:
         Mark neighbor as visited
         push(S, neighbor)
</pre>

<b>Example of DFS (same graph as above):</b><br/>
Starting from vertex 0:<br/>
• Push 0, visit 0 → Stack: [0]<br/>
• Pop 0, push neighbors 2, 1 → Stack: [2, 1]<br/>
• Pop 1, push neighbors 3 (2 already visited, 0 visited) → Stack: [2, 3]<br/>
• Pop 3, push neighbors 4 (1 visited) → Stack: [2, 4]<br/>
• Pop 4, no new neighbors (2, 3 visited) → Stack: [2]<br/>
• Pop 2, no new neighbors (0, 1, 4 visited) → Stack: []<br/>
<b>DFS Order:</b> 0, 1, 3, 4, 2<br/><br/>

<b>Comparison of BFS and DFS:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>BFS</b></td><td><b>DFS</b></td></tr>
<tr><td>Data Structure</td><td>Queue</td><td>Stack</td></tr>
<tr><td>Exploration</td><td>Level by level (breadth-wise)</td><td>Depth-wise, then backtrack</td></tr>
<tr><td>Shortest Path</td><td>Finds shortest path in unweighted graphs</td><td>Does not guarantee shortest path</td></tr>
<tr><td>Memory Usage</td><td>Higher (stores all nodes at current level)</td><td>Lower (stores only current path)</td></tr>
<tr><td>Completeness</td><td>Complete (finds solution if it exists)</td><td>Complete for finite graphs</td></tr>
<tr><td>Applications</td><td>Shortest path, level-order traversal, social networks</td><td>Topological sort, cycle detection, maze solving, backtracking</td></tr>
<tr><td>Time Complexity</td><td>O(V + E)</td><td>O(V + E)</td></tr>
<tr><td>Space Complexity</td><td>O(V)</td><td>O(V)</td></tr>
</table>""",
            },
        ]
    }
]


if __name__ == "__main__":
    generate_answer_sheet(
        "CACS201", "data-structures-algorithms", "Data Structures & Algorithms",
        2019, "semester-3", CACS201_2019
    )
    print("Answer sheet generation complete for CACS201 2019!")
