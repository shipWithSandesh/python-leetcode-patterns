"""
Pattern: Trees (DFS)
Problem: LeetCode 236 - Lowest Common Ancestor of a Binary Tree  [Medium]
Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Question:
    Find the lowest node in a binary tree that has both p and q as descendants (a node may be its own descendant).

Intuition:
    DFS returning a node if it is p or q, else whatever the children found. If both left and right return non-null, the current node is the split point, i.e. the LCA.

When to use this pattern:
    Ancestor/path questions on trees; combine child results post-order.

Complexity:
    Time O(n)
    Space O(h)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    if root is None or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right


if __name__ == "__main__":
    n = {i: TreeNode(i) for i in (3, 5, 1, 6, 2, 0, 8, 7, 4)}
    n[3].left, n[3].right = n[5], n[1]
    n[5].left, n[5].right = n[6], n[2]
    n[2].left, n[2].right = n[7], n[4]
    n[1].left, n[1].right = n[0], n[8]
    assert lowest_common_ancestor(n[3], n[5], n[1]) is n[3]
    assert lowest_common_ancestor(n[3], n[5], n[4]) is n[5]
    assert lowest_common_ancestor(n[3], n[7], n[8]) is n[3]
    assert lowest_common_ancestor(n[3], n[6], n[4]) is n[5]
    print("tree_lowest_common_ancestor: all tests passed")
