#!/usr/bin/env python3
from maze_generator import MazeGenerator
from collections import deque
from constance import OPEN_DIRS

class MazeSolver:
    def __init__(
        self,
        entry = (0, 0),
        exit = (14, 14)
        ) -> None:
        self.maze = MazeGenerator(20,20).get_maze()
        self.entry = entry
        self.exit = exit
        self.solution_path: list[str] = []
    
    def solver_bfs(self):
        entry_x, entry_y = self.entry
        exit_x, exit_y = self.exit
        queue: deque[tuple[str, int, int]] = (("", entry_x, entry_y))
        visited: set[tuple[int, int]] = {(entry_x, entry_y)}
        directions = OPEN_DIRS

        # Loop through maze until its empty
        while queue:
            move, current_x, current_y = queue[0]
            node = queue.popleft()
            print(node)

            # Check if current cell is exit cell
            if (current_x == exit_x and current_y == exit_y):
                self.solution_path.append(move)
                break
            
            # Append the direction of first element in deque
            self.solution_path.append(move)

            # Check all open neighbor of current cell
            for dir, d_x, d_y, cur in directions:
                current_val = self.maze[current_y][current_x]
                neighbor_x = current_x + d_x
                neighbor_y = current_y + d_y
                if (current_val & cur == 0 
                and (neighbor_x, neighbor_y) not in visited):
                    queue.append((dir, neighbor_x, neighbor_y))
                    visited.add((neighbor_x, neighbor_y))

if __name__ == "__main__":
    Maze = MazeSolver()
    Maze.solver_bfs
    print(Maze.solution_path)


