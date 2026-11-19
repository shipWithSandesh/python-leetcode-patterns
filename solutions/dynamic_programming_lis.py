"""
Pattern: Dynamic Programming (Binary Search)
Problem: LeetCode 300 - Longest Increasing Subsequence  [Medium]
Link: https://leetcode.com/problems/longest-increasing-subsequence/

Question:
    Return the length of the longest strictly increasing subsequence of nums.

Intuition:
    Keep `tails`, where tails[k] is the smallest possible tail of an increasing subsequence of length k+1. For each number, binary search its spot: replace or append. The length of tails is the answer.

When to use this pattern:
    Subsequence problems where a greedy 'smallest tail' can be maintained.

Complexity:
    Time O(n log n)
    Space O(n)
"""
from bisect import bisect_left
from typing import List


def length_of_lis(nums: List[int]) -> int:
    tails: List[int] = []
    for n in nums:
        i = bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)


if __name__ == "__main__":
    assert length_of_lis([10,9,2,5,3,7,101,18]) == 4
    assert length_of_lis([0,1,0,3,2,3]) == 4
    assert length_of_lis([7,7,7]) == 1
    assert length_of_lis([]) == 0
    print("dynamic_programming_lis: all tests passed")
