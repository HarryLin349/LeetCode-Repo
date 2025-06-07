from collections import deque 
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        idea:
        bfs from the source (room 0)
        visit all the rooms in order (queue)
        when we're in a room, we add it to a visited set
        '''
        visited = set()
        queue = deque([0])
        while queue:
            room = queue.popleft()
            visited.add(room)
            if len(visited) == len(rooms):
                return True
            keys = rooms[room]
            for key in keys:
                if key not in visited:
                    queue.append(key)
        return False
'''
Reflection: BFS, speed 26 mem 74. Pretty fast.
DFS? challenge
'''