class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # first instinct:
        # sort greeds and sizes
        # go down the sizes, assigning each size to the smallest greed.
        # for s in size:
        # if size matches cur child, increment fed and move on to next child 
        # else continue
        g.sort()
        s.sort()
        numSatisfied = 0
        curChild = 0
        for size in s:
            if curChild >= len(g): return numSatisfied
            if size >= g[curChild]:
                numSatisfied += 1
                curChild += 1
        return numSatisfied