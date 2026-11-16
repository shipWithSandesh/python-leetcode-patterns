"""
Pattern: 1D Dynamic Programming
Problem: LeetCode 198 - House Robber  [Medium]
Link: https://leetcode.com/problems/house-robber/

Question:
    Each house has some money. You can't rob two adjacent houses.
    Return the maximum amount you can rob.

Intuition:
    For house i you either skip it (keep best up to i-1) or rob it
    (nums[i] + best up to i-2):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    Only the last two values are needed, so use two variables instead
    of an array.

When to use this pattern:
    Climbing stairs, min cost climbing stairs, decode ways,
    coin change, longest increasing subsequence, word break.

Complexity:
    Time  O(n)
    Space O(1)
"""
from typing import List


def rob(nums: List[int]) -> int:
    prev2, prev1 = 0, 0  # best up to i-2, best up to i-1
    for money in nums:
        prev2, prev1 = prev1, max(prev1, prev2 + money)
    return prev1


if __name__ == "__main__":
    assert rob([1, 2, 3, 1]) == 4
    assert rob([2, 7, 9, 3, 1]) == 12
    assert rob([]) == 0
    assert rob([5]) == 5
    print("dynamic_programming_1d: all tests passed")
