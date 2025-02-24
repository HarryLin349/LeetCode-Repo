import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h hours to eat i piles
        # sum(elems // k) <= h
        # find the min k 
        # idea: bin search from max and min
        # time: O(nlogn)
        lo,hi, mid = 1, max(piles), 0
        answer = hi

        while lo <= hi:
            mid = (lo + hi) // 2
            csum = 0
            # check if its valid
            for pile in piles:
                csum += math.ceil(pile/mid)
            # print (f"{lo} {hi} -> {mid} takes {csum} hours")

            if csum > h:
                lo = mid + 1
            elif csum <= h:
                hi = mid - 1
            if csum <= h and mid < answer:
                answer = mid
        return answer

