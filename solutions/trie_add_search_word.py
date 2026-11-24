"""
Pattern: Trie (with wildcard DFS)
Problem: LeetCode 211 - Design Add and Search Words Data Structure  [Medium]
Link: https://leetcode.com/problems/design-add-and-search-words-data-structure/

Question:
    Support add_word and search, where '.' in a query matches any letter.

Intuition:
    Store words in a trie. A normal letter follows one child; a '.' branches into every child via DFS.

When to use this pattern:
    Prefix/dictionary lookups with pattern matching.

Complexity:
    Time  add O(L); search O(L) typical, O(26^L) worst with many dots
    Space O(total characters)
"""
from typing import Dict


class WordDictionary:
    def __init__(self) -> None:
        self.root: Dict = {}

    def add_word(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word: str) -> bool:
        def dfs(i: int, node: Dict) -> bool:
            if i == len(word):
                return "$" in node
            ch = word[i]
            if ch == ".":
                return any(dfs(i + 1, c) for k, c in node.items() if k != "$")
            return ch in node and dfs(i + 1, node[ch])

        return dfs(0, self.root)


if __name__ == "__main__":
    d = WordDictionary()
    for w in ("bad", "dad", "mad"):
        d.add_word(w)
    assert not d.search("pad")
    assert d.search("bad") and d.search(".ad") and d.search("b..")
    assert not d.search("b.")
    assert not WordDictionary().search("a")
    print("trie_add_search_word.py: all tests passed")
