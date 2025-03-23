class Solution:
    def numDecodings(self, s: str) -> int:
        # number -> letter

        # dp. At each stage, we either take the number (if cur or next isnt 0), or we assume its the start of the next
        # valid if cur ==1 or cur == 2 and next < 7
        # dp[i] = ways this string can be decoded, string from i .. n
        # either 0 or 1 (lol)
        n = len(s)
        memo = [-1] * (n + 1)

        def dp(i):
            # i: current position
            # j: skip
            # k: accumulated points
            
            # base cases
            if i >= n:
                return 1
            if memo[i] != -1:
                return memo[i]
            
            c1, c2 = 0,0
            # case 1: take the current
            if (s[i] != "0"):
                c1 = dp(i + 1)
            # case 2: take the current and the next
            if (i +1 < n):
                if (s[i] == "1" or (s[i] == "2" and int(s[i+1]) < 7)):
                    c2 = dp(i + 2)
            
            memo[i] = c1+c2
            return memo[i]
        return dp(0)


