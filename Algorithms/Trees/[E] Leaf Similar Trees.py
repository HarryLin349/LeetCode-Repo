# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        idea: we know something is a leaf if it has no children (left and right are None)
        maybe we can just O(n) space and traverse through each treenode?
        Each function returns an array of the leaf values
        '''
        def getLeaves(node):
            if node is None:
                return []
            elif node.left is None and node.right is None:
                return [node.val]
            else:
                res = []
                res += getLeaves(node.left)
                res += getLeaves(node.right)
                return res
        
        left = getLeaves(root1)
        right = getLeaves(root2)
        return left == right
        '''
        Post reflection
        Happy I decided to return and build arr instead of explicit adding, seems cleaner
        100% runtime and 94% mem! thats crazy good
        Solution aligns with my strategy
        Visit in consistent order and store returns in memory, then compare
        '''