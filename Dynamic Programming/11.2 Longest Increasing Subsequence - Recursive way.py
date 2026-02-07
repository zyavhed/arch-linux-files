class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def solve(idx, prev_maxi):
            if idx >= len(nums):
                return 0
            # Take
            if nums[idx] > prev_maxi:
                take = 1 + solve(idx+1, nums[idx])
            else:
                # meaning if you take that element, thats gonna be zero element. i.e.
                # breaks the constraint
                take = -1 # meaning dont take
            # skip
            skip = solve(idx+1, prev_maxi)
            return max(take, skip) if take != -1 else skip

        return solve(0,float('-inf'))
