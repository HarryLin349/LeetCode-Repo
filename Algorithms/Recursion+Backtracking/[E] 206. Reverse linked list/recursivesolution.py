# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    newHead = None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        self.helper(head)
        return self.newHead
    def helper (self, head: Optional[ListNode]):
        if head.next is None:
            self.newHead = head
            return head
        else:
            next = self.helper(head.next)
            next.next = head
            head.next = None
            return head