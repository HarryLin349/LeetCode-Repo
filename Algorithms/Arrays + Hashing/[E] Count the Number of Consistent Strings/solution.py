class Solution:
    def countConsistentStrings(self, allowed: str, words: list[str]) -> int:
        # idea: we just care about characters occuring
        # not necessarily counts
        allowSet = set(allowed)
        res = 0
        for word in words:
            valid = True
            for char in word:
                if char not in allowSet:
                    valid = False
                    break
            res += 1 if valid else 0
        return res