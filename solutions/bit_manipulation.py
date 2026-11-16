"""
Pattern: Bit Manipulation (XOR tricks)
Problem: LeetCode 136 - Single Number  [Easy]
Link: https://leetcode.com/problems/single-number/

Question:
    Every element appears twice except one. Find that single one,
    in O(n) time and O(1) extra space.

Intuition:
    XOR facts: a ^ a = 0, a ^ 0 = a, and XOR is order-independent.
    XOR all numbers together: every pair cancels to 0, leaving the single one.

Bonus in this file: LeetCode 338 - Counting Bits, using
    bits[i] = bits[i >> 1] + (i & 1)

When to use this pattern:
    Missing number, number of 1 bits, power of two (n & (n-1) == 0),
    reverse bits, subsets via bitmasks.

Complexity:
    Time  O(n)
    Space O(1)
"""
from functools import reduce
from operator import xor
from typing import List


def single_number(nums: List[int]) -> int:
    return reduce(xor, nums, 0)


def count_bits(n: int) -> List[int]:
    bits = [0] * (n + 1)
    for i in range(1, n + 1):
        bits[i] = bits[i >> 1] + (i & 1)
    return bits


if __name__ == "__main__":
    assert single_number([2, 2, 1]) == 1
    assert single_number([4, 1, 2, 1, 2]) == 4
    assert single_number([1]) == 1
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]
    print("bit_manipulation: all tests passed")
