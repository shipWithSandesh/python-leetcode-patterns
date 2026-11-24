"""
Pattern: Design (array + hash map)
Problem: LeetCode 380 - Insert Delete GetRandom O(1)  [Medium]
Link: https://leetcode.com/problems/insert-delete-getrandom-o1/

Question:
    Design a set with average O(1) insert, remove and getRandom.

Intuition:
    An array gives O(1) random pick; a hash map gives O(1) lookup of an element's index. To delete, swap the element with the last one, pop the tail, and fix the map.

When to use this pattern:
    Need O(1) random access together with O(1) delete.

Complexity:
    Time  O(1) average per operation
    Space O(n)
"""
import random
from typing import Dict, List


class RandomizedSet:
    def __init__(self) -> None:
        self.vals: List[int] = []
        self.pos: Dict[int, int] = {}

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        idx, last = self.pos[val], self.vals[-1]
        self.vals[idx] = last
        self.pos[last] = idx
        self.vals.pop()
        del self.pos[val]
        return True

    def get_random(self) -> int:
        return random.choice(self.vals)


if __name__ == "__main__":
    s = RandomizedSet()
    assert s.insert(1) and not s.insert(1)
    assert not s.remove(2)
    assert s.insert(2) and s.remove(1)
    assert s.get_random() == 2
    assert s.insert(3) and s.remove(3) and s.remove(2) and not s.vals
    print("design_randomized_set.py: all tests passed")
