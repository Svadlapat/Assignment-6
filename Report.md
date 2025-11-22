**Assignment 6 — Medians & Order Statistics + Elementary Data Structures**

Table of Contents

1.Introduction

2.Part 1 — Selection Algorithms
2.1 Problem Statement
2.2 Randomized Selection (Quickselect)
2.3 Deterministic Selection (Median of Medians)
2.4 Time Complexity Analysis
2.5 Space Complexity
2.6 Empirical Evaluation
2.7 Discussion of Results

3.Part 2 — Elementary Data Structures
3.1 Array
3.2 Stack
3.3 Queue
3.4 Singly Linked List
3.5 Optional: Rooted Tree
3.6 Performance Analysis
3.7 Applications

4.Conclusion

1. Introduction

This assignment focuses on two major concepts in algorithm design and data structures:
1. Order Statistics (k-th smallest element):
Implementing two efficient selection algorithms:
Randomized Quickselect (expected O(n))
Deterministic Median of Medians (worst-case O(n))

2. Elementary Data Structures:
Implementing foundational data structures from scratch:
Arrays, Stacks, Queues, Singly Linked Lists, and Trees
Analyzing their time complexity and practical applications

This report covers implementation details, complexity analysis, empirical evaluation, and real-world applications.

2. Part 1 — Selection Algorithms
2.1 Problem Statement

Given an unsorted array of size n, the task is to find the k-th smallest element.
Two algorithms were implemented:
Randomized Quickselect — expected linear time
Deterministic Median of Medians — guaranteed linear time

Both are in selection.py.

2.2 Randomized Selection (Quickselect)
Overview:
Randomized Quickselect is a selection algorithm based on the QuickSort partition procedure.

Algorithm Steps:
1.Pick a random pivot.
2.Partition the array:
All elements < pivot on the left
All elements > pivot on the right

Recursively process the partition containing the k-th smallest element.

Advantages:
Extremely fast in practice
Very small constant factors
Simple implementation

Disadvantage:
Worst case is O(n²) (when pivot repeatedly splits poorly)
However, the expected time remains O(n).

2.3 Deterministic Selection (Median of Medians)
Overview:
Median of Medians finds a “good pivot” deterministically, guaranteeing linear time.

Algorithm Steps:
Divide the array into groups of 5.
Compute the median of each group.
Recursively find the median of these medians — this becomes the pivot.
Partition the array using this pivot.
Recursively solve the correct partition.

Why Groups of 5?
Groups of 5 guarantee that:
At least 30% of elements are larger than pivot
At least 30% are smaller

Ensures good splitting → T(n) = T(n/5) + T(7n/10) + O(n)

Solution: T(n) = O(n) worst case.

Advantages:
Worst-case linear time
Immune to adversarial input

Disadvantages:
Very high constant factors
Slower in practice than Quickselect
More complex implementation

2.4 Time Complexity Analysis
| Algorithm              | Best Case | Average Case | Worst Case | Notes                  |
| ---------------------- | --------- | ------------ | ---------- | ---------------------- |
| Randomized Quickselect | O(n)      | **O(n)**     | O(n²)      | Fastest in practice    |
| Median of Medians      | O(n)      | **O(n)**     | **O(n)**   | Guaranteed linear time |

1.Why Random Quickselect is Expected O(n)?
Expected recurrence:
T(n) = T(n/2) + O(n)
Solution: O(n).

2.Why Median of Medians is Worst-Case O(n)
Recurrence:
T(n) ≤ T(n/5) + T(7n/10) + O(n)
Solves to O(n).

2.5 Space Complexity:
| Algorithm              | Extra Space | Notes                                   |
| ---------------------- | ----------- | --------------------------------------- |
| Randomized Quickselect | O(1)        | In-place, iterative implementation      |
| Median of Medians      | O(1)        | Only pivot selection uses some overhead |

Both implementations avoid recursion by using loops → constant space.

2.6 Empirical Evaluation

The provided script experiments.py runs timing experiments for:
Input sizes: 1,000 – 20,000

Distributions:
Random
Sorted
Reverse-sorted
Few unique values
Repeated trials per input
Always selects the median (k = n//2)
Measured Metrics
Runtime of Randomized Quickselect
Runtime of Deterministic Median of Medians

Data saved in:
results/selection_results.csv

2.7 Discussion of Results
Observations
Randomized Quickselect consistently outperforms deterministic selection.
Smaller constant factor
Simpler computations
Faster on all common distributions
Deterministic Median of Medians is slower
Group-of-five medians incur large overhead
Many extra comparisons and passes
On worst-case adversarial inputs (crafted), Quickselect may slow down.
But such cases are statistically rare

Conclusion for Part 1
Randomized Quickselect is preferred in practice.
Median of medians is preferred when worst-case guarantees are needed, such as:
Real-time systems
Cryptographic systems
Environments where adversarial input is possible

3. Part 2 — Elementary Data Structures

This part required implementing basic data structures from scratch.
All implementations are in datastructures.py.

3.1 Array
Features Implemented:
Insert
Delete
Access
Append

Complexity
| Operation | Time           |
| --------- | -------------- |
| Access    | O(1)           |
| Insert    | O(n)           |
| Delete    | O(n)           |
| Append    | Amortized O(1) |

3.2 Stack (Array-Based)

Operations:
push()
pop()
top()
is_empty()

Complexity
| Operation | Time |
| --------- | ---- |
| Push      | O(1) |
| Pop       | O(1) |
| Top       | O(1) |

3.3 Queue (Array-Based)

Operations:
enqueue()
dequeue()
front()

Complexity
| Operation | Time |
| --------- | ---- |
| Enqueue   | O(1) |
| Dequeue   | O(n) |
| Front     | O(1) |

3.4 Singly Linked List

Supports:
Insert front
Insert back
Delete front
Find
Traverse

Complexity
| Operation    | Time |
| ------------ | ---- |
| Insert front | O(1) |
| Insert back  | O(n) |
| Delete front | O(1) |
| Find         | O(n) |

3.5 Optional: Rooted Tree

A simple tree node with multiple children:
value
children list
add_child()

Used to represent hierarchical structures.

3.6 Performance Comparison: Arrays vs Linked Lists
| Feature       | Array          | Linked List                 |
| ------------- | -------------- | --------------------------- |
| Random access | O(1)           | O(n)                        |
| Insert front  | O(n)           | O(1)                        |
| Insert back   | Amortized O(1) | O(n) (without tail pointer) |
| Memory usage  | Compact        | Overhead (pointers)         |

3.7 Real-World Applications
Arrays:
Indexing-heavy applications
Image processing
Machine learning (tensors)

Stacks:
Function calls / Recursion
Undo-redo systems
Parsing (expression evaluation)

Queues:
Scheduling
BFS graph traversal
OS process queues

Linked Lists:
When frequent insertions/deletions occur
Real-time memory allocation systems
Implementing adjacency lists

Trees:
File systems
XML/HTML parsing
AI decision trees

4. Conclusion

This assignment provided comprehensive hands-on experience with:

Selection Algorithms:
Randomized Quickselect (fastest in practice)
Deterministic Median of Medians (provably linear)
Foundational Data Structures
Arrays, Stacks, Queues, Linked Lists, Trees

Implemented both algorithmic and data structure concepts, analyzed their performance, and compared empirical results. This assignment builds a strong foundation for advanced algorithm design, competitive programming, and real-world application development.

