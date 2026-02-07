from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        q = deque()
        q.append(0)

        level = 0
        while q:
            level += 1
            for _ in range(len(q)):
                front = q.popleft()
                for coin in coins:
                    if front + coin == amount:
                        return level
                    elif front + coin < amount:
                        q.append(front + coin)
        return -1