"""
Pattern: Bellman-Ford (bounded edges)
Problem: LeetCode 787 - Cheapest Flights Within K Stops  [Medium]
Link: https://leetcode.com/problems/cheapest-flights-within-k-stops/

Question:
    Find the cheapest price from src to dst with at most k stops, or -1.

Intuition:
    Run k+1 rounds of Bellman-Ford relaxation, each using a copy of the previous round so a round only extends paths by one flight. This enforces the stop limit that plain Dijkstra ignores.

When to use this pattern:
    Shortest path with a limit on number of edges.

Complexity:
    Time O(k*E), space O(V).
"""
from typing import List

def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    INF = float("inf")
    dist = [INF] * n
    dist[src] = 0
    for _ in range(k + 1):
        nxt = dist[:]
        for u, v, w in flights:
            if dist[u] + w < nxt[v]:
                nxt[v] = dist[u] + w
        dist = nxt
    return -1 if dist[dst] == INF else int(dist[dst])


if __name__ == "__main__":
    f = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    assert find_cheapest_price(4, f, 0, 3, 1) == 700
    assert find_cheapest_price(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1) == 200
    assert find_cheapest_price(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0) == 500
    assert find_cheapest_price(2, [], 0, 1, 1) == -1
    print("graph_bellman_ford_cheapest_flights.py: all tests passed")
