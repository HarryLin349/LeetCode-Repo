class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # idea: 
        # build a newList by iterating over intervals
        # compare each to see if there's an overlap between i and newInterval
        # if there is? skip it.
        # if there's no overlap with newInterval and nextStart > newIntervalEnd, add it
        # if newInterval wasn't added, add it to the end
        # no overlap if curend < newstart or curstart > newend

        newList = []

        for idx, i in enumerate(intervals):
            # interval is after new interval
            if (i[0] > newInterval[1]):
                newList.append(newInterval)
                # newList.append(i)
                return newList + intervals[idx:]
            # interval is before newInterval, curEnd < newStart
            elif (i[1] < newInterval[0]):
                newList.append(i)
            # cur interval overlaps with newInterval
            else:
                newInterval = [min(i[0], newInterval[0]), max(i[1], newInterval[1])]
            # overlap, skip            
        newList.append(newInterval)
        return newList

