class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = [1] * len(nums)
        for i in range(len(nums)):
            best = 0
            curr = nums[i]
            for j in range(0,i):
                # to make the sequence increasing, this is the way.
                if nums[j] < curr and ans[j] > best:
                    best = ans[j]
            ans[i] += best
        return max(ans)