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
        seen = {} # key is (key, dir) val is maxpath

        def zigZag(node, dir):
            if node is None:
                return -1
            if (node, dir) in seen:
                return seen[(node,dir)]

            if dir == "left":
                res = 1 + zigZag(node.left, "right")
            else:
                res = 1 + zigZag(node.right, "left")
            seen[(node, dir)] = res
            return res

        # explores the tree DFS style and gets the max zigzag length for each node
        # returns the max zigzag for that node 
        maxres = 0
        def dfs(node):
            nonlocal maxres
            if node is None:
                return 0
            # try each direction for the cur node
            r1 = zigZag(node, "left")
            r2 = zigZag(node, "right")
            maxres = max(maxres, r1, r2)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return maxres

            
'''
5% Speed 5% Memory
'''
