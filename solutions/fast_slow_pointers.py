"""
Pattern: Fast & Slow Pointers (Floyd's Tortoise and Hare)
Problem: LeetCode 142 - Linked List Cycle II  [Medium]
Link: https://leetcode.com/problems/linked-list-cycle-ii/

Question:
    Given the head of a linked list, return the node where the cycle begins.
    If there is no cycle, return None. Use O(1) memory.

Intuition:
    1. Move slow by 1 and fast by 2. If they meet, a cycle exists.
    2. Math: distance(head -> cycle start) == distance(meeting point -> cycle
       start) moving forward. So reset one pointer to head and move both by 1;
       where they meet again is the cycle start.

When to use this pattern:
    Cycle detection, middle of a linked list, happy number,
    palindrome linked list, find the duplicate number (LC 287).

Complexity:
    Time  O(n)
    Space O(1)
"""
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "Optional[ListNode]" = None):
        self.val = val
        self.next = next


def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            slow = head
            while slow is not fast:
                slow = slow.next
                fast = fast.next
            return slow
    return None


if __name__ == "__main__":
    nodes = [ListNode(v) for v in [3, 2, 0, -4]]
    for a, b in zip(nodes, nodes[1:]):
        a.next = b
    nodes[-1].next = nodes[1]
    assert detect_cycle(nodes[0]) is nodes[1]
    single = ListNode(1)
    assert detect_cycle(single) is None
    print("fast_slow_pointers: all tests passed")
