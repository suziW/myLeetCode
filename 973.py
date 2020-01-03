from typing import List
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        import heapq
        h = [(float('-inf'), [0, 0]) for _ in range(K)]
        for p in points:
            d = p[0]**2 + p[1]**2
            if d < -h[0][0]:
                heapq.heappushpop(h, (-d, p))
        return [i[1] for i in h]

if __name__ == "__main__":
    points = [[3,3],[5,-1],[-2,4]]
    K = 2
    r = Solution().kClosest(points, K)
    print(r)