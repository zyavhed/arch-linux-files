class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        memory = [[False]*n for _ in range(n)]
        count = 0
        # memory[2][5] -> means the string s[2:5+1] is either palindrome or not
        
        def isPalindrome(l,r):
            if l >= r:
                return True

            if memory[l][r]:
                return memory[l][r]

            if (s[l] == s[r]):
                memory[l][r] = isPalindrome(l+1, r-1)
                return memory[l][r]
                
            return memory[l][r]
        
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i,j):
                    count += 1
        return count