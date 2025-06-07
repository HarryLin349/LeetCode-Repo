from collections import deque 
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        idea:
        dfs from source
        explore all neighbors, then return
        '''
        visited = set()
        def dfs(i):
            print(f"visited room {i}")
            visited.add(i)
            for room in rooms[i]:
                if room not in visited:
                    dfs(room)
        
        dfs(0)
        return len(visited) == len(rooms)

'''
Reflection
DFS speed 100 mem 48
DFS pretty straight forward!
'''