import collections

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speed = [x for _,x in sorted(zip(position,speed), reverse=True)]
        position = sorted(position, reverse=True)
        i = 0
        while i < len(position):
            time = (target - position[i])/speed[i]
            if i < len(position) - 1:
                if speed[i + 1] * time + position[i+1] >= speed[i] * time + position[i]:
                    del position[i+1]
                    del speed[i+1]
                    i -=1
            i += 1
        return len(position)
