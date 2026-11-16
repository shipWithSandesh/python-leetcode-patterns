"""
Pattern: Sliding Window (variable size)
Problem: LeetCode 3 - Longest Substring Without Repeating Characters  [Medium]
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Question:
    Given a string s, return the length of the longest substring that has
    no repeating characters.

Intuition:
    Keep a window [left, right] that never contains a duplicate.
    Expand right one char at a time. If the new char was already seen inside
    the window, jump left to just after its last position.
    Storing the last index of every char lets left jump instead of crawl.

When to use this pattern:
    "Longest/shortest subarray or substring such that ...", fixed-size window
    averages/max, at-most-K-distinct, minimum window substring.

Complexity:
    Time  O(n)
    Space O(min(n, alphabet))
"""


def length_of_longest_substring(s: str) -> int:
    last_seen = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("abba") == 2
    print("sliding_window: all tests passed")
