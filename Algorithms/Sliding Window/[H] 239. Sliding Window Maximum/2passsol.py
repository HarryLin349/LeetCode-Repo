'''
This solution times out, but I still think it's clever, since its time complexity is O(n).
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        leftMax = []
        rightMax = []
        cLeftMax = nums[0]
        cRightMax = nums[-1]
        size = len(nums)
        ans = []
        for i in range(size):
            if i % k == 0:
                cLeftMax = nums[i]
            else:
                cLeftMax = max(cLeftMax, nums[i])
            leftMax.append(cLeftMax)
        for i in reversed(range(size)):
            if i % k == k-1:
                cRightMax = nums[i]
            else:
                cRightMax = max(cRightMax, nums[i])
            rightMax.insert(0, cRightMax)
        for i in range(size - k + 1):
            ans.append(max(rightMax[i], leftMax[i + k - 1]))
        return ans
