"""
Pattern: Dynamic Programming (1D)
Problem: LeetCode 213 - House Robber II  [Medium]
Link: https://leetcode.com/problems/house-robber-ii/

Question:
Houses are in a circle; you cannot rob two adjacent ones. Return the maximum loot.

Intuition:
First and last houses are adjacent, so you can't take both. Solve the linear House Robber twice: excluding the last, and excluding the first; take the max.

When to use this pattern:
Linear DP with a circular constraint: break the circle into two linear cases.

Complexity:
Time O(n), Space O(1).
"""
from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    def line(arr: List[int]) -> int:
        prev = cur = 0
        for x in arr:
            prev, cur = cur, max(cur, prev + x)
        return cur

    return max(line(nums[1:]), line(nums[:-1]))


if __name__ == "__main__":
    assert rob([2, 3, 2]) == 3
    assert rob([1, 2, 3, 1]) == 4
    assert rob([1]) == 1
    assert rob([1, 2, 3]) == 3
    print("dp_house_robber_ii.py: all tests passed")
