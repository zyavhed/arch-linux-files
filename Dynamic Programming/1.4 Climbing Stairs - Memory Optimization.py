class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first = 1
        second = 2
        for i in range(n-2): # from 3 to n
            third = first + second
            store_second = second
            second = third
            first = store_second
        return second  # or we can also return third