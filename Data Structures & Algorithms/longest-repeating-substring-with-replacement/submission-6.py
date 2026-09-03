class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        l = 0
        res = 0

        freq = {}

        for r in range(len(s)):
            if s[r] in freq:
                freq[s[r]] += 1
            else:
                freq[s[r]] = 1
            
            
            max_freq = max(freq.values())
            

            if ((r-l+1) - max_freq) > k:
                
                freq[s[l]] -= 1
                l += 1
                res = max(res,r-l+1)
            # elif(((r-l+1) - max_freq) <= k):
            res = max(res,r-l+1)
            
        
        return res



        