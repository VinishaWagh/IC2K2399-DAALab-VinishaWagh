# Lab Task 1

## Part 1. Trace It Yourself

Input: [8, 3, 15, 6, 2]  
Output: Largest Number = 15, Sorted Array = [2, 3, 6, 8, 15]  
Comparisons made: 4  

Dry Run:  
i = 1, A[i] = 3, max = 8, comparisons = 1  
i = 2, A[i] = 15, max = 15, comparisons = 2  
i = 3, A[i] = 6, max = 15, comparisons = 3  
i = 4, A[i] = 2, max = 15, comparisons = 4  

Sorting method used: Bubble Sort  
Sorting steps:  
Step 1: Swap 8 and 3 -> [3, 8, 15, 6, 2]  
Step 2: Compare 8 and 15 (No Swap) -> [3, 8, 15, 6, 2]  
Step 3: Swap 15 and 6 -> [3, 8, 6, 15, 2]  
Step 4: Swap 15 and 2 -> [3, 8, 6, 2, 15]  
Step 5: Compare 3 and 8 (No Swap) -> [3, 8, 6, 2, 15]  
Step 6: Swap 8 and 6 -> [3, 6, 8, 2, 15]  
Step 7: Swap 8 and 2 -> [3, 6, 2, 8, 15]  
Step 8: Compare 3 and 6 (No Swap) -> [3, 6, 2, 8, 15]  
Step 9: Swap 6 and 2 -> [3, 2, 6, 8, 15]  
Step 10: Swap 3 and 2 -> [2, 3, 6, 8, 15]  

Explanation:  
The code iterates through the array element by element, maintaining the maximum value seen so far and updating it whenever a larger element is found. It must inspect every element because any unexamined element could be larger than the current maximum. Searching maximum effort grows proportionally (O(n)), while Bubble Sort effort grows quadratically/explosively (O(n^2)).

## Part 2. Stack or Queue

Stack order: Task5, Task4, Task3, Task2, Task1  
Queue order: Task1, Task2, Task3, Task4, Task5  
Printer should use: Queue (FIFO)  
Reason: A printer needs First-Come, First-Served order to process print jobs fairly as they arrive.  

Dry Run:  
Stack (LIFO): push Task1, Task2, Task3, Task4, Task5 then pop in reverse  
Queue (FIFO): enqueue Task1 to Task5 then dequeue in same order  

Explanation:  
A printer requires tasks to be executed in arrival sequence so earlier submitters do not suffer indefinite delays. The Queue data structure guarantees First-In, First-Out (FIFO) processing, whereas a Stack would reverse the order (LIFO). If the input size grew 100 times, queue operations would grow proportionally (O(n)).

## Part 3. Build a Small Tree

```
         [ Subjects ]
          /        \
     [Math]        [Science]
     /    \         /     \
[Algebra] [Geometry] [Physics] [Chemistry]
```

Dry Run:  
Level 0: Math, Science  
Level 1 under Math: Algebra, Geometry  
Level 1 under Science: Physics, Chemistry  
Level order traversal: Math, Science, Algebra, Geometry, Physics, Chemistry  

Explanation:  
Level order traversal visits every node at depth 0, then depth 1, moving horizontally across each level. Using a queue-based Breadth-First Search (BFS), child nodes are enqueued as parents are processed, ensuring level-by-level output. If input size grew 100 times, tree traversal effort would grow proportionally (O(n)).

## Part 4. Count the Steps

Single loop runs: 5 times  
Nested loop total prints: 25 times  

Dry Run:  
Single loop, i = 1 to 5, prints 5 times  
Nested loop, i = 1 to 5 and j = 1 to 5, inner print runs 5 times for each i, total 25 times  

For n = 10:  
Single loop runs: 10 times  
Nested loop runs: 100 times  

For n = 20:  
Single loop runs: 20 times  

Explanation:  
The single loop scales linearly because the print operation executes once per iteration, causing effort to grow proportionally (O(n)). The nested loop runs n times inside another n-iteration loop, yielding n^2 total executions, which causes effort to grow quadratically/explosively (O(n^2)) as n increases.

## Acceptance Criteria Summary

| Part | Input | Output | Data Structure Used | 100x Growth Behavior | Explanation |
|---|---|---|---|---|---|
| Part 1 | [8, 3, 15, 6, 2] | Max: 15, Sorted: [2, 3, 6, 8, 15] | Array | Max: **Proportionally** (100x); Sort: **Explosively** (10,000x) | Linear scan vs quadratic bubble sort comparisons |
| Part 2 | Task1 to Task5 | Stack: Task5..Task1, Queue: Task1..Task5 | Stack (LIFO), Queue (FIFO) | **Proportionally** (100x) | Each element is pushed/enqueued and popped/dequeued once |
| Part 3 | Subject tree structure | Order: Math, Science, Algebra, Geometry, Physics, Chemistry | Tree, Queue | **Proportionally** (100x) | Breadth-First Search visits every node exactly once |
| Part 4 | n = 5, n = 10, n = 20 | Single: 5, 10, 20; Nested: 25, 100 | Integers / Loop Counters | Single: **Proportionally** (100x); Nested: **Explosively** (10,000x) | Single loop is O(n), nested loop is O(n^2) |

## How to run (Java)

Compile all Java files:
```bash
javac Part1Trace.java Part2StackQueue.java Part3Tree.java Part4Complexity.java
```

Run each part:
```bash
java Part1Trace
java Part2StackQueue
java Part3Tree
java Part4Complexity
```
