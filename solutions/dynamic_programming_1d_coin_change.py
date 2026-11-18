"""
Pattern: Dynamic Programming (1D, unbounded knapsack / min count)
Problem: LeetCode 322 - Coin Change  [Medium]
Link: https://leetcode.com/problems/coin-change/

Question:
    Given coin denominations and a target amount, return the fewest coins
    needed to make exactly that amount, or -1 if it is impossible. Each
    coin may be used any number of times.

Intuition:
    Let dp[a] be the fewest coins to make amount a. dp[0] = 0. For amount a,
    the last coin used could be any coin c <= a, so
        dp[a] = 1 + min(dp[a - c]) over all coins c.
    Fill amounts from 1 up to the target; unreachable amounts stay at
    infinity. Greedy (always take the biggest coin) is WRONG here, e.g.
    coins [1, 3, 4], amount 6: greedy gives 4+1+1 (3) but 3+3 (2) is best.

When to use this pattern:
    "Fewest/number of ways to reach a total using repeatable items":
    Coin Change II (LC 518), Perfect Squares (LC 279), Word Break (LC 139).

Complexity:
    Time  O(amount * len(coins))
    Space O(amount)
"""
from typing import List


def coin_change(coins: List[int], amount: int) -> int:
    INF = amount + 1                       # larger than any real answer
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] != INF else -1


if __name__ == "__main__":
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1, 3, 4], 6) == 2       # greedy would fail
    assert coin_change([186, 419, 83, 408], 6249) == 20
    assert coin_change([5], 5) == 1
    print("dynamic_programming_1d_coin_change.py: all tests passed")
