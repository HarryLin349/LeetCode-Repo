class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "": return True
        sChars = list(s)
        for char in t:
            if sChars[0] == char:
                sChars.pop(0)
            if len(sChars) == 0:
                return True
        return False