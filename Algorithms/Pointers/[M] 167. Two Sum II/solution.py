class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i1 = 1
        i2 = len(numbers)
        while (i1 < i2):
            sum = numbers[i1-1] + numbers[i2-1]
            if sum == target:
                return [i1,i2]
            elif sum < target:
                i1 += 1
            elif sum > target:
                i2 -= 1