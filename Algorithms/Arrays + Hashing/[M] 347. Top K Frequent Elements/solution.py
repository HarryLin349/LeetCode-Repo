class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        sorted_count = sorted(count.items(), key = lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(sorted_count[i][0])
        return result