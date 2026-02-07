class Solution:
    def numDecodings(self, s: str) -> int:
        def isValid(st):
            if st[0] == '0' or int(st) > 26:
                return False
            return True

        path = []
        res = []
        def dfs(curr, remaining):
            if len(remaining) == 0:
                res.append(path[:])
                # print(path)
                return

            for i in range(min(2,len(remaining))):
                curr = remaining[:i+1]
                if curr[0] == '0':
                    return  # can use break as well
                if not isValid(curr):
                    continue
                path.append(curr)
                dfs(remaining[:i+1], remaining[i+1:])
                path.pop()
        dfs("",s)
        return len(res)