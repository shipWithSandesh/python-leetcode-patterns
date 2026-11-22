"""
Pattern: DFS (grid)
Problem: LeetCode 695 - Max Area of Island  [Medium]
Link: https://leetcode.com/problems/max-area-of-island/

Question:
Given a binary grid, return the largest area of 4-connected 1s.

Intuition:
Scan cells; on an unvisited land cell run DFS, sinking cells as visited and counting them. Track the max.

When to use this pattern:
Connected components on a grid.

Complexity:
Time O(m*n); space O(m*n) recursion worst case.
"""

from typing import List


def max_area_of_island(grid: List[List[int]]) -> int:
    g = [r[:] for r in grid]
    rows, cols = len(g), len(g[0]) if g else 0

    def dfs(r: int, c: int) -> int:
        if r < 0 or c < 0 or r >= rows or c >= cols or g[r][c] != 1:
            return 0
        g[r][c] = 0
        return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

    return max((dfs(r, c) for r in range(rows) for c in range(cols)), default=0)


if __name__ == "__main__":
    assert max_area_of_island([[0, 0, 0, 0, 0, 0, 0, 0]]) == 0
    assert max_area_of_island([[1, 1, 0], [0, 1, 0], [1, 0, 1]]) == 3
    assert max_area_of_island([[1]]) == 1
    assert max_area_of_island([]) == 0
    print("dfs_max_area_of_island.py: all tests passed")
