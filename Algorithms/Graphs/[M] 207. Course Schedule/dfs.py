class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        # we can see these as an adjacency list of a graph
        # pre[i]: ai <- bi
        # when can we not take all courses?
        # cycles 
        # idea: DFS, if we encounter a cycle return false
        # how do we track cycles? visited for each traversal

        # build adjacency list (dict) to traverse
        # adj[i]: course ai and its requirements
        reqs = { i: [] for i in range(numCourses)}
        for ai, bi in prerequisites:
            reqs[ai].append(bi)
        
        visited = set()
        # now we can try DFS

        # returns true if a course is completable
        def dfs(course):
            if (course in visited):
                # we've detected a cycle
                return False
            elif len(reqs[course]) == 0:
                # no reqs, so this is completable
                return True
            
            visited.add(course)
            for nxt in reqs[course]:
                if not dfs(nxt):
                    return False
                # otherwise, we can say the next course is completable
                reqs[nxt] = []
            
            visited.remove(course)
            reqs[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
