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
        def is_overlapping(interval1, interval2):
            return not (interval1.end <= interval2.start)
        
        intervals.sort(key = lambda interval : interval.start)
        q = deque()
        q.extend(intervals)

        day = 0
        while q:
            day += 1
            front = q.popleft()
            for _ in range(len(q)):
                second = q.popleft()
                if is_overlapping(front, second):
                    q.append(second)
                else:
                    front = second
        return day
