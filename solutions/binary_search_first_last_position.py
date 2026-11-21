"""
Pattern: Binary Search (lower/upper bound)
Problem: LeetCode 34 - Find First and Last Position of Element in Sorted Array  [Medium]
Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Question:
    In a sorted array return the first and last index of target, or [-1, -1].

Intuition:
    Write one lower-bound search: first index with value >= x. First position is lower_bound(target); last is lower_bound(target+1) - 1. Check the value actually exists.

When to use this pattern:
    Sorted data with duplicates or insert-position questions: Search Insert Position (LC 35).

Complexity:
    Time O(log n), Space O(1)
"""
from typing import List


def search_range(nums: List[int], target: int) -> List[int]:
    def lower_bound(x: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        return lo

    first = lower_bound(target)
    if first == len(nums) or nums[first] != target:
        return [-1, -1]
    return [first, lower_bound(target + 1) - 1]


if __name__ == "__main__":
    assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert search_range([], 0) == [-1, -1]
    assert search_range([2, 2], 2) == [0, 1]
    print("binary_search_first_last_position.py: all tests passed")
