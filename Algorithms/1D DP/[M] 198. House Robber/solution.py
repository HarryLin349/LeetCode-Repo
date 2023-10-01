class Solution:
    def rob(self, nums: List[int]) -> int:
        answer = [-1] * len(nums)
        def opt(house):
            if house >= len(nums):
                return 0
            if answer[house] != -1:
                return answer[house]
            answer[house] = max(nums[house] + opt(house + 2), opt(house + 1))
            return answer[house]
        return opt(0)
