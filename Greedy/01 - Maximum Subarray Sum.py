class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxi = nums[0]
        Sum = 0
        for num in nums:
            Sum += num
            maxi = max(maxi, Sum)
            Sum = max(0, Sum)
        return maxi