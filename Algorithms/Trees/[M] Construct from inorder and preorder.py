# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    '''
    idea: first in preorder gives us the root
    from that num, bisect inorder to get immediate children
    if children arent already seen, we construct the tree, then set it as the L/R child of the cur
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        # print(preorder, inorder)
        root = preorder[0]
        splitidx = inorder.index(root)
        leftTree = self.buildTree(preorder[1:splitidx+1], inorder[:splitidx])
        rightTree = self.buildTree(preorder[splitidx+1:], inorder[splitidx+1:])

        return TreeNode(root, leftTree, rightTree)
        left = preorder[:splitidx]
        right = preorder[splitidx+1:]