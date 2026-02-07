class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(open,closed,curr):
            if open == closed == n:
                res.append(curr[:])
                return
            if closed > open:
                return
            if open > n or closed > n:
                return
            dfs(open+1, closed, curr + '(')
            dfs(open, closed+1, curr + ')')

        dfs(0,0,"")
        return res
        