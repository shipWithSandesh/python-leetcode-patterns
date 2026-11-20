"""
Pattern: Union Find (cycle detection)
Problem: LeetCode 684 - Redundant Connection  [Medium]
Link: https://leetcode.com/problems/redundant-connection/

Question:
    A tree with n nodes had one extra edge added. Return the edge that can be removed to restore a tree (the last such edge in input).

Intuition:
    Process edges in order, union endpoints. The first edge whose endpoints already share a root closes a cycle, so it is redundant.

When to use this pattern:
    Detecting cycles in undirected graphs, connected components, Kruskal-style problems.

Complexity:
    Time O(n * alpha(n)), space O(n).
"""
from typing import List

def find_redundant_connection(edges: List[List[int]]) -> List[int]:
    parent = list(range(len(edges) + 1))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return [a, b]
        parent[ra] = rb
    return []


if __name__ == "__main__":
    assert find_redundant_connection([[1, 2], [1, 3], [2, 3]]) == [2, 3]
    assert find_redundant_connection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]) == [1, 4]
    assert find_redundant_connection([[1, 2], [2, 3], [1, 3]]) == [1, 3]
    print("union_find_redundant_connection.py: all tests passed")
