"""
Pattern: Linked List (reversal in groups)
Problem: LeetCode 25 - Reverse Nodes in k-Group  [Hard]
Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

Question:
    Reverse the nodes of a linked list k at a time; leftover nodes (fewer than k) stay as they are.

Intuition:
    For each group, first check k nodes exist. Reverse those k nodes in place, then connect the previous group's tail to the new head and the new tail to the rest. A dummy head simplifies the first group.

When to use this pattern:
    Pointer surgery on sublists: Reverse Linked List (LC 206), Reorder List (LC 143).

Complexity:
    Time O(n), Space O(1)
"""
from typing import List, Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None) -> None:
        self.val, self.next = val, next


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    group_prev = dummy
    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next
        group_next = kth.next
        prev, cur = group_next, group_prev.next
        while cur is not group_next:
            cur.next, prev, cur = prev, cur, cur.next
        tail = group_prev.next
        group_prev.next = kth
        group_prev = tail


def _build(a: List[int]) -> Optional[ListNode]:
    d = ListNode()
    c = d
    for x in a:
        c.next = ListNode(x)
        c = c.next
    return d.next


def _list(n: Optional[ListNode]) -> List[int]:
    out = []
    while n:
        out.append(n.val)
        n = n.next
    return out


if __name__ == "__main__":
    assert _list(reverse_k_group(_build([1, 2, 3, 4, 5]), 2)) == [2, 1, 4, 3, 5]
    assert _list(reverse_k_group(_build([1, 2, 3, 4, 5]), 3)) == [3, 2, 1, 4, 5]
    assert _list(reverse_k_group(_build([1]), 1)) == [1]
    assert reverse_k_group(None, 2) is None
    print("linked_list_reverse_k_group.py: all tests passed")
