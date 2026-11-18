"""
Pattern: Two Pointers (opposite ends, greedy move)
Problem: LeetCode 11 - Container With Most Water  [Medium]
Link: https://leetcode.com/problems/container-with-most-water/

Question:
    Given heights of vertical lines at x = 0..n-1, pick two lines that,
    together with the x-axis, hold the most water. Return that area.

Intuition:
    Start with the widest container (first and last line). Area is
    width * min(height). Moving the TALLER line inward can only shrink the
    width without any chance of raising the limiting (shorter) height, so
    it can never help. Move the SHORTER line inward instead, hoping to find
    a taller one. Repeat until the pointers meet.

When to use this pattern:
    Sorted or "outside-in" problems where one pointer's move can be proven
    safe: Two Sum II (LC 167), 3Sum (LC 15), Trapping Rain Water (LC 42).

Complexity:
    Time  O(n)  - each pointer moves at most n steps in total
    Space O(1)
"""
from typing import List


def max_area(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        best = max(best, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return best


if __name__ == "__main__":
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
    assert max_area([1, 2, 1]) == 2
    assert max_area([5]) == 0
    print("two_pointer_container_most_water.py: all tests passed")
