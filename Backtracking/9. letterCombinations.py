class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        map = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz'
        }
        res = []
        def dfs(idx,path):
            # This is where we know we have consumed all the digits
            if idx == len(digits):
                res.append(path)
                return
            
            #exploring all the possible paths
            for ch in map[digits[idx]]:
                dfs(idx+1,path+ch)
        dfs(0,"")
        return res