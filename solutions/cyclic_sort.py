"""
Pattern: Cyclic Sort (index as hash)
Problem: LeetCode 41 - First Missing Positive  [Hard]
Link: https://leetcode.com/problems/first-missing-positive/

Question:
    Given an unsorted integer array nums, return the smallest missing
    positive integer. Must run in O(n) time and O(1) extra space.

Intuition:
    The answer is always in 1..n+1. Place every value v in 1..n at index v-1
    by swapping ("cyclic sort"). Then the first index i where nums[i] != i+1
    gives the answer i+1. If all are in place, the answer is n+1.

When to use this pattern:
    Arrays containing numbers in a range 1..n: missing number,
    find all duplicates, find the corrupt pair.

Complexity:
    Time  O(n)  - every swap puts one number in its final spot
    Space O(1)
"""
from typing import List


def first_missing_positive(nums: List[int]) -> int:
    n = len(nums)
    i = 0
    while i < n:
        correct = nums[i] - 1
        if 0 <= correct < n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i, v in enumerate(nums):
        if v != i + 1:
            return i + 1
    return n + 1


if __name__ == "__main__":
    assert first_missing_positive([1, 2, 0]) == 3
    assert first_missing_positive([3, 4, -1, 1]) == 2
    assert first_missing_positive([7, 8, 9, 11, 12]) == 1
    assert first_missing_positive([1, 1]) == 2
    print("cyclic_sort: all tests passed")
