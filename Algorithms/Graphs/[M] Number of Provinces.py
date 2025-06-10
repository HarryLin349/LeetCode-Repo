from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        ideas
        return total number of provinces
        note we have n cities from 0 .. n-1 
        
        keep a track of visited nodes
        on each traversal remove the edge?

        every time we call dfs on an unvisited node for the first time, we should 
        increment res, unless it leads to a node we already completed

        want: # of times we call dfs on a node 
        if we have visited, return 1
        else return 0
        '''
        visited = set()
        completed = set()

        nodeMap = defaultdict(list)
        n=len(isConnected)
        for i in range(n):
            for j in range(n):
                if i != j and isConnected[i][j] == 1:
                    nodeMap[i].append(j)
        print(nodeMap)
        
        def dfs(i):
            visited.add(i)
            for n in nodeMap[i]:
                if n not in visited:
                    dfs(n)

        res = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1
        
        return res
'''
Reflection:

Important that in an undirected graph, dfs WILL explore everything connected to a path
good to know. goes both ways.
time 38 mem 36
'''