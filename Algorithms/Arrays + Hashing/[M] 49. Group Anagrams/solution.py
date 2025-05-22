# Runtime 98.66%
# Memory 45.5%

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        found = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            print(sortedWord)
            if sortedWord in found:
                found[sortedWord].append(word)
            else:
                found[sortedWord] = [word]
        return found.values()
