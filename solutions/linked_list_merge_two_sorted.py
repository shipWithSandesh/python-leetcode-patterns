"""
Pattern: Linked List
Problem: LeetCode 21 - Merge Two Sorted Lists  [Easy]
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Question:
Merge two sorted linked lists into one sorted list.

Intuition:
Use a dummy head and a tail pointer; repeatedly attach the smaller head, then attach the leftover list.

When to use this pattern:
Combining sorted sequences; basis for merge sort and k-way merge.

Complexity:
Time O(m+n); space O(1).
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val, self.next = val, next


def merge_two_lists(a: Optional[ListNode], b: Optional[ListNode]) -> Optional[ListNode]:
    dummy = tail = ListNode()
    while a and b:
        if a.val <= b.val:
            tail.next, a = a, a.next
        else:
            tail.next, b = b, b.next
        tail = tail.next
    tail.next = a or b
    return dummy.next


def build(xs: list) -> Optional[ListNode]:
    head = None
    for x in reversed(xs):
        head = ListNode(x, head)
    return head


def to_list(n: Optional[ListNode]) -> list:
    out = []
    while n:
        out.append(n.val)
        n = n.next
    return out


if __name__ == "__main__":
    assert to_list(merge_two_lists(build([1, 2, 4]), build([1, 3, 4]))) == [1, 1, 2, 3, 4, 4]
    assert to_list(merge_two_lists(None, None)) == []
    assert to_list(merge_two_lists(None, build([0]))) == [0]
    print("linked_list_merge_two_sorted.py: all tests passed")
