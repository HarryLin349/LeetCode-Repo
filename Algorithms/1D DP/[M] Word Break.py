class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        idea: 
        as we progress, either take the cur word or dont
        '''
        n = len(s)
        words = set(wordDict)
        memo = [-1 for _ in range(n)]
        
        def dp(i):
            if i >= n or s[i:] in words:
                return True
            if (memo[i] != -1):
                return memo[i]
            for j in range(i,n):
                if s[i:j] in words and dp(j):
                    memo[i] = True
                    return memo[i]
            memo[i] = False
            return memo[i]
        return dp(0)