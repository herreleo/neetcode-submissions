class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        #remove or filter(skip) non alphanumerical characters 

        for c in s:
            if c.isalnum():
                clean += c
        
        clean = clean.lower()

        

        p1 = 0
        p2 = len(clean)-1

        #run until indexes meet
        while p1 != p2 and abs(p1-p2 != 1):
            print(p1,p2)
            if clean[p1] == clean[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        
        return True #p1 == p2



        