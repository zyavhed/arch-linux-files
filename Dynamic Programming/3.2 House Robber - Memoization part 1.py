class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memory = {i: -1 for i in range(n)}

        def dfs(idx):
            if idx >= n:
                return 0
            if memory[idx] != -1:
                return memory[idx]

            maxi = 0
            # try robbing any house from idx onward, but obey +2 rule
            for i in range(idx, n):
                maxi = max(maxi, nums[i] + dfs(i + 2))

            memory[idx] = maxi
            return maxi

        # still try starting at every index (your original outer loop)
        maxi = 0
        for i in range(n):
            maxi = max(maxi, dfs(i))

        return maxi
