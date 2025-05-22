class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        answer = [1] * length
        l,r = 1,1
        for i in range(length):
            answer[i] *= l
            l *= nums[i]
            answer[length - i - 1] *= r
            r *= nums[length - i - 1]
        print(answer)
        return answer