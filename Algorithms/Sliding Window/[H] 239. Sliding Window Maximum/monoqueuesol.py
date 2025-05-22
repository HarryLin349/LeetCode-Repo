import collections

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        d = collections.deque()
        ans = []
        for i, num in enumerate(nums):
            while d and nums[d[-1]] < num:
                d.pop()
            if (d and d[0] <= i - k):
                d.popleft()
            d.append(i)
            if i >= k - 1:
                ans.append(nums[d[0]])
        return ans