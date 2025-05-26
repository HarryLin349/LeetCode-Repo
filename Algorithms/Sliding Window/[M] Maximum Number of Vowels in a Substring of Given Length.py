class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        '''
        string s, int k, max number of vowels in any substring of s with len k
        sliding window, advance by 1
        if in set increase
        n = 5 k = 2
        01234

        '''
        vowels = set(['a','e','i','o','u'])
        curcount = 0
        for i in range(k):
            if s[i] in vowels:
                curcount += 1
        res = curcount
        # print(f"init {s[:k]}, {curcount}")
        for i in range(1, len(s) -k +1):
            if s[i-1] in vowels:
                curcount -= 1
            if s[i+k-1] in vowels:
                curcount += 1
            # print(f"{i}-{i+k-1}, {s[i:i+k]} = {curcount}")
            res = max (res, curcount)
        return res