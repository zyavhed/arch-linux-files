from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        target = total // 2

        bits = 1  # bit 0 set -> sum 0 is possible
        for num in nums:
            bits |= (bits << num)         # shift the bitset by num and OR
            # optional early exit:
            if (bits >> target) & 1:
                return True

        return ((bits >> target) & 1) == 1