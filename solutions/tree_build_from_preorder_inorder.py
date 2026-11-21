"""
Pattern: Trees (divide and conquer)
Problem: LeetCode 105 - Construct Binary Tree from Preorder and Inorder Traversal  [Medium]
Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

Question:
    Rebuild a binary tree from its preorder and inorder traversals (unique values).

Intuition:
    The first preorder value is the root. Its position in inorder splits left and right subtrees; the left size tells how many preorder items belong to the left. A hashmap gives O(1) index lookup.

When to use this pattern:
    Reconstructing structures from traversals: Serialize/Deserialize (LC 297), Postorder+Inorder (LC 106).

Complexity:
    Time O(n), Space O(n)
"""
from typing import Dict, List, Optional


class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None,
                 right: "Optional[TreeNode]" = None) -> None:
        self.val, self.left, self.right = val, left, right


def build_tree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    idx: Dict[int, int] = {v: i for i, v in enumerate(inorder)}
    pos = 0

    def build(lo: int, hi: int) -> Optional[TreeNode]:
        nonlocal pos
        if lo > hi:
            return None
        val = preorder[pos]
        pos += 1
        node = TreeNode(val)
        m = idx[val]
        node.left = build(lo, m - 1)
        node.right = build(m + 1, hi)
        return node

    return build(0, len(inorder) - 1)


def _pre(n: Optional[TreeNode]) -> List[int]:
    return [] if not n else [n.val] + _pre(n.left) + _pre(n.right)


def _ino(n: Optional[TreeNode]) -> List[int]:
    return [] if not n else _ino(n.left) + [n.val] + _ino(n.right)


if __name__ == "__main__":
    p, i = [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]
    t = build_tree(p, i)
    assert _pre(t) == p and _ino(t) == i
    assert build_tree([], []) is None
    t = build_tree([1], [1])
    assert t.val == 1 and t.left is None and t.right is None
    p, i = [1, 2, 3], [3, 2, 1]
    t = build_tree(p, i)
    assert _pre(t) == p and _ino(t) == i
    print("tree_build_from_preorder_inorder.py: all tests passed")
