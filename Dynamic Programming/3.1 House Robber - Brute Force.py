class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxi = 0
        def dfs(idx, curr):
            nonlocal maxi
            if idx >= n:
                return
            # did i get maximum out of all these loot?
            maxi = max(maxi, curr)
            for i in range(idx+2, n):
                dfs(i, curr+nums[i])


        for i in range(n):
            dfs(i, nums[i])

        return maxi
