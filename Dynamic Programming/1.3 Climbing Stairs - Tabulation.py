class Solution:
    def climbStairs(self, n: int) -> int:
        # here, in this answers arrays, answers[i] represents
        # the number of ways to get to nth stair from ith stair
        answers = [-1] * (n+1)
        #think about it:
        # if you are at nth stair, whats the way to get to nth stair?
        # obviously, its zero
        answers[n] = 0
        #think, if you are at nth stair, in how many ways you can get to 
        # nth stair from (n-1) th stair? obviously, its only one way.
        answers[n-1] = 1
        # similarly for to get to nth stair from (n-2)th stair, its two ways
        # these are base conditions to fill others answers
        answers[n-2] = 2

        for i in range(3,n+1): # from 3 to n
            # take sum of next two elements
            answers[n-i] = answers[n-i+1] + answers[n-i+2]
        return answers[0]
