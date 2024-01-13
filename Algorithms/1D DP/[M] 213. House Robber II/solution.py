class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        # from 0 to n - 1
        answer1 = [0] * (n +1 )
        # from 0 to n
        answer2 = [0] * (n + 1)
        answer1[n-2], answer2[n-1] = nums[n-2], nums[n-1]

        # from n-1 to 0
        for i in range(n - 3, -1, -1):
            answer1[i] = max(answer1[i+1], answer1[i+2] + nums[i])
        # from n to 0
        for i in range(n - 2, -1, -1):
            answer2[i] = max(answer2[i+1], answer2[i+2] + nums[i])

        return max(answer1[0], answer2[1])
