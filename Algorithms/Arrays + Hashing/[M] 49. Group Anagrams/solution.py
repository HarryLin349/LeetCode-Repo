class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        found = {}
        for word in strs:
            sortedWord = ''.join(sorted(word))
            print(sortedWord)
            if sortedWord in found:
                found[sortedWord].append(word)
            else:
                found[sortedWord] = [word]
        return found.values()
