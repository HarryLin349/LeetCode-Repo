class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = []
        start, end = 0, 0
        maxCount = 0
        for char in s:
            if (char in seen):
                start += 1
                while seen.pop(0) != char:
                    start += 1
            seen.append(char)
            end += 1
            if end - start > maxCount:
                maxCount = end - start
        return maxCount