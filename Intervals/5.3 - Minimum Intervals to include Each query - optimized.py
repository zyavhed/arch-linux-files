import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        idx_element_mapping = {idx : element for idx,element in enumerate(queries)}
        # sorting based on start value
        intervals.sort(key = lambda interval : interval[0])
        queries.sort()
        
        min_heap = []
        idx = 0
        answers = {}

        s = 0
        e = 1
        for q in queries:
            if q in answers:
                continue
            # pushing
            while idx < len(intervals) and q >= intervals[idx][s]:
                if q <= intervals[idx][e]:
                    heapq.heappush(min_heap, (intervals[idx][e]-intervals[idx][s]+1, intervals[idx][e]))
                idx += 1
            # popping
            while min_heap and min_heap[0][e] < q:
                heapq.heappop(min_heap)
            answers[q] = min_heap[0][s] if min_heap else -1
        res = []
        for idx in range(len(queries)):
            res.append(answers[idx_element_mapping[idx]])
        return res