class Solution:
    def reverseString(self, s: list[str]) -> None:
        spare = ""
        length = len(s)
        for x in range(floor(length/2)):
            spare = s[x]
            s[x] = s[length - x -1]
            s[length - x  - 1] = spare
        
        """
        Do not return anything, modify s in-place instead.
        """