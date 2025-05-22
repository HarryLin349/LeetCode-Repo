from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        '''
        idea: given these intervals, return the max overlap at one time
        sort intervals by start time. 
        increase cur count whenever we encounter an interval and havent left the cur ? 
        keep track of all active and pop when cur start > end ? 
        '''
        ongoing = []
        intervals.sort()
        for start, end in intervals:
            ongoing.append((start, 1))
            ongoing.append((end, -1))
        
        ongoing.sort()
        cur = 0
        res = 0
        for _, delta in ongoing:
            cur += delta
            res = max(res, cur)
        return res
