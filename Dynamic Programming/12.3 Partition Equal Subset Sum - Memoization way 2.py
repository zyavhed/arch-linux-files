class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # this solution is based on if we can find a subset which has
        # sum of half_sum of nums? if yes, definately, the other subset
        # will have the half sum
        total_sum = sum(nums)

        if total_sum % 2 == 1:
            return False
        
        half_sum = total_sum // 2
        n = len(nums)
        memory = {}
        def solve(sum1, idx):
            if (sum1,idx) in memory:
                return memory[(sum1,idx)]
            if idx >= n and sum1 == half_sum:
                return True
            elif idx >= n and sum1 != half_sum:
                return False
            memory[(sum1,idx)] = solve(sum1+nums[idx],idx+1) or solve(sum1,idx+1)
            return memory[(sum1,idx)]
        return solve(0,0)