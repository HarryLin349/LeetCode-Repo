# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # intuitively:
        # iterate once: make a max array that tracks max from right
        # iterate once: if val < maxArr[pos] delete it
        rightmax = []
        cur = head
        while (cur):
            rightmax.append(cur.val)
            cur = cur.next
        curMax = rightmax[-1]
        for ind in reversed(range(len(rightmax))):
            temp = rightmax[ind]
            if curMax < rightmax[ind]:
                curMax = rightmax[ind]
            else:
                rightmax[ind] = curMax
        prev = head
        cur = head
        pos = 0
        while (cur):
            if (cur.val < rightmax[pos]):
                # delete current node
                if (cur == head):
                    head = cur.next
                else:
                    prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
            pos += 1
        return head