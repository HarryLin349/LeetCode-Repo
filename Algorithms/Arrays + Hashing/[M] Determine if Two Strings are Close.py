from collections import defaultdict
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        ideas
            op1 swap 2 existing chars
            op2 replace all a -> b
        
        we have unlimited transformations
        so theoretically if we have all the same character counts, we can repeatedly 
        swap spots until we match?
        we can also swap character counts, so
            op1 -> any ordering valid, as long as we have char counts
            op2 -> any dist valid as long as the raw counts match
        
        so we need to check for two things
            1) word1 and word2 have the same letters (and none diff)
            2) word1 and word2's letters have the same frequency dist.
        
        naively, 1) -> generate a set of letters and compare
                 2) -> foreach word, count each letter in arr, sort and compare
        '''
        w1count = defaultdict(int)
        w2count = defaultdict(int)
        if len(word1) != len(word2):
            return False
        for char in word1:
            w1count[char] += 1
        for char in word2:
            w2count[char] += 1
        # print(w1count)
        # print(w2count)
        if w1count.keys() != w2count.keys():
            return False
        w1freq = [count for key,count in w1count.items()]
        w2freq = [count for key,count in w2count.items()]
        w1freq.sort()
        w2freq.sort()
        # print(w1freq, w2freq)
        return w1freq == w2freq