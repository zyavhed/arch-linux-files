class Solution:
    def canPartition(self, nums: List[int]) -> bool:
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
                
            take = False
            if sum1 < half_sum:
                take = solve(sum1+nums[idx],idx+1)
            skip = solve(sum1,idx+1)
            memory[(sum1,idx)] = take or skip
            return memory[(sum1,idx)]
        return solve(0,0)