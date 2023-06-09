class Solution:
    def maxArea(self, height: List[int]) -> int:
        curMax = 0
        l = 0
        r = len(height) - 1
        while (l < r):
            curArea = min(height[l], height[r]) * (r - l)
            curMax = max(curMax, curArea)
            if (height[l] < height[r]):
                l += 1
            else:
                r -= 1
        return curMax