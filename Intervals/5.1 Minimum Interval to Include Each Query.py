class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        mapping = {}

        for s,e in intervals:
            window_size = e-s+1
            for i in range(s,e+1):
                mapping[i] = min( mapping.get(i,float('inf')), window_size)
        
        ans = []
        for q in queries:
            if q not in mapping:
                ans.append(-1)
            else:
                ans.append(mapping[q])
        return ans