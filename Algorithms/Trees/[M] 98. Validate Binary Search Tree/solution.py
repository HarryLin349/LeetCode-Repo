# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    prev = None
    def isValidBST(self, root: Optional[TreeNode]) -> bool:       
        if not root: return True
        left = self.isValidBST(root.left)
        curr = root.val > self.prev if self.prev != None else True
        self.prev = root.val
        right = self.isValidBST(root.right)
        if not left or not curr or not right:
            return False
        return True
 