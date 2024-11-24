from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = 0
        minLen = len(s)
        minStr = s
        valid = False
        remaining = Counter(t)
        for end in range(len(s)):
            curChar = s[end]
            if curChar in remaining:
                remaining[curChar] -= 1
            while (all(v <= 0 for v in remaining.values())):
                valid = True
                if s[start] in t:
                    remaining[s[start]] += 1
                start += 1
            if valid:
                start -=1
                remaining[s[start]] -= 1
            if (all(v <= 0 for v in remaining.values())):
                substr = s[start:end+1]
                if (len(substr) < minLen):
                    minLen = len(substr)
                    minStr = substr
        return minStr if (all(v <= 0 for v in remaining.values())) else ""