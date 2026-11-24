"""
Pattern: Trees (bottom-up DFS with early exit)
Problem: LeetCode 110 - Balanced Binary Tree  [Easy]
Link: https://leetcode.com/problems/balanced-binary-tree/

Question:
    Check that every node's subtrees differ in height by at most 1.

Intuition:
    Compute heights bottom-up and return -1 as a sentinel the moment any subtree is unbalanced, avoiding the O(n^2) top-down recompute.

When to use this pattern:
    Tree property checks that combine child results.

Complexity:
    Time  O(n)
    Space O(h)
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val, self.left, self.right = val, left, right


def is_balanced(root: Optional[TreeNode]) -> bool:
    def height(n: Optional[TreeNode]) -> int:
        if not n:
            return 0
        l = height(n.left)
        if l < 0:
            return -1
        r = height(n.right)
        if r < 0 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)

    return height(root) >= 0


if __name__ == "__main__":
    assert is_balanced(None)
    assert is_balanced(TreeNode(1, TreeNode(2), TreeNode(3)))
    t = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2))
    assert not is_balanced(t)
    assert is_balanced(TreeNode(1))
    print("tree_balanced.py: all tests passed")
