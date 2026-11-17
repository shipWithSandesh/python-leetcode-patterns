"""
Pattern: Hashing (complement lookup)
Problem: LeetCode 1 - Two Sum  [Easy]
Link: https://leetcode.com/problems/two-sum/

Question:
    Given an UNSORTED array nums and a target, return the indices of the two
    numbers that add up to target. Exactly one solution exists, and you may
    not use the same element twice.

Intuition:
    For each number x we need target - x. Instead of scanning the rest of
    the array (O(n^2)), remember every number we've seen in a dict
    value -> index. Before storing x, check whether its complement is
    already in the dict. One pass, and it handles duplicates naturally.
    Compare with two_pointer.py: sorted input -> two pointers, O(1) space;
    unsorted input -> hash map, O(n) space but no sort.

When to use this pattern:
    "Have I seen the matching piece before?": pair sums, contains duplicate
    (LC 217), longest consecutive sequence (LC 128), subarray sum equals K
    (prefix_sum.py), isomorphic strings.

Complexity:
    Time  O(n)
    Space O(n)
"""
from typing import Dict, List


def two_sum(nums: List[int], target: int) -> List[int]:
    seen: Dict[int, int] = {}
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
    print("hashing_two_sum: all tests passed")
