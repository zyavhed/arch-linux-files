class Solution:
    def longestPalindrome(self, s: str) -> str:        
        def isPalindrome(l,r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
                
            return memory[l][r]]
        # starting from biggest window size
        # kind of sliding window
        n = len(s)
        for windowSize in range(n,0,-1): # n -> 1
            l = 0
            r = l + windowSize - 1
            while r < n:
                if isPalindrome(l,r):
                    return s[l:r+1]
                l += 1
                r += 1