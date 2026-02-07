class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        lastIdx = {ch:idx for idx,ch in enumerate(s)}
        
        maxEnd = 0
        size = 0
        res = []
        for i,c in enumerate(s):
            maxEnd = max(maxEnd, lastIdx[c])
            size += 1
            if i == maxEnd:
                res.append(size)
                size = 0
        return res