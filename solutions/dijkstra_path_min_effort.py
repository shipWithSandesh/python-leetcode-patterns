"""
Pattern: Dijkstra (grid, minimax path)
Problem: LeetCode 1631 - Path With Minimum Effort  [Medium]
Link: https://leetcode.com/problems/path-with-minimum-effort/

Question:
    Move from top-left to bottom-right of a height grid; effort of a path is the max absolute height difference between consecutive cells. Minimise it.

Intuition:
    Dijkstra where the "distance" is the max edge on the path so far: new_cost = max(cost, diff). Pop the cheapest cell from a min-heap and relax neighbours.

When to use this pattern:
    Shortest path where cost combines by max (bottleneck) or sum; weighted grids.

Complexity:
    Time O(mn log(mn)), space O(mn).
"""
from typing import List

import heapq


def minimum_effort_path(heights: List[List[int]]) -> int:
    m, n = len(heights), len(heights[0])
    dist = [[float("inf")] * n for _ in range(m)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]
    while heap:
        d, r, c = heapq.heappop(heap)
        if (r, c) == (m - 1, n - 1):
            return d
        if d > dist[r][c]:
            continue
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < m and 0 <= nc < n:
                nd = max(d, abs(heights[nr][nc] - heights[r][c]))
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(heap, (nd, nr, nc))
    return 0


if __name__ == "__main__":
    assert minimum_effort_path([[1, 2, 2], [3, 8, 2], [5, 3, 5]]) == 2
    assert minimum_effort_path([[1, 2, 3], [3, 8, 4], [5, 3, 5]]) == 1
    assert minimum_effort_path([[10]]) == 0
    print("dijkstra_path_min_effort.py: all tests passed")
