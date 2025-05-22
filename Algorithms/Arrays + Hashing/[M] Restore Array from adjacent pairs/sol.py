from collections import defaultdict
class Solution:
    def restoreArray(self, adjacentPairs: list[list[int]]) -> list[int]:
        '''
        idea: ordering matters? likely not, still a probable way to solve either way
        sorting? sort by first key and 
        note that the first and last elems should have 1 occurence, and the rest should have two
        after that, we can probably build off in any (?) order

        idea: have a dict of num -> edges
        pick the solo to be first, and then build off each neighbor by picking the next in the mapping
        '''

        edges = defaultdict(set)
        for pair in adjacentPairs:
            n1, n2 = pair[0], pair[1]
            edges[n1].add(n2)
            edges[n2].add(n1)
        res = []
        for key, val in edges.items():
            if len(val) == 1:
                res.append(key)
                nxt = val.pop()
                res.append(nxt)
                edges[nxt].remove(key)
                del edges[key]
                break
        
        while edges:
            cur = res[-1]
            if len(edges[cur]) == 0:
                break
            nxt = edges[cur].pop()
            res.append(nxt)
            edges[nxt].remove(cur)
            del edges[cur]
        return res