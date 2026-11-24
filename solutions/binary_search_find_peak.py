"""
Pattern: Binary Search (on slope)
Problem: LeetCode 162 - Find Peak Element  [Medium]
Link: https://leetcode.com/problems/find-peak-element/

Question:
    Return the index of any element strictly greater than its neighbours, in O(log n).

Intuition:
    If nums[mid] < nums[mid+1] we are on an upslope, so a peak lies to the right; otherwise one lies at mid or left. Halve accordingly.

When to use this pattern:
    Binary search without a sorted array, when a local direction guarantees a target side.

Complexity:
    Time  O(log n)
    Space O(1)
"""
from typing import List


def find_peak_element(nums: List[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo


if __name__ == "__main__":
    assert find_peak_element([1, 2, 3, 1]) == 2
    assert find_peak_element([1]) == 0
    assert find_peak_element([1, 2, 1, 3, 5, 6, 4]) in (1, 5)
    assert find_peak_element([3, 2, 1]) == 0
    assert find_peak_element([1, 2]) == 1
    print("binary_search_find_peak.py: all tests passed")
