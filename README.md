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
| 46 | design_min_stack.py | Design (augmented data structure) | 155. Min Stack | Medium |
| 47 | intervals_non_overlapping.py | Intervals | 435. Non-overlapping Intervals | Medium |
| 48 | backtracking_permutations.py | Backtracking | 46. Permutations | Medium |
| 49 | dynamic_programming_lis.py | Dynamic Programming (Binary Search) | 300. Longest Increasing Subsequence | Medium |
| 50 | greedy_best_time_to_buy_sell_stock.py | Greedy / One Pass | 121. Best Time to Buy and Sell Stock | Easy |
| 51 | prefix_sum_product_except_self.py | Prefix Sum | 238. Product of Array Except Self | Medium |
| 52 | two_pointer_trapping_rain_water.py | Two Pointers | 42. Trapping Rain Water | Hard |
| 53 | linked_list_remove_nth_node.py | Linked List (Fast/Slow Pointers) | 19. Remove Nth Node From End of List | Medium |
| 54 | string_longest_palindromic_substring.py | Strings (Expand Around Center) | 5. Longest Palindromic Substring | Medium |
| 55 | tree_lowest_common_ancestor.py | Trees (DFS) | 236. Lowest Common Ancestor of a Binary Tree | Medium |
| 56 | backtracking_word_search.py | Backtracking (grid DFS) | 79. Word Search | Medium |
| 57 | dynamic_programming_2d_edit_distance.py | Dynamic Programming (2D, two strings) | 72. Edit Distance | Hard |
| 58 | dp_on_trees_max_path_sum.py | DP on Trees (post-order DFS) | 124. Binary Tree Maximum Path Sum | Hard |
| 59 | topological_sort_course_schedule_ii.py | Topological Sort (Kahn BFS) | 210. Course Schedule II | Medium |
| 60 | union_find_redundant_connection.py | Union Find (cycle detection) | 684. Redundant Connection | Medium |
| 61 | dijkstra_path_min_effort.py | Dijkstra (grid, minimax path) | 1631. Path With Minimum Effort | Medium |
| 62 | graph_bellman_ford_cheapest_flights.py | Bellman-Ford (bounded edges) | 787. Cheapest Flights Within K Stops | Medium |
| 63 | matrix_rotate_image.py | Matrix (in-place transform) | 48. Rotate Image | Medium |
| 64 | matrix_set_zeroes.py | Matrix (in-place markers) | 73. Set Matrix Zeroes | Medium |
| 65 | string_palindromic_substrings.py | Strings (Expand Around Center) | 647. Palindromic Substrings | Medium |
| 66 | dp_max_subarray.py | DP (Kadane) | 53. Maximum Subarray | Medium |
| 67 | dp_max_product_subarray.py | DP (min/max tracking) | 152. Maximum Product Subarray | Medium |
| 68 | dp_climbing_stairs.py | DP (1D) | 70. Climbing Stairs | Easy |
| 69 | two_pointer_move_zeroes.py | Two Pointers (read/write) | 283. Move Zeroes | Easy |
| 70 | tree_diameter.py | Trees (DFS) | 543. Diameter of Binary Tree | Easy |
| 71 | tree_build_from_preorder_inorder.py | Trees (divide and conquer) | 105. Construct Binary Tree from Preorder and Inorder Traversal | Medium |
| 72 | dp_word_break.py | DP (prefix reachability) | 139. Word Break | Medium |
| 73 | backtracking_letter_combinations.py | Backtracking | 17. Letter Combinations of a Phone Number | Medium |
| 74 | binary_search_first_last_position.py | Binary Search (bounds) | 34. Find First and Last Position of Element in Sorted Array | Medium |
| 75 | linked_list_reverse_k_group.py | Linked List (k-group reversal) | 25. Reverse Nodes in k-Group | Hard |
| 76 | backtracking_generate_parentheses.py | Backtracking | 22. Generate Parentheses | Medium |
| 77 | backtracking_palindrome_partitioning.py | Backtracking | 131. Palindrome Partitioning | Medium |
| 78 | dp_decode_ways.py | DP (1D) | 91. Decode Ways | Medium |
| 79 | dynamic_programming_2d_unique_paths.py | DP (2D) | 62. Unique Paths | Medium |
| 80 | binary_search_2d_matrix.py | Binary Search (virtual array) | 74. Search a 2D Matrix | Medium |
| 81 | stack_decode_string.py | Stack | 394. Decode String | Medium |
| 82 | stack_evaluate_rpn.py | Stack | 150. Evaluate Reverse Polish Notation | Medium |
| 83 | tree_invert_binary_tree.py | Trees (DFS) | 226. Invert Binary Tree | Easy |
| 84 | dfs_max_area_of_island.py | DFS (grid) | 695. Max Area of Island | Medium |
| 85 | linked_list_merge_two_sorted.py | Linked List | 21. Merge Two Sorted Lists | Easy |
| 86 | boyer_moore_majority_element.py | Boyer-Moore Voting | 169. Majority Element | Easy |
| 87 | hashing_contains_duplicate.py | Hashing | 217. Contains Duplicate | Easy |
| 88 | hashing_valid_anagram.py | Hashing | 242. Valid Anagram | Easy |
| 89 | binary_search_basic.py | Binary Search | 704. Binary Search | Easy |
| 90 | binary_search_sqrt.py | Binary Search | 69. Sqrt(x) | Easy |
| 91 | tree_kth_smallest_bst.py | Trees (BST) | 230. Kth Smallest Element in a BST | Medium |
| 92 | bfs_right_side_view.py | BFS | 199. Binary Tree Right Side View | Medium |
| 93 | knapsack_target_sum.py | 0/1 Knapsack | 494. Target Sum | Medium |
| 94 | dp_house_robber_ii.py | DP (1D) | 213. House Robber II | Medium |
| 95 | merge_intervals_min_arrows.py | Intervals | 452. Minimum Number of Arrows to Burst Balloons | Medium |
| 96 | linked_list_reorder_list.py | Linked List | 143. Reorder List | Medium |
| 97 | design_randomized_set.py | Design | 380. Insert Delete GetRandom O(1) | Medium |
| 98 | trie_add_search_word.py | Trie | 211. Design Add and Search Words Data Structure | Medium |
| 99 | merge_intervals_meeting_rooms_ii.py | Intervals + Heap | 253. Meeting Rooms II | Medium |
| 100 | dfs_clone_graph.py | DFS | 133. Clone Graph | Medium |
| 101 | dfs_pacific_atlantic.py | DFS | 417. Pacific Atlantic Water Flow | Medium |
| 102 | dp_stock_cooldown.py | DP (state machine) | 309. Best Time to Buy and Sell Stock with Cooldown | Medium |
| 103 | tree_balanced.py | Trees | 110. Balanced Binary Tree | Easy |
| 104 | binary_search_find_peak.py | Binary Search | 162. Find Peak Element | Medium |
| 105 | bit_manipulation_counting_bits.py | Bit Manipulation | 338. Counting Bits | Easy |

## Suggested learning order

Hashing → Two Pointers → Sliding Window → Prefix Sum → Binary Search → Linked List (reversal, fast/slow) → Stack → Intervals → Heaps → Trees → BFS/DFS → Backtracking → DP → Graphs (topo sort, union-find) → Trie → Bits.

Maintained by [Sandesh Pande](https://github.com/shipWithSandesh).
