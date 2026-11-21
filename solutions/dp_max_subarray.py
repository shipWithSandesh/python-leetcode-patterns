"""
Pattern: Dynamic Programming (Kadane)
Problem: LeetCode 53 - Maximum Subarray  [Medium]
Link: https://leetcode.com/problems/maximum-subarray/

Question:
    Return the largest sum of any contiguous non-empty subarray.

Intuition:
    At each index, either extend the best subarray ending at the previous index or start fresh here. If the running sum goes negative it only hurts, so drop it.

When to use this pattern:
    Best contiguous run problems: Max Product Subarray (LC 152), Best Time to Buy and Sell Stock (LC 121).

Complexity:
    Time O(n), Space O(1)
"""
from typing import List


def max_subarray(nums: List[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best


if __name__ == "__main__":
    assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_subarray([1]) == 1
    assert max_subarray([-3, -1, -2]) == -1
    assert max_subarray([5, 4, -1, 7, 8]) == 23
    print("dp_max_subarray.py: all tests passed")
