"""
Pattern: Trees (BST / Inorder)
Problem: LeetCode 230 - Kth Smallest Element in a BST  [Medium]
Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Question:
Return the k-th smallest value (1-indexed) in a binary search tree.

Intuition:
Inorder traversal of a BST visits values in sorted order. Walk iteratively with a stack and stop at the k-th visit.

When to use this pattern:
Order statistics on BSTs; any time sorted order is needed from a BST.

Complexity:
Time O(h + k), Space O(h).
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val, self.left, self.right = val, left, right


def kth_smallest(root: Optional[TreeNode], k: int) -> int:
    stack: List[TreeNode] = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
    raise ValueError("k out of range")


if __name__ == "__main__":
    t = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    assert kth_smallest(t, 1) == 1
    assert kth_smallest(t, 3) == 3
    assert kth_smallest(t, 4) == 4
    assert kth_smallest(TreeNode(5), 1) == 5
    print("tree_kth_smallest_bst.py: all tests passed")
