class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r,c,prevValue, visited):
            if r < 0 or c < 0:
                return
            if (r,c) in visited or r >= rows or c >= cols or heights[r][c] < prevValue:
                return
            visited.add((r,c))
            dfs(r,c-1,heights[r][c], visited)
            dfs(r-1,c,heights[r][c], visited)
            dfs(r,c+1,heights[r][c], visited)
            dfs(r+1,c,heights[r][c], visited)
        
        pac = set()
        atl = set()
        last_row = rows - 1
        last_col = cols - 1
        for r in range(rows):
            dfs(r,0,heights[r][0],pac)
            dfs(r,last_col,heights[r][last_col],atl)
        for c in range(cols):
            dfs(0,c,heights[0][c],pac)
            dfs(last_row,c,heights[last_row][c],atl)

        res = []
        for data in pac:
            if data in atl:
                res.append(data)
        return res
        