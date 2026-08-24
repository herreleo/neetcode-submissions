class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ["{", "[", "("]
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if not stack:
                    return False
                elif c == "}" and stack[-1] == "{":
                    stack.pop()
                elif c == ")" and stack[-1] == "(":
                    stack.pop()
                elif c == "]" and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            
        return True if not stack else False
        

                

