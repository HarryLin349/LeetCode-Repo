class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        cur = 0
        res = 0
        for change in gain:
            cur += change
            res = max(res, cur)
        return res