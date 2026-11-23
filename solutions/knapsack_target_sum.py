"""
Pattern: 0/1 Knapsack (subset sum count)
Problem: LeetCode 494 - Target Sum  [Medium]
Link: https://leetcode.com/problems/target-sum/

Question:
Assign + or - to every number so the total equals target; count the ways.

Intuition:
Let P be the sum of numbers with + and N the rest: P - N = target and P + N = total, so P = (total + target) / 2. Count subsets summing to P with a 1D 0/1 knapsack, iterating sums downward.

When to use this pattern:
Counting or checking subsets with a given sum; +/- sign assignment problems.

Complexity:
Time O(n * P), Space O(P).
"""
from typing import List


def find_target_sum_ways(nums: List[int], target: int) -> int:
    total = sum(nums)
    if abs(target) > total or (total + target) % 2:
        return 0
    goal = (total + target) // 2
    dp = [0] * (goal + 1)
    dp[0] = 1
    for x in nums:
        for s in range(goal, x - 1, -1):
            dp[s] += dp[s - x]
    return dp[goal]


if __name__ == "__main__":
    assert find_target_sum_ways([1, 1, 1, 1, 1], 3) == 5
    assert find_target_sum_ways([1], 1) == 1
    assert find_target_sum_ways([1], 2) == 0
    assert find_target_sum_ways([0, 0, 1], 1) == 4
    print("knapsack_target_sum.py: all tests passed")
