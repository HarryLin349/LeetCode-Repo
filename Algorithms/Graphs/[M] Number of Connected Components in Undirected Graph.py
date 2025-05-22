class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # idea:
        # DFS with prev, if cycle stop
        # each DFS will explore one connected component 
        # keep track of if a node is visited // completed 
        # count # times as we need to DFS

        edgemap = {i:[] for i in range(n)}
        for a,b in edges:
            edgemap[a].append(b)
            edgemap[b].append(a)
        
        # explores the node
        visited = set()
        completed = set()

        def dfs(node, prev):
            if node in visited: # we've hit a cycle, stop exploring
                return
            visited.add(node)
            for neighbor in edgemap[node]:
                if neighbor == prev:
                    continue
                dfs(neighbor, node)
            return

        count = 0
        for i in range(n):
            if i in visited:
                continue
            else:
                dfs(i, -1)
                count += 1
        return count
