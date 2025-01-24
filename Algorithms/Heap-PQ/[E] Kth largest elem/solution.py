class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pqueue = []
        for num in nums:
            heappush(pqueue, num *- 1)
        result = -1
        for i in range(k):
            result = heappop(pqueue)
        return result * -1