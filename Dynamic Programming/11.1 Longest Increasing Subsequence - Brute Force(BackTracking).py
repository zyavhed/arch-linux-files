class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        maxi = 0
        # this idx tells whether to include or exclude the element
        def solve(idx, max_element_till_now, number_of_elements_included):
            nonlocal maxi
            if idx >= len(nums):
                maxi = max(maxi, number_of_elements_included)
                return
            # Take
            if nums[idx] > max_element_till_now:
                solve(idx+1, nums[idx], number_of_elements_included+1)
            # skip
            solve(idx+1, max_element_till_now, number_of_elements_included)
                
        solve(0,float('-inf'), 0)
        return maxi
