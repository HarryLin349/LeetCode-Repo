# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''

        fn: returns the subtree with the specified node deleted
        idea
        to delete a node,

        if node is none, return none

        if key < root.val:
            node.left = deleteNode(node.left, val)
        elif key > root.val
            ...
        else:
            # this is the key
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            cur = root.right
            while cur:
                cur = root.left
            
            root.val = cur.val

            root.right = deleteNode(root.val)


        replace it with its successor (if it exists)

        '''
        if not root:
            return None
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            cur = root.right
            while cur.left:
                cur = cur.left
            
            root.val = cur.val
            root.right = self.deleteNode(root.right, cur.val)
        
        return root

'''
reflection
Im so sleepy man
but yea fire
100 speed 6 mem
needed neetcode
binart search trees are prob not asked much
'''