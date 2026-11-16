"""
Pattern: Two Pointers
Problem: LeetCode 167 - Two Sum II (Input Array Is Sorted)  [Medium]
Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Question:
    Given a 1-indexed array `numbers` sorted in non-decreasing order, find two
    numbers that add up to `target`. Return their indices [i, j] (1-indexed).
    Exactly one solution exists. Use only O(1) extra space.

Intuition:
    Because the array is sorted, put one pointer at each end.
    - If the sum is too small, move the left pointer right (bigger number).
    - If the sum is too big, move the right pointer left (smaller number).
    Each step safely throws away one candidate, so we never miss the answer.

When to use this pattern:
    Sorted arrays, pairs/triplets with a target sum, palindromes,
    removing duplicates in place, "container with most water".

Complexity:
    Time  O(n)  - each pointer moves at most n times
    Space O(1)
"""
from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        current = numbers[left] + numbers[right]
        if current == target:
            return [left + 1, right + 1]
        if current < target:
            left += 1
        else:
            right -= 1
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum([2, 3, 4], 6) == [1, 3]
    assert two_sum([-1, 0], -1) == [1, 2]
    print("two_pointer: all tests passed")
