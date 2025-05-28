from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        counts = defaultdict(int)
        seen = set()
        for num in arr:
            counts[num] += 1
        for num, count in counts.items():
            if count in seen:
                return False
            seen.add(count)
        return True