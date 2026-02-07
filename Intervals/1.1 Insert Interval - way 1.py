class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_intervals = []
        for i in range(len(intervals)):
            s1, e1 = intervals[i]
            s2, e2 = newInterval

            # means the interval should be appended
            # and there is no intersection further
            if e2 < s1:
                new_intervals.append(newInterval)
                new_intervals.extend(intervals[i:])
                return new_intervals
            # means this interval is not intersected
            elif e1 < s2:
                new_intervals.append(intervals[i])
            # yeah, intersection happens here
            else:
                newInterval = [min(s1,s2), max(e1,e2)]
        new_intervals.append(newInterval)
        return new_intervals