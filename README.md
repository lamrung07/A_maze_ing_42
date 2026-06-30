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
```

### Execution

```bash
make run      # Execute the main script
```

### Debug

```bash
make debug    # Debug with pdb 
```

### Cleanup

```bash
make clean    # Remove temporary files or caches
```

### Cleanup

```bash
make lint    # Runs static analysis flake8 and mypy
```

---

## Configuration File

The program reads a `config.txt` configuration file with the following structure:

```
# A-Maze-ing config file

width       = 25                # Number of columns (must be odd)
height      = 15                # Number of rows (must be odd)
entry       = 0,0               # Entry point (col,row)
exit        = 24,14             # Exit point (col,row)
seed        = 3,5               # Point where maze creation start (col, row)
output_file = output_maze.txt   # Output file name
perfect     = True              # Maze is perfect or not
```

| Key         | Type    | Description                                 |
|-------------|---------|---------------------------------------------|
| `width`     | int     | Maze width in cells (should be odd)         |
| `height`    | int     | Maze height in cells (should be odd)        |
| `start`     |(int,int)| Coordinates of the maze entrance            |
| `exit`      |(int,int)| Coordinates of the maze exit                |
| `seed`      |(int,int)| Coordinates of the maze seed                |
| `perfect`   | boolean | Maze perfection                             |

---

## Maze Generation Algorithm

**Algorithm chosen:** Recursive Backtracker (Depth-First Search)

### How it works

Starting from a random cell (or a seed), the algorithm:
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
The `mazegen` module is decoupled from the CLI entry point (`a_maze_ing.py`) and can be reused independently in other projects. It exposes maze generation as an importable component rather than tying it to this specific script.

Key points:

- **Seed-based & size-based reproducibility**: MazeGenerator class in maze_generator accepts a `seed`, `height`, `width`, ...  parameter. Passing the same seed always produces the identical maze layout, making results deterministic and easy to test, debug, or share.

```python
  from mazegen.maze_generator import MazeGenerator

  maze = MazeGenerator(width=20, height=20 ...)
```
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

- The maze generation algorithm works well and produces correct, reliable results.
- The core algorithms are solid and perform as expected.
- Teamwork was effective, with good communication throughout the project.
- The project workflow is well structured, making collaboration easier.

### What could be improved

- The display/visualization part of the project needs improvement.
- The maze solving algorithm could be optimized or refined further.
- Gitflow was not well utilized.

### Tools used

| Tool | Purpose |
|---|---|
| Git / GitHub | Version control and code review via pull requests |
| VS Code | IDE |

---


### Display Options

- The maze was displayed by the output in hexdeximal form of the grid
- The path solution was displayed by the string which represent the 
sollution from entry to exit in the maze (EX: NSESWSWWN...)
- We all use ASCII characters to display them, this can be improved also
by using some graphical tools    
---

## Resources

### Documentation & References
- Geekforgeek & W3Schools: Python systax
- Artificial Intelligence Search Problem: Solve Maze using Breadth First Search (BFS) Algorithm (Medium, Luthfisauqi)
- Exploring the Depths: Solving Mazes with A* Search Algorithm (Medium, Matteo Tosato)
- Youtube: freeCodeCamp, Tech with Tim, Linh Ei 
- Github: krameraad, Ceren Kurt

### AI Usage

AI (Claude) was used during this project for the following tasks:
- Structure and design the overall project
- Design workflow and tasks to accomplish the project
- Create test and fix bugs during coding part
- Find related ressources
