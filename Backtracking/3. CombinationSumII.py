class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        nums = sorted(candidates)

        def dfs(Sum, start):
            if Sum == target:
                res.append(path[:])
                return
            if Sum > target:
                return

            for i in range(start,len(nums)):
                # When you are at the same depth level in the recursion tree…
                # you skip numbers that are the same as the previous one.
                # because the previous one will take care of the processing
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(Sum+nums[i], i+1)
                path.pop()
                
        dfs(0, 0)
        return res