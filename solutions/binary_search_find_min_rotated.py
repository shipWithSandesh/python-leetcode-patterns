"""
Pattern: Binary Search (compare with the right boundary)
Problem: LeetCode 153 - Find Minimum in Rotated Sorted Array  [Medium]
Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Question:
    A sorted array of unique values was rotated at an unknown pivot. Return
    its minimum element in O(log n) time.

Intuition:
    Compare nums[mid] with nums[right].
      - If nums[mid] > nums[right], the drop (the minimum) lies strictly to
        the right of mid, so search (mid, right].
      - Otherwise the right half is sorted, so the minimum is at mid or to
        its left: shrink right to mid (keep mid, it may be the answer).
    Loop until left == right; that index holds the minimum.

When to use this pattern:
    A sorted-but-rotated array, or any monotone predicate where one half
    can be discarded: Search in Rotated Sorted Array (LC 33), Find Peak
    Element (LC 162).

Complexity:
    Time  O(log n)
    Space O(1)
"""
from typing import List


def find_min(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return nums[left]


if __name__ == "__main__":
    assert find_min([3, 4, 5, 1, 2]) == 1
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0
    assert find_min([11, 13, 15, 17]) == 11     # not rotated
    assert find_min([1]) == 1
    assert find_min([2, 1]) == 1
    print("binary_search_find_min_rotated.py: all tests passed")
