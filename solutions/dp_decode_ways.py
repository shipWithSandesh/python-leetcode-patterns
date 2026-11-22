"""
Pattern: Dynamic Programming (1D)
Problem: LeetCode 91 - Decode Ways  [Medium]
Link: https://leetcode.com/problems/decode-ways/

Question:
Digits map A=1..Z=26. Count the ways to decode a digit string.

Intuition:
dp[i] = ways for the first i chars. A single digit 1-9 adds dp[i-1]; a two-digit 10-26 adds dp[i-2]. Only the last two values are needed.

When to use this pattern:
Counting ways to split a sequence where each step depends on the last 1-2 positions.

Complexity:
Time O(n); space O(1).
"""

def num_decodings(s: str) -> int:
    prev2, prev1 = 1, 1 if s and s[0] != "0" else 0
    for i in range(2, len(s) + 1):
        cur = 0
        if s[i - 1] != "0":
            cur += prev1
        if 10 <= int(s[i - 2:i]) <= 26:
            cur += prev2
        prev2, prev1 = prev1, cur
    return prev1 if s else 0


if __name__ == "__main__":
    assert num_decodings("12") == 2
    assert num_decodings("226") == 3
    assert num_decodings("06") == 0
    assert num_decodings("10") == 1
    print("dp_decode_ways.py: all tests passed")
