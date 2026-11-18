"""
Pattern: Monotonic Stack (increasing heights, resolve on pop)
Problem: LeetCode 84 - Largest Rectangle in Histogram  [Hard]
Link: https://leetcode.com/problems/largest-rectangle-in-histogram/

Question:
    Given bar heights of a histogram (each bar has width 1), return the
    area of the largest rectangle that fits inside it.

Intuition:
    For each bar, the best rectangle using it as the shortest bar extends
    left and right until a shorter bar is hit. A stack of indices with
    increasing heights finds both borders in one pass: when a bar shorter
    than the stack top arrives, the top's right border is found (current
    index) and its left border is the new top beneath it. Pop, compute
    height * width, repeat. A sentinel height 0 at the end flushes the stack.

When to use this pattern:
    "Nearest smaller/greater element on either side": Daily Temperatures
    (LC 739), Maximal Rectangle (LC 85), Trapping Rain Water (LC 42).

Complexity:
    Time  O(n)  - every index is pushed and popped once
    Space O(n)  - the stack
"""
from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    stack: List[int] = []           # indices, heights strictly non-decreasing
    best = 0
    for i, h in enumerate(heights + [0]):           # sentinel flushes the stack
        while stack and heights[stack[-1]] >= h:
            height = heights[stack.pop()]
            left_border = stack[-1] if stack else -1
            best = max(best, height * (i - left_border - 1))
        stack.append(i)
    return best


if __name__ == "__main__":
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([]) == 0
    assert largest_rectangle_area([5]) == 5
    assert largest_rectangle_area([1, 1, 1, 1]) == 4
    assert largest_rectangle_area([6, 5, 4, 3, 2, 1]) == 12
    print("monotonic_stack_largest_rectangle.py: all tests passed")
