class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        def merge_triplet(j, i):
            for k in range(3):
                triplets[j][k] = max(triplets[i][k], triplets[j][k])
        
        def should_we_merge(pivot, other):
            should_be_merged = False
            for k in range(3):
                if max(triplets[pivot][k], triplets[other][k]) > target[k]:
                    return False
                if triplets[other][k] == target[k]:
                    should_be_merged = True
            return should_be_merged
        #selection of pivot element
        pivot = -1
        for i in range(len(triplets)):
            candidate = -1
            for j in range(3):
                if triplets[i][j] > target[j]:
                    candidate = -1
                    break
                if triplets[i][j] == target[j] and candidate == -1:
                    candidate = i
            if candidate != -1:
                pivot = candidate
                break
        # no one could become pivot element
        if pivot == -1:
            return False
        
        #merging process
        for other in range(pivot+1, len(triplets)):
            if should_we_merge(pivot, other):
                merge_triplet(pivot, other)
        #could we achieve the target?
        return triplets[pivot] == target