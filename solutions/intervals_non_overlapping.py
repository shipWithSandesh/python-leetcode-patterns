"""
Pattern: Intervals
Problem: LeetCode 435 - Non-overlapping Intervals  [Medium]
Link: https://leetcode.com/problems/non-overlapping-intervals/

Question:
    Given intervals, return the minimum number to remove so the rest do not overlap.

Intuition:
    Greedy: sort by end time and always keep the interval that ends earliest; it leaves the most room. Any interval starting before the last kept end overlaps and is removed.

When to use this pattern:
    Scheduling, interval selection, minimum removals to avoid conflicts.

Complexity:
    Time O(n log n)  - sorting
    Space O(1) extra
"""
from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    intervals = sorted(intervals, key=lambda x: x[1])
    removed, end = 0, float("-inf")
    for s, e in intervals:
        if s >= end:
            end = e
        else:
            removed += 1
    return removed


if __name__ == "__main__":
    assert erase_overlap_intervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    assert erase_overlap_intervals([[1,2],[1,2],[1,2]]) == 2
    assert erase_overlap_intervals([[1,2],[2,3]]) == 0
    assert erase_overlap_intervals([]) == 0
    print("intervals_non_overlapping: all tests passed")
