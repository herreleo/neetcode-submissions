class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sequence = 0 

        lookup = set(nums)


        #loop thru nums


        for num in nums:
            #start of a sequence
            if num-1 not in lookup:
                length = 0
                #check unitl sequence ends 
                while(num+length in lookup):
                    
                    length += 1
                
        
                sequence = max(sequence,length)
            
    
        return sequence

                        
        
        