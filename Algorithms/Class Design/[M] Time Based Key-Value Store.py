import heapq 

class TimeMap:
    # more insertions or accesses?
    # more insertions --> array per key
    # more accesses --> pqueue per key, logn set and 
    
    # idea: map is a map of key:string -> val: pqueue

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            # insert into 
            heapq.heappush(self.map[key], (timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.map:
            return ""
        for i in reversed(range(len(self.map[key]))):
            if self.map[key][i][0] <= timestamp:
                return self.map[key][i][1]
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)