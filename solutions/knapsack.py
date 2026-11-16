"""
Pattern: 0/1 Knapsack DP
Problem: LeetCode 416 - Partition Equal Subset Sum  [Medium]
Link: https://leetcode.com/problems/partition-equal-subset-sum/

Question:
    Given an array of positive integers, can it be split into two subsets
    with equal sums?

Intuition:
    Two equal halves means one subset sums to total/2. If total is odd,
    it's impossible. Otherwise it's 0/1 knapsack: can some items reach
    exactly `target`?  dp[s] = True if sum s is reachable.
    Loop s DOWNWARD so each number is used at most once.

When to use this pattern:
    Target sum, last stone weight II, ones and zeroes,
    coin change (unbounded variant loops upward).

Complexity:
    Time  O(n * target)
    Space O(target)
"""
from typing import List


def can_partition(nums: List[int]) -> bool:
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]
        if dp[target]:
            return True
    return dp[target]


if __name__ == "__main__":
    assert can_partition([1, 5, 11, 5]) is True
    assert can_partition([1, 2, 3, 5]) is False
    assert can_partition([2, 2]) is True
    print("knapsack: all tests passed")
