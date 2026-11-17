"""
Pattern: Binary Search on the Answer
Problem: LeetCode 875 - Koko Eating Bananas  [Medium]
Link: https://leetcode.com/problems/koko-eating-bananas/

Question:
    piles[i] bananas in each pile. Koko picks an eating speed k (bananas per
    hour); each hour she eats up to k from ONE pile. Return the minimum k
    that lets her finish all piles within h hours.

Intuition:
    We don't search inside the array, we search the range of possible
    answers: k is between 1 and max(piles). The check "can she finish at
    speed k?" is monotonic: if speed k works, any faster speed works too.
    So binary search for the first k where the check becomes True.
    Hours at speed k = sum(ceil(p / k)) = sum((p + k - 1) // k).

When to use this pattern:
    "Minimise the maximum" / "find the smallest value such that ...":
    capacity to ship packages in D days (LC 1011), split array largest sum
    (LC 410), minimum days to make bouquets (LC 1482).

Complexity:
    Time  O(n log M)  - M = max(piles), each check is O(n)
    Space O(1)
"""
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    def can_finish(k: int) -> bool:
        return sum((p + k - 1) // k for p in piles) <= h

    low, high = 1, max(piles)
    while low < high:
        mid = (low + high) // 2
        if can_finish(mid):
            high = mid       # mid works; maybe something smaller does too
        else:
            low = mid + 1    # too slow
    return low


if __name__ == "__main__":
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
    assert min_eating_speed([1], 1) == 1
    assert min_eating_speed([1000000000], 2) == 500000000
    print("binary_search_koko_bananas: all tests passed")
