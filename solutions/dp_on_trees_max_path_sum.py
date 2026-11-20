"""
Pattern: DP on Trees (post-order DFS)
Problem: LeetCode 124 - Binary Tree Maximum Path Sum  [Hard]
Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

Question:
    Find the maximum sum of any non-empty path in a binary tree (path need not pass the root).

Intuition:
    Post-order: each node returns the best downward gain (node + max(0, best child gain)). The best path bending at the node is node + left gain + right gain; track the global max. Negative gains are dropped.

When to use this pattern:
    Tree problems where the answer can bend at any node (diameter, longest univalue path).

Complexity:
    Time O(n), space O(h).
"""
from typing import List

from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val, self.left, self.right = val, left, right


def max_path_sum(root: Optional[TreeNode]) -> int:
    best = float("-inf")

    def gain(node: Optional[TreeNode]) -> int:
        nonlocal best
        if not node:
            return 0
        l, r = max(gain(node.left), 0), max(gain(node.right), 0)
        best = max(best, node.val + l + r)
        return node.val + max(l, r)

    gain(root)
    return int(best)


if __name__ == "__main__":
    assert max_path_sum(TreeNode(1, TreeNode(2), TreeNode(3))) == 6
    t = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_path_sum(t) == 42
    assert max_path_sum(TreeNode(-3)) == -3
    print("dp_on_trees_max_path_sum.py: all tests passed")
