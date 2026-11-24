"""
Pattern: Bit Manipulation + DP
Problem: LeetCode 338 - Counting Bits  [Easy]
Link: https://leetcode.com/problems/counting-bits/

Question:
    For each i in 0..n return the number of 1 bits in i.

Intuition:
    i has the same bits as i>>1 plus its lowest bit, so ans[i] = ans[i>>1] + (i&1).

When to use this pattern:
    Bit counts over a range; DP over bit shifts.

Complexity:
    Time  O(n)
    Space O(n)
"""
from typing import List


def count_bits(n: int) -> List[int]:
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i >> 1] + (i & 1)
    return ans


if __name__ == "__main__":
    assert count_bits(2) == [0, 1, 1]
    assert count_bits(5) == [0, 1, 1, 2, 1, 2]
    assert count_bits(0) == [0]
    assert count_bits(8)[8] == 1
    print("bit_manipulation_counting_bits.py: all tests passed")
