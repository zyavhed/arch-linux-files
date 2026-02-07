class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        if groupSize == 1:
            return True
        
        minHeap = [] # stores (next_expected_num, current_group_size)
        hand.sort()
        for num in hand:
            if not minHeap or minHeap[0][0] > num:
                heapq.heappush(minHeap, (num+1, 1)) # create a new group
            elif minHeap[0][0] == num:
                curr_num, curr_size = heapq.heappop(minHeap)
                if curr_size + 1 < groupSize:
                    heapq.heappush(minHeap, (num+1, curr_size+1))
            elif minHeap[0][0] < num:
                return False



        return len(minHeap) == 0