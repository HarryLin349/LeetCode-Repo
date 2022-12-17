class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        l, r = 0,0
        if (not root1):
            return root2
        if (not root2):
            return root1
        t3 = TreeNode(root1.val + root2.val)
        t3.left = self.mergeTrees(root1.left, root2.left)
        t3.right = self.mergeTrees(root1.right, root2.right)
        return t3