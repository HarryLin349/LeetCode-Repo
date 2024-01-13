# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        p1 = p.val
        q1 = q.val
        if p1 < root.val and q1 < root.val:
            return self.lowestCommonAncestor(root.left, p,q)
        elif p1 > root.val and q1 > root.val:
            return  self.lowestCommonAncestor(root.right, p,q)
        else:
            return root