class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda interval: interval[0])
        ans = []
        for q in queries:
            ans_for_q = float('inf')
            for s,e in intervals:
                if q < s:
                    break
                elif s<=q<=e:
                    ans_for_q = min(ans_for_q, e-s+1)
            ans.append(ans_for_q if ans_for_q != float('inf') else -1)
        return ans