class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        def can_circuit(start):
            fuel = 0
            for step in range(n):
                i = (start + step) % n
                fuel += gas[i] - cost[i]
                if fuel < 0:
                    return False
            return True

        for start in range(n):
            if can_circuit(start):
                return start

        return -1