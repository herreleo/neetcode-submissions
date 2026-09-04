class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        #create dict of s1 
        s1_dict = Counter(s1)
        print (s1_dict)

        l = 0
        r = len(s1)
        # print(l,r)

        while r <= len(s2):
            
           
            inter = s2[l:r]
            # print(inter)
            
            inter_dict = Counter(inter)
            if s1_dict == inter_dict:
                
                return True
            
            l += 1
            r += 1
        
        return False
    

        