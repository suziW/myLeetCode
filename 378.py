from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import heapq
        h = [(matrix[i][0], i, 0) for i in range(min(len(matrix), k))]
        heapq.heapify(h)
        print(h)
        
        count = 0
        r = 0
        while count < k:
            count += 1
            r, i, j = heapq.heappop(h)
            if j < len(matrix) - 1:
                heapq.heappush(h, (matrix[i][j+1], i, j+1))
        return r

if __name__ == "__main__":
    matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]]
    k = 8
    r = Solution().kthSmallest(matrix, k)
    print(r)