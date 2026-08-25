class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [0] * len(temperatures)
        # print(res)
        # stack = []
        # #[30,38,30,36,35,40,28]
        # for i, t in enumerate(temperatures):

        #      while stack and t <= stack[-1]:
        #         #
        #     stack.add(i)

        ans = [0] * len(temperatures)
        stack = []  # stores indices
    
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
            
        return ans


        