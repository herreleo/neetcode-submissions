class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low = 0
        high = len(nums) - 1
        print(high)
        m = len(nums)// 2
        print(m)
        while low<=high:
            m = low + (high - low) // 2

            if target == nums[m]:
                return m
            elif target < nums[m]:
                high = m-1
                
            else: 
                low = m+1
                
        return -1


            
        