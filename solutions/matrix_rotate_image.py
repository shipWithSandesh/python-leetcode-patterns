"""
Pattern: Matrix (in-place transform)
Problem: LeetCode 48 - Rotate Image  [Medium]
Link: https://leetcode.com/problems/rotate-image/

Question:
    Rotate an n x n matrix 90 degrees clockwise in place.

Intuition:
    Clockwise rotation = transpose, then reverse every row. Both steps are in place.

When to use this pattern:
    Matrix rearrangements that must be in place; compose simple transforms.

Complexity:
    Time O(n^2), space O(1).
"""
from typing import List

def rotate(matrix: List[List[int]]) -> None:
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()


if __name__ == "__main__":
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate(m)
    assert m == [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    m = [[1, 2], [3, 4]]
    rotate(m)
    assert m == [[3, 1], [4, 2]]
    m = [[1]]
    rotate(m)
    assert m == [[1]]
    print("matrix_rotate_image.py: all tests passed")
