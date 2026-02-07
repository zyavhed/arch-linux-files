from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return 0
            
        q = deque()
        level = 0
        q.append(0)

        while q:
            level += 1
            for _ in range(len(q)):
                front = q.popleft()
                if front + nums[front] >= n-1:
                    return level
                for i in range( front+1, front + nums[front]+1 ):
                    q.append(i)