"""
Pattern: Backtracking
Problem: LeetCode 46 - Permutations  [Medium]
Link: https://leetcode.com/problems/permutations/

Question:
    Return all permutations of an array of distinct integers.

Intuition:
    Build a permutation one slot at a time; choose any unused number, recurse, then undo the choice (backtrack).

When to use this pattern:
    Generating all arrangements/subsets/combinations with choose-explore-unchoose.

Complexity:
    Time O(n * n!)
    Space O(n) recursion (excluding output)
"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    res: List[List[int]] = []
    path: List[int] = []
    used = [False] * len(nums)

    def dfs() -> None:
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i, n in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(n)
            dfs()
            path.pop()
            used[i] = False

    dfs()
    return res


if __name__ == "__main__":
    assert sorted(permute([1,2,3])) == [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert permute([1]) == [[1]]
    assert len(permute([1,2,3,4])) == 24
    print("backtracking_permutations: all tests passed")
