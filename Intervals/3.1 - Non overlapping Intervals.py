class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        i = 0
        count = 0
        for j in range(1, len(intervals)):
            first_s, first_e = intervals[i]
            second_s, second_e = intervals[j]
            # Is overlapping? 
            if second_s < first_e:
                # surely we need to remove 1 from it.
                count += 1
                # removing that guy which is extending more towards right
                # in this case, if the first ending value is more
                # it means it is extending more towards right
                # so we need to remove first and choose second
                # thats why we shift our focus to where currently j is
                if first_e >= second_e:
                    i = j
            else:
                #if not overlapped, means we can move i to j
                # so that we can make comparision for futher
                i = j
        return count