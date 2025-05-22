class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # idea: use dfs and a topological ordering
        # have an array "taken"
        # base case: if we encounter a course with no reqs, we append to order list and return true
        # recursive case:
        # explore all neighbors
        # if false, return false
        
        order = []
        visited = set()
        completed = set()
        courseMap = { i:[] for i in range(numCourses)}

        for ai, bi in prerequisites:
            courseMap[ai].append(bi)
        
        def dfs(course):
            if (course in visited):
                return False
            if (course in completed):
                return True

            visited.add(course)

            # check all neighbors, if any false, return False
            for req in courseMap[course]:
                if not dfs(req):
                    return False
            visited.remove(course)
            completed.add(course)
            order.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return order