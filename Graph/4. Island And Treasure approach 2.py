from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        def bfs(i,j):
            visited = set()
            q = deque()

            q.append((i,j))
            level = 0
            while q:
                size = len(q)

                for _ in range(size):
                    r,c = q.popleft()
                    visited.add((r,c)) # marking visited because this has been processed now
                    if grid[r][c] == 0:
                        return level
                    for dr,dc in dirs:
                        new_r = r + dr
                        new_c = c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] != -1 and (new_r, new_c) not in visited:
                            q.append((new_r,new_c)) 
                level += 1
            return INF


        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == INF:
                    grid[i][j] = bfs(i,j)
    