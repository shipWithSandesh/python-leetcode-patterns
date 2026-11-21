"""
Pattern: Trees (DFS, return height / track global)
Problem: LeetCode 543 - Diameter of Binary Tree  [Easy]
Link: https://leetcode.com/problems/diameter-of-binary-tree/

Question:
    Return the length (in edges) of the longest path between any two nodes.

Intuition:
    The longest path through a node is left height + right height. DFS returns each node's height while updating a global best with that sum.

When to use this pattern:
    Path problems where the answer 'bends' at a node but the return value goes one way: Max Path Sum (LC 124).

Complexity:
    Time O(n), Space O(h) recursion
"""
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val, self.left, self.right = val, left, right


def diameter_of_binary_tree(root: Optional[TreeNode]) -> int:
    best = 0

    def height(node: Optional[TreeNode]) -> int:
        nonlocal best
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)
        return 1 + max(l, r)

    height(root)
    return best


if __name__ == "__main__":
    t = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert diameter_of_binary_tree(t) == 3
    assert diameter_of_binary_tree(TreeNode(1, TreeNode(2))) == 1
    assert diameter_of_binary_tree(TreeNode(1)) == 0
    assert diameter_of_binary_tree(None) == 0
    print("tree_diameter.py: all tests passed")
