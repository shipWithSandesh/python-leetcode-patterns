"""
Pattern: Depth-First Search (flood fill on a grid)
Problem: LeetCode 200 - Number of Islands  [Medium]
Link: https://leetcode.com/problems/number-of-islands/

Question:
    Given a 2D grid of "1" (land) and "0" (water), count the islands.
    An island is land connected horizontally or vertically.

Intuition:
    Scan every cell. When you hit unvisited land, that's a new island:
    count it, then DFS from it and "sink" every connected land cell
    (mark it "0") so it is never counted again.
    An explicit stack avoids Python's recursion limit on big grids.

When to use this pattern:
    Connected components, flood fill, max area of island,
    surrounded regions, path existence, cycle detection in graphs.

Complexity:
    Time  O(rows * cols)
    Space O(rows * cols) worst case for the stack
"""
from typing import List


def num_islands(grid: List[List[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue
            islands += 1
            stack = [(r, c)]
            grid[r][c] = "0"
            while stack:
                cr, cc = stack.pop()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        stack.append((nr, nc))
    return islands


if __name__ == "__main__":
    g1 = [list("11110"), list("11010"), list("11000"), list("00000")]
    g2 = [list("11000"), list("11000"), list("00100"), list("00011")]
    assert num_islands(g1) == 1
    assert num_islands(g2) == 3
    print("dfs: all tests passed")
