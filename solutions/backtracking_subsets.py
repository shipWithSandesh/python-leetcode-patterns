"""
Pattern: Backtracking (choose / explore / un-choose)
Problem: LeetCode 78 - Subsets  [Medium]
Link: https://leetcode.com/problems/subsets/

Question:
    Given an array of unique integers, return all possible subsets (the
    power set), in any order.

Intuition:
    Build subsets one decision at a time. At each step we hold a current
    path; every path is itself a valid subset, so record a copy of it. Then
    try adding each remaining element (only those AFTER the last chosen
    index, so no subset is generated twice in a different order), recurse,
    and undo the choice (pop) before trying the next one.
    There are 2^n subsets, so that is the unavoidable output size.

When to use this pattern:
    "Generate all combinations / subsets / permutations / partitions":
    Combination Sum (LC 39), Permutations (LC 46), Subsets II (LC 90).

Complexity:
    Time  O(n * 2^n)  - 2^n subsets, each copied in up to O(n)
    Space O(n)        - recursion depth (excluding output)
"""
from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int) -> None:
        result.append(path[:])              # every path is a valid subset
        for i in range(start, len(nums)):
            path.append(nums[i])            # choose
            backtrack(i + 1)                # explore
            path.pop()                      # un-choose

    backtrack(0)
    return result


if __name__ == "__main__":
    def norm(x):
        return sorted(sorted(s) for s in x)

    assert norm(subsets([1, 2, 3])) == norm(
        [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])
    assert subsets([]) == [[]]
    assert norm(subsets([0])) == [[], [0]]
    assert len(subsets(list(range(10)))) == 1024
    print("backtracking_subsets.py: all tests passed")
