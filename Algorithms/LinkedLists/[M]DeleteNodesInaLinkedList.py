# Definition for singly-linked list.
# class listNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        # problem: how to get the prev node to point to the next node?
        # through traversal we can only go forward
        # idea: we shift all the values over
        # then delete the last node
        # while cur:
        # cur.val = cur.next.val
        cur = node
        while (cur and cur.next):
            cur.val = cur.next.val
            if (cur.next.next is None):
                cur.next = None
            cur = cur.next

        """
        :type node: listNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        