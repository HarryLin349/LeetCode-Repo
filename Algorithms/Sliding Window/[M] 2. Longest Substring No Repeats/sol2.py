class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        maxCount = 0
        seen = []
        for char in s:
            if char not in seen:
                count += 1
            else:
                while (seen.pop(0) != char):
                    count -= 1
            seen.append(char)
            maxCount = max(maxCount, count)
        return maxCount