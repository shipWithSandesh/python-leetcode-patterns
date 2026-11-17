"""
Pattern: Breadth-First Search (level by level on a tree)
Problem: LeetCode 102 - Binary Tree Level Order Traversal  [Medium]
Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

Question:
    Given the root of a binary tree, return its node values level by level,
    from left to right, as a list of lists.

Intuition:
    A queue processes nodes in the order they were discovered, which is
    exactly level order. The trick to separate levels: at the start of each
    round, the queue holds ONE full level. Record its size, pop exactly that
    many nodes, and push their children - those form the next level.

When to use this pattern:
    Anything "per level" on a tree: right side view (LC 199), zigzag order
    (LC 103), level averages (LC 637), minimum depth (LC 111), connecting
    next pointers (LC 116).

Complexity:
    Time  O(n)  - each node is visited once
    Space O(w)  - w = maximum width of the tree (queue size)
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    if root is None:
        return []
    result: List[List[int]] = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result


if __name__ == "__main__":
    tree = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(tree) == [[3], [9, 20], [15, 7]]
    assert level_order(TreeNode(1)) == [[1]]
    assert level_order(None) == []
    skewed = TreeNode(1, TreeNode(2, TreeNode(3)))
    assert level_order(skewed) == [[1], [2], [3]]
    print("bfs_binary_tree_level_order: all tests passed")
