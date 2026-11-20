"""
Pattern: Backtracking (grid DFS)
Problem: LeetCode 79 - Word Search  [Medium]
Link: https://leetcode.com/problems/word-search/

Question:
    Given a grid of letters and a word, return True if the word can be traced through adjacent cells without reusing a cell.

Intuition:
    DFS from every cell matching word[0]. Mark the current cell as visited (temporarily overwrite it), recurse into 4 neighbours for the next letter, then restore it (backtrack).

When to use this pattern:
    Path search in a grid/graph where a cell cannot be reused in the same path.

Complexity:
    Time O(m*n*3^L), space O(L) recursion.
"""
from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    m, n = len(board), len(board[0])

    def dfs(r: int, c: int, i: int) -> bool:
        if i == len(word):
            return True
        if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[i]:
            return False
        tmp, board[r][c] = board[r][c], "#"
        found = any(dfs(r + dr, c + dc, i + 1) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)))
        board[r][c] = tmp
        return found

    return any(dfs(r, c, 0) for r in range(m) for c in range(n))


if __name__ == "__main__":
    b = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    assert exist(b, "ABCCED")
    assert exist(b, "SEE")
    assert not exist(b, "ABCB")
    assert exist([["a"]], "a")
    print("backtracking_word_search.py: all tests passed")
