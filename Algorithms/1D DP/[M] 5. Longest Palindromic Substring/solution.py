class Solution:
    def longestPalindrome(self, s: str) -> str:
        # recurrence
        # ans[i][j] returns if s[i:j+1] is a palindrom
        n = len(s)
        ans = [[False for _ in range(n)] for _ in range(n)]

        cmax = s[0]
        for i in range(n):
            ans[i][i] = True
            if i < n - 1 and s[i] == s[i + 1]:
                ans[i][i+1] = True
                cmax = s[i:i+2]
        for j in range(2,n):
            length = j
            for i in range(0, n - length):
                # print("looking at start/end", i, i+length)
                if s[i] == s[i + length]:
                    if ans[i+1][i+length-1]: # 5, 10 6 9
                        cmax = s[i:i+length + 1]
                        ans[i][i+length] = True
        return cmax
