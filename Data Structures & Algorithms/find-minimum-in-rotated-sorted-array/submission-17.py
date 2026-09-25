class Solution:
    def findMin(self, nums: List[int]) -> int:

        l = 0
        r = len(nums)-1

        smallest = nums[l]

        while l <= r:
           

            if nums[l] < nums[r]:
                smallest = min(smallest, nums[l])
                break
                
            m = (l+ r)//2
            smallest = min(smallest, nums[m])
            if nums[m] >= nums[l] :
                #search right 

                l = m+1
                      
            
            else:

                r = m-1
                
        
        return smallest
