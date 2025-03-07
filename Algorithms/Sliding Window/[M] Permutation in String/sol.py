class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # idea: permutation just means same char counts
        # so we maintain a char count of s1 and s2
        # and then check s2 with a sliding window
        # note that the sliding window has to be length of s1 to be a full permutation
        # so we just start with l, r = 0, len(s1) -1
        # increment both by 1 and update the char counts as needed
        # O(n^2)

        n,m = len(s1), len(s2)
        if n > m:
            return False
        s1perms = [0] * 26
        s2perms = [0] * 26
        for char in s1:
            s1perms[ord('a') - ord(char)] += 1
        
        for i in range(n):
            print()
            s2perms[ord('a') - ord(s2[i])] += 1
            
        print (f"s1 perms {s1perms}")
        l, r = 0, n-1
        while r < m-1:
            if s1perms == s2perms:
                return True
            # increment window
            s2perms[ord('a') - ord(s2[l])] -= 1
            s2perms[ord('a') - ord(s2[r+1])] += 1
            l += 1
            r += 1
        return s1perms == s2perms

