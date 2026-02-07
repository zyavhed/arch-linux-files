class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        def is_overlapping(interval1, interval2):
            s1, e1 = interval1
            s2, e2 = interval2
            return not (e1<s2 or e2 < s1)

        new_intervals = []
        new_intervals.append(intervals[0])
        for i in range(1, len(intervals)):
            if is_overlapping(intervals[i], new_intervals[-1]):
                s1, e1 = new_intervals.pop()
                s2, e2 = intervals[i]
                new_intervals.append([min(s1, s2), max(e1, e2)])
            else:
                new_intervals.append(intervals[i])
        return new_intervals