class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        '''
        string s
        string a
        string b
        int k

        i is beautiful if
        1) i < len(s) - len(a)
        2) s[i:i+len(a)] == a
        3) there exists an ind j where
            - 1) and 2) for b
            - |j - i| <= k

        basically if we find occurences of a and b within k of eachother.
        idea: find all occurences of a seena
                find all occurences of b seenb
            for all compared a and b, return all a's where a b is within k
        '''
        def findWords(s, word):
            seena = []
            wlen = len(word)
            for i in range(len(s) - wlen + 1):
                if s[i:i+wlen] == word:
                    seena.append(i)
            return seena
            
        res = []
        seena = findWords(s, a)
        seenb = findWords(s, b)
        for i in range(len(seena)):
            for j in range(len(seenb)):
                if abs(seenb[j] - seena[i]) <= k:
                    res.append(seena[i])
                    break
        return res
        '''
        reflection:
        pretty smooth, first intuition works, but ..
        speed 5 mem 24.. oof
        considere bin search algorithm and see time complexity
        look into KMP string matching.. too tired rn
        '''