"""
Pattern: Linked List (Fast/Slow Pointers)
Problem: LeetCode 19 - Remove Nth Node From End of List  [Medium]
Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Question:
    Remove the n-th node from the end of a singly linked list and return the head.

Intuition:
    Advance a fast pointer n steps ahead of a slow pointer, then move both until fast reaches the end; slow sits just before the target. A dummy head handles removing the first node.

When to use this pattern:
    Position-from-the-end problems in one pass.

Complexity:
    Time O(L)
    Space O(1)
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast, slow = fast.next, slow.next
    slow.next = slow.next.next
    return dummy.next


def build(vals: List[int]) -> Optional[ListNode]:
    dummy = cur = ListNode()
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(node: Optional[ListNode]) -> List[int]:
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


if __name__ == "__main__":
    assert to_list(remove_nth_from_end(build([1,2,3,4,5]), 2)) == [1,2,3,5]
    assert to_list(remove_nth_from_end(build([1]), 1)) == []
    assert to_list(remove_nth_from_end(build([1,2]), 2)) == [2]
    print("linked_list_remove_nth_node: all tests passed")
