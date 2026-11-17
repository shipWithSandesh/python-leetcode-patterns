"""
Pattern: Design (combine data structures to hit O(1) operations)
Problem: LeetCode 146 - LRU Cache  [Medium]
Link: https://leetcode.com/problems/lru-cache/

Question:
    Design a Least Recently Used cache with a fixed capacity:
    - get(key): return the value if present (and mark it as recently used),
      else -1.
    - put(key, value): insert or update; if over capacity, evict the least
      recently used key.
    Both operations must run in O(1) average time.

Intuition:
    A hash map gives O(1) lookup but no order; a doubly linked list gives
    O(1) reordering but no lookup. Use both: the map points key -> list
    node, and the list keeps nodes from least to most recently used.
    Dummy head/tail nodes remove all the edge cases.
    (In Python, collections.OrderedDict does exactly this internally - shown
    below as the short version; interviewers usually want the manual one.)

When to use this pattern:
    Design questions: LFU cache (LC 460), min stack (LC 155), time-based
    key-value store (LC 981), design Twitter (LC 355), randomized set (LC 380).

Complexity:
    Time  O(1) for get and put
    Space O(capacity)
"""
from collections import OrderedDict
from typing import Dict, Optional


class _Node:
    def __init__(self, key: int = 0, value: int = 0) -> None:
        self.key = key
        self.value = value
        self.prev: Optional["_Node"] = None
        self.next: Optional["_Node"] = None


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.map: Dict[int, _Node] = {}
        self.head = _Node()  # least recently used side
        self.tail = _Node()  # most recently used side
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: _Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def _append(self, node: _Node) -> None:
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        node = self.map.get(key)
        if node is None:
            return -1
        self._remove(node)
        self._append(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self._remove(self.map[key])
        node = _Node(key, value)
        self.map[key] = node
        self._append(node)
        if len(self.map) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.map[lru.key]


class LRUCacheOrderedDict:
    """Short version using OrderedDict (move_to_end + popitem(last=False))."""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache: "OrderedDict[int, int]" = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


if __name__ == "__main__":
    for cls in (LRUCache, LRUCacheOrderedDict):
        c = cls(2)
        c.put(1, 1)
        c.put(2, 2)
        assert c.get(1) == 1
        c.put(3, 3)            # evicts key 2
        assert c.get(2) == -1
        c.put(4, 4)            # evicts key 1
        assert c.get(1) == -1
        assert c.get(3) == 3
        assert c.get(4) == 4

        one = cls(1)
        one.put(1, 10)
        one.put(1, 20)         # update, no eviction
        assert one.get(1) == 20
        one.put(2, 30)
        assert one.get(1) == -1 and one.get(2) == 30
    print("design: all tests passed")
