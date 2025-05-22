from collections import defaultdict
class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        '''
        ideas:
        manually doing all these changes -> probably too slow
        inserting a char in a string could be O(n) for each... O(n^2 * t)
        we only need length, so rules can be:
        represent chars as numbers?
        each iteration, we go from 1 ->26, then we replace with 1,2 (+1 increase)
        for t = 24 on 1,2,3

        25,26,27
        25, 1,2, 2,3

        1 -> 1,2 (+1)-> 1,2, 1,2  (+2), 1,2, 1,2, 1,2, 1,2 (+4)
        exponential growth, plus constantly shifting forward

        1 + 26 

        for t = 54 on 1
        55 (1)
        26 + 26  + 3, 
        1,2 + 25 + 3 (2)
        26,27 + 3 (3)
        1,2, 2,3 + 3 
        4,5,5,6 (4)

        alt: lets just have a char freq map and iterate
        for each thing .. 
        e.g. if we have two y's, we want to create two zs
            nextInd = i + 1
            nextCount[i + 1] = charCount[i]
            unless i == 26, then we have to add one a and b:
            nextCount[0] += 1 and nextCount[1] += 1 
        '''
        charCount = [0] * 26
        nextCount = [0] * 26
        a = ord('a')
        for char in s:
            charCount[ord(char) - a] += 1
        for ind in range(t):
            # print(f"==iteration {ind}") 
            for i in range(26):
                if i == 25:
                    if charCount[i] == 0:
                        nextCount[0] = 0
                    else:
                        # print ("  handling z..")
                        # print("  cur", charCount)
                        # print("  next", nextCount)
                        nextCount[0] = charCount[i]
                        nextCount[1] += charCount[i]
                else:
                    nextCount[i + 1] = charCount[i]
                    charCount[i] = 0
            # print("next",nextCount)
            charCount = nextCount.copy()
        # print (charCount)
        mod = 10 ** 9 + 7
        return sum(charCount) % mod