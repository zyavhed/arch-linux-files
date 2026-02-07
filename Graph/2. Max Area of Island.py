class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        def dfs(r,c):
            if (r,c) in visited or r>=len(grid) or r<0 or c>=len(grid[0]) or c<0:
                return 0
            if grid[r][c] == 0:
                return 0
            visited.add((r,c))
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        maxi = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxi = max(maxi, dfs(r,c))
        
        return maxi