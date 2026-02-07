from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        rows, cols = len(grid), len(grid[0])
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        def bfs(q,visited):
            while q:
                size = len(q)

                for _ in range(size):
                    r,c = q.popleft()
                    visited.add((r,c)) # marking visited because this has been processed now
                    for dr,dc in dirs:
                        new_r = r + dr
                        new_c = c + dc
                        if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == INF and (new_r, new_c) not in visited:
                            grid[new_r][new_c] = grid[r][c] + 1
                            q.append((new_r, new_c))

        visited = set()
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        bfs(q,visited)
    