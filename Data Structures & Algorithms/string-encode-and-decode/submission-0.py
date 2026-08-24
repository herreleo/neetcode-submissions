class Solution:

    def encode(self, strs: List[str]) -> str:
        #naive approach: concat each string with a delimter
        master_string = ""
        for s in strs:
            length = len(s)
            encode = str(length) + "#" + s
            master_string += encode
        
        return master_string

    def decode(self, s: str) -> List[str]:
        res, i = [], 0

        while i < len(s):
            #inner counter
            j = i
            while s[j] != "#":
                j +=1
            length = int(s[i:j])
            
            res.append(s[j+1:length + j+1])
            i = j+1+length

        return res




        

        
                   
            

            
            



            
            
        
        


         
       

