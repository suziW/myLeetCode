from typing import List
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq as hq
        for i in range(len(stones)): stones[i] = -stones[i]
        hq.heapify(stones)
        while len(stones) > 1:
            print(stones)
            h1, h2 = -hq.heappop(stones), -hq.heappop(stones)
            print(h1, h2)
            if h1 != h2:
                hq.heappush(stones ,-abs(h1 - h2))
        print(stones)
        return -stones[0]

if __name__ == "__main__":
    stones = [2,7,4,1,8,1]
    r = Solution().lastStoneWeight(stones)
    print(r)