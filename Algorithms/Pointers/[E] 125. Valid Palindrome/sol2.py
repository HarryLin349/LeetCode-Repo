import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # intuition: pointer on left and right
        # while l < r compare
        # if not equal return false
        # return true
        sanitized = s.lower()
        sanitized = re.sub(r'[^a-zA-Z0-9]', '', sanitized)
        print(sanitized)
        l,r = 0, len(sanitized) - 1
        while (l < r):
            if sanitized[l] != sanitized[r]:
                return False
            l += 1
            r -= 1
        return True