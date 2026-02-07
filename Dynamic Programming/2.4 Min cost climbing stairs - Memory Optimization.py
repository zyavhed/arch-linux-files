class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)

        one_step_mini_cost = cost[n-1]
        two_step_mini_cost = cost[n-2]

        # we have to perform this n-3 times
        # this is for n = 2
        curr_mini_cost = min(one_step_mini_cost, two_step_mini_cost)
        for i in range(n-3,-1,-1):
            curr_mini_cost = cost[i] + min(one_step_mini_cost, two_step_mini_cost)
            temp_two_step_mini_cost = two_step_mini_cost
            two_step_mini_cost = curr_mini_cost
            one_step_mini_cost = temp_two_step_mini_cost
        return min(one_step_mini_cost, two_step_mini_cost)