# Definition for singly-linked list.
# class listNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[listNode]) -> bool:
        nodes = []
        curr = head
        while (curr):
            nodes.append(curr)
            if (curr.next in nodes):
                return True
            curr = curr.next
        return False