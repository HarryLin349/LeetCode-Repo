class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        ops = ["+","-","/","*",]
        stack = []
        first = True
        for s in tokens:
            if s in ops:
                a2, a1 = stack.pop(), stack.pop()
                if s == "+":
                    stack.append(a1 + a2)
                elif s == "-":
                    stack.append(a1 - a2)
                elif s == "*":
                    stack.append(a1 * a2)
                else:
                    stack.append(int(a1 / a2))
            else:
                stack.append(int(s))
        return stack[-1]