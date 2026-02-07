class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        def last_occurrence(ch):
            idx = n - 1
            while s[idx] != ch:
                idx -= 1
            return idx

        start = 0
        result = []

        while start < n:
            end = last_occurrence(s[start])
            curr = start + 1

            while curr <= end:
                end = max(end, last_occurrence(s[curr]))
                curr += 1

            result.append(end - start + 1)
            start = end + 1

        return result