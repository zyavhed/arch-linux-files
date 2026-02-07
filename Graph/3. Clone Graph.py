"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.map = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        new_node = Node(node.val)
        self.map[node.val] = new_node

        for neighbor in node.neighbors:
            if neighbor.val not in self.map:
                neighbor_node = self.cloneGraph(neighbor)
            new_node.neighbors.append(self.map[neighbor.val])
        return new_node