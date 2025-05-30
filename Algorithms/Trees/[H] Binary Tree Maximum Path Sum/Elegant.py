# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        '''
        ideas:
        we want the max path sum of a non empty path
        note that possible paths can start and end at any node

        maybe if we store the max sum of a node's descendants?
        store leftsum, rightsum (implied inclusive)
        return the max of either + self
        '''
        maxres = -10 ** 5

        # returns the max possible val of node and descendants
        def getSum(node):
            nonlocal maxres
            if node is None:
                return 0
            leftSum = getSum(node.left) + node.val
            rightSum = getSum(node.right) + node.val
            bothSum = leftSum + rightSum - node.val
            maxres = max(leftSum, rightSum, bothSum, maxres)
            return max(node.val, leftSum, rightSum,0)
        
        getSum(root)
        return maxres