"""
Pattern: Hashing (set lookup, only start sequences at their beginning)
Problem: LeetCode 128 - Longest Consecutive Sequence  [Medium]
Link: https://leetcode.com/problems/longest-consecutive-sequence/

Question:
    Given an unsorted array of integers, return the length of the longest
    run of consecutive values (e.g. 1,2,3,4), in O(n) time.

Intuition:
    Sorting would be O(n log n). Instead put everything in a set for O(1)
    membership. A number x is the START of a run only if x - 1 is NOT in the
    set. For each start, count upward (x+1, x+2, ...) while the numbers
    exist. Because we only walk from run starts, each number is visited a
    constant number of times, so the total work is linear.

When to use this pattern:
    Need O(1) "have I seen it?" checks to avoid sorting: Two Sum (LC 1),
    Contains Duplicate (LC 217), Happy Number (LC 202).

Complexity:
    Time  O(n)  - each element is part of exactly one counted walk
    Space O(n)  - the set
"""
from typing import List


def longest_consecutive(nums: List[int]) -> int:
    seen = set(nums)
    best = 0
    for x in seen:
        if x - 1 not in seen:               # x begins a run
            length = 1
            while x + length in seen:
                length += 1
            best = max(best, length)
    return best


if __name__ == "__main__":
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    assert longest_consecutive([5]) == 1
    assert longest_consecutive([1, 1, 1]) == 1
    assert longest_consecutive([-2, -1, 0, 10]) == 3
    print("hashing_longest_consecutive.py: all tests passed")
