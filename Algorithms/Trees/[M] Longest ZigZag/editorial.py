# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        '''
        ideas
        we want to try every node 
        and keep track of the longest seen

        maxZigZag(node, dir) -> longest path at or below node, going at dir
        '''

        self.maxres = 0
        def maxZigZag(node, curPath, dir):
            if node is None:
                return
            self.maxres = max(self.maxres, curPath)
            if dir == "l":
                # option 1, go to left 
                maxZigZag(node.left, curPath + 1, "r")
                # option 2, start new route at the right child
                maxZigZag(node.right, 1, "l")
            else:
                # option 1, go to right 
                maxZigZag(node.right, curPath + 1, "l")
                # option 2, start new route at the left child
                maxZigZag(node.left, 1, "r")
        
        maxZigZag(root, 0, "l")
        maxZigZag(root, 0, "r")

        return self.maxres

        '''
        post reflection
        naive way wasn't too far off from editorial
        we check both ways of l/r
        main difference is we do the "either travel or dont" step 
        by either travelling (allowed) or ignoring and travelling to the other child (which is the start of a new path len 1)
        '''