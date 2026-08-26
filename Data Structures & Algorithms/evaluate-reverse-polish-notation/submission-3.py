class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = 0

        stack = []

        for t in tokens:
            #dd to stack first or check for type first
            if t == "+":
                    first = stack.pop() #2
                    second = stack.pop() #1
                    res = first+second #3
                    stack.append(res) #3r

            elif t == "-":
                    first = stack.pop() #4
                    second = stack.pop()
                    res = second-first
                    stack.append(res)
                
            elif t == "*":
                    first = stack.pop()
                    second = stack.pop()
                    res = first*second
                    stack.append(res) #9
                
            elif t == "/":
                    first = stack.pop()
                    second = stack.pop()
                    res = int(second / first)
                    stack.append(res) #9
            else:
                
                stack.append(int(t)) # 9 4
                
        res = stack.pop()
        return res
                

        