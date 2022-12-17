class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = []
        remaining = s1
        for char in s2:
            if char not in s1:
                remaining = s1
                seen=[]
            elif char not in remaining:
                while seen[0] != char:
                    remaining += seen.pop(0)
                seen.pop(0)
                seen.append(char)
            else:
                index = remaining.index(char)
                remaining = remaining[:index] + remaining [index+1:]
                seen.append(char)
            if len(remaining) == 0: return True
        return False