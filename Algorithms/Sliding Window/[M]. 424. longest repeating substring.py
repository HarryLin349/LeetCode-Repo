class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curLetter = s[0]
        letterCount = [0]*26
        start = 0
        maxCount = 0
        maxLength = 0
        for i in range(len(s)):
            curInd = ord(s[i]) - 65
            letterCount[curInd] += 1
            maxCount = max(maxCount, letterCount[curInd])
            if (i - start + 1 - maxCount > k):
                letterCount[ord(s[start]) - 65] -= 1
                start += 1
            maxLength = max(maxLength, i - start + 1)
        return maxLength
        
