from typing import List

class DNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Solution:
    @staticmethod
    def removeNode(node: DNode):
        """Remove a node from doubly linked list in O(1)."""
        if not node:
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        # Build doubly linked list with dummy head
        head = DNode(-1)
        tail = head
        for val in hand:
            node = DNode(val)
            tail.next = node
            node.prev = tail
            tail = node

        # Process each group
        for _ in range(len(hand) // groupSize):
            if not head.next:
                return False

            # Start of the current group
            group_start = head.next
            prev_val = group_start.val
            self.removeNode(group_start)  # remove first node

            curr = head.next
            for _ in range(1, groupSize):
                # Find next consecutive node
                while curr and curr.val == prev_val:
                    curr = curr.next
                if not curr or curr.val - prev_val != 1:
                    return False
                prev_val = curr.val
                next_node = curr.next
                self.removeNode(curr)
                curr = next_node
        return True
