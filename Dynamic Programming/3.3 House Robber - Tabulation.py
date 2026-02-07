class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        maximum_upto_house_ith = [0] * n
        maximum_upto_house_ith[0] = nums[0]
        maximum_upto_house_ith[1] = max(nums[0], nums[1])
        for i in range(2,n):
            maximum_upto_house_ith[i] = max(maximum_upto_house_ith[i-1], nums[i] + maximum_upto_house_ith[i-2])
        return maximum_upto_house_ith[n-1]
        

