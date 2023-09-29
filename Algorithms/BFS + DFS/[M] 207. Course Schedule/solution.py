class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for course in prerequisites:
            first = course[0]
            second = course[1]
            adj[second].append(first)
            indegree[first] += 1
        print (adj)
        nodesVisited = 0
        queue = []

        for i in range(len(adj)):
            if indegree[i] == 0:
                queue.append(i)
        
        while queue:
            curNode = queue.pop(0)
            nodesVisited += 1
            for neighbor in adj[curNode]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return nodesVisited == numCourses

