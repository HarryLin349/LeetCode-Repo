class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # opt(i) -> longest subsequence from ai..an and bj..bm
        n,m = len(text1), len(text2)
        ans = [[-1 for _ in range(m)] for _ in range(n)]
        def opt(i,j):
            if i >= n or j >= m:
                return 0
            if ans[i][j] != -1:
                return ans[i][j]
            # case 1: we use ai
            sol1, sol2, sol3 = 0,0,0
            if text1[i] == text2[j]:
                sol1 = 1 + opt(i + 1, j + 1)
            sol2 = opt(i+1, j)
            sol3 = opt(i, j+1)
            ans[i][j] = max(sol1, sol2, sol3)
            return ans[i][j]
            # case 2: we use bi
            # case 3: we use both
        return opt(0,0)