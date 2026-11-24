"""
Pattern: DFS (reverse search from borders)
Problem: LeetCode 417 - Pacific Atlantic Water Flow  [Medium]
Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

Question:
    Find cells from which water can flow to both the Pacific (top/left) and Atlantic (bottom/right) oceans.

Intuition:
    Instead of flowing down from every cell, start at each ocean's border and climb uphill (>=). Cells reachable from both oceans are the answer.

When to use this pattern:
    Multi-source reachability on a grid; reverse the direction of the search.

Complexity:
    Time  O(m*n)
    Space O(m*n)
"""
from typing import List, Set, Tuple


def pacific_atlantic(h: List[List[int]]) -> List[List[int]]:
    if not h:
        return []
    m, n = len(h), len(h[0])

    def reach(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        seen = set(starts)
        stack = list(starts)
        while stack:
            r, c = stack.pop()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and h[nr][nc] >= h[r][c]:
                    seen.add((nr, nc))
                    stack.append((nr, nc))
        return seen

    pac = reach([(0, c) for c in range(n)] + [(r, 0) for r in range(m)])
    atl = reach([(m - 1, c) for c in range(n)] + [(r, n - 1) for r in range(m)])
    return sorted([r, c] for r, c in pac & atl)


if __name__ == "__main__":
    g = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    assert pacific_atlantic(g) == [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]]
    assert pacific_atlantic([[1]]) == [[0, 0]]
    assert pacific_atlantic([[2, 1], [1, 2]]) == [[0, 0], [0, 1], [1, 0], [1, 1]]
    print("dfs_pacific_atlantic.py: all tests passed")
