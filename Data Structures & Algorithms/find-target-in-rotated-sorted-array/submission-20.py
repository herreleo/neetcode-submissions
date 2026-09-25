class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r = len(nums)-1

        while l <= r:

            
            m = (l+r) // 2 
            print(l,m,r)
            if target == nums[m]:
                return m
            if nums[l] < nums[r]:
                
                 if nums[m] < target:
                    l = m+1
                    
                 else:
                    r = m-1
                     
          
            elif nums[m] >= nums[l] :
                #search right 
                if nums[m] > target and target >= nums[l]:
                    r = m-1
                else:
                    l = m+1
                      
            else:

                if nums[m] < target and target <= nums[r]:
                    l = m+1
                else:
                    r = m-1
            
            
        
        return -1
            
        