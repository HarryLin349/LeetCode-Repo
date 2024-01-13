# 1347. Minimum Number of Steps to Make Two Strings Anagram
# Medium
from collections import Counter

class Solution:
    #intuition: we count the difference between the strings t and s
    # use array to rep character count
    # then we know every negative difference between t and s must be swapped
    # and every positive difference is automatically handled by that swap
    def minSteps(self, s: str, t: str) -> int:
        diffCount = [0] * 26
        diff = 0 
        for i in range(len(s)):
            diffCount[ord(t[i]) - ord('a')] += 1
            diffCount[ord(s[i]) - ord('a')] -= 1

        for num in diffCount:
            if num > 0:
                diff += num
        return diff