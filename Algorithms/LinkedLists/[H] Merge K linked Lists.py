# Definition for singly-linked list.
# class listNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKlists(self, lists: list[Optional[listNode]]) -> Optional[listNode]:
        n = len(lists)
        def mergeTwolists(list1, list2):
            cur1 = list1
            cur2 = list2
            dummy = listNode()
            cur = dummy
            while cur1 and cur2:
                if cur1.val < cur2.val:
                    cur.next = cur1
                    cur1 = cur1.next
                else:
                    cur.next = cur2
                    cur2 = cur2.next
                cur = cur.next
            if cur1:
                cur.next = cur1
            else:
                cur.next = cur2
            return dummy.next
        
        for i in range(1, n):
            list1, list2 = lists[i-1], lists[i]
            newlist = mergeTwolists(list1,list2)
            lists[i] = newlist
        
        return lists[-1] if n > 0 else None