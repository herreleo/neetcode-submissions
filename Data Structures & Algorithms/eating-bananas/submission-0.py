class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        high = max(piles)

        low = 1

        #4, // 2
    
        #while condition ? 
        while low <= high:
            hours = 0
            mid = low + (high - low) // 2

            for pile in piles:
                hours += math.ceil(pile/mid)
            
            if hours <= h:
                high = mid-1
                
            
            else:
                low = mid+1
            
        return low




