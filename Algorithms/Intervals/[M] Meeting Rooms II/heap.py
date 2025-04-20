from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
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
            print("interval", start, end)
            # remove prev from ongoing if possible
            if ongoing and start >= ongoing[0]:
                heappop(ongoing) 
            # add the current meeting to ongoing
            heappush(ongoing, end)
            res = max(res, len(ongoing))
        return res