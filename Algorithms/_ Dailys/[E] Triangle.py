'''
Simple elif with unpacking
'''
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        '''
        triangle iff any 2 sides > remaining
        equilateral iff all equal
        isosceles iff two equal
        none if any side > remaining 2
        '''
        a,b,c = nums
        if a == b and b == c:
            return "equilateral"
        elif a + b <= c or a + c <= b or b+c <= a:
            return "none"
        elif a == b or b == c or a == c:
            return "isosceles"
        else:
            return "scalene"