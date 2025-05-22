class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        '''
        idea: given these intervals, return the max overlap at one time
        sort intervals by start time. 
        increase cur count whenever we encounter an interval and havent left the cur ? 
        keep track of all active and pop when cur start > end ? 
        '''
        ongoing = []
        res = 0
        intervals.sort()
        for start, end in intervals:
            # remove any prev from ongoing
            new = []
            for i in ongoing:
                if i > start:
                    new.append(i)
            ongoing = new
            res = max(res, len(ongoing) + 1)
            # add the current interval to ongoing
            ongoing.append(end)
        return res