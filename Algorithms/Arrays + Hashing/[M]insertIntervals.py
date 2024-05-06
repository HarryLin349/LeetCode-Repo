class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intuition:
        # do a linear scan.
        # curStart, curEnd = newInterval[0], newInterval[1]
        # if interval's start or end is in newInterval, pop that interval
        # (we pick a maximally small start and maximally large end)
        # insert new interval if interval start is after curEnd or if reached end 
        ans = []
        hasAppended = False
        curStart, curEnd = newInterval[0], newInterval[1]
        for i in range(len(intervals)):
            # print('looking at',i,': ',intervals[i])
            # if start after newS and start before newE
            # or if end after newS and end before newE
            if (intervals[i][0] <= newInterval[1] and newInterval[0] <= intervals[i][1]):
                curStart = min(curStart, intervals[i][0])
                curEnd = max(curEnd, intervals[i][1])
                # print('skipping because its within [', curStart, curEnd, ']')
                continue
            elif (intervals[i][1] > curEnd and not hasAppended):
                # print('adding [', curStart, curEnd, '] before it')
                ans.append([curStart, curEnd])
                hasAppended = True
            ans.append(intervals[i])
            # print('added')
        if (not hasAppended):
            # print('afterwards, adding [', curStart, curEnd, ']')
            ans.append([curStart, curEnd])
        return ans
        