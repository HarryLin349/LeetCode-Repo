class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
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