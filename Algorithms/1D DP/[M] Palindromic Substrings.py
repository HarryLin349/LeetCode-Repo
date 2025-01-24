class Solution:
    def countSubstrings(self, s: str) -> int:
        # idea: for 0.. n, count substrings
        # use dp to memoize, dp[i][j] means s[i:j+1] is a palindrome

        # init dp array
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        
        substrings = n
        for i in range(n):
            dp[i][i] = 1
            if (i+1 < n) and s[i] == s[i+1]:
                dp[i][i+1] = 1
                substrings += 1

        # count
        for l in range (2,n):
            for i in range(0, n-l):
                if (s[i] == s[i + l] and dp[i+1][i + l -1] == 1):
                    dp[i][i+l] = 1
                    substrings +=1
        return substrings

