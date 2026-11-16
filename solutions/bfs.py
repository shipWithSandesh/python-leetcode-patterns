"""
Pattern: Breadth-First Search (multi-source BFS on a grid)
Problem: LeetCode 994 - Rotting Oranges  [Medium]
Link: https://leetcode.com/problems/rotting-oranges/

Question:
    Grid cells: 0 empty, 1 fresh orange, 2 rotten orange. Every minute,
    fresh oranges next to a rotten one (up/down/left/right) become rotten.
    Return the minimum minutes until no fresh orange remains, or -1.

Intuition:
    All rotten oranges spread at the same time, so start BFS from ALL of them
    at once (multi-source). Each BFS level = one minute. Count fresh oranges;
    if any remain after BFS, return -1.

When to use this pattern:
    Shortest path in an unweighted graph/grid, level-order traversal,
    word ladder, 01-matrix, walls and gates.

Complexity:
    Time  O(rows * cols)
    Space O(rows * cols)
"""
from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1
    minutes = 0
    while queue and fresh:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1


if __name__ == "__main__":
    assert oranges_rotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]) == 4
    assert oranges_rotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]) == -1
    assert oranges_rotting([[0, 2]]) == 0
    print("bfs: all tests passed")
