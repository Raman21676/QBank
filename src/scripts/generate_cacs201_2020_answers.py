#!/usr/bin/env python3
import sys; sys.path.insert(0, '/Users/kalikali/Desktop/QBank/src/scripts')
from generate_answer_sheets import generate_answer_sheet

CACS201_2020 = [
    {
        "title": "Group B",
        "instruction": "Attempt any SIX questions. [6×5=30]",
        "questions": [
            {
                "num": "2",
                "question": "What is data structure? Explain different operations to be performed on data structure.",
                "marks": "1+4",
                "answer": """<b>Data Structure:</b> A data structure is a specialized format for organizing, processing, retrieving and storing data. It defines the relationship between the data elements and the operations that can be performed on them. Data structures are essential for designing efficient algorithms and are classified as linear (arrays, linked lists, stacks, queues) and non-linear (trees, graphs).<br/><br/>
<b>Different Operations on Data Structures:</b><br/>
1. <b>Traversal:</b> Visiting each element of the data structure exactly once. For example, printing all elements of an array or linked list.<br/>
2. <b>Insertion:</b> Adding a new element to the data structure at a specific position. For example, inserting a node in a linked list or an element in an array.<br/>
3. <b>Deletion:</b> Removing an element from the data structure. For example, deleting a node from a tree or an element from a stack.<br/>
4. <b>Searching:</b> Finding the location of a specific element within the data structure. Linear search and binary search are common searching techniques.<br/>
5. <b>Sorting:</b> Arranging the elements in a specific order (ascending or descending). Examples include bubble sort, quick sort, merge sort, and heap sort.<br/>
6. <b>Merging:</b> Combining two sorted data structures into a single sorted data structure.<br/>
7. <b>Updating:</b> Modifying the value of an existing element at a given position.""",
            },
            {
                "num": "3",
                "question": "Define greedy algorithm and heuristic algorithm. Briefly explain Big-Oh notation.",
                "marks": "3+2",
                "answer": """<b>Greedy Algorithm:</b> A greedy algorithm is an algorithmic paradigm that follows the problem-solving heuristic of making the locally optimal choice at each stage with the hope of finding a global optimum. It makes the choice that seems best at the moment without considering future consequences. Greedy algorithms are used when a problem has the properties of greedy choice property and optimal substructure. Examples include Dijkstra's shortest path algorithm, Kruskal's and Prim's minimum spanning tree algorithms, and the fractional knapsack problem.<br/><br/>
<b>Heuristic Algorithm:</b> A heuristic algorithm is a technique designed to solve a problem more quickly when classic methods are too slow, or to find an approximate solution when classic methods fail to find any exact solution. Heuristics use practical methods, experience-based techniques, or rules of thumb rather than formal proofs. They are commonly used in artificial intelligence, optimization problems, and search algorithms where finding an exact solution is computationally infeasible. Examples include A* search algorithm, genetic algorithms, and simulated annealing.<br/><br/>
<b>Big-Oh Notation:</b> Big-Oh notation (O) is a mathematical notation used in computer science to describe the performance or complexity of an algorithm. Specifically, it describes the upper bound of the growth rate of an algorithm's time or space requirement as the input size increases.<br/><br/>
<b>Common Big-Oh complexities:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Notation</b></td><td><b>Name</b></td><td><b>Example</b></td></tr>
<tr><td>O(1)</td><td>Constant time</td><td>Accessing an array element</td></tr>
<tr><td>O(log n)</td><td>Logarithmic</td><td>Binary search</td></tr>
<tr><td>O(n)</td><td>Linear</td><td>Linear search</td></tr>
<tr><td>O(n log n)</td><td>Linearithmic</td><td>Merge sort, Quick sort</td></tr>
<tr><td>O(n²)</td><td>Quadratic</td><td>Bubble sort, Selection sort</td></tr>
<tr><td>O(2ⁿ)</td><td>Exponential</td><td>Recursive Fibonacci</td></tr>
</table>""",
            },
            {
                "num": "4",
                "question": "What is circular queue? Write an algorithm to insert an item in circular queue.",
                "marks": "2+3",
                "answer": """<b>Circular Queue:</b> A circular queue is a linear data structure that follows the FIFO (First In First Out) principle, where the last position is connected back to the first position to form a circle. It is also known as a ring buffer. In a circular queue, when the rear reaches the end of the array, it wraps around to the beginning if there are empty slots. This overcomes the limitation of a simple queue where space before the front pointer cannot be reused even if the queue is not full.<br/><br/>
<b>Algorithm to Insert an Item in Circular Queue:</b><br/>
<pre>
Algorithm CQINSERT(QUEUE, FRONT, REAR, MAX, ITEM)
1. If (FRONT == 0 AND REAR == MAX - 1) OR (FRONT == REAR + 1) then
       Print "Queue Overflow"
       Exit
2. If FRONT == -1 then        // Queue is empty
       FRONT = 0
       REAR = 0
   Else if REAR == MAX - 1 then  // Wrap around
       REAR = 0
   Else
       REAR = REAR + 1
3. QUEUE[REAR] = ITEM
4. Print "Item inserted successfully"
5. Exit
</pre>""",
            },
            {
                "num": "5",
                "question": "How does AVL tree differ from BST? Construct an AVL tree from following data: 35, 56, 68, 65, 44, 41, 31, 49, 20.",
                "marks": "1+4",
                "answer": """<b>Difference between AVL Tree and BST:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>Binary Search Tree (BST)</b></td><td><b>AVL Tree</b></td></tr>
<tr><td>Balance</td><td>May become unbalanced (skewed)</td><td>Always balanced (self-balancing)</td></tr>
<tr><td>Height</td><td>Can be O(n) in worst case</td><td>Always O(log n)</td></tr>
<tr><td>Rotations</td><td>No rotations needed</td><td>Uses rotations (LL, RR, LR, RL) to maintain balance</td></tr>
<tr><td>Balance Factor</td><td>Not considered</td><td>Must be -1, 0, or +1 for every node</td></tr>
<tr><td>Search Time</td><td>O(n) worst case</td><td>O(log n) guaranteed</td></tr>
<tr><td>Insertion/Deletion</td><td>Simple, no rebalancing</td><td>Complex, requires rebalancing</td></tr>
</table><br/><br/>
<b>AVL Tree Construction with data: 35, 56, 68, 65, 44, 41, 31, 49, 20</b><br/><br/>
<b>Step 1:</b> Insert 35 → Tree: 35<br/>
<b>Step 2:</b> Insert 56 → 35's right → Tree: 35(R:56) — Balanced (BF= -1)<br/>
<b>Step 3:</b> Insert 68 → 56's right → BF(35)= -2 → <b>RR Rotation</b> at 35<br/>
   After RR: 56 is root, 35 left, 68 right<br/>
<b>Step 4:</b> Insert 65 → 68's left → Tree balanced (BF values: 56:0, 35:0, 68:-1, 65:0)<br/>
<b>Step 5:</b> Insert 44 → 35's right → Balanced<br/>
<b>Step 6:</b> Insert 41 → 44's left → BF(35)= +2, BF(44)= -1 → <b>LR Rotation</b> at 35<br/>
   After LR: 41 becomes root of subtree, 35 left, 44 right<br/>
<b>Step 7:</b> Insert 31 → 35's left → Balanced<br/>
<b>Step 8:</b> Insert 49 → 44's right → Balanced<br/>
<b>Step 9:</b> Insert 20 → 31's left → BF(41)= +2, BF(35)= +2 → <b>LL Rotation</b> at 41<br/>
   After LL: 35 becomes root of subtree, 31 left, 41 right, 20 is left of 31<br/><br/>
<b>Final AVL Tree Structure:</b><br/>
<pre>
              56
            /    \
          41      68
         /  \    /
       35   44  65
      /  \    \
    31   49   (none)
   /
 20
</pre>""",
            },
            {
                "num": "6",
                "question": "What is B-tree? Create a B-tree of order 4 using following data: 6, 4, 22, 10, 2, 14, 3, 8, 11, 13, 5, 9.",
                "marks": "2+3",
                "answer": """<b>B-Tree:</b> A B-tree is a self-balancing tree data structure that maintains sorted data and allows searches, sequential access, insertions, and deletions in logarithmic time. It is a generalization of a binary search tree in which a node can have more than two children. A B-tree of order m (or degree m) has the following properties:<br/>
• All leaf nodes are at the same level.<br/>
• Every node except root must have at least ⌈m/2⌉ - 1 keys and at most m - 1 keys.<br/>
• Every internal node has at most m children.<br/>
• The root has at least 2 children if it is not a leaf node.<br/>
• Keys within a node are stored in ascending order.<br/><br/>
<b>B-Tree of Order 4 (max 3 keys per node, max 4 children):</b><br/>
Data: 6, 4, 22, 10, 2, 14, 3, 8, 11, 13, 5, 9<br/><br/>
<b>Step 1:</b> Insert 6 → [6]<br/>
<b>Step 2:</b> Insert 4 → [4, 6]<br/>
<b>Step 3:</b> Insert 22 → [4, 6, 22] (full)<br/>
<b>Step 4:</b> Insert 10 → Node overflows. Split: median 6 goes up as root.<br/>
   Root: [6], Left: [4], Right: [10, 22]<br/>
<b>Step 5:</b> Insert 2 → [2, 4] (left child)<br/>
<b>Step 6:</b> Insert 14 → [10, 14, 22] (right child — full)<br/>
<b>Step 7:</b> Insert 3 → [2, 3, 4] (left child — full)<br/>
<b>Step 8:</b> Insert 8 → Goes to left of right child? No, 8 < 10, so new child between 4 and 6? Let's trace properly with splits.<br/>
   After insert 3, left child [2,3,4] is full. Insert 8: 8 > 6, goes to right subtree. 8 < 10, so new left child of [10,14,22]? No, 8 < 10, so goes to position before 10. Node becomes [8,10,14,22] — overflow! Split: median 14 promoted to root.<br/>
   Root: [6, 14], Children: [2,3,4], [8,10], [22]<br/>
<b>Step 9:</b> Insert 11 → 11 > 6, 11 < 14, goes to middle child [8,10] → [8,10,11]<br/>
<b>Step 10:</b> Insert 13 → [8,10,11,13] — overflow! Split: median 10 or 11. Let's use 10 or 11. Split at 10: [8] and [11,13], promote 10 to root. Root becomes [6,10,14] — but max 3 keys, so root overflows!<br/>
   Split root: median 10 promoted to new root. New root: [10], Left: [6], Right: [14].<br/>
   Now reorganize children: [2,3,4] under [6], [8] under [6], [11,13] under [14], [22] under [14].<br/>
<b>Step 11:</b> Insert 5 → 5 < 10, 5 < 6, goes to [2,3,4] → [2,3,4,5] — overflow! Split: promote 3 or 4. Split at 3: [2] and [4,5], promote 3 to [6] → [3,6] (max 3 OK).<br/>
   Children of [3,6]: [2], [4,5], [8]<br/>
<b>Step 12:</b> Insert 9 → 9 < 10, 9 > 6, goes to [8] → [8,9]<br/><br/>
<b>Final B-Tree of Order 4:</b><br/>
<pre>
              [10]
            /      \
         [3, 6]    [14]
        /  |   \    /  \
    [2] [4,5] [8,9] [11,13] [22]
</pre>""",
            },
            {
                "num": "7",
                "question": "What is binary search? Write an algorithm to search an item using binary search.",
                "marks": "2+3",
                "answer": """<b>Binary Search:</b> Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed down the possible locations to just one. The time complexity of binary search is O(log n), making it much faster than linear search (O(n)) for large datasets. Binary search requires the array to be sorted beforehand.<br/><br/>
<b>Algorithm for Binary Search:</b><br/>
<pre>
Algorithm BINARY_SEARCH(A, N, ITEM)
// A is a sorted array of N elements
// ITEM is the element to be searched

1. Set LB = 0, UB = N - 1
2. While LB <= UB do
       MID = (LB + UB) / 2
       If A[MID] == ITEM then
           Print "Item found at index", MID
           Exit
       Else if A[MID] < ITEM then
           LB = MID + 1
       Else
           UB = MID - 1
3. Print "Item not found"
4. Exit
</pre><br/>
<b>Example:</b> Search for 23 in sorted array [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]<br/>
• Iteration 1: LB=0, UB=9, MID=4, A[4]=16 < 23 → LB=5<br/>
• Iteration 2: LB=5, UB=9, MID=7, A[7]=56 > 23 → UB=6<br/>
• Iteration 3: LB=5, UB=6, MID=5, A[5]=23 == 23 → <b>Found at index 5!</b>""",
            },
            {
                "num": "8",
                "question": "What is graph? Explain Kruskal's algorithm to construct minimum spanning tree with example.",
                "marks": "1+4",
                "answer": """<b>Graph:</b> A graph is a non-linear data structure consisting of a finite set of vertices (also called nodes) and a set of edges that connect pairs of vertices. Graphs are used to represent networks, relationships, and paths. A graph G is formally defined as G = (V, E), where V is the set of vertices and E is the set of edges. Graphs can be directed (edges have direction) or undirected, weighted (edges have costs) or unweighted.<br/><br/>
<b>Kruskal's Algorithm for Minimum Spanning Tree (MST):</b><br/>
Kruskal's algorithm is a greedy algorithm that finds a minimum spanning tree for a connected, undirected, weighted graph. The MST is a subset of edges that connects all vertices with the minimum total edge weight, without any cycles.<br/><br/>
<b>Algorithm:</b><br/>
1. Sort all edges in non-decreasing order of their weight.<br/>
2. Initialize an empty set for the MST.<br/>
3. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far using Union-Find.<br/>
4. If cycle is not formed, include this edge. Otherwise, discard it.<br/>
5. Repeat step 3 until there are (V-1) edges in the MST.<br/><br/>
<b>Example:</b> Consider a graph with vertices A, B, C, D, E and edges:<br/>
<table border='1' cellpadding='4'>
<tr><td><b>Edge</b></td><td>A-B</td><td>B-C</td><td>A-C</td><td>C-D</td><td>B-D</td><td>D-E</td><td>C-E</td></tr>
<tr><td><b>Weight</b></td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>1</td><td>7</td></tr>
</table><br/>
<b>Step 1:</b> Sort edges by weight: D-E(1), A-B(2), B-C(3), A-C(4), C-D(5), B-D(6), C-E(7)<br/>
<b>Step 2:</b> Pick D-E(1) — no cycle → MST = {D-E}<br/>
<b>Step 3:</b> Pick A-B(2) — no cycle → MST = {D-E, A-B}<br/>
<b>Step 4:</b> Pick B-C(3) — no cycle → MST = {D-E, A-B, B-C}<br/>
<b>Step 5:</b> Pick A-C(4) — forms cycle (A-B-C-A) → <b>Reject</b><br/>
<b>Step 6:</b> Pick C-D(5) — no cycle → MST = {D-E, A-B, B-C, C-D}<br/>
Now we have 4 edges (V-1 = 5-1 = 4). Stop.<br/><br/>
<b>Total weight of MST = 1 + 2 + 3 + 5 = 11</b>""",
            },
        ]
    },
    {
        "title": "Group C",
        "instruction": "Attempt any TWO questions. [2×10=20]",
        "questions": [
            {
                "num": "9",
                "question": "Define stack. List the applications of stack. Trace the algorithm to convert infix to postfix with following infix expression ((A+B)-C*D/E)*(H-I)*F+G and evaluate the obtained postfix expression with following values: A=4, B=2, C=4, D=3, E=8, F=2, G=3, H=5, I=1",
                "marks": "1+1+4+4",
                "answer": """<b>Stack:</b> A stack is a linear data structure that follows the LIFO (Last In First Out) principle. Elements can only be inserted and deleted from one end called the top. The main operations are PUSH (insert) and POP (delete).<br/><br/>
<b>Applications of Stack:</b><br/>
1. Expression evaluation and conversion (infix to postfix/prefix)<br/>
2. Function call management (call stack in programming)<br/>
3. Undo/Redo operations in text editors<br/>
4. Backtracking algorithms<br/>
5. Parenthesis matching<br/>
6. Browser history navigation<br/>
7. Memory management (recursion)<br/><br/>
<b>Infix to Postfix Conversion:</b><br/>
Expression: ((A+B)-C*D/E)*(H-I)*F+G<br/><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Symbol</b></td><td><b>Stack</b></td><td><b>Postfix</b></td></tr>
<tr><td>(</td><td>(</td><td></td></tr>
<tr><td>(</td><td>((</td><td></td></tr>
<tr><td>A</td><td>((</td><td>A</td></tr>
<tr><td>+</td><td>((+</td><td>A</td></tr>
<tr><td>B</td><td>((+</td><td>AB</td></tr>
<tr><td>)</td><td>(</td><td>AB+</td></tr>
<tr><td>-</td><td>(-</td><td>AB+</td></tr>
<tr><td>C</td><td>(-</td><td>AB+C</td></tr>
<tr><td>*</td><td>(-*</td><td>AB+C</td></tr>
<tr><td>D</td><td>(-*</td><td>AB+CD</td></tr>
<tr><td>/</td><td>(-/</td><td>AB+CD*</td></tr>
<tr><td>E</td><td>(-/</td><td>AB+CD*E</td></tr>
<tr><td>)</td><td></td><td>AB+CD*E/-</td></tr>
<tr><td>*</td><td>*</td><td>AB+CD*E/-</td></tr>
<tr><td>(</td><td>*(</td><td>AB+CD*E/-</td></tr>
<tr><td>H</td><td>*(</td><td>AB+CD*E/-H</td></tr>
<tr><td>-</td><td>*(-</td><td>AB+CD*E/-H</td></tr>
<tr><td>I</td><td>*(-</td><td>AB+CD*E/-HI</td></tr>
<tr><td>)</td><td>*</td><td>AB+CD*E/-HI-</td></tr>
<tr><td>*</td><td>*</td><td>AB+CD*E/-HI-*</td></tr>
<tr><td>F</td><td>*</td><td>AB+CD*E/-HI-*F</td></tr>
<tr><td>+</td><td>+</td><td>AB+CD*E/-HI-*F*</td></tr>
<tr><td>G</td><td>+</td><td>AB+CD*E/-HI-*F*G</td></tr>
<tr><td>End</td><td></td><td>AB+CD*E/-HI-*F*G+</td></tr>
</table><br/>
<b>Postfix Expression: AB+CD*E/-HI-*F*G+</b><br/><br/>
<b>Evaluation (A=4, B=2, C=4, D=3, E=8, F=2, G=3, H=5, I=1):</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Symbol</b></td><td><b>Operation</b></td><td><b>Stack</b></td></tr>
<tr><td>4</td><td>Push 4</td><td>4</td></tr>
<tr><td>2</td><td>Push 2</td><td>4, 2</td></tr>
<tr><td>+</td><td>4+2=6</td><td>6</td></tr>
<tr><td>4</td><td>Push 4</td><td>6, 4</td></tr>
<tr><td>3</td><td>Push 3</td><td>6, 4, 3</td></tr>
<tr><td>*</td><td>4*3=12</td><td>6, 12</td></tr>
<tr><td>8</td><td>Push 8</td><td>6, 12, 8</td></tr>
<tr><td>/</td><td>12/8=1.5</td><td>6, 1.5</td></tr>
<tr><td>-</td><td>6-1.5=4.5</td><td>4.5</td></tr>
<tr><td>5</td><td>Push 5</td><td>4.5, 5</td></tr>
<tr><td>1</td><td>Push 1</td><td>4.5, 5, 1</td></tr>
<tr><td>-</td><td>5-1=4</td><td>4.5, 4</td></tr>
<tr><td>*</td><td>4.5*4=18</td><td>18</td></tr>
<tr><td>2</td><td>Push 2</td><td>18, 2</td></tr>
<tr><td>*</td><td>18*2=36</td><td>36</td></tr>
<tr><td>3</td><td>Push 3</td><td>36, 3</td></tr>
<tr><td>+</td><td>36+3=39</td><td>39</td></tr>
</table><br/>
<b>Final Result = 39</b>""",
            },
            {
                "num": "10",
                "question": "What is double linked list? How does it differ from circular linked list? Write an algorithm or function to add a node at the beginning and end of double linked list.",
                "marks": "1+1+4+4",
                "answer": """<b>Doubly Linked List:</b> A doubly linked list is a type of linked list in which each node contains three parts: data, a pointer to the next node, and a pointer to the previous node. This allows traversal in both forward and backward directions.<br/><br/>
<b>Difference between Doubly Linked List and Circular Linked List:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>Doubly Linked List</b></td><td><b>Circular Linked List</b></td></tr>
<tr><td>Structure</td><td>Each node has next and prev pointers</td><td>Last node points back to first node</td></tr>
<tr><td>Traversal</td><td>Bidirectional (forward and backward)</td><td>Unidirectional or bidirectional depending on type</td></tr>
<tr><td>End condition</td><td>Last node's next is NULL</td><td>Last node's next points to head</td></tr>
<tr><td>Memory</td><td>Requires extra memory for prev pointer</td><td>No extra pointer needed</td></tr>
<tr><td>Applications</td><td>Browser history, undo functionality</td><td>Round-robin scheduling, multiplayer games</td></tr>
</table><br/><br/>
<b>Algorithm to Add Node at Beginning of Doubly Linked List:</b><br/>
<pre>
Algorithm INSERT_BEGINNING(head, data)
1. Create a new node NEW_NODE
2. NEW_NODE.data = data
3. NEW_NODE.prev = NULL
4. NEW_NODE.next = head
5. If head != NULL then
       head.prev = NEW_NODE
6. head = NEW_NODE
7. Exit
</pre><br/>
<b>Algorithm to Add Node at End of Doubly Linked List:</b><br/>
<pre>
Algorithm INSERT_END(head, data)
1. Create a new node NEW_NODE
2. NEW_NODE.data = data
3. NEW_NODE.next = NULL
4. If head == NULL then
       NEW_NODE.prev = NULL
       head = NEW_NODE
       Exit
5. Set TEMP = head
6. While TEMP.next != NULL do
       TEMP = TEMP.next
7. TEMP.next = NEW_NODE
8. NEW_NODE.prev = TEMP
9. Exit
</pre><br/>
<b>C Function Implementation:</b><br/>
<pre>
struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

void insertBeginning(struct Node** head, int data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    new_node->data = data;
    new_node->prev = NULL;
    new_node->next = *head;
    if (*head != NULL)
        (*head)->prev = new_node;
    *head = new_node;
}

void insertEnd(struct Node** head, int data) {
    struct Node* new_node = (struct Node*)malloc(sizeof(struct Node));
    struct Node* temp = *head;
    new_node->data = data;
    new_node->next = NULL;
    if (*head == NULL) {
        new_node->prev = NULL;
        *head = new_node;
        return;
    }
    while (temp->next != NULL)
        temp = temp->next;
    temp->next = new_node;
    new_node->prev = temp;
}
</pre>""",
            },
            {
                "num": "11",
                "question": "What is heap? Differentiate between min heap and max heap. Sort the following data in ascending order by heap sort method: 2, 9, 3, 12, 15, 8, 11.",
                "marks": "2+2+6",
                "answer": """<b>Heap:</b> A heap is a specialized tree-based data structure that satisfies the heap property. It is a complete binary tree where every level is fully filled except possibly the last level, which is filled from left to right. Heaps are commonly used to implement priority queues and in sorting algorithms like heap sort.<br/><br/>
<b>Difference between Min Heap and Max Heap:</b><br/>
<table border='1' cellpadding='4' cellspacing='0'>
<tr><td><b>Aspect</b></td><td><b>Min Heap</b></td><td><b>Max Heap</b></td></tr>
<tr><td>Property</td><td>Parent node is less than or equal to its children</td><td>Parent node is greater than or equal to its children</td></tr>
<tr><td>Root</td><td>Contains the minimum element</td><td>Contains the maximum element</td></tr>
<tr><td>Usage</td><td>Finding smallest element, Dijkstra's algorithm</td><td>Finding largest element, heap sort</td></tr>
<tr><td>Insertion</td><td>New element bubbled up if smaller than parent</td><td>New element bubbled up if larger than parent</td></tr>
<tr><td>Deletion</td><td>Remove root (min), replace with last, heapify down</td><td>Remove root (max), replace with last, heapify down</td></tr>
</table><br/><br/>
<b>Heap Sort in Ascending Order (using Max Heap):</b><br/>
Data: 2, 9, 3, 12, 15, 8, 11<br/><br/>
<b>Step 1: Build Max Heap</b><br/>
Initial array: [2, 9, 3, 12, 15, 8, 11]<br/>
Heapify from last non-leaf node (index 2, value 3):<br/>
• Heapify 3: children 8, 11 → swap 3 with 11 → [2, 9, 11, 12, 15, 8, 3]<br/>
• Heapify 9: children 12, 15 → swap 9 with 15 → [2, 15, 11, 12, 9, 8, 3]<br/>
• Heapify 2: children 15, 11 → swap 2 with 15 → [15, 2, 11, 12, 9, 8, 3]<br/>
  Now heapify 2: children 12, 9 → swap 2 with 12 → [15, 12, 11, 2, 9, 8, 3]<br/>
  Then heapify 2: children none (leaf) → done.<br/>
<b>Max Heap: [15, 12, 11, 2, 9, 8, 3]</b><br/><br/>
<b>Step 2: Heap Sort (extract elements one by one)</b><br/>
<table border='1' cellpadding='4'>
<tr><td><b>Step</b></td><td><b>Swap root with last</b></td><td><b>Heapify</b></td><td><b>Sorted</b></td></tr>
<tr><td>1</td><td>Swap 15 and 3 → [3,12,11,2,9,8,15]</td><td>Heapify [3,12,11,2,9,8] → [12,9,11,2,3,8]</td><td>[15]</td></tr>
<tr><td>2</td><td>Swap 12 and 8 → [8,9,11,2,3,12]</td><td>Heapify [8,9,11,2,3] → [11,9,8,2,3]</td><td>[12,15]</td></tr>
<tr><td>3</td><td>Swap 11 and 3 → [3,9,8,2,11]</td><td>Heapify [3,9,8,2] → [9,3,8,2]</td><td>[11,12,15]</td></tr>
<tr><td>4</td><td>Swap 9 and 2 → [2,3,8,9]</td><td>Heapify [2,3,8] → [8,3,2]</td><td>[9,11,12,15]</td></tr>
<tr><td>5</td><td>Swap 8 and 2 → [2,3,8]</td><td>Heapify [2,3] → [3,2]</td><td>[8,9,11,12,15]</td></tr>
<tr><td>6</td><td>Swap 3 and 2 → [2,3]</td><td>Heapify [2] → [2]</td><td>[3,8,9,11,12,15]</td></tr>
<tr><td>7</td><td>Only 2 left</td><td></td><td>[2,3,8,9,11,12,15]</td></tr>
</table><br/>
<b>Sorted Array (Ascending): [2, 3, 8, 9, 11, 12, 15]</b>""",
            },
        ]
    }
]

generate_answer_sheet("CACS201", "data-structures-algorithms", "Data Structures & Algorithms", 2020, "semester-3", CACS201_2020)
