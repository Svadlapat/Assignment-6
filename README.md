# Assignment 6 — Medians & Order Statistics + Elementary Data Structures

This repository contains the complete implementation, analysis, and experimental evaluation for **Assignment 6**, which covers:

1. **Selection Algorithms (Order Statistics)**
   - Randomized Quickselect — Expected O(n)
   - Deterministic Median of Medians — Worst-case O(n)
   - Empirical performance comparison

2. **Elementary Data Structures**
   - Arrays
   - Stacks
   - Queues
   - Singly Linked Lists
   - Optional Tree Node implementation

---

## 📁 Repository Structure
Assignment-6/
 ├── selection.py # Deterministic and randomized selection algorithms
 ├── datastructures.py # Implementations of all required data structures
 ├── experiments.py # Script to benchmark both selection algorithms
 └── results/ # Auto-generated folder to store CSV results
 ├── REPORT.md # Detailed theoretical and empirical analysis
 └── README.md # Instructions and documentation (you are here)

 Instruction to execution:
 **A. Test selection algorithms**
 Run the following to check that the selection algorithms work:

```bash
python selection.py
```
**B. Test data structures**
This performs several small sanity checks for Arrays, Stack, Queue, and Linked List.

```bash
python datastructures.py
```
**C. Running Experiments (Empirical Analysis)**

To generate timing data comparing:
Randomized Quickselect
Deterministic Median of Medians

```bash
python experiments.py
```
This will produce:
results/selection_results.csv

