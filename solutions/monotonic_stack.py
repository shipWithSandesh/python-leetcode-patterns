"""
Pattern: Monotonic Stack
Problem: LeetCode 739 - Daily Temperatures  [Medium]
Link: https://leetcode.com/problems/daily-temperatures/

Question:
    Given daily temperatures, return an array where answer[i] is the number
    of days you have to wait after day i to get a warmer temperature
    (0 if there is no such day).

Intuition:
    Keep a stack of indices whose temperatures are strictly decreasing
    (they are still "waiting" for a warmer day). When today is warmer than
    the day on top of the stack, today is that day's answer: pop and record.

When to use this pattern:
    "Next greater/smaller element", stock span, largest rectangle in
    histogram, trapping rain water, remove K digits.

Complexity:
    Time  O(n) - each index is pushed and popped once
    Space O(n)
"""
from typing import List


def daily_temperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack: List[int] = []  # indices, temps decreasing
    for i, t in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < t:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    return answer


if __name__ == "__main__":
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
    print("monotonic_stack: all tests passed")
