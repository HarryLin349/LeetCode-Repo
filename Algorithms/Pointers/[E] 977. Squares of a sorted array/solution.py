class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        positives = []
        negatives = []
        sortedNums = []
        lnum = len(nums)
        for num in nums:
            if num < 0:
                negatives.insert(0, pow(num,2))
            else:
                positives.append(pow(num,2))
        while (len(positives) > 0 and len(negatives) > 0):
            if (positives[0] < negatives[0]):
                sortedNums.append(positives.pop(0))
            else:
                sortedNums.append(negatives.pop(0))
        if (len(positives) > 0):
            sortedNums.extend(positives)
        else:
            sortedNums.extend(negatives)
        return sortedNums