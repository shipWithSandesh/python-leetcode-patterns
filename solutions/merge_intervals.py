"""
Pattern: Merge Intervals
Problem: LeetCode 56 - Merge Intervals  [Medium]
Link: https://leetcode.com/problems/merge-intervals/

Question:
    Given an array of intervals [start, end], merge all overlapping intervals
    and return the non-overlapping intervals that cover all of the input.

Intuition:
    Sort by start time. Then walk once: if the current interval starts before
    (or exactly when) the last merged one ends, they overlap, so extend the
    end. Otherwise start a new merged interval.

When to use this pattern:
    Meeting rooms, insert interval, interval intersections,
    minimum arrows to burst balloons, calendar booking.

Complexity:
    Time  O(n log n) for sorting
    Space O(n) for the output
"""
from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    intervals.sort(key=lambda x: x[0])
    merged: List[List[int]] = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


if __name__ == "__main__":
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [0, 4]]) == [[0, 4]]
    print("merge_intervals: all tests passed")
