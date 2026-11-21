"""
Pattern: Dynamic Programming (1D, prefix reachability)
Problem: LeetCode 139 - Word Break  [Medium]
Link: https://leetcode.com/problems/word-break/

Question:
    Can string s be segmented into a sequence of dictionary words?

Intuition:
    dp[i] is True if the prefix of length i can be segmented. dp[i] is True if some j<i has dp[j] True and s[j:i] is a word.

When to use this pattern:
    Can this prefix be built from pieces: Coin Change (LC 322), Decode Ways (LC 91).

Complexity:
    Time O(n * L) with L max word length, Space O(n)
"""
from typing import List


def word_break(s: str, word_dict: List[str]) -> bool:
    words = set(word_dict)
    max_len = max((len(w) for w in words), default=0)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"])
    assert word_break("applepenapple", ["apple", "pen"])
    assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
    assert not word_break("a", [])
    print("dp_word_break.py: all tests passed")
