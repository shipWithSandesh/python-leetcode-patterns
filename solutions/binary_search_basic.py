"""
Pattern: Binary Search
Problem: LeetCode 704 - Binary Search  [Easy]
Link: https://leetcode.com/problems/binary-search/

Question:
Given a sorted array and a target, return its index or -1.

Intuition:
Keep a window [lo, hi]; compare the middle element with the target and discard the half that cannot contain it.

When to use this pattern:
Sorted data, or any monotonic condition you can test in O(1).

Complexity:
Time O(log n), Space O(1).
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


if __name__ == "__main__":
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([], 1) == -1
    assert search([5], 5) == 0
    print("binary_search_basic.py: all tests passed")
