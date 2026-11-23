"""
Pattern: Hashing
Problem: LeetCode 217 - Contains Duplicate  [Easy]
Link: https://leetcode.com/problems/contains-duplicate/

Question:
Return True if any value appears at least twice in the array.

Intuition:
Remember what you've seen in a set; the first repeat answers the question immediately.

When to use this pattern:
Membership / duplicate checks where O(1) lookup beats sorting.

Complexity:
Time O(n), Space O(n).
"""
from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    seen = set()
    for x in nums:
        if x in seen:
            return True
        seen.add(x)
    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([]) is False
    print("hashing_contains_duplicate.py: all tests passed")
