class Solution:
    def countPairs(self, deliciousness: list[int]) -> int:
        '''
        ideas: 
        naively, iterate over O(n^2) and check each pair 
        keep a set of powers of 2 to check? based on the max
        or have a function to check if its power of 2 by dividing repeatedly 
        '''
        '''
        For each of the powers from 2^0 .. 2^21
        We check to see if we've already seen the needed complement
        '''
        MOD = 10**9 + 7
        seen = {}
        res = 0
        # for each power, we count the amount that sum to this target
        for d in deliciousness:
            for i in range(22):
                power = 2**i
                target = power - d
                if target in seen:
                    res += seen[target]
            if d in seen:
                seen[d] += 1
            else:
                seen[d] = 1
        return res % MOD
                