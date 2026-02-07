class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []
        # max heap of length k
        for x,y in points:
            d = x**2+y**2
            h.append([-d,[x,y]])
        heapq.heapify(h)
        while len(h) > k:
            heapq.heappop(h)
        return [point for d,point in h]