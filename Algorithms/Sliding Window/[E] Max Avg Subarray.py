class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        '''
        ideas
        we want a length equal to k
        with the max average value

        track max average w/ variable, maxavg

        sliding window, just increment l and r by 1 each time
        then divide by k at the end
        '''
        l, r = 0, k-1
        curAvg = sum(nums[:k])
        maxAvg = curAvg
        for i in range(1, len(nums) - k + 1):
            curAvg += nums[i+k-1]
            curAvg -= nums[i-1]
            maxAvg = max(maxAvg, curAvg)
        return maxAvg / k
