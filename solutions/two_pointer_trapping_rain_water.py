"""
Pattern: Two Pointers
Problem: LeetCode 42 - Trapping Rain Water  [Hard]
Link: https://leetcode.com/problems/trapping-rain-water/

Question:
    Given bar heights, compute how much rain water is trapped between them.

Intuition:
    Water above a bar = min(max-left, max-right) - height. Two pointers: the side with the smaller max is the limiting side, so settle that side and move inward.

When to use this pattern:
    Answers depend on prefix and suffix maxima; squeeze from both ends.

Complexity:
    Time O(n)
    Space O(1)
"""
from typing import List


def trap(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    left_max = right_max = water = 0
    while l < r:
        if height[l] < height[r]:
            left_max = max(left_max, height[l])
            water += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            water += right_max - height[r]
            r -= 1
    return water


if __name__ == "__main__":
    assert trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert trap([4,2,0,3,2,5]) == 9
    assert trap([]) == 0
    assert trap([1,2,3]) == 0
    print("two_pointer_trapping_rain_water: all tests passed")
