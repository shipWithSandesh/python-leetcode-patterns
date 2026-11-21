"""
Pattern: Backtracking
Problem: LeetCode 17 - Letter Combinations of a Phone Number  [Medium]
Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/

Question:
    Given digits 2-9, return all letter combinations the digits could represent on a phone keypad.

Intuition:
    Choose one letter per digit, in order. Recurse on the next digit with the path so far; when the path length equals the digit count, record it.

When to use this pattern:
    Enumerating all combinations built position by position: Subsets (LC 78), Permutations (LC 46).

Complexity:
    Time O(4^n * n), Space O(n) recursion
"""
from typing import List

KEYS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}


def letter_combinations(digits: str) -> List[str]:
    if not digits:
        return []
    out: List[str] = []
    path: List[str] = []

    def go(i: int) -> None:
        if i == len(digits):
            out.append("".join(path))
            return
        for ch in KEYS[digits[i]]:
            path.append(ch)
            go(i + 1)
            path.pop()

    go(0)
    return out


if __name__ == "__main__":
    assert sorted(letter_combinations("23")) == sorted(
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    assert letter_combinations("") == []
    assert letter_combinations("2") == ["a", "b", "c"]
    assert len(letter_combinations("79")) == 16
    print("backtracking_letter_combinations.py: all tests passed")
