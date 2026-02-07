class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(any_str):
            l = 0
            r = len(any_str) - 1
            while l <= r:
                if any_str[l] != any_str[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(remaining, path):
            # Here, we have consumed all the part of the string which is palindrome.
            if remaining == "":
                res.append(path[:])
                return
            for i in range(len(remaining)):
                first_part_of_partitioning = remaining[:i+1]
                if isPalindrome(first_part_of_partitioning):
                    path.append(first_part_of_partitioning)
                    dfs(remaining[i+1:], path)
                    path.pop()
        dfs(s, [])
        return res