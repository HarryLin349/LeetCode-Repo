class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        idea -->
        maintain a stack of the asteroids res
        for each new asteroid:
            if res and res[-1] > 0 and asteroid < 0:
                while (res and res[-1] > 0):
                    if res[-1] < -asteroid:
                        res.pop()
                    elif res[-1] > -asteroid:
                        break
                    else:
                        res.pop()
                        break
            else:
                res.append(asteroid)
        return res
        '''
        res = []
        for asteroid in asteroids:
            if res and res[-1] > 0 and asteroid < 0:
                broken = False
                while (res and res[-1] > 0):
                    if res[-1] < -asteroid:
                        # print(f"broke {res[-1]}")
                        res.pop()
                    elif res[-1] > -asteroid:
                        # print(f"broke by {res[-1]}")
                        broken = True
                        break
                    else:
                        # print(f"mutual {res[-1]}")
                        res.pop()
                        broken = True
                        break
                if not broken:
                    # print(f"added {asteroid}")
                    res.append(asteroid)
            else:
                # print(f"no collision {asteroid}")
                res.append(asteroid)
        return res