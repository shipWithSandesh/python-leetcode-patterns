"""
Pattern: Two Pointers (sort + fix one + squeeze the rest)
Problem: LeetCode 15 - 3Sum  [Medium]
Link: https://leetcode.com/problems/3sum/

Question:
    Given an integer array nums, return all unique triplets [a, b, c]
    such that a + b + c == 0. The answer must not contain duplicate triplets.

Intuition:
    Sort the array. Fix the first number nums[i]; now we need a PAIR in the
    rest of the array summing to -nums[i] -> that's Two Sum II on a sorted
    array, solved with two pointers. To avoid duplicates, skip equal values
    for i, and after finding a triplet skip equal values for both pointers.
    If nums[i] > 0 we can stop: everything after it is positive too.

When to use this pattern:
    k-Sum problems (3Sum, 3Sum Closest, 4Sum), counting triplets under a
    target, any "find pairs/triplets" on data you are allowed to sort.

Complexity:
    Time  O(n^2)  - O(n log n) sort + O(n) two-pointer scan per i
    Space O(1) extra (ignoring the output and the sort)
"""
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums = sorted(nums)
    n = len(nums)
    result: List[List[int]] = []
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
    return result


if __name__ == "__main__":
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
    assert three_sum([]) == []
    assert three_sum([-2, 0, 1, 1, 2]) == [[-2, 0, 2], [-2, 1, 1]]
    print("two_pointer_3sum: all tests passed")
