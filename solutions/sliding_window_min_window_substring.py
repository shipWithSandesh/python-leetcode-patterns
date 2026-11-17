"""
Pattern: Sliding Window (variable size, shrink while valid)
Problem: LeetCode 76 - Minimum Window Substring  [Hard]
Link: https://leetcode.com/problems/minimum-window-substring/

Question:
    Given strings s and t, return the smallest substring of s that contains
    every character of t (including duplicates). Return "" if none exists.

Intuition:
    Count what t needs. Expand the right end of the window, and each time a
    character's need is fully met, bump a "formed" counter. When every
    distinct character is satisfied, the window is valid: record it, then
    shrink from the left as long as it stays valid, because we want the
    SMALLEST window. Expand to find a valid window, shrink to minimise it.

When to use this pattern:
    "Smallest/longest substring or subarray such that ...", anagram search
    (LC 438), permutation in string (LC 567), longest repeating character
    replacement (LC 424).

Complexity:
    Time  O(|s| + |t|)  - each index enters and leaves the window once
    Space O(|t|)        - character counts
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""
    need = Counter(t)
    required = len(need)
    window: Counter = Counter()
    formed = 0
    best_len, best_start = float("inf"), 0
    left = 0
    for right, ch in enumerate(s):
        window[ch] += 1
        if ch in need and window[ch] == need[ch]:
            formed += 1
        while formed == required:
            if right - left + 1 < best_len:
                best_len, best_start = right - left + 1, left
            out = s[left]
            window[out] -= 1
            if out in need and window[out] < need[out]:
                formed -= 1
            left += 1
    return "" if best_len == float("inf") else s[best_start:best_start + int(best_len)]


if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("", "a") == ""
    assert min_window("aaflslflsldkalskaaa", "aaa") == "aaa"
    print("sliding_window_min_window_substring: all tests passed")
