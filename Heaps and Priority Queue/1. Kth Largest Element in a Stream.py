class KthLargest:

    # maintain min heap of length k
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums[:]
        heapq.heapify(self.h)
        while len(self.h) > self.k:
            heapq.heappop(self.h)
        
    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        elif len(self.h) == self.k and val > self.h[0]:
            heapq.heappushpop(self.h, val)
        return self.h[0]