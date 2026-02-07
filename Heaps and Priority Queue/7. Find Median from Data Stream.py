class MedianFinder:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    def addNum(self, num: int) -> None:
        if not self.left_max_heap :
            heapq.heappush(self.left_max_heap, -num)
        elif num < -self.left_max_heap[0]:
            heapq.heappush(self.left_max_heap, -num)
        else:
            heapq.heappush(self.right_min_heap, num)

        while abs(len(self.left_max_heap) - len(self.right_min_heap)) > 1:
            if len(self.left_max_heap) > len(self.right_min_heap):
                popped = -heapq.heappop(self.left_max_heap)
                heapq.heappush(self.right_min_heap, popped)
            else:
                popped = heapq.heappop(self.right_min_heap)
                heapq.heappush(self.left_max_heap, -popped)

    def findMedian(self) -> float:
        total_len = len(self.left_max_heap) + len(self.right_min_heap)
        if total_len == 1:
            return -self.left_max_heap[0]
        elif total_len % 2 == 1:
            if len(self.left_max_heap) > len(self.right_min_heap):
                return -self.left_max_heap[0]
            else:
                return self.right_min_heap[0]
        else:
            return (-self.left_max_heap[0] + self.right_min_heap[0])/2

        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()