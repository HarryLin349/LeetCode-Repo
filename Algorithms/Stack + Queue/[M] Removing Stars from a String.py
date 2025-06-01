class Solution:
    def removeStars(self, s: str) -> str:
        '''
        idea:
        naively, can just iterate over?
        O(n) time per deletion -> O(n^2) time
        stack?if star, pop the last two
        '''
        stack = []
        for char in s:
            if char == "*":
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)