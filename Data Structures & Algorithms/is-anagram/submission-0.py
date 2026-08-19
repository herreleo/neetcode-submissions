class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        first = []
        second = []
        for c in s: 
            first.append(c)

        for c in t:
            second.append(c)
        
        first.sort()
        second.sort()

        if first == second:
            return True
        
        else:
            return False
        