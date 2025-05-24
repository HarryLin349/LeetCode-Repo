class Solution:
    def numTilings(self, n: int) -> int:
        '''
        1,2,3,4 ,5 ,6 ,7  ,8  ,9  ,10
        1,2,5,11,24,53,117,258,569,1255
          1,2,3 ,5 ,10, 64,141,311,686
          0,1,1 ,2 ,5 ,11 ,24 ,53

        dp(i) = dp(i-1) * 2 + dp(i-3)
        '''
        MAX = 10**9 + 7
        memo = [-1] * (n+1)
        memo[0] = 1
        memo[1] = 1
        def dp(i):
            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = dp(i-1) * 2 + dp(i-3)
            return memo[i]
        res = dp(n)
        return res % MAX