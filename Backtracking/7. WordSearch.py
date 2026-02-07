class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        m, n = len(board), len(board[0])
        
        def dfs(r, c, idx):
            # Word fully matched
            if idx == len(word):
                return True
            
            # Boundary check
            if r < 0 or r >= m or c < 0 or c >= n:
                return False
            
            # Visited check
            if board[r][c] == "$":
                return False
            
            # Character match check
            if board[r][c] != word[idx]:
                return False
            
            # Mark visited
            temp = board[r][c]
            board[r][c] = "$"
            
            # Explore neighbors
            res = (
                dfs(r+1, c, idx+1) or
                dfs(r-1, c, idx+1) or
                dfs(r, c+1, idx+1) or
                dfs(r, c-1, idx+1)
            )
            
            # Undo mark
            board[r][c] = temp
            
            return res
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
