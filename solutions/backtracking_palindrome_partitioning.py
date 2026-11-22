"""
Pattern: Backtracking
Problem: LeetCode 131 - Palindrome Partitioning  [Medium]
Link: https://leetcode.com/problems/palindrome-partitioning/

Question:
Partition string s so every substring is a palindrome; return all partitions.

Intuition:
At each index try every prefix that is a palindrome, recurse on the rest, then undo. Precomputing a palindrome table avoids rechecking.

When to use this pattern:
Enumerating all splits of a sequence subject to a per-piece validity check.

Complexity:
Time O(n * 2^n); space O(n^2) for the table plus O(n) recursion.
"""

from typing import List


def partition(s: str) -> List[List[str]]:
    n = len(s)
    pal = [[False] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            pal[i][j] = s[i] == s[j] and (j - i < 2 or pal[i + 1][j - 1])
    res: List[List[str]] = []
    path: List[str] = []

    def go(start: int) -> None:
        if start == n:
            res.append(path[:])
            return
        for end in range(start, n):
            if pal[start][end]:
                path.append(s[start:end + 1])
                go(end + 1)
                path.pop()

    go(0)
    return res


if __name__ == "__main__":
    assert sorted(partition("aab")) == [["a", "a", "b"], ["aa", "b"]]
    assert partition("a") == [["a"]]
    assert len(partition("aaa")) == 4
    print("backtracking_palindrome_partitioning.py: all tests passed")
