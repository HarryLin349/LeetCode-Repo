# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        idea:
        we want the LCA of two nodes
        simple idea: have fn "hasNode" -> returns if subtree contains p or q
        node is a CA if it hasNode for p and for q
        can return a tuple (b, b) for p, q
        we want the lowest common ancestor, so we can probably just take minimal depth
        '''
        lowest = None
        lowestDepth = 0

        def hasPQ(node, depth):
            nonlocal lowestDepth
            nonlocal lowest
            if node is None:
                return False
            l,r,mid = False, False, False
            if node is p or node is q:
                mid = True
            l = hasPQ(node.left, depth + 1)
            r = hasPQ(node.right, depth + 1)
            if l+r+mid >= 2 and depth >= lowestDepth:
                lowest = node
                lowestDepth = depth
            return l or r or mid
        hasPQ(root, 0)
        return lowest

'''
Reflection: 
Pretty straightforward approach, ended up working
    Wonder if the tuple return is the best.. maybe we can just return bool?
    But then how do we handle if left has p and right has q?
    could return 0,1,2,3.. seems even more hacky
    good idea: we only need to see if either contains. 
    Remember if we get 2 signals, we must have seen p and q
    if we only get 1, we can do better (traverse down)
Speed 68 Mem 5
'''