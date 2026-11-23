"""
Pattern: BFS (level order)
Problem: LeetCode 199 - Binary Tree Right Side View  [Medium]
Link: https://leetcode.com/problems/binary-tree-right-side-view/

Question:
Return the values visible when looking at a binary tree from its right side, top to bottom.

Intuition:
Process the tree level by level; the last node of each level is the one visible from the right.

When to use this pattern:
Anything level-based: per-level aggregates, shortest steps in unweighted graphs.

Complexity:
Time O(n), Space O(w) where w is the max width.
"""
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val, self.left, self.right = val, left, right


def right_side_view(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    res: List[int] = []
    q = deque([root])
    while q:
        res.append(q[-1].val)  # last node of the level
        for _ in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res


if __name__ == "__main__":
    t = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
    assert right_side_view(t) == [1, 3, 4]
    assert right_side_view(None) == []
    assert right_side_view(TreeNode(1, TreeNode(2))) == [1, 2]
    print("bfs_right_side_view.py: all tests passed")
