class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        maxHeight = 0
        potentialWater = 0
        for i in range(len(height)):
            if (height[i] >= maxHeight):
                water += potentialWater
                potentialWater = 0
                maxHeight = height[i]
                continue
            potentialWater += maxHeight - height[i]
        potentialWater = 0
        maxHeight2 = 0
        for i in reversed(range(len(height))):
            if height[i] == maxHeight:
                water += potentialWater
                break
            if (height[i] >= maxHeight2):
                water += potentialWater
                potentialWater = 0
                maxHeight2 = height[i]
                continue
            potentialWater += maxHeight2 - height[i]
        return water