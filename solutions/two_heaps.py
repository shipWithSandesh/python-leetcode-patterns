"""
Pattern: Two Heaps
Problem: LeetCode 295 - Find Median from Data Stream  [Hard]
Link: https://leetcode.com/problems/find-median-from-data-stream/

Question:
    Design a class with addNum(num) and findMedian() for a stream of numbers.

Intuition:
    Keep the smaller half in a max-heap (`low`, stored negated since Python's
    heapq is a min-heap) and the larger half in a min-heap (`high`).
    Keep sizes balanced: len(low) == len(high) or len(low) == len(high) + 1.
    The median is then the top of `low`, or the average of both tops.

When to use this pattern:
    Sliding window median, IPO (maximize capital),
    any "running median / balance two halves" problem.

Complexity:
    addNum      O(log n)
    findMedian  O(1)
    Space       O(n)
"""
import heapq


class MedianFinder:
    def __init__(self):
        self.low = []   # max-heap via negatives
        self.high = []  # min-heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))
        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    print("two_heaps: all tests passed")
