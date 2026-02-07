class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        min_costing_arr = [-1] * (n)

        min_costing_arr[n-1] = cost[n-1]
        min_costing_arr[n-2] = cost[n-2]

        for i in range(n-3, -1, -1):
            min_costing_arr[i] = cost[i] + min(min_costing_arr[i+1], min_costing_arr[i+2])
        return min(min_costing_arr[0], min_costing_arr[1]) 