# Python LeetCode Patterns

LeetCode problems solved in Python, organised by **pattern** so you learn the *idea* once and reuse it everywhere.

Every file has:
- the problem statement and LeetCode link
- the intuition, explained in plain words
- when to use the pattern
- the best (optimal) solution in clean Python
- time and space complexity
- runnable tests: `python solutions/<file>.py`

New problems are added daily.

## Run all tests

```bash
for f in solutions/*.py; do python "$f"; done
```

## Patterns

| # | File | Pattern | Problem | Difficulty |
|---|------|---------|---------|------------|
| 1 | two_pointer.py | Two Pointers | 167. Two Sum II | Medium |
| 2 | sliding_window.py | Sliding Window | 3. Longest Substring Without Repeating Characters | Medium |
| 3 | prefix_sum.py | Prefix Sum + Hash Map | 560. Subarray Sum Equals K | Medium |
| 4 | binary_search.py | Modified Binary Search | 33. Search in Rotated Sorted Array | Medium |
| 5 | fast_slow_pointers.py | Fast & Slow Pointers | 142. Linked List Cycle II | Medium |
| 6 | merge_intervals.py | Merge Intervals | 56. Merge Intervals | Medium |
| 7 | cyclic_sort.py | Cyclic Sort | 41. First Missing Positive | Hard |
| 8 | linked_list_reversal.py | In-place Reversal | 206. Reverse Linked List | Easy |
| 9 | monotonic_stack.py | Monotonic Stack | 739. Daily Temperatures | Medium |
| 10 | hashing.py | Hashing | 49. Group Anagrams | Medium |
| 11 | top_k_elements.py | Top K / Heap / Bucket Sort | 347. Top K Frequent Elements | Medium |
| 12 | k_way_merge.py | K-way Merge | 23. Merge k Sorted Lists | Hard |
| 13 | bfs.py | Breadth-First Search | 994. Rotting Oranges | Medium |
| 14 | dfs.py | Depth-First Search | 200. Number of Islands | Medium |
| 15 | backtracking.py | Backtracking | 39. Combination Sum | Medium |
| 16 | dynamic_programming_1d.py | 1D DP | 198. House Robber | Medium |
| 17 | dynamic_programming_2d.py | 2D DP | 1143. Longest Common Subsequence | Medium |
| 18 | knapsack.py | 0/1 Knapsack | 416. Partition Equal Subset Sum | Medium |
| 19 | greedy.py | Greedy | 55. Jump Game | Medium |
| 20 | topological_sort.py | Topological Sort | 207. Course Schedule | Medium |
| 21 | union_find.py | Union-Find | 547. Number of Provinces | Medium |
| 22 | trie.py | Trie | 208. Implement Trie | Medium |
| 23 | bit_manipulation.py | Bit Manipulation | 136. Single Number (+338 Counting Bits) | Easy |
| 24 | two_heaps.py | Two Heaps | 295. Find Median from Data Stream | Hard |
| 25 | tree_traversal.py | Tree DFS | 98. Validate Binary Search Tree | Medium |

## Suggested learning order

Hashing → Two Pointers → Sliding Window → Prefix Sum → Binary Search → Linked List (reversal, fast/slow) → Stack → Intervals → Heaps → Trees → BFS/DFS → Backtracking → DP → Graphs (topo sort, union-find) → Trie → Bits.

Maintained by [Sandesh Pande](https://github.com/shipWithSandesh).
