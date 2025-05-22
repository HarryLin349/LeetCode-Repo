class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        # idea: check if we have cycles with DFS

        visited = set()
        completed = set()
        nodes = set()

        edgemap = {i:[] for i in range(n)}
        for a, b in edges:
            nodes.add(a)
            nodes.add(b)
            edgemap[a].append(b)
            edgemap[b].append(a)
        
        # returns true if this node's path has no cycles
        def dfs(node, parent):
            if node in completed:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            # visit all neighbots
            for neighbor in edgemap[node]:
                if neighbor == parent:
                    continue # skip parents
                if not dfs(neighbor, node):
                    return False
            
            visited.remove(node)
            completed.add(node)
            return True
        
        if len(edges) == 0:
            return True
        if not dfs(edges[0][0], None):
            return False

        return nodes == completed