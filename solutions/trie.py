"""
Pattern: Trie (Prefix Tree)
Problem: LeetCode 208 - Implement Trie (Prefix Tree)  [Medium]
Link: https://leetcode.com/problems/implement-trie-prefix-tree/

Question:
    Implement insert(word), search(word) -> bool (exact word),
    and startsWith(prefix) -> bool.

Intuition:
    Each node holds a dict of children (char -> node) and a flag marking the
    end of a word. Words sharing a prefix share the same path, so lookups
    cost O(length of word), regardless of how many words are stored.

When to use this pattern:
    Autocomplete, word search II, replace words, longest common prefix,
    design add-and-search words.

Complexity:
    Time  O(L) per operation, L = word length
    Space O(total characters inserted)
"""


class TrieNode:
    __slots__ = ("children", "is_end")

    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_end = True

    def _walk(self, s: str):
        node = self.root
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_end

    def startsWith(self, prefix: str) -> bool:  # LeetCode's method name
        return self._walk(prefix) is not None


if __name__ == "__main__":
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.startsWith("app") is True
    t.insert("app")
    assert t.search("app") is True
    print("trie: all tests passed")
