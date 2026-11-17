"""
Pattern: Shortest Path in a Weighted Graph (Dijkstra)
Problem: LeetCode 743 - Network Delay Time  [Medium]
Link: https://leetcode.com/problems/network-delay-time/

Question:
    times[i] = (u, v, w): a signal takes w time from node u to node v.
    Nodes are 1..n. A signal is sent from node k. Return the time for all
    nodes to receive it, or -1 if some node can't be reached.

Intuition:
    Dijkstra: always expand the closest not-yet-finalized node using a
    min-heap of (distance, node). Skip stale heap entries. The answer is
    the largest shortest distance, if every node was reached.
    Works because all weights are non-negative.

When to use this pattern:
    Path with minimum effort, cheapest flights (Bellman-Ford/BFS variant),
    swim in rising water, any weighted shortest path.

Complexity:
    Time  O(E log V)
    Space O(V + E)
"""
import heapq
from collections import defaultdict
from typing import List


def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    dist = {}
    heap = [(0, k)]
    while heap:
        d, node = heapq.heappop(heap)
        if node in dist:
            continue  # stale entry
        dist[node] = d
        for nxt, w in graph[node]:
            if nxt not in dist:
                heapq.heappush(heap, (d + w, nxt))
    return max(dist.values()) if len(dist) == n else -1


if __name__ == "__main__":
    assert network_delay_time([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2
    assert network_delay_time([[1, 2, 1]], 2, 1) == 1
    assert network_delay_time([[1, 2, 1]], 2, 2) == -1
    print("dijkstra: all tests passed")
