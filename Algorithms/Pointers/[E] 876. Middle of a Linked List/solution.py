class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        while fast:
            fast = fast.next
            if fast is None:
                return slow
            fast = fast.next
            slow = slow.next
        return slow
