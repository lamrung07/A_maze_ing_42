*This project has been created as part of the 42 curriculum by ngulam, davileli.*

# 🧩 A-Maze-ing

> A maze generator and solver built in Python as part of the 42 curriculum.

---

## Description

A-Maze-ing is a program that procedurally generates mazes and solves them.
The goal of this project is to explore maze generation algorithms, practice modular Python programming, and manage a collaborative development workflow.

The program takes a configuration file as input, generates a maze according to the specified parameters, and displays it — along with its solution — in the terminal (or via a graphical interface, if enabled).

---

## Instructions

### Requirements

- Written in Python3 or later
- Must adhere to flake8 coding standard and all function must pass mypy for type checking
- All errors and leaks must be handled. Include docstrings in functions and classes following PEP 257
- Include a Makefile to automate common tasks
- *(Optional)* MLX or another display library if graphical output is enabled

### Compilation

```bash
make install  # Install project dependencies 
make run      # Execute the main script
```

### Execution

```bash
python3 a_maze_ing.py config.txt
```

### Cleanup

```bash
make clean    # Remove temporary files or caches
```

---

## Configuration File

The program reads a `config.txt` configuration file with the following structure:

```
# A-Maze-ing config file

width       = 25        # Number of columns (must be odd)
height      = 15        # Number of rows (must be odd)
start       = 0,0       # Entry point (col,row)
end         = 24,14     # Exit point (col,row)
```

| Key         | Type    | Description                                 |
|-------------|---------|---------------------------------------------|
| `width`     | int     | Maze width in cells (should be odd)         |
| `height`    | int     | Maze height in cells (should be odd)        |
| `start`     | col,row | Coordinates of the maze entrance            |
| `end`       | col,row | Coordinates of the maze exit                |

---

## Maze Generation Algorithm

**Algorithm chosen:** Recursive Backtracker (Depth-First Search)

### How it works

Starting from a random cell, the algorithm:
1. Marks the current cell as visited.
2. Randomly picks an unvisited neighbouring cell.
3. Removes the wall between them and moves to that neighbour.
4. If no unvisited neighbours exist, it backtracks to the previous cell.
5. Repeats until every cell has been visited.

### Why we chose it

- **Simplicity** — the logic maps naturally to a recursive function, making the code easy to reason about and debug.
- **Perfect mazes** — it always produces a perfect maze (exactly one path between any two cells), which guarantees the solver has a unique solution.
- **Visually appealing** — the resulting mazes tend to have long, winding corridors that look good in a terminal.
- **Good learning value** — implementing DFS with backtracking reinforced stack-based thinking and recursion management in Python.

Alternatives considered: Prim's algorithm (more uniform, less winding) and Kruskal's algorithm (good for visual variety).

---

## Reusable Code



---

## Team & Project Management

### Team Members

| Name | Role |
|---|---|
| [ngulam]   | Maze generation algorithm, config parser, solver |
| [davileli] | Solver, display layer (terminal + graphical) |
| [ngulam, davileli]   | Makefile, testing, integration, documentation |

### Planning

**Initial plan (Week 1)**
- Day 1–2: Project setup, README, repo structure, Makefile, config parser
- Day 3–4: Grid data structure and terminal display
- Day 5–7: Generation algorithm

**Week 2**
- Day 1–3: Solver implementation
- Day 4–5: Graphical display (stretch goal)
- Day 6–7: Testing, edge cases, README


### What worked well

### What could be improved

### Tools used

| Tool | Purpose |
|---|---|
| Git / GitHub | Version control and code review via pull requests |
| VS Code | IDE |

---


### Display Options

---

## Resources

### Documentation & References


### AI Usage

AI (Claude) was used during this project for the following tasks:
