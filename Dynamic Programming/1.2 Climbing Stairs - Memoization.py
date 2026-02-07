class Solution:
    def climbStairs(self, n: int) -> int:
        memory = {}
        def decline(curr_stair):
            if curr_stair in memory:
                return memory[curr_stair]
            if curr_stair == 0:
                return 1
            if curr_stair < 0:
                return 0
            memory[curr_stair] = decline(curr_stair-1) + decline(curr_stair - 2)
            return memory[curr_stair]
        return decline(n) #means delining from nth stair
