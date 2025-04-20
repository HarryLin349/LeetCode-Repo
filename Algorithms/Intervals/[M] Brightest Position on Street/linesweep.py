class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        '''
        ideas:
        each lights[i] covers an interval
        count the area with most overlapping intervals
        start -> increase brightness by 1
        end -> decrease brightness by 1 (after that num)
        '''
        changes = []
        for pos, r in lights:
            changes.append((pos - r, 1))
            changes.append((pos + r, -1))
        changes.sort(key = lambda x: (x[0], -x[1]))
        print(changes)

        cur = 0
        curmax = 0
        pos = 0
        for change, delta in changes:
            cur += delta
            if cur > curmax:
                # print(f"new max {cur} at {change}")
                curmax = cur
                pos = change
        return pos
