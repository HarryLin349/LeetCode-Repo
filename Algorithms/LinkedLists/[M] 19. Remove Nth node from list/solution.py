# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nodes = []
        count = 0
        if not head.next: return None
        while (curr):
            nodes.append(curr)
            if len(nodes) > n + 1:
                nodes.pop(0)
            curr = curr.next
            count += 1
        if n == count: return head.next
        nodes[0].next = nodes[1].next
        return head