class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mini = 1000
        n = len(cost)

        def dfs(idx, curr_cost):
            nonlocal mini
            if idx >= n:
                mini = min(curr_cost, mini)
                return
            dfs(idx + 1, curr_cost + cost[idx])
            dfs(idx + 2, curr_cost + cost[idx])

        dfs(0, 0)
        dfs(1, 0)
        return mini