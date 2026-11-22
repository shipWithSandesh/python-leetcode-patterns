"""
Pattern: Backtracking
Problem: LeetCode 22 - Generate Parentheses  [Medium]
Link: https://leetcode.com/problems/generate-parentheses/

Question:
Given n pairs of parentheses, return all well-formed combinations.

Intuition:
Build the string one char at a time. Add '(' while fewer than n are used; add ')' only if it would not exceed the number of '('. This prunes invalid branches so every path is valid.

When to use this pattern:
Generating all valid sequences under constraints that can be checked incrementally.

Complexity:
Time O(4^n / sqrt(n)) (Catalan number of results); space O(n) recursion.
"""

from typing import List


def generate_parenthesis(n: int) -> List[str]:
    res: List[str] = []
    path: List[str] = []

    def go(open_n: int, close_n: int) -> None:
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if open_n < n:
            path.append("(")
            go(open_n + 1, close_n)
            path.pop()
        if close_n < open_n:
            path.append(")")
            go(open_n, close_n + 1)
            path.pop()

    go(0, 0)
    return res


if __name__ == "__main__":
    assert generate_parenthesis(1) == ["()"]
    assert sorted(generate_parenthesis(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
    assert len(generate_parenthesis(4)) == 14
    print("backtracking_generate_parentheses.py: all tests passed")
