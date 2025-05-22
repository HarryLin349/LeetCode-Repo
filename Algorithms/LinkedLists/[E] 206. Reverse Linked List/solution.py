class Solution:
    def reverselist(self, head: Optional[listNode]) -> Optional[listNode]:
        cur = head
        prev = None
        nxt  = None
        while (cur):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev