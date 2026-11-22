"""
Pattern: Trees (DFS)
Problem: LeetCode 226 - Invert Binary Tree  [Easy]
Link: https://leetcode.com/problems/invert-binary-tree/

Question:
Mirror a binary tree by swapping left and right children everywhere.

Intuition:
Recursively invert both subtrees, then swap them.

When to use this pattern:
Any problem where the answer is built from the answers of the subtrees.

Complexity:
Time O(n); space O(h).
"""

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val, self.left, self.right = val, left, right


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


def preorder(n: Optional[TreeNode]) -> list:
    return [] if n is None else [n.val] + preorder(n.left) + preorder(n.right)


if __name__ == "__main__":
    t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    assert preorder(invert_tree(t)) == [4, 7, 9, 6, 2, 3, 1]
    assert invert_tree(None) is None
    s = invert_tree(TreeNode(1, TreeNode(2)))
    assert s.left is None and s.right.val == 2
    print("tree_invert_binary_tree.py: all tests passed")
