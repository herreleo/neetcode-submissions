class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #array is sorted so I do not have to look beyond 

        res = []
        
        p2 = len(numbers)-1
      
        
        p1 = 0

        

    
        while numbers[p1] + numbers[p2] != target:
            
            
            step = numbers[p1]+ numbers[p2]
            if step == target:
                res.append(p1+1)
                res.append(p2+1)
                return res
            
            else:
                #change the pointer 
                if step < target:
                    #move right pointer 
                    p1 +=1
                else:
                    p2 -= 1
        res.append(p1+1)
        res.append(p2+1)
        return res


        

        