"""
Pattern: Top K Elements (Heap / Bucket Sort)
Problem: LeetCode 347 - Top K Frequent Elements  [Medium]
Link: https://leetcode.com/problems/top-k-frequent-elements/

Question:
    Given an integer array nums and an integer k, return the k most frequent
    elements (any order).

Intuition:
    Count frequencies, then pick the top k.
    - Heap: keep a min-heap of size k -> O(n log k).
    - Best: bucket sort. Frequency can be at most n, so make buckets
      0..n where bucket[f] holds numbers seen f times, then read buckets
      from high to low -> O(n).

When to use this pattern:
    K closest points, Kth largest element, top K frequent words,
    sort characters by frequency.

Complexity (bucket sort):
    Time  O(n)
    Space O(n)
"""
import heapq
from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for num, f in freq.items():
        buckets[f].append(num)
    result: List[int] = []
    for f in range(len(buckets) - 1, 0, -1):
        for num in buckets[f]:
            result.append(num)
            if len(result) == k:
                return result
    return result


def top_k_frequent_heap(nums: List[int], k: int) -> List[int]:
    """Alternative O(n log k) heap solution."""
    freq = Counter(nums)
    return [num for num, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]


if __name__ == "__main__":
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent_heap([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    print("top_k_elements: all tests passed")
