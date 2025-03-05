class Solution:
    def trap(self, height: List[int]) -> int:
        # idea: pointers l, r
        # move outside in

        l, r = 0, len(height) - 1
        max_l, max_r, water = height[0],height[r],0
        while l < r:
            if max_l < max_r:
                water += max_l - height[l]
                l += 1
                max_l = max(height[l], max_l)
                # eval max_l, since it's the limiting factor
            else:
                water += max_r - height[r]
                r -= 1
                max_r = max(height[r], max_r)
        return water