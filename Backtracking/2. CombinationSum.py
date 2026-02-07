class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(Sum, start):
            if Sum == target:
                res.append(path[:])
                return
            if Sum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(Sum+nums[i], i)
                path.pop()
                
        dfs(0, 0)
        return res
        