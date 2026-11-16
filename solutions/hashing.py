"""
Pattern: Hashing / Hash Map grouping
Problem: LeetCode 49 - Group Anagrams  [Medium]
Link: https://leetcode.com/problems/group-anagrams/

Question:
    Given an array of strings, group the anagrams together.
    Return the groups in any order.

Intuition:
    Anagrams share the same character counts. Build a key from the 26-letter
    count tuple (O(k) per word, faster than sorting each word, O(k log k)),
    and bucket every word under its key in a dict.

When to use this pattern:
    Two Sum, contains duplicate, valid anagram, longest consecutive sequence,
    any "have I seen this before / group by property" question.

Complexity:
    Time  O(n * k)  n words, k = max word length
    Space O(n * k)
"""
from collections import defaultdict
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = defaultdict(list)
    for word in strs:
        count = [0] * 26
        for ch in word:
            count[ord(ch) - ord("a")] += 1
        groups[tuple(count)].append(word)
    return list(groups.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    normalized = sorted(sorted(g) for g in result)
    assert normalized == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    assert group_anagrams([""]) == [[""]]
    print("hashing: all tests passed")
