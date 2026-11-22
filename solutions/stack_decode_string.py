"""
Pattern: Stack
Problem: LeetCode 394 - Decode String  [Medium]
Link: https://leetcode.com/problems/decode-string/

Question:
Decode strings like 3[a2[c]] into accaccacc.

Intuition:
On '[' push the current string and repeat count; on ']' pop and build prev + cur*count. Nested brackets are handled by the stack.

When to use this pattern:
Nested structures that must be resolved innermost-first.

Complexity:
Time O(output length); space O(depth).
"""

def decode_string(s: str) -> str:
    stack = []
    cur, num = "", 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            stack.append((cur, num))
            cur, num = "", 0
        elif ch == "]":
            prev, k = stack.pop()
            cur = prev + cur * k
        else:
            cur += ch
    return cur


if __name__ == "__main__":
    assert decode_string("3[a]2[bc]") == "aaabcbc"
    assert decode_string("3[a2[c]]") == "accaccacc"
    assert decode_string("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert decode_string("") == ""
    print("stack_decode_string.py: all tests passed")
