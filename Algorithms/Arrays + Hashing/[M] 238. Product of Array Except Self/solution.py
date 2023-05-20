class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, answer = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        prod = 1
        for i in range(len(nums)):
            prod *= nums[i]
            left[i] = prod
        prod = 1
        for i in reversed(range(len(nums))):
            prod *= nums[i]
            right[i] = prod
        for i in range(len(nums)):
            l = 1 if i == 0 else left[i-1]
            r = 1 if i == len(nums) - 1 else right[i+1]
            answer[i] = l * r
        print(answer)
        return answer