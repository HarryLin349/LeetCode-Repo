class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # intuition -> make a dict of K,V -> int, int (number, count)
        # when we see a num we increment its count
        # we then sort that dict by values and return the first k keys
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        sortedCounts = sorted(counts, key=counts.get, reverse=True)
        return sortedCounts[:k]