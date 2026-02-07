class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        idx = 0
        current = 0
        for i in range(len(gas)):
            val = gas[i] - cost[i]
            current += val
            if current < 0:
                current = 0
                idx = i + 1 # meaning, i should try from next index
        return idx