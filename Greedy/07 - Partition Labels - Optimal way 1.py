class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        last_idx = {ch:idx for idx,ch in enumerate(s)}

        start = 0
        result = []

        while start < n:
            end = last_idx[s[start]]
            curr = start + 1

            while curr <= end:
                end = max(end, last_idx[s[curr]])
                curr += 1

            result.append(end - start + 1)
            start = end + 1

        return result
