class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # sort first
        # overlapping --> start or end of one is within portion of other
        # greedy -> just remove overlaps as we see them
        # ideally remove intervals with max number of overlaps ?
        # min number to remove to make the rest non overlapping == max number that dont overlap

        # sort by finishing time
        # iterate over each
        # take the cur finished if it doesnt conflict with any taken so far ?
        init = len(intervals)
        taken = set()

        intervals.sort(key=lambda x: x[1])
        print(intervals)
        for i in intervals:
            take = True
            for j in taken:
                if not (i[0] >= j[1] or i[1] <= j[0]):
                    # print (f"{i} overlaps with {j}")
                    take = False
                    break
            if take:
                taken.add((i[0], i[1]))
        # print ("taken",taken)
        return init - len(taken)
        '''
        ---
          ----------------
            ---  ---  ---
        
        '''