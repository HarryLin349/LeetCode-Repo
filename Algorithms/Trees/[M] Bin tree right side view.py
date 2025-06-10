from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        ideas:
        visit depth wise. track levels.
        Only enqueue the last nodes of the next level
        '''
        res = []
        q = deque([root])
        nextq = deque()
        while q:
            cur = q.popleft()
            if not cur:
                continue
            if cur.left:
                nextq.append(cur.left)
            if cur.right:
                nextq.append(cur.right)
            if not q:
                # last elem of the level
                res.append(cur.val)
                q = nextq
                nextq = deque()

        return res
