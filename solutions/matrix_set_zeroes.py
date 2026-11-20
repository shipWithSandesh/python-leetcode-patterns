"""
Pattern: Matrix (in-place markers)
Problem: LeetCode 73 - Set Matrix Zeroes  [Medium]
Link: https://leetcode.com/problems/set-matrix-zeroes/

Question:
    If a cell is 0, set its entire row and column to 0, in place.

Intuition:
    Use the first row and first column as marker storage for which rows/columns to zero. Remember separately whether the first row/column themselves had a zero.

When to use this pattern:
    In-place matrix updates where you need O(1) extra space: reuse the input as scratch.

Complexity:
    Time O(mn), space O(1).
"""
from typing import List

def set_zeroes(matrix: List[List[int]]) -> None:
    m, n = len(matrix), len(matrix[0])
    first_row = any(matrix[0][j] == 0 for j in range(n))
    first_col = any(matrix[i][0] == 0 for i in range(m))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if first_row:
        for j in range(n):
            matrix[0][j] = 0
    if first_col:
        for i in range(m):
            matrix[i][0] = 0


if __name__ == "__main__":
    m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    set_zeroes(m)
    assert m == [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    m = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    set_zeroes(m)
    assert m == [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]
    m = [[1, 2]]
    set_zeroes(m)
    assert m == [[1, 2]]
    print("matrix_set_zeroes.py: all tests passed")
