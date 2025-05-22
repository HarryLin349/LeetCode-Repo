class Codec:
    def encode(self, strs: list[str]) -> str:
        numwords = str(len(strs))
        posstr = "."
        finalstr = ""
        for string in strs:
            finalstr += string
            posstr += str(len(string)) + "." 
        finalstr += posstr
        finalstr += numwords
        return finalstr
        """Encodes a list of strings to a single string.
        """
        

    def decode(self, s: str) -> list[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        numwords = s.rfind('.')
        numwords = int(s[numwords + 1:])
        numcount = 0
        posstr = ""
        i = -2
        while (numcount < numwords + 1):
            posstr = s[i] + posstr
            if s[i] == ".":
                numcount += 1
            i -= 1
        numwords = int(numwords)
        poslist = posstr.split(".")[1:-1]
        pos = 0
        for i in poslist:
            strlen = int(i)
            nextword = s[pos:pos + strlen]
            pos += strlen
            strs.append(nextword)
        return strs
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))