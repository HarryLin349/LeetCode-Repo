class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # idea: since we need the answer that occurs last in the input, we 
        # should traverse edge by edge
        # each edge, we check if its reachable to each other by dfs
        # if it is, we set the edge to that answer
        # if not, we add that edge to the graph
        # the idea is that in a cycle there should be a way to reach each other even w/o that edge
        # so dumb... such an arbitrary condition
        n = len(edges)
        edgemap = {i:[] for i in range(1, n+1)}
        visited = set()
        def isreachable(u,v):
            if u in visited:
                return False
            if u == v:
                return True
            visited.add(u)
            result = False
            for neighbor in edgemap[u]:
                result = result or isreachable(neighbor, v)
            visited.remove(u)            
            return result

        edge = []        
        for ai, bi in edges:
            if isreachable(ai, bi):
                edge = [ai, bi]
            else:
                edgemap[ai].append(bi)
                edgemap[bi].append(ai)
        return edge
