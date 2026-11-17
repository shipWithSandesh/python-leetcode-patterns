"""
Pattern: Monotonic Queue (Deque)
Problem: LeetCode 239 - Sliding Window Maximum  [Hard]
Link: https://leetcode.com/problems/sliding-window-maximum/

Question:
    Given nums and a window size k, return the max of each window of size k
    as it slides from left to right.

Intuition:
    Keep a deque of indices whose values are DECREASING. The front is always
    the current window's max.
    - Pop from the back any index whose value <= new value (they can never
      be a max again while the new value is in the window).
    - Pop from the front if it slid out of the window.

When to use this pattern:
    Sliding window min/max, shortest subarray with sum >= K,
    constrained subsequence sum, jump game VI.

Complexity:
    Time  O(n) - each index enters and leaves the deque once
    Space O(k)
"""
from collections import deque
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    dq = deque()
    result: List[int] = []
    for i, num in enumerate(nums):
        while dq and nums[dq[-1]] <= num:
            dq.pop()
        dq.append(i)
        if dq[0] <= i - k:
            dq.popleft()
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result


if __name__ == "__main__":
    assert max_sliding_window([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
    assert max_sliding_window([1], 1) == [1]
    assert max_sliding_window([9, 8, 7], 2) == [9, 8]
    print("monotonic_queue: all tests passed")
