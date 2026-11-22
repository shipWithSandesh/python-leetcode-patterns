"""
Pattern: Dynamic Programming (2D)
Problem: LeetCode 62 - Unique Paths  [Medium]
Link: https://leetcode.com/problems/unique-paths/

Question:
A robot moves only right or down on an m x n grid. Count paths from top-left to bottom-right.

Intuition:
Each cell's count is the sum of the cell above and the cell to the left. A single rolling row is enough.

When to use this pattern:
Grid counting problems with restricted moves.

Complexity:
Time O(m*n); space O(n).
"""

def unique_paths(m: int, n: int) -> int:
    row = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            row[j] += row[j - 1]
    return row[-1]


if __name__ == "__main__":
    assert unique_paths(3, 7) == 28
    assert unique_paths(3, 2) == 3
    assert unique_paths(1, 1) == 1
    assert unique_paths(10, 10) == 48620
    print("dynamic_programming_2d_unique_paths.py: all tests passed")
