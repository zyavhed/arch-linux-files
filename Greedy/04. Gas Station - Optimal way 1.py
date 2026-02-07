class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        net = [g-c for g,c in zip(gas,cost)]
        if sum(net) < 0:
            return -1

        idx = 0
        cumulative_sum = 0

        for i,val in enumerate(net):
            cumulative_sum += val
            if cumulative_sum < 0:
                cumulative_sum = 0
                idx = i + 1 # meaning, i should try from next index
        return idx