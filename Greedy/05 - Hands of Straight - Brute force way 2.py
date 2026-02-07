import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        n = len(hand) // groupSize
        stacks = [[] for _ in range(n)]

        for h in hand:
            for s in stacks:
                if not s or (h - s[-1] == 1 and len(s) < groupSize):
                    s.append(h)
                    break
            else:
                return False
        return True

# or this, they both mean same
# import heapq
# class Solution:
#     def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
#         if len(hand) % groupSize != 0:
#             return False
#         hand.sort()
#         n = len(hand) // groupSize
#         stacks = [[] for _ in range(n)]

#         for h in hand:
#             was_pushed = False
#             for s in stacks:
#                 if not s or (h - s[-1] == 1 and len(s) < groupSize):
#                     s.append(h)
#                     was_pushed = True
#                     break
#             if not was_pushed:
#                 return False
#         return True
