"""
Pattern: Hashing
Problem: LeetCode 242 - Valid Anagram  [Easy]
Link: https://leetcode.com/problems/valid-anagram/

Question:
Return True if t is an anagram of s (same letters, same counts).

Intuition:
Count the characters of both strings; they are anagrams iff the counts match exactly.

When to use this pattern:
Comparing multisets of characters or items; frequency maps.

Complexity:
Time O(n), Space O(k) where k is the alphabet size.
"""
from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return len(s) == len(t) and Counter(s) == Counter(t)


if __name__ == "__main__":
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    print("hashing_valid_anagram.py: all tests passed")
