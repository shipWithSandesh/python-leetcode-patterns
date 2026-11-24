"""
Pattern: DFS (graph copy with visited map)
Problem: LeetCode 133 - Clone Graph  [Medium]
Link: https://leetcode.com/problems/clone-graph/

Question:
    Return a deep copy of a connected undirected graph.

Intuition:
    Map each original node to its clone. On first visit create the clone and register it before recursing, so cycles reuse the existing clone.

When to use this pattern:
    Copying graphs or structures with cycles/shared references.

Complexity:
    Time  O(V + E)
    Space O(V)
"""
from typing import Dict, List, Optional


class Node:
    def __init__(self, val: int = 0, neighbors: "Optional[List[Node]]" = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def clone_graph(node: Optional[Node]) -> Optional[Node]:
    if not node:
        return None
    copies: Dict[Node, Node] = {}

    def dfs(n: Node) -> Node:
        if n in copies:
            return copies[n]
        c = Node(n.val)
        copies[n] = c
        c.neighbors = [dfs(m) for m in n.neighbors]
        return c

    return dfs(node)


if __name__ == "__main__":
    assert clone_graph(None) is None
    a, b, c = Node(1), Node(2), Node(3)
    a.neighbors, b.neighbors, c.neighbors = [b, c], [a, c], [a, b]
    x = clone_graph(a)
    assert x is not a and x.val == 1
    assert [n.val for n in x.neighbors] == [2, 3]
    assert x.neighbors[0].neighbors[0] is x  # cycle preserved
    s = clone_graph(Node(7))
    assert s.val == 7 and s.neighbors == []
    print("dfs_clone_graph.py: all tests passed")
