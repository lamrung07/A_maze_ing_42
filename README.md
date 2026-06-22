*This project has been created as part of the 42 curriculum by ngulam, davileli.*

# 🌀 A-Maze-ing

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
make re       # Full recompile
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
- **Good learning value** — implementing DFS with backtracking reinforced stack-based thinking and recursion management in C.

Alternatives considered: Prim's algorithm (more uniform, less winding) and Kruskal's algorithm (good for visual variety), but DFS offered the best balance of simplicity and output quality for our scope.

---

## Reusable Code

The following modules were written to be project-agnostic and can be reused:

| Module | Location | Description |
|---|---|---|
| Config parser | `src/config/parser.c` | Reads key=value `.cfg` files into a struct. Drop it into any project that needs file-based config. |
| 2D grid allocator | `src/utils/grid.c` | Allocates, initialises, and frees a generic 2D `int` grid. Useful for any grid-based problem. |
| Stack (array-based) | `src/utils/stack.c` | A simple fixed-size stack used by the DFS. Can be reused for any iterative DFS/BFS. |
| Display helpers | `src/display/terminal.c` | Renders any 2D int grid to the terminal using box-drawing characters. |

To reuse a module, copy the `.c` and its corresponding `.h` into your project and include the header.

---

## Team & Project Management

### Team Members

| Name | Role |
|---|---|
| [Name 1] | Maze generation algorithm, config parser |
| [Name 2] | Solver, display layer (terminal + graphical) |
| [Name 3] | Makefile, testing, integration, documentation |

### Planning

**Initial plan (Week 1)**
- Day 1–2: Project setup, repo structure, Makefile, config parser
- Day 3–4: Grid data structure and terminal display
- Day 5–7: Generation algorithm

**Week 2**
- Day 1–3: Solver implementation
- Day 4–5: Graphical display (stretch goal)
- Day 6–7: Testing, edge cases, README

**How it evolved**
The config parser took longer than expected because we decided mid-way to support comments and blank lines, which required a small rewrite. We dropped the graphical display from the initial sprint and moved it to an optional advanced feature completed in the final two days.

### What worked well

- Splitting the project into clearly independent modules (grid, parser, algo, display) meant we rarely blocked each other.
- Daily 15-minute syncs on Discord kept everyone aligned without being time-consuming.
- Writing the config parser first meant both teammates could develop against a real config file immediately.

### What could be improved

- We underestimated the solver complexity. More upfront design time on that module would have saved debugging time.
- Better commit message discipline early on would have made the git log more useful for tracing bugs.

### Tools used

| Tool | Purpose |
|---|---|
| Git / GitHub | Version control and code review via pull requests |
| Discord | Daily standups and async communication |
| Valgrind | Memory leak detection |
| GDB | Debugging |
| VS Code + clangd | IDE with C intellisense |
| Notion | Task tracking and planning board |

---

## Advanced Features *(if implemented)*

### Multiple Algorithms

If compiled with `ALGO=prim`, the program uses **Prim's algorithm** instead of DFS:

```bash
make ALGO=prim
./amazeing configs/default.cfg
```

| Algorithm | Flag | Characteristics |
|---|---|---|
| Recursive Backtracker | `recursive` (default) | Long corridors, winding paths |
| Prim's | `prim` | More uniform texture, shorter dead ends |

### Display Options

Pass `display = graphical` in your config to enable the MLX graphical window. Requires MLX to be installed.

---

## Resources

### Documentation & References

- [Maze generation algorithms — Jamis Buck's blog](https://weblog.jamisbuck.org/2011/2/7/maze-generation-algorithm-recap) — Excellent visual breakdown of multiple generation algorithms.
- [Depth-First Search — Wikipedia](https://en.wikipedia.org/wiki/Depth-first_search)
- [42 Project Subject — A-Maze-ing](https://projects.intra.42.fr) *(internal link)*
- [MiniLibX documentation](https://harm-smits.github.io/42docs/libs/minilibx) — Used for graphical display.

### AI Usage

AI (Claude) was used during this project for the following tasks:

- **Code structure advice** — We asked for feedback on how to split responsibilities between files before starting to code.
- **Debugging** — When stuck on a segfault in the backtracking loop, we pasted the relevant function and asked for a review. The AI spotted an off-by-one error in the bounds check.
- **README drafting** — The initial structure of this README was generated by AI and then edited and completed by the team.
- **No code was copy-pasted directly** — All AI-suggested snippets were rewritten and adapted by hand to fit our data structures and style.