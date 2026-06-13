#!/usr/bin/env python3

# -----------------------------------------------
# MazeGenerator class
# -----------------------------------------------

class MazeGenerator:

    def __init__(
        self,
        width: int,
        height: int,
        entry: dict[str, int],
        exit: dict[str, int],
        perfect: bool,
        pattern: str,
        seed: Optional[int]
    ) -> None:

    self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.pattern = pattern or '42'
        self.seed = seed

    

    