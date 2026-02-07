class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [ ['.' for i in range(n)] for j in range(n)] 
        res = []
        
        def is_queen_placeable_in_board_at_position(row,col):
            r = 0
            while r < row:
                if board[r][col] == 'Q':
                    return False
                r += 1
            # diagonal left
            r = row-1
            c = col-1
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1
            # diagonal right
            r = row-1
            c = col+1
            while r >= 0 and c < n:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c += 1
            return True

        def dfs(row):
            if row == n:
                res.append([''.join(row) for row in board])
                return
            for col in range(n):
                if is_queen_placeable_in_board_at_position(row,col):
                    board[row][col] = 'Q'
                    dfs(row+1)
                    board[row][col] = '.'


        dfs(0)
        return res
