"""
Pattern: Stack (match the most recent opener)
Problem: LeetCode 20 - Valid Parentheses  [Easy]
Link: https://leetcode.com/problems/valid-parentheses/

Question:
    Given a string containing only ()[]{}, decide whether the brackets are
    valid: every opener is closed by the same type, in the correct order.

Intuition:
    The bracket we must close first is always the MOST RECENT unclosed one:
    last-in, first-out, which is exactly a stack. Push each opener. On a
    closer, the stack must be non-empty and its top must be the matching
    opener, otherwise the string is invalid. At the end the stack must be
    empty (no unclosed openers left).

When to use this pattern:
    Nested or "most recent first" structure: Decode String (LC 394),
    Evaluate Reverse Polish Notation (LC 150), Min Stack (LC 155),
    Basic Calculator (LC 224).

Complexity:
    Time  O(n)
    Space O(n)  - stack in the worst case (all openers)
"""


def is_valid(s: str) -> bool:
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("") is True
    assert is_valid("(") is False
    assert is_valid("]") is False
    print("stack.py: all tests passed")
