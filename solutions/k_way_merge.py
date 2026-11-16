"""
Pattern: K-way Merge (Min-Heap)
Problem: LeetCode 23 - Merge k Sorted Lists  [Hard]
Link: https://leetcode.com/problems/merge-k-sorted-lists/

Question:
    You are given k sorted linked lists. Merge them into one sorted list.

Intuition:
    The next smallest node overall is always one of the k current heads.
    Keep the heads in a min-heap; pop the smallest, attach it, and push that
    node's next. Push (value, index, node) so ties never compare nodes.

When to use this pattern:
    Merge K sorted arrays, Kth smallest in a sorted matrix,
    smallest range covering K lists, find K pairs with smallest sums.

Complexity:
    Time  O(N log k)  N = total nodes
    Space O(k)
"""
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    dummy = ListNode()
    tail = dummy
    while heap:
        _, i, node = heapq.heappop(heap)
        tail.next = node
        tail = node
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    return dummy.next


def build(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    t = dummy
    for v in values:
        t.next = ListNode(v)
        t = t.next
    return dummy.next


def to_list(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    assert to_list(merge_k_lists(lists)) == [1, 1, 2, 3, 4, 4, 5, 6]
    assert to_list(merge_k_lists([])) == []
    assert to_list(merge_k_lists([None])) == []
    print("k_way_merge: all tests passed")
