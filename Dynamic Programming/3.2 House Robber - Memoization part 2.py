class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i >= n:
                return 0
            if i in memo:
                return memo[i]
            # choose: rob this house or skip it
            rob = nums[i] + dfs(i + 2)
            skip = dfs(i + 1)
            memo[i] = max(rob, skip)
            return memo[i]

        return dfs(0)
