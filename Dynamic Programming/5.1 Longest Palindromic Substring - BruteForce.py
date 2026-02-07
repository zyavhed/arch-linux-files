class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        longest_substr = ""
        maxi = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if isPalindrome(i,j) and (j-i+1) > maxi:
                    maxi = j-i+1
                    longest_substr = s[i:j+1]
        return longest_substr


        