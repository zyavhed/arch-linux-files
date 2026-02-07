class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        def solve(sum1, sum2, idx):
            if idx >= n and sum1 == sum2:
                return True
            elif idx >= n and sum1 != sum2:
                return False
            return solve(sum1+nums[idx],sum2,idx+1) or solve(sum1,sum2+nums[idx],idx+1)
        return solve(0,0,0)