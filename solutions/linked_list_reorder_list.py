"""
Pattern: Linked List (fast/slow, reverse, merge)
Problem: LeetCode 143 - Reorder List  [Medium]
Link: https://leetcode.com/problems/reorder-list/

Question:
    Reorder L0->L1->...->Ln into L0->Ln->L1->Ln-1->... in place.

Intuition:
    Three classic steps combined: find the middle with fast/slow pointers, reverse the second half, then interleave the two halves node by node.

When to use this pattern:
    In-place list rearrangement that needs access from both ends.

Complexity:
    Time  O(n) - three linear passes
    Space O(1)
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def reorder_list(head: Optional[ListNode]) -> None:
    if not head or not head.next:
        return
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
    prev, cur = None, slow.next
    slow.next = None
    while cur:
        cur.next, prev, cur = prev, cur, cur.next
    a, b = head, prev
    while b:
        a.next, b.next, a, b = b, a.next, a.next, b.next


def build(vals: List[int]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    for v in vals:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(n: Optional[ListNode]) -> List[int]:
    out = []
    while n:
        out.append(n.val)
        n = n.next
    return out


if __name__ == "__main__":
    for inp, exp in [([1, 2, 3, 4], [1, 4, 2, 3]), ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]), ([1], [1]), ([1, 2], [1, 2])]:
        h = build(inp)
        reorder_list(h)
        assert to_list(h) == exp
    print("linked_list_reorder_list.py: all tests passed")
