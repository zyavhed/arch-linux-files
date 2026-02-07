class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
            
        jumps = 0
        current_jump_end = 0
        farthest_reach = 0

        for i in range(n):
            farthest_reach = max(farthest_reach, i + nums[i])
            if i == current_jump_end:
                jumps += 1
                current_jump_end = farthest_reach
            if current_jump_end >= n-1:
                return jumps
