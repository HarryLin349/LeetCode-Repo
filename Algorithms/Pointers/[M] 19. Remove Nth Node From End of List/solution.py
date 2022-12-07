# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next
        print ("len-n-1, len-n",nodes[len(nodes) - n - 1].val, nodes[len(nodes) - n].val)
        if (n == len(nodes)):
            head = head.next
        else:
            nodes[len(nodes) - n - 1].next = nodes[len(nodes) - n].next
        return head
