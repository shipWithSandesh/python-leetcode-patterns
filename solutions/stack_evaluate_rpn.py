"""
Pattern: Stack
Problem: LeetCode 150 - Evaluate Reverse Polish Notation  [Medium]
Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/

Question:
Evaluate an arithmetic expression in postfix notation; division truncates toward zero.

Intuition:
Push numbers; on an operator pop two operands (right first), apply, push the result.

When to use this pattern:
Postfix/expression evaluation, undo-style processing.

Complexity:
Time O(n); space O(n).
"""

from typing import List


def eval_rpn(tokens: List[str]) -> int:
    st: List[int] = []
    for t in tokens:
        if t in "+-*/" and len(t) == 1:
            b, a = st.pop(), st.pop()
            if t == "+":
                st.append(a + b)
            elif t == "-":
                st.append(a - b)
            elif t == "*":
                st.append(a * b)
            else:
                st.append(int(a / b))
        else:
            st.append(int(t))
    return st[0]


if __name__ == "__main__":
    assert eval_rpn(["2", "1", "+", "3", "*"]) == 9
    assert eval_rpn(["4", "13", "5", "/", "+"]) == 6
    assert eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
    assert eval_rpn(["-7", "2", "/"]) == -3
    print("stack_evaluate_rpn.py: all tests passed")
