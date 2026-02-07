class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = set()
        def dfs(curr):
            if len(path) == len(nums):
                    res.append(curr[:])
                    return
            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.add(nums[i])
                dfs(curr + [nums[i]])
                path.remove(nums[i])

        dfs([])
        return res