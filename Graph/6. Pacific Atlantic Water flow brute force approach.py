class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs_for_pacific(r,c,prevValue, visited):
            if r < 0 or c < 0:
                return True
            if (r,c) in visited or r >= rows or c >= cols or heights[r][c] > prevValue:
                return False
            visited.add((r,c))
            left = dfs_for_pacific(r,c-1,heights[r][c], visited)
            if left:
                return True
            up = dfs_for_pacific(r-1,c,heights[r][c], visited)
            if up:
                return True
            right = dfs_for_pacific(r,c+1,heights[r][c], visited)
            if right:
                return True
            down = dfs_for_pacific(r+1,c,heights[r][c], visited)
            if down:
                return True
            return False


        def dfs_for_atlantic(r,c,prevValue, visited):
            if r >= rows or c >= cols:
                return True
            if (r,c) in visited or r < 0 or c < 0 or heights[r][c] > prevValue:
                return False
            visited.add((r,c))
            left = dfs_for_atlantic(r,c-1,heights[r][c], visited)
            if left:
                return True
            up = dfs_for_atlantic(r-1,c,heights[r][c], visited)
            if up:
                return True
            right = dfs_for_atlantic(r,c+1,heights[r][c], visited)
            if right:
                return True
            down = dfs_for_atlantic(r+1,c,heights[r][c], visited)
            if down:
                return True
            return False
        
        res = []
        for i in range(rows):
            for j in range(cols):
                if dfs_for_pacific(i,j,heights[i][j], set()) and dfs_for_atlantic(i,j,heights[i][j], set()):
                    res.append([i,j])
        return res