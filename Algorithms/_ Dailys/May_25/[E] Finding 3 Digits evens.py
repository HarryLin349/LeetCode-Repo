from collections import defaultdict
class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        '''
        - 3 digit integer, combination of elems in digits
        - no leading zeroes
        - integer is even
        idea: iterate over each and check manually (lol..)
        '''
        res = []
        seen = []
        counts = defaultdict(int)
        for digit in digits:
            counts[digit] += 1
        for i in range(100, 1000, 2):
            n1, n2, n3 = i // 100, (i // 10) % 10, i % 10
            # seen.append((n1,n2,n3))
            counts[n1] -= 1
            counts[n2] -= 1
            counts[n3] -= 1
            if counts[n1] >=0 and counts[n2] >= 0 and counts[n3] >= 0:
                res.append(i)
            counts[n1] += 1
            counts[n2] += 1
            counts[n3] += 1
        return res


        # n = len(digits)
        # res = set()
        # for i in range(n):
        #     for j in range(n):
        #         for k in range(n):
        #             if i == j or i == k or j == k:
        #                 continue
        #             n1, n2, n3 = digits[i], digits[j], digits[k]
        #             if n1 != 0 and n3 % 2 == 0:
        #                 res.add(n1*100 + n2 *10 + n3)
        # return sorted(list(res))
