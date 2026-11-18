"""
Pattern: Sliding Window (variable size, never shrinks below best)
Problem: LeetCode 424 - Longest Repeating Character Replacement  [Medium]
Link: https://leetcode.com/problems/longest-repeating-character-replacement/

Question:
    Given an uppercase string s and an integer k, you may replace at most k
    characters. Return the length of the longest substring containing a
    single repeated letter after the replacements.

Intuition:
    A window is valid if (window size - count of its most frequent letter)
    <= k: those "other" letters are the ones we would replace. Expand right
    always; if the window becomes invalid, slide the left edge by one (the
    window size stays the same, it just moves). We never need to shrink the
    window below the best size seen, so the max frequency only has to be
    kept as a running maximum, not recomputed after shrinking.

When to use this pattern:
    "Longest substring with at most k changes/distinct/violations":
    Longest Substring Without Repeating (LC 3), Max Consecutive Ones III
    (LC 1004), Fruit Into Baskets (LC 904).

Complexity:
    Time  O(n)  - each index visited once
    Space O(1)  - at most 26 letter counts
"""
from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    counts: dict = defaultdict(int)
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] += 1
        max_freq = max(max_freq, counts[ch])
        if (right - left + 1) - max_freq > k:       # too many replacements needed
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("", 3) == 0
    assert character_replacement("A", 0) == 1
    assert character_replacement("ABCDE", 0) == 1
    assert character_replacement("AAAA", 0) == 4
    print("sliding_window_char_replacement.py: all tests passed")
