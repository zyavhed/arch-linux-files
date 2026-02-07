class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        deletion_cost = {}

        for ch,cost in zip(s,cost):
            deletion_cost[ch] = deletion_cost.get(ch, 0) + cost
        
        return sum(deletion_cost.values()) - max(deletion_cost.values())