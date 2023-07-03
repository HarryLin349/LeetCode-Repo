class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(l,r,combo):
            if len(combo) == n * 2:
                result.append(combo)
                return
            if l < n:
                dfs(l + 1,r,combo + "(")
            if r < l:
                dfs(l,r + 1,combo+")")
        dfs(0,0,"")
        return result