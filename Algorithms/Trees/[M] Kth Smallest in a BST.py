# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # idea:
        # kth smallest will just be the kth elemnt in preorder traversal, right?
        # preorder traverse, and have a running count
        # if count = k, return
        remaining = k
        answer = -1
        def traverse(root):
            nonlocal remaining
            nonlocal answer 
            if not root:
                return
            traverse(root.left)
            remaining -= 1
            if remaining == 0:
                answer = root.val
                return
            traverse(root.right)
        
        traverse(root)
        return answer