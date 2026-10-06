class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        #binary search of middle array last value

        l = 0
        r = len(matrix) - 1

        

        
        while l <= r:


            m = l + (r-l) //2
            print(l,m,r)

            #if number is in range 
            #if target >= matrix[m][0] or target <= [m][len(matrix[m]) - 1]
            if target >= matrix[m][0] and target <= matrix[m][len(matrix[m]) - 1]:
                print("First")
                low = 0
                high = len(matrix[m]) -1
                
                #is in this range do binary search in this tree
                while low<=high:
                    mid = low + (high - low) // 2

                    if target == matrix[m][mid]:
                        return True
                    elif target < matrix[m][mid]:
                        high = mid-1
                        
                    else: 
                        low = mid+1
                return False
                

            
            elif target < matrix[m][0]:

                r = m - 1
                print("Hi")
            else:
                #target > matrix[m][len(matrix[m]-1)]
                l = m + 1
        
        return False
                




            
        