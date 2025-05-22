from collections import defaultdict
from heapq import heapify, heappush, heappop
class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        '''
        ideas:
        return the k most freq of string
        go through and add to a dict
        then add each entry to a maxheap ordered by count, word
        '''
        freqs = defaultdict(int)
        for word in words:
            freqs[word] += 1

        res = list(freqs.items())
        res.sort(key=lambda x: (-x[1], x[0]))
        final = [x[0] for x in res]
        return final[:k]

        # maxheap = []
        # for word, count in freqs.items():
        #     heappush(maxheap, (-count,word))
        # res = []

        # for i in range(k):
        #     res.append(heappop(maxheap))

        return res
