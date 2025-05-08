# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        '''
        idea: comparison node by node would be very expensive
        ok.. try it anyway?
        '''
        def isSame(n1, n2):
            if n1 == None or n2 == None:
                return n1 == None and n2 == None
            return n1.val == n2.val and isSame(n1.left, n2.left) and isSame(n1.right, n2.right)
        
        def dfs(node):
            res = False
            if node and node.val == subRoot.val:
                res = res or isSame(node, subRoot)
            if node != None:
                res = res or dfs(node.left) or dfs(node.right)
            return res
        return dfs(root)