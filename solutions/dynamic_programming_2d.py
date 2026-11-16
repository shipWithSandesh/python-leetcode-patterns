"""
Pattern: 2D Dynamic Programming (two strings)
Problem: LeetCode 1143 - Longest Common Subsequence  [Medium]
Link: https://leetcode.com/problems/longest-common-subsequence/

Question:
    Given strings text1 and text2, return the length of their longest common
    subsequence (characters in order, not necessarily contiguous), or 0.

Intuition:
    dp[i][j] = LCS of text1[:i] and text2[:j].
    - If text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    - Else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    Each row only needs the previous row, so keep a single 1D array.

When to use this pattern:
    Edit distance, unique paths, longest palindromic subsequence,
    distinct subsequences, interleaving strings.

Complexity:
    Time  O(m * n)
    Space O(n) with the rolling row
"""


def longest_common_subsequence(text1: str, text2: str) -> int:
    n = len(text2)
    prev = [0] * (n + 1)
    for ch1 in text1:
        curr = [0] * (n + 1)
        for j in range(1, n + 1):
            if ch1 == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    return prev[n]


if __name__ == "__main__":
    assert longest_common_subsequence("abcde", "ace") == 3
    assert longest_common_subsequence("abc", "abc") == 3
    assert longest_common_subsequence("abc", "def") == 0
    print("dynamic_programming_2d: all tests passed")
