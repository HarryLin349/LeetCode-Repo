# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        c1 = list1
        c2 = list2
        while (c1 or c2):
            if not c1:
                cur.next = c2
                return head.next
            elif not c2:
                cur.next = c1
                return head.next
            else:
                if c1.val < c2.val:
                    cur.next = c1
                    c1 = c1.next
                else:
                    cur.next = c2
                    c2 = c2.next
            cur = cur.next
        return head.next