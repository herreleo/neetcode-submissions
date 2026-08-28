class Solution:
    def trap(self, height: List[int]) -> int:


        #[0,1,2,3,4,5,6,7,8,9]
        #[0,2,0,3,1,0,1,3,2,1]
        water = 0
        p1 = 0

        p2 = len(height)-1

        max_l = height[p1]
        max_r = height[p2]
        while p1 != p2:
            #pointer to update 
            if max_l < max_r or max_l == max_r:
                
                p1 += 1
                w = max_l - height[p1]
                if w < 0:
                    water += 0
                    max_l = height[p1]
                
                else:
                    water += w



            else:
                p2 -= 1
                w = max_r - height[p2]
                if w < 0:
                    water += 0
                    max_r =  height[p2]
                else:
                    water += w
        
        return water

            



