"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:       
        if not node:
            return None
        if node in self.visited:
            return self.visited[node]
        
        cloneNode = Node(node.val)
        self.visited[node] = cloneNode

        for neighbor in node.neighbors:
            cloneNode.neighbors.append(self.cloneGraph(neighbor))        
        return cloneNode

