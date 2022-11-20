class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        left = 1
        right = n
        mid = floor((left + right) / 2)
        lastBad = 0
        while True:            
            isBad = isBadVersion(mid)
            if isBad:
                if right - left <= 1:
                    return mid 
                right = mid
            else:
                if right - left <= 1:
                    return mid + 1
                left = mid + 1
            mid = floor((left + right) / 2)

            
            