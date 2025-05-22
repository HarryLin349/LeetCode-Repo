from heapq import heappush, heappop, heapify
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # problem:  find the most freq elems
        # naive approach: dict of elems 
        # then sort by seen and return first k

        '''
        idea: tuples of (num, occurence)
        heapify and then return the top k
        '''
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        lst = []
        res = []
        for key, val in seen.items():
            lst.append((-val,key))
        heapify(lst)
        for i in range(k):
            res.append(heappop(lst)[1])
        return res
