from collections import deque


def checking_mach_parentheses(s):
    stack = deque()
    for char in s:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0


sa = "(movi)ment(o)"
print(checking_mach_parentheses(sa))
