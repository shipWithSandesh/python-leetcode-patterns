"""
Pattern: Greedy
Problem: LeetCode 55 - Jump Game  [Medium]
Link: https://leetcode.com/problems/jump-game/

Question:
    nums[i] is the max jump length from index i. Starting at index 0,
    can you reach the last index?

Intuition:
    Track the farthest index reachable so far. Walk left to right; if you
    ever stand on an index beyond `farthest`, you're stuck. Otherwise update
    farthest = max(farthest, i + nums[i]). No need to try every path:
    the locally best reach is globally enough.

When to use this pattern:
    Jump game II, gas station, task scheduler, assign cookies,
    non-overlapping intervals, best time to buy/sell stock II.

Complexity:
    Time  O(n)
    Space O(1)
"""
from typing import List


def can_jump(nums: List[int]) -> bool:
    farthest = 0
    for i, jump in enumerate(nums):
        if i > farthest:
            return False
        farthest = max(farthest, i + jump)
        if farthest >= len(nums) - 1:
            return True
    return True


if __name__ == "__main__":
    assert can_jump([2, 3, 1, 1, 4]) is True
    assert can_jump([3, 2, 1, 0, 4]) is False
    assert can_jump([0]) is True
    print("greedy: all tests passed")
