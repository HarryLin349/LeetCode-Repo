# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        '''
        ideas
        we want the maximum twin sum of the linked list
        naively, could just push all the nodes to a list
        and iterate over, taking the max of l,r where l = 0 r = n-1

        O(1) space? 
        '''
        lst = []
        cur = head
        while cur:
            lst.append(cur.val)
            cur = cur.next
        l,r = 0, len(lst) - 1

        maxsum = 0
        while l < r:
            maxsum = max(maxsum, lst[l] + lst[r])
            l += 1
            r -= 1
        return maxsum