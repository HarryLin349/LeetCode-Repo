class Solution:
    def isValid(self, s: str) -> bool:
        starters = ["(", "{", "["]
        enders = {")": "(","}": "{", "]": "["}
        stack = []
        for char in s:
            if char in starters:
                stack.append(char)
            else:
                if len(stack) == 0: return False
                c = stack.pop()
                if enders[char] != c:
                    return False
        if len(stack) > 0: return False
        return True