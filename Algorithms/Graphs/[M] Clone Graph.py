
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # idea: maintain a dict of nodes 
        # and a queue?
        # when we encounter node curNode, we check to see if its in the dict
            # if yes, we use that as the current,
            # else we run clone on it
        # we then iterate through its neighbors and do the same
        if not node:
            return None
        seenNodes = {}
        def cloneNode(node: Optional['Node']):
            if not node:
                return None
            if node.val in seenNodes.keys():
                return seenNodes[node.val]
            newNode = Node(node.val, [])
            seenNodes[node.val] = newNode
            newNeighbors = []
            for neighbor in node.neighbors:
                newNeighbor = cloneNode(neighbor)
                newNeighbors.append(newNeighbor)
            newNode.neighbors = newNeighbors
            return newNode
        cloned = cloneNode(node)
        return cloned

            