class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        for i in range(n):
            #expanding from ith index outward (odd length)
            l, r = i, i
            while l > -1 and r < n and s[l] == s[r]:
                count += 1
                l,r = l-1, r+1
            #expanding from ith index outward (even length)
            l, r = i, i+1
            while l > -1 and r < n and s[l] == s[r]:
                count += 1
                l,r = l-1, r+1
        return count