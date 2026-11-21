"""
Pattern: Dynamic Programming (1D, Fibonacci)
Problem: LeetCode 70 - Climbing Stairs  [Easy]
Link: https://leetcode.com/problems/climbing-stairs/

Question:
    You can climb 1 or 2 steps at a time. How many distinct ways reach step n?

Intuition:
    The last move was a 1-step from n-1 or a 2-step from n-2, so ways(n) = ways(n-1) + ways(n-2). Only the last two values are needed.

When to use this pattern:
    Counting ways where the state depends on a few previous states: House Robber (LC 198), Coin Change (LC 322).

Complexity:
    Time O(n), Space O(1)
"""
def climb_stairs(n: int) -> int:
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(10) == 89
    print("dp_climbing_stairs.py: all tests passed")
