"""
Pattern: Union-Find (Disjoint Set Union)
Problem: LeetCode 547 - Number of Provinces  [Medium]
Link: https://leetcode.com/problems/number-of-provinces/

Question:
    isConnected[i][j] = 1 if city i and city j are directly connected.
    A province is a group of directly or indirectly connected cities.
    Return the number of provinces.

Intuition:
    Start with every city as its own group (n groups). For every connected
    pair, union their groups; each successful union reduces the count by 1.
    Path compression + union by rank make each operation almost O(1).

When to use this pattern:
    Redundant connection, accounts merge, number of connected components,
    graph valid tree, Kruskal's minimum spanning tree.

Complexity:
    Time  O(n^2 * alpha(n))  (alpha is the near-constant inverse Ackermann)
    Space O(n)
"""
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x: int) -> int:
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]  # path compression
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True


def find_circle_num(is_connected: List[List[int]]) -> int:
    n = len(is_connected)
    uf = UnionFind(n)
    for i in range(n):
        for j in range(i + 1, n):
            if is_connected[i][j]:
                uf.union(i, j)
    return uf.count


if __name__ == "__main__":
    assert find_circle_num([[1, 1, 0], [1, 1, 0], [0, 0, 1]]) == 2
    assert find_circle_num([[1, 0, 0], [0, 1, 0], [0, 0, 1]]) == 3
    print("union_find: all tests passed")
