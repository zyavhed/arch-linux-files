class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        half = total // 2
        possible_sums = set()
        possible_sums.add(0)

        for num in nums:
            element_to_be_added_in_set = []
            for element in possible_sums:
                summed = element+num
                if summed == half:
                    return True
                if summed < half:
                    element_to_be_added_in_set.append(summed)
            possible_sums.update(element_to_be_added_in_set)
        return False