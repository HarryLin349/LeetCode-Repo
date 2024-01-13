class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        print (points)
        distances = [(x[0]** 2 + x[1] ** 2, x[0], x[1]) for x in points]
        answer = []
        heapq.heapify(distances)
        answer = [[x[1], x[2]] for x in heapq.nsmallest(k,distances)]
        return answer