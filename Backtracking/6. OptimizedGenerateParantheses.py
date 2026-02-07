class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(open_count, close_count, curr):
            if open_count == close_count == n:
                res.append(curr)
                return
            
            # Add '(' if we still can
            if open_count < n:
                dfs(open_count + 1, close_count, curr + "(")
            
            # Add ')' only if valid
            if close_count < open_count:
                dfs(open_count, close_count + 1, curr + ")")
        
        dfs(0, 0, "")
        return res
