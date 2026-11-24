"""
Pattern: DP (state machine)
Problem: LeetCode 309 - Best Time to Buy and Sell Stock with Cooldown  [Medium]
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

Question:
    Maximise profit with unlimited transactions, but you must wait one day after selling before buying.

Intuition:
    Model three states per day: holding a stock, just sold, resting. Each day's state depends only on the previous day's, so keep three variables.

When to use this pattern:
    Choices per day with transition rules between states.

Complexity:
    Time  O(n)
    Space O(1)
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    hold, sold, rest = float("-inf"), 0, 0
    for p in prices:
        prev_sold = sold
        sold = hold + p
        hold = max(hold, rest - p)
        rest = max(rest, prev_sold)
    return max(sold, rest)


if __name__ == "__main__":
    assert max_profit([1, 2, 3, 0, 2]) == 3
    assert max_profit([1]) == 0
    assert max_profit([]) == 0
    assert max_profit([5, 4, 3]) == 0
    assert max_profit([1, 4, 2, 7]) == 6
    print("dp_stock_cooldown.py: all tests passed")
