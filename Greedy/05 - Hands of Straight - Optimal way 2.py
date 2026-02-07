import heapq
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize!=0:
            return False
        freq=Counter(hand)

        min_heap = [v for v in freq]
        heapq.heapify(min_heap)
        
        while min_heap:
            first = min_heap[0]
            for card in range(first, first+groupSize):
                if card not in freq:
                    return False
                freq[card] -= 1

                if freq[card] == 0:
                    if card != min_heap[0]:
                        return False
                    
                    heapq.heappop(min_heap)
                    del freq[card]
        return True