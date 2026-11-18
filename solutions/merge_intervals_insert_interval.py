"""
Pattern: Intervals (three-phase linear scan)
Problem: LeetCode 57 - Insert Interval  [Medium]
Link: https://leetcode.com/problems/insert-interval/

Question:
    Given a list of non-overlapping intervals sorted by start, insert a new
    interval and merge any overlaps. Return the resulting sorted list.

Intuition:
    Because the input is already sorted, no sorting is needed. Walk through
    in three phases:
      1. Copy every interval that ends BEFORE the new one starts.
      2. Merge every interval that overlaps the new one (its start is <= the
         new end) by widening the new interval to min(starts), max(ends).
      3. Copy the remaining intervals that start AFTER the new one ends.

When to use this pattern:
    Sorted intervals plus an insertion or query: Merge Intervals (LC 56),
    Meeting Rooms, Interval List Intersections (LC 986).

Complexity:
    Time  O(n)  - single pass, thanks to the input being sorted
    Space O(n)  - output list
"""
from typing import List


def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    result: List[List[int]] = []
    i, n = 0, len(intervals)
    start, end = new_interval

    while i < n and intervals[i][1] < start:        # phase 1: strictly before
        result.append(intervals[i])
        i += 1
    while i < n and intervals[i][0] <= end:         # phase 2: overlapping
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])
    result.extend(intervals[i:])                    # phase 3: strictly after
    return result


if __name__ == "__main__":
    assert insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]
    assert insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [[1, 2], [3, 10], [12, 16]]
    assert insert([], [5, 7]) == [[5, 7]]
    assert insert([[1, 5]], [2, 3]) == [[1, 5]]
    assert insert([[1, 5]], [6, 8]) == [[1, 5], [6, 8]]
    assert insert([[3, 5]], [1, 2]) == [[1, 2], [3, 5]]
    print("merge_intervals_insert_interval.py: all tests passed")
