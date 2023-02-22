class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = {}
        for x in s:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        print(counts)
        for x in t:
            if x in counts:
                counts[x] -= 1
            else:
                return False
        print(counts)
        for x in counts:
            print(x)
            if counts[x] != 0:
                return False
        return True
        
