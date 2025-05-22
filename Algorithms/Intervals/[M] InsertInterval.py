class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # idea: 
        # build a newlist by iterating over intervals
        # compare each to see if there's an overlap between i and newInterval
        # if there is? skip it.
        # if there's no overlap with newInterval and nextStart > newIntervalEnd, add it
        # if newInterval wasn't added, add it to the end
        # no overlap if curend < newstart or curstart > newend

        newlist = []

        for idx, i in enumerate(intervals):
            # interval is after new interval
            if (i[0] > newInterval[1]):
                newlist.append(newInterval)
                # newlist.append(i)
                return newlist + intervals[idx:]
            # interval is before newInterval, curEnd < newStart
            elif (i[1] < newInterval[0]):
                newlist.append(i)
            # cur interval overlaps with newInterval
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
            # overlap, skip
        newlist.append(newInterval)
        return newlist

