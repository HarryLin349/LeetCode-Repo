class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # problem:  find the most freq elems
        # naive approach: dict of elems 
        # then sort by seen and return first k

        # idea: dict of elems and freq
        # then have n buckets for freq  
        # and pop from the highest down until k elems popped
        seen = {}
        n = len(nums)
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        buckets = [[] for _ in range(n)]

        # populate buckets
        for key, value in seen.items():
            buckets[value - 1].append(key)

        # get top k
        res = []
        remaining = k
        for i in reversed(range(n)):
            while len(buckets[i]) > 0 and k > 0:
                res.append(buckets[i].pop())
                k -= 1
        return res