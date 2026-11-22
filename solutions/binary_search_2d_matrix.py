"""
Pattern: Binary Search (virtual array)
Problem: LeetCode 74 - Search a 2D Matrix  [Medium]
Link: https://leetcode.com/problems/search-a-2d-matrix/

Question:
Matrix rows are sorted and each row starts above the previous row's last value. Does target exist?

Intuition:
Treat the matrix as one sorted array of m*n items; index mid maps to row mid//n, column mid%n.

When to use this pattern:
Sorted data hidden behind a different shape.

Complexity:
Time O(log(m*n)); space O(1).
"""

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    n = len(matrix[0])
    lo, hi = 0, len(matrix) * n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        v = matrix[mid // n][mid % n]
        if v == target:
            return True
        if v < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False


if __name__ == "__main__":
    m = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(m, 3) is True
    assert search_matrix(m, 13) is False
    assert search_matrix([[1]], 1) is True
    assert search_matrix([], 1) is False
    print("binary_search_2d_matrix.py: all tests passed")
