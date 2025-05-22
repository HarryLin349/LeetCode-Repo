class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print(nums)
        answer = []
        for ind, num in enumerate(nums):
            result = self.twoSum(nums, num * -1, ind)
            if len(result) == 0:
                continue
            for ans in result:
                ans.append(num)
                if sorted(ans) not in answer:
                    answer.append(sorted(ans))
        return answer
    
    def twoSum(self, numbers: list[int], target: int, forbidden: int) -> list[int]:
        i1 = 0
        i2 = len(numbers) - 1
        answer = []
        while (i1 < i2):
            sum = numbers[i1] + numbers[i2]
            if sum == target and i1 != forbidden and i2 != forbidden:
                answer.append([numbers[i1],numbers[i2]])
                i1 += 1
            elif sum < target:
                i1 += 1
            else:
                i2 -= 1
        return answer
    
