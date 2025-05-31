class Solution:
    def decodeString(self, s: str) -> str:
        '''
        ideas:
            we need to handle recursive duplicates
            3[a2[c]]
            1. when we see a digit, we know to start creating a string
            2. when we see an end ], we know we've finished
            have a function that returns the final string 
        '''
        res = ""

        '''
        when we see a digit, we know to start forming d * the word
            this word can contain subwords
                need to build off the 
                    whenever we see a "]", pop the current word from the curword stack
                    add it to the new current word, += mult * word
        '''
        words = [""]
        mults = [""]
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                words.append("")
                mults.append(char)
                i += 1
                while (s[i].isdigit()):
                    mults[-1] += s[i]
                    i += 1
                continue
            elif char == "[":
                i += 1
                continue
            elif char == "]":
                word, mult = words.pop(), mults.pop()
                words[-1] = words[-1] + int(mult) * word
            else:
                words[-1] += char
            i += 1
        # print(words)
        # print(mults)
        return words[0]