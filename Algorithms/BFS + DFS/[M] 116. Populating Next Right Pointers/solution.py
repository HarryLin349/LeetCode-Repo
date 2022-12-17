"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None: 
            return
        queue = [root]
        nextInd = 0
        curInd = 0
        curAdd = 2
        while len(queue) > 0:
            cur = queue.pop(0)
            if (curInd == nextInd):
                cur.next = None
                nextInd += curAdd
                curAdd *= 2
            else:
                cur.next = queue[0]
            if (cur.left):
                queue.append(cur.left)
            if (cur.right):
                queue.append(cur.right)
            curInd += 1
        return root


