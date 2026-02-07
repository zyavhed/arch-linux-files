class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_from_house_robber_i(temp_nums) -> int:
            n = len(temp_nums)
            if n == 1:
                return temp_nums[0]

            prev2 = temp_nums[0]                     # dp[i-2]
            prev1 = max(temp_nums[0], temp_nums[1])       # dp[i-1]

            for i in range(2, n):
                current = max(prev1, temp_nums[i] + prev2)
                prev2, prev1 = prev1, current
            return prev1
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        soln_without_first_num = rob_from_house_robber_i(nums[1:])
        soln_without_last_num = rob_from_house_robber_i(nums[:len(nums) - 1])
        return max(soln_without_first_num, soln_without_last_num) 