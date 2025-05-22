class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        '''
        ideas:
        maintain a stack for odds, if even reset, if odd add on
        even better, just have a variable
        '''
        curOdds = 0
        for num in arr:
            if num % 2 == 0:
                curOdds = 0
            else:
                curOdds += 1
            if curOdds == 3:
                return True
        return False