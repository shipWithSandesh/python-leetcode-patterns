"""
Pattern: Two Pointers (read/write)
Problem: LeetCode 283 - Move Zeroes  [Easy]
Link: https://leetcode.com/problems/move-zeroes/

Question:
    Move all zeroes to the end in place, keeping the order of non-zero elements.

Intuition:
    Keep a write pointer for the next slot of a non-zero value. Scan with a read pointer; swap each non-zero into the write slot. Zeroes drift to the end.

When to use this pattern:
    In-place filtering/partitioning of arrays: Remove Duplicates (LC 26), Remove Element (LC 27).

Complexity:
    Time O(n), Space O(1)
"""
from typing import List


def move_zeroes(nums: List[int]) -> None:
    w = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[w], nums[r] = nums[r], nums[w]
            w += 1


if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    move_zeroes(a)
    assert a == [1, 3, 12, 0, 0]
    a = [0]
    move_zeroes(a)
    assert a == [0]
    a = [1, 2]
    move_zeroes(a)
    assert a == [1, 2]
    print("two_pointer_move_zeroes.py: all tests passed")
