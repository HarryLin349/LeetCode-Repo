# Definition for singly-linked list.
# class listNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[listNode]) -> bool:
        # constant memory:
        slow = head
        fast = head
        while (slow and fast):
            slow = slow.next
            fast = fast.next
            if (fast is None): return False
            fast = fast.next
            if (fast is None): return False
            if slow == fast: return True
