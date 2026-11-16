"""
Pattern: In-place Linked List Reversal
Problem: LeetCode 206 - Reverse Linked List  [Easy]
Link: https://leetcode.com/problems/reverse-linked-list/

Question:
    Given the head of a singly linked list, reverse it and return the new head.

Intuition:
    Walk the list keeping three references: prev, curr, next.
    Point curr.next back to prev, then shift everything one step forward.
    Save next BEFORE you overwrite curr.next, or you lose the rest of the list.

When to use this pattern:
    Reverse a sub-list (LC 92), reverse in k-groups (LC 25),
    palindrome linked list, reorder list.

Complexity:
    Time  O(n)
    Space O(1) iterative (the recursive version uses O(n) stack)
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def build(values: List[int]) -> Optional[ListNode]:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: Optional[ListNode]) -> List[int]:
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


if __name__ == "__main__":
    assert to_list(reverse_list(build([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert to_list(reverse_list(build([1, 2]))) == [2, 1]
    assert to_list(reverse_list(build([]))) == []
    print("linked_list_reversal: all tests passed")
