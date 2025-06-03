# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        Idea
        we want the # of nodes with no parent > it
        how can we track this?
        cant modify the TreeNode class itself 
        maybe just pass a param, parent, that specifies the maximal sum so far
        and if the cur node is > it, we can increment res
        '''
        res = 0

        def countGoodNodes(node, parent):
            res = 0
            if node is None:
                return 0
            if node.val >= parent:
                # print(f"node {node.val} is a good node!")
                res += 1
            # else:
            #     print(f"node {node.val} is not a good node, parent {parent} is greater")

            
            newparent = max(parent, node.val)
            res += countGoodNodes(node.left, newparent)
            res += countGoodNodes(node.right, newparent)
            return res
        
        return countGoodNodes(root, root.val)
        '''
        reflection:
        nice! building confidence with tree problems
        and recursion in general 
        Basic idea here is we're traveling down the tree
        and just tracking every node >= the cur max
        and we can just return that as res += 1 per which is really nice
        since we just have to worry about the current node result + its subtree results
        '''