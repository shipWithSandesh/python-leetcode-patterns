"""
Pattern: Dynamic Programming (2D, two strings)
Problem: LeetCode 72 - Edit Distance  [Hard]
Link: https://leetcode.com/problems/edit-distance/

Question:
    Minimum insert/delete/replace operations to convert word1 into word2.

Intuition:
    dp[i][j] = cost to turn first i chars of word1 into first j chars of word2. If chars match, take dp[i-1][j-1]; otherwise 1 + min(delete, insert, replace). Only the previous row is needed.

When to use this pattern:
    Comparing two sequences: LCS, edit distance, distinct subsequences.

Complexity:
    Time O(m*n), space O(n).
"""
from typing import List

def min_distance(word1: str, word2: str) -> int:
    m, n = len(word1), len(word2)
    prev = list(range(n + 1))
    for i in range(1, m + 1):
        cur = [i] + [0] * n
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                cur[j] = prev[j - 1]
            else:
                cur[j] = 1 + min(prev[j], cur[j - 1], prev[j - 1])
        prev = cur
    return prev[n]


if __name__ == "__main__":
    assert min_distance("horse", "ros") == 3
    assert min_distance("intention", "execution") == 5
    assert min_distance("", "abc") == 3
    assert min_distance("same", "same") == 0
    print("dynamic_programming_2d_edit_distance.py: all tests passed")
