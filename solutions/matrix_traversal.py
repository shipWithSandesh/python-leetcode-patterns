"""
Pattern: Matrix Traversal (layer by layer)
Problem: LeetCode 54 - Spiral Matrix  [Medium]
Link: https://leetcode.com/problems/spiral-matrix/

Question:
    Given an m x n matrix, return all elements in spiral order.

Intuition:
    Keep four boundaries: top, bottom, left, right. Walk right along top,
    down along right, left along bottom, up along left, shrinking each
    boundary after use. Check top <= bottom and left <= right before the
    bottom/left passes so single rows/columns aren't read twice.

When to use this pattern:
    Rotate image, set matrix zeroes, search a 2D matrix,
    game of life, diagonal traverse.

Complexity:
    Time  O(m * n)
    Space O(1) besides the output
"""
from typing import List


def spiral_order(matrix: List[List[int]]) -> List[int]:
    result: List[int] = []
    if not matrix:
        return result
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1
    return result


if __name__ == "__main__":
    assert spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [1, 2, 3, 6, 9, 8, 7, 4, 5]
    assert spiral_order([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
    assert spiral_order([[1], [2], [3]]) == [1, 2, 3]
    print("matrix_traversal: all tests passed")
