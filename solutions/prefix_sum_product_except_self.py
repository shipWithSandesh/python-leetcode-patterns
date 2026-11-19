"""
Pattern: Prefix Sum
Problem: LeetCode 238 - Product of Array Except Self  [Medium]
Link: https://leetcode.com/problems/product-of-array-except-self/

Question:
    Return answer[i] = product of all elements except nums[i], without division, in O(n).

Intuition:
    answer[i] = (product of everything left of i) * (product of everything right of i). Fill left products in one pass, then multiply by right products in a reverse pass.

When to use this pattern:
    Need aggregate of everything except the current element; prefix/suffix aggregates.

Complexity:
    Time O(n)
    Space O(1) extra (output excluded)
"""
from typing import List


def product_except_self(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res


if __name__ == "__main__":
    assert product_except_self([1,2,3,4]) == [24,12,8,6]
    assert product_except_self([-1,1,0,-3,3]) == [0,0,9,0,0]
    assert product_except_self([5,2]) == [2,5]
    print("prefix_sum_product_except_self: all tests passed")
