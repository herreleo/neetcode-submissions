class Solution:
    def minWindow(self, s: str, t: str) -> str:

        #for sliding window 
        #for loop
            #while condition 
                #typially shrink/adjust window
            #always update 

        
        #create a frequency map for t 
        t_frequency = Counter(t)
        window = {}
        have = 0
        need = len(t_frequency)
        res = [-1,-1]
        resLen = float("infinity")
 
        l = 0
        for r,c in enumerate(s):
            #add r boundary to map 
            if c not in window:
                window[c] = 1
            else:
                window[c] += 1
            
            if c in t_frequency and window[c] == t_frequency[c] :
                have += 1
            
            while have == need:
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                
                window[s[l]] -= 1
                if s[l] in t_frequency and window[s[l]] < t_frequency[s[l]]:
                    have -= 1
                l += 1

        l,r = res

        return s[l:r+1] if resLen != float("infinity") else ""
            
            



        
        