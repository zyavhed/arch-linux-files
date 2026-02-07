"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from collections import deque
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count, mini = 0,0

        starts = sorted([interval.start for interval in intervals])
        ends = sorted([interval.end for interval in intervals])

        s,e = 0,0

        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                # this time we are taking max because 
                # this tell us whats the maximum
                # occurances that happened
                # i.e. how much is max intersection kind of
                mini = max(mini, count)
                s += 1
            else:
                count -= 1
                e += 1
        return mini
