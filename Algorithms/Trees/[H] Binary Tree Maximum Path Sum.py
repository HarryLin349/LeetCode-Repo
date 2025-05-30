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
        leftSum = defaultdict(int)
        rightSum = defaultdict(int)
        bothSum = defaultdict(int)

        # returns the max possible val of node and descendants
        def getSum(node):
            if node is None:
                return 0
            leftSum[node] = getSum(node.left) + node.val
            rightSum[node] = getSum(node.right) + node.val
            bothSum[node] = leftSum[node] + rightSum[node] - node.val
            return max(node.val, leftSum[node], rightSum[node],0)
        
        getSum(root)
        maxres = -10 ** 5
        return max(max(leftSum.values()), max(rightSum.values()), max(bothSum.values()))

'''
7+11+4+5+8+13

5's left: 27 right: 21 both: 48
8's left: 21 right: both: 
'''