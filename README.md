# Missionaries and Cannibals Game 

##  Overview

This project solves the classic **Missionaries and Cannibals problem** using Artificial Intelligence search algorithms.
It provides a graphical user interface (GUI) built with **Tkinter** to visualize the solution step by step.

---

##  Problem Description

Three missionaries and three cannibals must cross a river using a boat that can carry at most two people.

### Constraints:

* The boat cannot carry more than 2 people.
* Cannibals can never outnumber missionaries on either side (unless missionaries are 0).

---

##  Objective

Move all missionaries and cannibals from the left bank to the right bank safely.

---

##  Algorithm Used

This project uses:

* **A* Search Algorithm**

### A* Formula:

f(n) = g(n) + h(n)

* g(n): Cost so far (number of steps)
* h(n): Estimated cost (remaining missionaries + cannibals)

---

##  Features

* Interactive GUI using Tkinter
* Step-by-step visualization
* Valid state checking
* Optimal solution using A*

---

##  Project Structure

```
project/
│── main.py
│── README.md
```

---

##  How to Run

### Requirements:

* Python 3.x

### Run:

```bash
python main.py
```

---

##  How to Use

* Click **Next Step** to move through the solution
* Watch how the algorithm reaches the goal safely

---

##  Example Output

* Displays missionaries (M) and cannibals (C)
* Shows boat movement
* Ends with "Goal Reached!"

---

##  Concepts Covered

* State Space Search
* A* Algorithm
* Heuristic Functions
* AI Problem Solving

---

##  Future Improvements

* Add BFS and DFS for comparison
* Auto-play animation
* Performance metrics (time, nodes explored)
* Web version using Streamlit

---

##  Author

#Ahmed Bissar
#Ahmed saad
#Ahmed Abbas
