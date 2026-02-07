class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        def dfs(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i-1] == nums[i]:
                    # meaning it has already been processed
                    continue
                path.append(nums[i])
                dfs(i+1)
                path.pop()
            
        dfs(0)
        return res