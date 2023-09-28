# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sameTree(self, p, q):
        if not p or not q:
            if not p and not q:
                return True
            else:
                return False
        if p.val != q.val:
            return False
        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root:
            return False
        result = False
        if root.val == subRoot.val:
            result = self.sameTree(root, subRoot)
        return result or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)