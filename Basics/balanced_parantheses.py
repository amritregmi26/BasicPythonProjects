class Solution:
    def balanced_parentheses(self, s: str) -> bool:
        closing_equivalents = {")": "(", "}": "{", "]": "["}
        stack = []
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) > 0 and closing_equivalents[c] == stack[len(stack) - 1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0