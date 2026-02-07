class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memory = {}

        def solve(idx, prev_idx):
            if idx == n:
                return 0
            if (idx, prev_idx) in memory:
                return memory[(idx, prev_idx)]

            # Option 1: skip
            best = solve(idx + 1, prev_idx)

            # Option 2: take
            if prev_idx == -1 or nums[idx] > nums[prev_idx]:
                best = max(best, 1 + solve(idx + 1, idx))
            memory[(idx, prev_idx)] = best
            return memory[(idx, prev_idx)]

        return solve(0, -1)