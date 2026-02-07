class Solution:
    def longestPalindrome(self, s: str) -> str:                
        n = len(s)
        maxLen = 0
        maxLenLeft, maxLenRight = 0,0
        for i in range(n):
            #expanding from ith index outward (odd length)
            l, r = i-1, i+1
            while l > -1 and r < n and s[l] == s[r]:
                l,r = l-1, r+1
            #shifting one more inwards because the outer are invalid condition
            l,r = l+1, r-1
            if r - l + 1 > maxLen:
                maxLen = r-l+1
                maxLenLeft, maxLenRight = l,r

            #expanding from ith index outward (even length)
            l, r = i, i+1
            while l > -1 and r < n and s[l] == s[r]:
                l,r = l-1, r+1
            #shifting one more inwards because the outer are invalid condition
            l,r = l+1, r-1
            if r - l + 1 > maxLen:
                maxLen = r-l+1
                maxLenLeft, maxLenRight = l,r
        return s[maxLenLeft:maxLenRight+1]