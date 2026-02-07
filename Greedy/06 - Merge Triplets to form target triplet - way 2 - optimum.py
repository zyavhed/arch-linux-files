class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        check = [[t, False] for t in target]
        required = len(check)

        for triplet in triplets:
            # asking myself, can this be part of the triplet?
            should_we_merge = False
            merging_idx = []
            for i in range(3):
                if triplet[i] > target[i]:
                    should_we_merge = False
                    break
                if triplet[i] == target[i] and check[i][1] == False:
                    merging_idx.append(i)
                    should_we_merge = True
            
            if should_we_merge:
                required -= len(merging_idx)
                if required == 0:
                    return True
                for idx in merging_idx:
                    check[idx][1] = True
        return False