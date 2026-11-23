"""
Pattern: Boyer-Moore Voting
Problem: LeetCode 169 - Majority Element  [Easy]
Link: https://leetcode.com/problems/majority-element/

Question:
Return the element that appears more than n/2 times in the array (it always exists).

Intuition:
Pair off each majority vote with a different element; they cancel. Because the majority appears more than half the time, it survives as the final candidate.

When to use this pattern:
Finding an element occurring more than n/2 (or n/k with k-1 counters) times in O(1) space.

Complexity:
Time O(n), Space O(1).
"""
from typing import List


def majority_element(nums: List[int]) -> int:
    candidate, count = 0, 0
    for x in nums:
        if count == 0:
            candidate = x
        count += 1 if x == candidate else -1
    return candidate


if __name__ == "__main__":
    assert majority_element([3, 2, 3]) == 3
    assert majority_element([2, 2, 1, 1, 1, 2, 2]) == 2
    assert majority_element([7]) == 7
    print("boyer_moore_majority_element.py: all tests passed")
