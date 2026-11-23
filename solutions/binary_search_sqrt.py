"""
Pattern: Binary Search (on answer)
Problem: LeetCode 69 - Sqrt(x)  [Easy]
Link: https://leetcode.com/problems/sqrtx/

Question:
Return the integer part of the square root of non-negative x without using built-in sqrt.

Intuition:
The predicate mid*mid <= x is true then false as mid grows, so binary search for the last true value.

When to use this pattern:
Searching a numeric answer space where feasibility is monotonic.

Complexity:
Time O(log x), Space O(1).
"""
def my_sqrt(x: int) -> int:
    lo, hi, ans = 0, x, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            ans = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return ans


if __name__ == "__main__":
    assert my_sqrt(4) == 2
    assert my_sqrt(8) == 2
    assert my_sqrt(0) == 0
    assert my_sqrt(1) == 1
    assert my_sqrt(2147395599) == 46339
    print("binary_search_sqrt.py: all tests passed")
