from typing import List, Tuple
from queue import SimpleQueue

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        current_color = image[sr][sc]
        if current_color == color:
            return image
        max_row = len(image)
        max_col = len(image[0])
        def adjacent(r: int, c: int) -> List[Tuple[int, int]]:
            results = []
            if r - 1 >= 0:
                results.append((r - 1, c))
            if c - 1 >= 0:
                results.append((r, c - 1))
            if r + 1 < max_row:
                results.append((r + 1, c))
            if c + 1 < max_col:
                results.append((r, c + 1))
            return results

        q: "SimpleQueue[Tuple[int, int]]" = SimpleQueue()
        q.put((sr, sc))
        while not q.empty():
            r, c = q.get()
            image[r][c] = color
            for adj_row, adj_col in adjacent(r, c):
                if image[adj_row][adj_col] == current_color:
                    q.put((adj_row, adj_col))
        return image
