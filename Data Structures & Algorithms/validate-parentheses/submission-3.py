class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if (c == "(" or c == "[" or c == "{"):
                stack.append(c)
            else:
                if c == ")":
                    if not stack or stack[-1] != "(":
                        return False
                    stack.pop()
                elif c == "]":
                    if not stack or stack[-1] != "[":
                        return False
                    stack.pop()
                elif c == "}":
                    if not stack or stack[-1] != "{":
                        return False
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        return False
                   