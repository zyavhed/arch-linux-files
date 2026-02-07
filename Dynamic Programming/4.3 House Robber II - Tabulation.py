class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_from_house_robber_i(temp_nums):
            n = len(temp_nums)
            if n == 1:
                return temp_nums[0]
            maximum_upto_house_ith = [0] * n
            maximum_upto_house_ith[0] = temp_nums[0]
            maximum_upto_house_ith[1] = max(temp_nums[0], temp_nums[1])
            for i in range(2,n):
                maximum_upto_house_ith[i] = max(maximum_upto_house_ith[i-1], temp_nums[i] + maximum_upto_house_ith[i-2])
            return maximum_upto_house_ith[n-1]
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        soln_without_first_num = rob_from_house_robber_i(nums[1:])
        soln_without_last_num = rob_from_house_robber_i(nums[:len(nums) - 1])
        return max(soln_without_first_num, soln_without_last_num) 