class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # idea: backtracking --> each step, pick a letter for each number

        # for each number, we choose a letter it could represent
        # add it to the current
        # and then remove it
        # stopping condition = when our current string is equal to length of digits

        answers = []
        digitmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def backtrack(i, curString):
            if (i == len(digits)):
                answers.append(curString)
                return
            print (f"i {i} digits[i] {digits[i]}")
            letters = digitmap[digits[i]]            
            # for each possible letter, add it to the cur
            for letter in letters:
                curString += letter
                backtrack(i+1, curString)
                curString = curString[:-1]
        if digits == "":
            return []
        backtrack(0, "")
        return answers