class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # or max heap of length k-1
        h = [-x for x in nums]
        heapq.heapify(h)
        
        for i in range(k-1):
            heapq.heappop(h)
        return -h[0]