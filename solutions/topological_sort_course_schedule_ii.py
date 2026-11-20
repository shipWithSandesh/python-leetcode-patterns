"""
Pattern: Topological Sort (Kahn BFS)
Problem: LeetCode 210 - Course Schedule II  [Medium]
Link: https://leetcode.com/problems/course-schedule-ii/

Question:
    Return a valid order to take numCourses given prerequisite pairs [a, b] (b before a), or [] if impossible.

Intuition:
    Build the graph and in-degrees. Start with zero in-degree courses, pop one, append to order, and decrement neighbours. If the order has fewer than numCourses entries, there is a cycle.

When to use this pattern:
    Ordering with dependencies: build order, task scheduling, cycle detection in directed graphs.

Complexity:
    Time O(V+E), space O(V+E).
"""
from typing import List

from collections import deque


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(num_courses)]
    indeg = [0] * num_courses
    for a, b in prerequisites:
        adj[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(num_courses) if indeg[i] == 0)
    order: List[int] = []
    while q:
        u = q.popleft()
        order.append(u)
        for v in adj[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return order if len(order) == num_courses else []


if __name__ == "__main__":
    assert find_order(2, [[1, 0]]) == [0, 1]
    o = find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
    assert o[0] == 0 and o[-1] == 3 and len(o) == 4
    assert find_order(2, [[1, 0], [0, 1]]) == []
    assert find_order(1, []) == [0]
    print("topological_sort_course_schedule_ii.py: all tests passed")
