# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # intuitively: we can keep a set of seen nodes
        # if node in seen return true
        # else return false
        seen = set()
        cNode = head
        while (cNode):
            if (cNode is None):
                return False
            if cNode in seen:
                return True
            seen.add(cNode)
            cNode = cNode.next

        # constant memory -> 