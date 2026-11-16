"""
Pattern: Tree DFS (in-order traversal with bounds)
Problem: LeetCode 98 - Validate Binary Search Tree  [Medium]
Link: https://leetcode.com/problems/validate-binary-search-tree/

Question:
    Given the root of a binary tree, determine if it is a valid BST:
    every node's left subtree has smaller values, right subtree larger,
    and both subtrees are BSTs too.

Intuition:
    Checking only the direct children is a classic trap. Instead pass down
    the allowed (low, high) range: going left tightens high, going right
    tightens low. (Equivalent idea: an in-order traversal of a BST is
    strictly increasing.)

When to use this pattern:
    Max depth, diameter, path sum, lowest common ancestor,
    kth smallest in BST, serialize/deserialize a tree.

Complexity:
    Time  O(n)
    Space O(h) for the stack, h = tree height
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    stack = [(root, float("-inf"), float("inf"))]
    while stack:
        node, low, high = stack.pop()
        if not node:
            continue
        if not (low < node.val < high):
            return False
        stack.append((node.left, low, node.val))
        stack.append((node.right, node.val, high))
    return True


if __name__ == "__main__":
    assert is_valid_bst(TreeNode(2, TreeNode(1), TreeNode(3))) is True
    bad = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(bad) is False
    trap = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    assert is_valid_bst(trap) is False
    print("tree_traversal: all tests passed")
