class Solution:
    def partition(self, s: str) -> list[list[str]]:
        # all possible --> backtracking? 
        # build cases as we go, don't discard any
        
        # idea: have a list[str] cur
        # at each step, either:
        # start a new string
        # append to the previous string

        # if our index == n, and each string in cur is a palindrome, add it

        answers = []

        def isPalindrome(string):
            l,r = 0, len(string) - 1
            while l <= r:
                if string[l] != string[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def backtrack(i, cur):

            # stopping case
            if (i == len(s)):
                for word in cur:
                    if not isPalindrome(word):
                        return
                answers.append(cur[:])
                return
            
            # decisions
            
            # if cur word exists, add to existing
            if (len(cur) > 0):
                cur[-1] += s[i]
                backtrack(i+1, cur)
                cur[-1] = cur[-1][:-1]

            # create a new word
            cur.append(s[i])
            backtrack(i+1, cur)
            cur.pop()
        
        backtrack(0, [])
        return answers