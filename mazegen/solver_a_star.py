#!/usr/bin/env python3
from maze_generator import MazeGenerator
from collections import deque
from constance import A_STAR_DIRS, OPEN_DIRS

class MazeSolverA_star:
    def __init__(
        self,
        width: int = 10,
        height: int = 10,
        entry = (0, 0),
        exit = (9, 9)
        ) -> None:
        # self.maze: grid of int from 1-15
        self.maze = MazeGenerator(width,height).get_maze()
        self.entry = entry
        self.exit = exit
        self.width = width
        self.height = height
        self.solution_path: str = ""

    def solver_a_star(self):
        """
        Add path contain 'N','E','S','W' to self.solution_path
        which represent the shortest path from entry to exit
        """
        entry_x, entry_y = self.entry
        exit_x, exit_y = self.exit
        entry = (entry_x, entry_y)
        exit = (exit_x, exit_y)
        def h(current: set[int, int] , target: set[int, int]) -> int:
            """Calculate Manhattan distance from current to target node"""
            return abs(current[0] - target[0]) + abs(current[1] - target[1])
        # open_list: a list of (f, g, position)
        open_list: list[int, int, set[int, int]] = [(h(entry, exit), 0, entry)]
        g_cost = {entry: 0}
        came_from = {}
        directions = OPEN_DIRS
        pre_directions = A_STAR_DIRS
        visited: set[tuple[int, int]] = set()
        visited.add((entry_x, entry_y))

        while open_list:
            f, g, current = min(open_list, key=lambda x: x[0])
            open_list.remove((f, g, current))

            if current == exit:
                path = []
                while current in came_from:
                    previous = came_from[current]
                    n_x = current[0] - previous[0]
                    n_y = current[1] - previous[1]
                    move = pre_directions[(n_x, n_y)]
                    path.append(move)
                    current = previous
                # path.append(entry)
                return path[::-1]

            # Check all open neighbor of current cell
            for dir, d_x, d_y, cur in directions:
                current_val = self.maze[current[1]][current[0]]
                neighbor_x = current[0] + d_x
                neighbor_y = current[1] + d_y
                neighbor = (neighbor_x, neighbor_y)
                # Ingest neighbor cell if there is no wall
                if (current_val & cur == 0
                and (neighbor_x, neighbor_y) not in visited):
                    new_g = g + 1
                    if new_g < g_cost.get(neighbor, float('inf')):
                        g_cost[neighbor] = new_g
                        came_from[neighbor] = current
                        f = new_g + h(neighbor, exit)
                        open_list.append((f, new_g, neighbor))

if __name__ == "__main__":
    solver = MazeSolverA_star()
    print(solver.solver_a_star())