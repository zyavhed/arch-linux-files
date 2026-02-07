class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])

        new_intervals = []
        new_intervals.append(intervals[0])
        for i in range(1, len(intervals)):
            s1 , e1 = new_intervals[-1]
            s2 , e2 = intervals[i]
            # s1 < s2 for sure because we already sort them
            if s2 <= e1:
                new_intervals[-1][1] = max(e1, e2)
            else:
                new_intervals.append(intervals[i])
        return new_intervals