class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        def solve(idx, has_first_element_taken):
            if idx == n-1 and has_first_element_taken:
                return 0
            if idx >= n:
                return 0
            if idx == 0:
                rob = nums[idx] + solve(idx+2, True)
            else:
                rob = nums[idx] + solve(idx+2, has_first_element_taken)
            skip = solve(idx+1, has_first_element_taken)
            return max(rob, skip)
        return solve(0, False)