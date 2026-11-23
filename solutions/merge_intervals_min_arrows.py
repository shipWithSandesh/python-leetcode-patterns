"""
Pattern: Intervals (Greedy)
Problem: LeetCode 452 - Minimum Number of Arrows to Burst Balloons  [Medium]
Link: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

Question:
Balloons are horizontal intervals [start, end]; an arrow at x bursts all balloons covering x. Return the minimum arrows.

Intuition:
Sort by end. Shoot at the first balloon's end; it bursts every balloon starting at or before that point. When a balloon starts after the arrow, shoot a new one.

When to use this pattern:
Interval covering/stabbing: sort by end and greedily pick the earliest end.

Complexity:
Time O(n log n), Space O(1) extra.
"""
from typing import List


def find_min_arrow_shots(points: List[List[int]]) -> int:
    arrows, end = 0, float("-inf")
    for s, e in sorted(points, key=lambda p: p[1]):
        if s > end:
            arrows += 1
            end = e
    return arrows


if __name__ == "__main__":
    assert find_min_arrow_shots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert find_min_arrow_shots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert find_min_arrow_shots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
    assert find_min_arrow_shots([[-2147483648, 2147483647]]) == 1
    print("merge_intervals_min_arrows.py: all tests passed")
