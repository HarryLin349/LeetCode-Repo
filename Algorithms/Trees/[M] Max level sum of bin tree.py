# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        idea: visit level by level
        at the end of each level update minlvl and maxsum
        '''
        minlvl, maxsum = 1, root.val
        curlvl, csum = 1,0
        q = deque([root])
        nextq = deque()
        while q:
            cur = q.popleft()
            csum += cur.val
            if cur.left:
                nextq.append(cur.left)
            if cur.right:
                nextq.append(cur.right)
            if not q:
                if csum > maxsum:
                    minlvl = curlvl
                    maxsum = csum
                q = nextq
                nextq = deque()
                curlvl += 1
                csum = 0
        return minlvl

'''
Reflection

speed 92 mem 15

Pretty straightforward, small hiccup with understanding the csum requirement
wondering if my strat is the right way to write it
'''