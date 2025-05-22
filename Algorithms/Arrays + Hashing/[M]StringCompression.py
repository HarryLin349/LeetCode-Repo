class Solution:
    def compress(self, chars: list[str]) -> int:
        # idea
        # keep track of "cur" character
        # while curchar is prev, increment counter and pop
        # if curchar isnt prev or count > 9, add char and the count (if count not one)
        # update curchar
        prevChar = chars[0]
        curInd = 0
        count = 0
        while(curInd < len(chars)):
            curChar = chars[curInd]
            chars.pop(curInd)
            if (curChar == prevChar):
                count += 1
            else:
                chars.insert(curInd, prevChar)
                curInd += 1
                if (count > 1):
                    digits = list(str(count))
                    chars[curInd:curInd] = digits
                    curInd += len(digits)
                prevChar = curChar
                count = 1
        chars.insert(curInd, prevChar)
        curInd += 1
        if (count > 1):
            digits = list(str(count))
            chars[curInd:curInd] = digits
            curInd += len(digits)
        print(chars)



        