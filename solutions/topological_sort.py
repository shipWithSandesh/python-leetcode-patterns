"""
Pattern: Topological Sort (Kahn's algorithm, BFS)
Problem: LeetCode 207 - Course Schedule  [Medium]
Link: https://leetcode.com/problems/course-schedule/

Question:
    There are numCourses courses. prerequisites[i] = [a, b] means you must
    take b before a. Return True if you can finish all courses.

Intuition:
    Courses are nodes, prerequisites are edges b -> a. You can finish all
    courses only if the graph has no cycle. Kahn's algorithm: repeatedly
    take a course with in-degree 0 and remove its edges. If we take all
    courses, there's no cycle.

When to use this pattern:
    Course schedule II (return the order), alien dictionary,
    build/task dependency order, parallel courses.

Complexity:
    Time  O(V + E)
    Space O(V + E)
"""
from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, pre in prerequisites:
        graph[pre].append(course)
        indegree[course] += 1
    queue = deque(i for i in range(num_courses) if indegree[i] == 0)
    taken = 0
    while queue:
        node = queue.popleft()
        taken += 1
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return taken == num_courses


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]]) is True
    assert can_finish(2, [[1, 0], [0, 1]]) is False
    assert can_finish(4, [[1, 0], [2, 1], [3, 2]]) is True
    print("topological_sort: all tests passed")
