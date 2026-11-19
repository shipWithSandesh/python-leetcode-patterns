"""
Pattern: Strings (Expand Around Center)
Problem: LeetCode 5 - Longest Palindromic Substring  [Medium]
Link: https://leetcode.com/problems/longest-palindromic-substring/

Question:
    Return the longest palindromic substring of s.

Intuition:
    Every palindrome mirrors around a center (a character or a gap between two). Expand outward from each of the 2n-1 centers while characters match, tracking the longest.

When to use this pattern:
    Palindrome questions where O(n^2) is acceptable and simple.

Complexity:
    Time O(n^2)
    Space O(1)
"""
def longest_palindrome(s: str) -> str:
    best = ""
    for c in range(len(s)):
        for l, r in ((c, c), (c, c + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if r - l - 1 > len(best):
                best = s[l + 1:r]
    return best


if __name__ == "__main__":
    assert longest_palindrome("babad") in ("bab", "aba")
    assert longest_palindrome("cbbd") == "bb"
    assert longest_palindrome("a") == "a"
    assert longest_palindrome("") == ""
    print("string_longest_palindromic_substring: all tests passed")
