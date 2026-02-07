from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh_oranges_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh_oranges_count += 1

        level = 0
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        while q and fresh_oranges_count > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr,dc in dirs:
                    new_r = r + dr
                    new_c = c + dc
                    if (
                        new_r < 0 or new_r >= rows or
                        new_c < 0 or new_c >= cols or
                        grid[new_r][new_c] != 1
                    ):
                        # no need to process this elemet
                        continue
                    grid[new_r][new_c] = 2 #make it rotten
                    fresh_oranges_count -= 1
                    q.append((new_r,new_c)) #append it for further processing
            level += 1
        if fresh_oranges_count > 0:
            return -1
        return level