"""
Pattern: Top K Elements (min-heap of size k)
Problem: LeetCode 215 - Kth Largest Element in an Array  [Medium]
Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

Question:
    Return the kth largest element of an unsorted array (kth in sorted
    order, not the kth distinct value).

Intuition:
    Keep a min-heap holding the k largest values seen so far. Its root is
    the smallest of those k, i.e. exactly the kth largest. For each new
    number, push it, and if the heap grows past k, pop the root (the
    smallest) so only the k largest survive. Sorting would cost O(n log n);
    the heap costs O(n log k), which is better when k is small.
    (Quickselect gives O(n) average, but the heap is simpler and safer.)

When to use this pattern:
    "kth largest/smallest", "top k frequent", "k closest points":
    Top K Frequent Elements (LC 347), K Closest Points (LC 973).

Complexity:
    Time  O(n log k)
    Space O(k)
"""
import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    heap: List[int] = []
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


if __name__ == "__main__":
    assert find_kth_largest([3, 2, 1, 5, 6, 4], 2) == 5
    assert find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
    assert find_kth_largest([1], 1) == 1
    assert find_kth_largest([7, 7, 7], 2) == 7
    assert find_kth_largest([-1, -2, -3], 3) == -3
    print("top_k_elements_kth_largest.py: all tests passed")
