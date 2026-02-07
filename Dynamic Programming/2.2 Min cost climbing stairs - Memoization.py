class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memory = {}

        def dfs(idx):
            if idx in memory:
                return memory[idx]
            if idx >= n:
                return 0
            memory[idx] = cost[idx] + min( dfs(idx+1), dfs(idx+2) )
            return memory[idx]
        
        # i want minimum cost whichever from taking step 1 or step 2
        return min(dfs(0), dfs(1))