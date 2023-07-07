import collections 
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        mono = collections.deque()
        result = [0] * n
        for i, val in enumerate(temperatures):
            while mono and val > temperatures[mono[-1]]:
                j = mono.pop()
                result[j] = i - j
            mono.append(i)
        return result
