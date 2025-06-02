# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        idea:
        iterate through the list with an index
        1>2>3>4>5
        we want
        1>3>5>2>4

        so if we had
        odds = 12345
        evens = 2345
        
        odds = 1345
        evens = 245

        135
        24->None

        maybe for each elem, skip forward by 2
        odds.next = cur
        evens.next = cur.next

        cur = cur.next.next

        '''
        if not head or not head.next:
            return head
        
        odds = head
        evens = head.next
        evenshead = head.next
        cur = head.next.next
        while cur:
            odds.next = cur
            evens.next = cur.next
            odds = odds.next
            evens = evens.next
            if cur.next:
                cur = cur.next.next
            else:
                break
        odds.next = evenshead

        return head