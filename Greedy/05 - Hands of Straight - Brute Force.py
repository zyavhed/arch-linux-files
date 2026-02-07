import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        def get_minimum(hand_counts):
            return min(hand_counts.keys())

        def decreament_count(hand_counts, number):
            hand_counts[number] -= 1
            if hand_counts[number] == 0:
                del hand_counts[number]


        hand_counts = Counter(hand)
        while hand_counts:
            mini = get_minimum(hand_counts)
            decreament_count(hand_counts, mini)
            for i in range(1,groupSize):
                if mini + i in hand_counts:
                    decreament_count(hand_counts, mini + i)
                else:
                    return False
        return True