"""
Pattern: Design (augmented data structure)
Problem: LeetCode 155 - Min Stack  [Medium]
Link: https://leetcode.com/problems/min-stack/

Question:
    Design a stack supporting push, pop, top and get_min, all in O(1).

Intuition:
    A plain stack cannot tell you the minimum without scanning. Store, with
    every element, the minimum of the stack AT THE TIME it was pushed:
    (value, min_so_far). The minimum for the current stack is always the one
    stored with the top entry, and popping automatically restores the
    previous minimum. No extra scanning, no recomputation.

When to use this pattern:
    "Support operation X in O(1) on top of a classic structure":
    LRU Cache (LC 146), Max Stack (LC 716), Implement Queue using Stacks
    (LC 232).

Complexity:
    Time  O(1) for every operation
    Space O(n)  - one extra integer per element
"""
from typing import List, Tuple


class MinStack:
    def __init__(self) -> None:
        self._stack: List[Tuple[int, int]] = []     # (value, min up to here)

    def push(self, val: int) -> None:
        current_min = min(val, self._stack[-1][1]) if self._stack else val
        self._stack.append((val, current_min))

    def pop(self) -> None:
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1][0]

    def get_min(self) -> int:
        return self._stack[-1][1]


if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.get_min() == -3
    s.pop()
    assert s.top() == 0
    assert s.get_min() == -2
    s.push(-2)
    s.push(5)
    assert s.get_min() == -2
    s.pop()
    s.pop()
    assert s.get_min() == -2
    s2 = MinStack()
    s2.push(1)
    assert s2.top() == 1 and s2.get_min() == 1
    print("design_min_stack.py: all tests passed")
