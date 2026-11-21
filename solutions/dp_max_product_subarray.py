"""
Pattern: Dynamic Programming (track min and max)
Problem: LeetCode 152 - Maximum Product Subarray  [Medium]
Link: https://leetcode.com/problems/maximum-product-subarray/

Question:
    Return the largest product of any contiguous non-empty subarray.

Intuition:
    A negative number flips the biggest product into the smallest. So keep both the max and min product ending here; each new number can make either the new max. Zero resets both.

When to use this pattern:
    When an operation can flip ordering (negatives, sign changes) and you need an extreme over contiguous ranges.

Complexity:
    Time O(n), Space O(1)
"""
from typing import List


def max_product(nums: List[int]) -> int:
    best = hi = lo = nums[0]
    for x in nums[1:]:
        cands = (x, hi * x, lo * x)
        hi, lo = max(cands), min(cands)
        best = max(best, hi)
    return best


if __name__ == "__main__":
    assert max_product([2, 3, -2, 4]) == 6
    assert max_product([-2, 0, -1]) == 0
    assert max_product([-2, 3, -4]) == 24
    assert max_product([-3]) == -3
    print("dp_max_product_subarray.py: all tests passed")
