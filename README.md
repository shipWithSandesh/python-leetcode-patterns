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
| 26 | dijkstra.py | Dijkstra / Shortest Path | 743. Network Delay Time | Medium |
| 27 | monotonic_queue.py | Monotonic Queue | 239. Sliding Window Maximum | Hard |
| 28 | matrix_traversal.py | Matrix Traversal | 54. Spiral Matrix | Medium |
| 29 | two_pointer_3sum.py | Two Pointers | 15. 3Sum | Medium |
| 30 | sliding_window_min_window_substring.py | Sliding Window | 76. Minimum Window Substring | Hard |
| 31 | binary_search_koko_bananas.py | Binary Search on Answer | 875. Koko Eating Bananas | Medium |
| 32 | bfs_binary_tree_level_order.py | BFS (Tree Levels) | 102. Binary Tree Level Order Traversal | Medium |
| 33 | dp_on_trees.py | DP on Trees | 337. House Robber III | Medium |
| 34 | design.py | Design | 146. LRU Cache | Medium |
| 35 | hashing_two_sum.py | Hashing | 1. Two Sum | Easy |
| 36 | merge_intervals_insert_interval.py | Intervals | 57. Insert Interval | Medium |
| 37 | sliding_window_char_replacement.py | Sliding Window | 424. Longest Repeating Character Replacement | Medium |
| 38 | two_pointer_container_most_water.py | Two Pointers | 11. Container With Most Water | Medium |
| 39 | binary_search_find_min_rotated.py | Binary Search | 153. Find Minimum in Rotated Sorted Array | Medium |
| 40 | monotonic_stack_largest_rectangle.py | Monotonic Stack | 84. Largest Rectangle in Histogram | Hard |
| 41 | top_k_elements_kth_largest.py | Top K Elements | 215. Kth Largest Element in an Array | Medium |
| 42 | backtracking_subsets.py | Backtracking | 78. Subsets | Medium |
| 43 | dynamic_programming_1d_coin_change.py | Dynamic Programming (1D) | 322. Coin Change | Medium |
| 44 | hashing_longest_consecutive.py | Hashing | 128. Longest Consecutive Sequence | Medium |
| 45 | stack.py | Stack | 20. Valid Parentheses | Easy |

## Suggested learning order

Hashing → Two Pointers → Sliding Window → Prefix Sum → Binary Search → Linked List (reversal, fast/slow) → Stack → Intervals → Heaps → Trees → BFS/DFS → Backtracking → DP → Graphs (topo sort, union-find) → Trie → Bits.

Maintained by [Sandesh Pande](https://github.com/shipWithSandesh).
