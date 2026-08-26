class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0

        p1 = 0
        p2 = len(heights)-1

        while p1 != p2:
            h1 = heights[p1]
            h2 = heights[p2]

            h = min(h1,h2)

            a = h * (p2-p1)
            area = max(a, area)
             #pointer to change 
            if h1 > h2:
                p2 -= 1
            else:
                p1 += 1
            
        return area

            

        