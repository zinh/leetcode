from typing import List, Tuple
from queue import LifoQueue

Grid = List[List[int]]
Coor = Tuple[int, int]
def print_grid(grid: Grid):
    for row in grid:
        print(row)

class Solution:
    def maxAreaOfIsland(self, grid: Grid) -> int:
        max_row, max_col = len(grid), len(grid[0])
        def adjacent(c: Coor) -> List[Coor]:
            row, col = c
            results: List[Coor] = []
            if row - 1 >= 0:
                results.append((row - 1, col))
            if row + 1 < max_row:
                results.append((row + 1, col))
            if col - 1 >= 0:
                results.append((row, col - 1))
            if col + 1 < max_col:
                results.append((row, col + 1))
            return results
        current_region = 2
        h = {}
        print_grid(grid)
        for row_id, row in enumerate(grid):
            for col_id, cell in enumerate(row):
                if cell == 1:
                    q = set()
                    q.add((row_id, col_id))
                    while len(q) > 0: 
                        current_row, current_col = q.pop()
                        # print(current_region, (current_row, current_col))
                        for adj_row, adj_col in adjacent((current_row, current_col)):
                            if grid[adj_row][adj_col] == 1:
                                q.add((adj_row,adj_col))
                        grid[current_row][current_col] = current_region
                        if current_region in h:
                            h[current_region] += 1
                        else:
                            h[current_region] = 1
                    current_region += 1
        if len(h) == 0:
            return 0
        return max(h.values())
