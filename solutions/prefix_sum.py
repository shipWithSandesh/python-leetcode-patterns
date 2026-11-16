"""
Pattern: Prefix Sum + Hash Map
Problem: LeetCode 560 - Subarray Sum Equals K  [Medium]
Link: https://leetcode.com/problems/subarray-sum-equals-k/

Question:
    Given an integer array nums (may contain negatives) and an integer k,
    return the total number of contiguous subarrays whose sum equals k.

Intuition:
    sum(i..j) = prefix[j] - prefix[i-1].  We want prefix[j] - prefix[i-1] == k,
    i.e. prefix[i-1] == prefix[j] - k.  While walking the array, count how
    many earlier prefixes equal (current_prefix - k) using a hash map.
    Sliding window does NOT work here because of negative numbers.

When to use this pattern:
    Range-sum queries, "number of subarrays with sum/xor = k",
    equal 0s and 1s, divisible-by-k subarrays.

Complexity:
    Time  O(n)
    Space O(n)
"""
from collections import defaultdict
from typing import List


def subarray_sum(nums: List[int], k: int) -> int:
    count = 0
    prefix = 0
    seen = defaultdict(int)
    seen[0] = 1  # empty prefix
    for num in nums:
        prefix += num
        count += seen[prefix - k]
        seen[prefix] += 1
    return count


if __name__ == "__main__":
    assert subarray_sum([1, 1, 1], 2) == 2
    assert subarray_sum([1, 2, 3], 3) == 2
    assert subarray_sum([1, -1, 0], 0) == 3
    print("prefix_sum: all tests passed")
