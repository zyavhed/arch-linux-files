class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #min heap of length 2
        h = nums[:]
        heapq.heapify(h)
        while len(h) > k:
            heapq.heappop(h)
        return h[0]