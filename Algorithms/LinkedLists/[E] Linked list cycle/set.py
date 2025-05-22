# Definition for singly-linked list.
# class listNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[listNode]) -> bool:
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                return True
            visited.add(cur)
            cur = cur.next
        
        return False