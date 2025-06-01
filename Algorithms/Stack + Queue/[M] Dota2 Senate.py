from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        '''
        idea: load up 2 queues, rad and deque, based on index
        while both are empty, choose the lower one. pop the opposing and shove the cur to the back
        '''
        rq = deque()
        dq = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                rq.append(i)
            else:
                dq.append(i)
        while rq and dq:
            if dq[0] < rq[0]:
                # pop rq, move dq to the back
                dq.append(dq[0] + len(senate))
            else:
                rq.append(rq[0] + len(senate))
            dq.popleft()
            rq.popleft()

        return "Radiant" if rq else "Dire"