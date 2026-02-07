class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if i == len(nums):
                res.append(path[:])
                return
            
            #take ith element
            path.append(nums[i])
            dfs(i+1)
            path.pop()

            #not take ith element
            dfs(i+1)

        dfs(0)
        return res
        