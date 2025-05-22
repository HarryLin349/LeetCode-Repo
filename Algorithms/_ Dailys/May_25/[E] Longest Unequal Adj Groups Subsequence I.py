class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        '''
        ideas:
        for a subsequence 0,0 1, 0, 1
        we just need to take whenever the group swaps
        we should account for two possibilities, first taken is 0 and first taken is 1
        '''
        cur1 = 0
        cur2 = 1
        r1,r2 = [], []
        for i in range(len(words)):
            if (cur1 != groups[i]):
                r1.append(words[i])
                cur1 = groups[i]
            if (cur2 != groups[i]):
                r2.append(words[i])
                cur2 = groups[i]
        return r1 if len(r1) > len(r2) else r2
