from collections import defaultdict
from heapq import heappush, heappop, heapreplace

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        ideas
        greedy: take the valid task with the most remaining count
        use a maxheap to track tasks by their remaining counts
        track time last executed
        how do we skip tasks that have been executed in last N?
        have a queue/buffer of N tasks, at each pop
        '''
        time = 1
        taskCounts = defaultdict(int)
        taskTimes = defaultdict(int)
        pq = []

        for task in tasks:
            taskCounts[task] += 1
        for task, count in taskCounts.items():
            heappush(pq, (-count, task))
        
        while pq:
            # print("time:", time, pq)
            popped = []
            task, count = 0,0
            added = False
            while True and pq:
                count,task = heappop(pq)
                if taskTimes[task] == 0 or time - taskTimes[task] > n:
                    taskTimes[task] = time
                    # print(f"task taken: {task} {-count}")
                    added = True
                    break
                # print(f"{task}{-count} done within {n}, skipping")
                popped.append((count, task))
            for c in popped:
                heappush(pq, c)
            popped = []
            if count + 1 < 0 and added:
                heappush(pq,((count + 1), task))
            time += 1
        return time - 1