class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False
        
        half_sum = total_sum // 2
        n = len(nums)

        # dp[idx][sum1]
        memory = [[-1] * (half_sum + 1) for _ in range(n + 1)]

        def solve(idx, sum1):
            # base cases
            if sum1 == half_sum:
                return True
            if idx == n or sum1 > half_sum:
                return False

            if memory[idx][sum1] != -1:
                return memory[idx][sum1]

            take = solve(idx + 1, sum1 + nums[idx])
            skip = solve(idx + 1, sum1)

            memory[idx][sum1] = take or skip
            return memory[idx][sum1]

        return solve(0, 0)
