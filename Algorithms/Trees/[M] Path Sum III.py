# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        '''
        idea:
        top down? track the current path sum
            left path is left, node.val
            right path is right, node.val
        and then if == target sum, add it?

        issue is paths arent necessarily from root or to base
        maybe memoize the cost from root for each node
        and then check each combination of node - node?
        seems kind of goofy but..

        # even better, have an array of parent sums and iterate over all of those ..

        '''
        res = 0
        def findSum(node, csum, psums):
            nonlocal res
            if not node:
                return csum
            # print(f"node {node.val} csum {csum} psums {psums}")
            csum += node.val
            for psum in psums:
                if csum - psum == targetSum:
                    # print(f"    at node {node.val} with csum {csum} found match with psum {psum}: {csum - psum}")
                    res += 1
            psums += [csum]
            leftSum = findSum(node.left, csum, psums.copy())
            rightSum = findSum(node.right, csum, psums.copy())
            return csum
        findSum(root, 0, [0])
        return res


        '''
        Reflection
        I did better than I thought!! Thought I couldn't solve this one but did pretty well
        Speed 39% Mem 8%
        The Memoization solution is really smart. Basically, for each path sum, track the # of ways to get that sum

        then when we're at node n with csum k, and we need k - p for target (can be negative), we add cache[p] to the results if it exists

        Then we remove this entry of cache[k] after popping out to above this node, since it no longer can apply to any other paths
        holay!
        '''