"""
Pattern: Modified Binary Search
Problem: LeetCode 33 - Search in Rotated Sorted Array  [Medium]
Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

Question:
    A sorted array of distinct integers was rotated at an unknown pivot
    (e.g. [4,5,6,7,0,1,2]). Return the index of target, or -1. Must be O(log n).

Intuition:
    At any mid, at least one half [lo..mid] or [mid..hi] is still sorted.
    Check which half is sorted, then check whether target lies inside that
    sorted half. If yes, search there; otherwise search the other half.

When to use this pattern:
    Sorted / rotated arrays, "first/last position", search on the answer
    (min capacity, Koko eating bananas), peak element.

Complexity:
    Time  O(log n)
    Space O(1)
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:  # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:  # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1


if __name__ == "__main__":
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search([1], 0) == -1
    assert search([3, 1], 1) == 1
    print("binary_search: all tests passed")
