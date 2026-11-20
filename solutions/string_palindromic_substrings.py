"""
Pattern: Strings (Expand Around Center)
Problem: LeetCode 647 - Palindromic Substrings  [Medium]
Link: https://leetcode.com/problems/palindromic-substrings/

Question:
    Count the palindromic substrings of s.

Intuition:
    Every palindrome has a center: a character (odd length) or a gap between two (even). Expand outward from each of the 2n-1 centers while ends match, counting each success.

When to use this pattern:
    Palindrome counting/longest palindrome where n is a few thousand.

Complexity:
    Time O(n^2), space O(1).
"""
from typing import List

def count_substrings(s: str) -> int:
    count = 0
    for center in range(2 * len(s) - 1):
        l = center // 2
        r = l + center % 2
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count


if __name__ == "__main__":
    assert count_substrings("abc") == 3
    assert count_substrings("aaa") == 6
    assert count_substrings("a") == 1
    assert count_substrings("") == 0
    print("string_palindromic_substrings.py: all tests passed")
