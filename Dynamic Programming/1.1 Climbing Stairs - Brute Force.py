class Solution:
    def climbStairs(self, n: int) -> int:
        def climb(curr_stair):
            if curr_stair == n:
                return 1
            if curr_stair > n:
                return 0
            return climb(curr_stair+1) + climb(curr_stair+2)
        return climb(0) #means climbing from 0th stair

        # thinking in reverse order
        def decline(curr_stair):
            if curr_stair == 0:
                return 1
            if curr_stair < 0:
                return 0
            return decline(curr_stair-1) + decline(curr_stair - 2)
        return decline(n) #means delining from nth stair
