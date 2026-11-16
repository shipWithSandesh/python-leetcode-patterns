"""
Pattern: Backtracking
Problem: LeetCode 39 - Combination Sum  [Medium]
Link: https://leetcode.com/problems/combination-sum/

Question:
    Given distinct positive integers `candidates` and a `target`, return all
    unique combinations where the chosen numbers sum to target. The same
    number may be used unlimited times.

Intuition:
    Build combinations step by step: choose -> explore -> un-choose.
    Pass a `start` index so we only pick candidates at or after the current
    one; that prevents duplicates like [2,3] and [3,2].
    Sorting lets us stop early once a candidate exceeds the remaining sum.

When to use this pattern:
    Subsets, permutations, combinations, N-Queens, Sudoku solver,
    word search, palindrome partitioning.

Complexity:
    Time  O(N^(T/M))  exponential; T = target, M = smallest candidate
    Space O(T/M) recursion depth
"""
from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    result: List[List[int]] = []
    path: List[int] = []

    def backtrack(start: int, remaining: int) -> None:
        if remaining == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            c = candidates[i]
            if c > remaining:
                break  # sorted, so nothing after this fits either
            path.append(c)
            backtrack(i, remaining - c)  # i, not i+1: reuse allowed
            path.pop()

    backtrack(0, target)
    return result


if __name__ == "__main__":
    assert combination_sum([2, 3, 6, 7], 7) == [[2, 2, 3], [7]]
    assert combination_sum([2, 3, 5], 8) == [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert combination_sum([2], 1) == []
    print("backtracking: all tests passed")
