from collections import deque
import numpy as np

class Solution:
    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        '''
        hamming distance = number of positions with diff chars
        select longest subdp(cur+1, cur)seq where groups unequal and word lens =1 and hamming is 1
        seems like dp ?
        for dp at i given last taken at k 
        either take the ith word:
            dp(i) = 1 + dp(i+1, i)
        or dont
            dp(i) = dp(i+1,j)
        naively, calculate hamming distance on a word by word basis (O(n) for each comparison)
            opt: can precompute and memoize
        '''
        n = len(words)
        def validTarget(w1, w2):
            if len(w1) != len(w2):
                return False
            diff = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    diff += 1
            return diff == 1
        
        memo = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        def dp(cur, last):
            if cur >= n:
                return []
            if last != -1 and memo[cur][last] != -1:
                return memo[cur][last]
            # case 1, add the cur
            sol1, sol2 = deque(), deque()
            if last == -1 or (validTarget(words[cur], words[last]) and groups[cur] != groups[last]):
                # if last == -1:
                #     print(f"first pick: {words[cur]}")
                # else:
                #     print (f"valid pick between {words[cur]} and {words[last]}. Adding {words[cur]}")
                sol1 = [words[cur]]
                sol1 += dp(cur+1, cur)
                # print(f"==cur sol at {cur} {last}: {sol1}")
            sol2 = dp(cur+1, last)
            if (len(sol1) > len(sol2)):
                memo[cur][last] = sol1
            else:
                memo[cur][last] = sol2
            return memo[cur][last]
        res = dp(0,-1)
        # print(memo)
        return res