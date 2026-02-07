class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = [-x for x in stones]
        heapq.heapify(h)

        while len(h) > 1:
            first = heapq.heappop(h)
            second = heapq.heappop(h)
            if first != second:
                heapq.heappush(h, -abs(first-second))
        if h:
            return -heapq.heappop(h)
        else:
            return 0