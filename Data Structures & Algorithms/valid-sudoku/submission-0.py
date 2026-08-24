class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #check for rows first 

        for row in board:
            validrow = set()
            for square in row:
                if square.isdigit():
                    num = int(square)
                    if num not in validrow:
                        validrow.add(num)
                    else:
                        return False
        
        #check for valid columns 

        rows = len(board)
        cols = len(board[0])

        for c in range(cols):
            validcol = set()
            for r in range(rows):
                if (board[r][c]).isdigit():
                    num = int(board[r][c])
                    if num not in validcol:
                        validcol.add(num)
                    else:
                        return False
                
        # 0 1 3 

        starts = [(0,0), (0,3), (0,6),
                    (3,0), (3,3), (3,6),
                    (6,0), (6,3), (6,6)]
                
        for i,j in starts:
            validbox = set()
            for r in range(i,i+3):
                for c in range(j,j+3):
                    if (board[r][c]).isdigit():
                        num = int(board[r][c])
                        if num not in validbox:
                            validbox.add(num)
                        else:
                            return False
        
        return True



        