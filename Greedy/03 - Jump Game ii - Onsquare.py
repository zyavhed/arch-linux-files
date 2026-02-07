from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0

        dp = [float('inf')] * n
        dp[n-1] = 0  # last index needs 0 jumps

        for i in range(n-2, -1, -1):
            steps = nums[i]
            # If you can reach or pass the last index
            if i + steps >= n - 1:
                dp[i] = 1
            elif steps > 0:
                dp[i] = 1 + min(dp[i+1 : i+steps+1])
        return dp[0]