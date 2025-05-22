class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print(nums)
        answer = []
        for ind, num in enumerate(nums):
            if ind > 0 and nums[ind] == nums[ind - 1]:
                continue
            result = self.twoSum(nums[ind + 1:], num * -1)
            if len(result) == 0:
                continue
            for ans in result:
                if ans[0] > num:
                    ans.insert(0,num)
                elif ans[1] > num:
                    ans.insert(1,num)
                else:
                    ans.append(num)
                if ans not in answer:
                    answer.append(ans)
        return answer
    
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i1 = 0
        i2 = len(numbers) - 1
        answer = []
        while (i1 < i2):
            sum = numbers[i1] + numbers[i2]
            if sum == target:
                answer.append([numbers[i1],numbers[i2]])
                i1 += 1
            elif sum < target:
                i1 += 1
            else:
                i2 -= 1
        return answer
    
