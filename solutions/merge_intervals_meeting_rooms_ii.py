"""
Pattern: Intervals + Min-Heap
Problem: LeetCode 253 - Meeting Rooms II  [Medium]
Link: https://leetcode.com/problems/meeting-rooms-ii/

Question:
    Given meeting time intervals, return the minimum number of rooms required.

Intuition:
    Sort by start. Keep a min-heap of end times of occupied rooms. If the earliest-ending room is free by the new start, reuse it; otherwise open a room. Heap size is the answer.

When to use this pattern:
    Maximum overlap of intervals; scheduling resources.

Complexity:
    Time  O(n log n)
    Space O(n)
"""
import heapq
from typing import List


def min_meeting_rooms(intervals: List[List[int]]) -> int:
    heap: List[int] = []  # end times of rooms in use
    for start, end in sorted(intervals):
        if heap and heap[0] <= start:
            heapq.heapreplace(heap, end)
        else:
            heapq.heappush(heap, end)
    return len(heap)


if __name__ == "__main__":
    assert min_meeting_rooms([[0, 30], [5, 10], [15, 20]]) == 2
    assert min_meeting_rooms([[7, 10], [2, 4]]) == 1
    assert min_meeting_rooms([]) == 0
    assert min_meeting_rooms([[1, 5], [5, 8]]) == 1
    print("merge_intervals_meeting_rooms_ii.py: all tests passed")
