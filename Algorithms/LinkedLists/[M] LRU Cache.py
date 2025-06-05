from collections import deque 

class LRUCache:
    '''
    ideas: 
    O(1) get and put
    so we probably need hashing / dict for access

    to put (evict) we should probably also maintain a queue 
    but how do we remove and readd?
    maybe our dict has (key, val, time)
    and our queue is (key, time)
    if any queue elem time doesnt match the key time, we pop

    '''

    def __init__(self, capacity: int):
        self.queue = deque()
        self.dict = {}
        self.time = 0
        self.capacity = capacity

    def get(self, key: int) -> int:
        res = 0
        if key in self.dict:
            res = self.dict[key][0]
            self.dict[key] = (res, self.time)
            self.queue.append((key, self.time))
        else:
            res = -1
        
        return res

    def put(self, key: int, value: int) -> None:
        self.time += 1
        self.dict[key] = (value, self.time) # updated, dict possible has +1 elem
        self.queue.append((key,self.time))
        while len(self.dict) > self.capacity and self.queue:
            key, oldtime = self.queue.popleft()
            if key not in self.dict:
                continue
            curtime = self.dict[key][1]
            if oldtime == curtime:
                del self.dict[key]
'''
Reflection
Okay, fire. Didn't think I could do it, but I could
Had a clear approach, debug statements were powerful. Good to run through cases. 
Stopping conditions should always mirror given contraints (e.g. look at len of dict and not len of queue, we dont care how long the queue is)
Time 61 Mem 6
'''

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)