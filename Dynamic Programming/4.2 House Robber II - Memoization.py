class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        temp_n = n-1
        def dfs(i,temp_nums,memo):
            if i >= temp_n:
                return 0
            if i in memo:
                return memo[i]
            # choose: rob this house or skip it
            rob = temp_nums[i] + dfs(i + 2, temp_nums, memo)
            skip = dfs(i + 1, temp_nums, memo)
            memo[i] = max(rob, skip)
            return memo[i]

        soln_without_first_num = dfs(0,nums[1:],{})
        soln_without_last_num = dfs(0,nums[:n-1],{})
        return max(soln_without_first_num, soln_without_last_num) 