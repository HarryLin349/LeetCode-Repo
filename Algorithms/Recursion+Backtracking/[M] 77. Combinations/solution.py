from collections import deque
import copy

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(first: int, cur: List[int]):
            if (len(cur) == k):
                output.append(cur[:])
                return
            for i in range (first, n + 1):
                cur.append(i)
                backtrack(i + 1, cur)
                cur.pop()
        backtrack(1, [])
        return output
