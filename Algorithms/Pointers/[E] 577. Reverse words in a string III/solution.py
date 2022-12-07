class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(" ")
        result = ""
        for word in a[:-1]:
            result += word[::-1]
            result += " "
        result += a[-1][::-1]
        return result