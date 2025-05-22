class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        '''
        idea: can attend meeting = no conflicts
        sort by start time to take meetings as they come
        if we start a new interval and havent left the last, return false
        '''
        intervals.sort()
        for i in range(len(intervals) -1):
            cur, nxt = intervals[i], intervals[i+1]
            if (cur[1] > nxt[0]):
                return False
        return True
        