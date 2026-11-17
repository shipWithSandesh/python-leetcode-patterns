"""
Pattern: DP on Trees (post-order, return a state tuple per node)
Problem: LeetCode 337 - House Robber III  [Medium]
Link: https://leetcode.com/problems/house-robber-iii/

Question:
    Houses form a binary tree; each node holds money. Robbing two directly
    connected houses (parent and child) on the same night alerts the police.
    Return the maximum money that can be robbed.

Intuition:
    This is House Robber (LC 198, see dynamic_programming_1d.py) on a tree.
    For every node compute TWO answers bottom-up with a post-order DFS:
      rob     = node.val + (children's best when they are NOT robbed)
      not_rob = sum over children of max(child rob, child not_rob)
    Returning both values from each call means every node is solved once,
    with no memo dictionary needed.

When to use this pattern:
    Optimal value over a tree where a node's choice depends on its children:
    binary tree maximum path sum (LC 124), diameter of binary tree (LC 543),
    binary tree cameras (LC 968), longest univalue path.

Complexity:
    Time  O(n)  - each node visited once
    Space O(h)  - recursion depth, h = tree height
"""
from typing import Optional, Tuple


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def rob(root: Optional[TreeNode]) -> int:
    def dfs(node: Optional[TreeNode]) -> Tuple[int, int]:
        """Return (best if node is robbed, best if node is skipped)."""
        if node is None:
            return 0, 0
        left_rob, left_skip = dfs(node.left)
        right_rob, right_skip = dfs(node.right)
        rob_this = node.val + left_skip + right_skip
        skip_this = max(left_rob, left_skip) + max(right_rob, right_skip)
        return rob_this, skip_this

    return max(dfs(root))


if __name__ == "__main__":
    t1 = TreeNode(3, TreeNode(2, None, TreeNode(3)), TreeNode(3, None, TreeNode(1)))
    assert rob(t1) == 7
    t2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(3)), TreeNode(5, None, TreeNode(1)))
    assert rob(t2) == 9
    assert rob(None) == 0
    assert rob(TreeNode(5)) == 5
    # skipping two levels can beat alternating: 4 + 3 = 7 vs 1 + 2 = 3
    assert rob(TreeNode(4, TreeNode(1, TreeNode(2, TreeNode(3))))) == 7
    print("dp_on_trees: all tests passed")
