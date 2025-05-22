class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # idea: build an array
        # sort the array
        # iterate over each interval, if it doesn't overlap with the next, add it
        # else, merge the two intervals 
        intervals.sort(key=lambda x: x[0])
        res = [[-1, -1]]
        for i in intervals:
            if i[0] > res[-1][1]: # cur start > last end, no overlap
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])
        res.pop(0)
        return res