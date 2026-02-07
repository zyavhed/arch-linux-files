from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647

        if not grid or not grid[0]:
            return
        
        m, n = len(grid), len(grid[0])

        # Directions for BFS
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def bfs(start_r, start_c):
            """Perform BFS from (start_r, start_c) until we find a treasure (0)."""
            visited = set()
            q = deque()
            q.append((start_r, start_c, 0))  # (r, c, distance)
            visited.add((start_r, start_c))
            
            while q:
                r, c, dist = q.popleft()
                
                # Found a treasure
                if grid[r][c] == 0:
                    return dist
                
                # Expand neighbors
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < m and 0 <= nc < n
                        and grid[nr][nc] != -1
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc, dist + 1))
            
            return INF  # No treasure reachable

        # For every land cell: run BFS to find the nearest treasure
        for r in range(m):
            for c in range(n):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
