from typing import List
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        import heapq
        dp = [float('inf') for _ in range(n+1)]
        dp[1] = 1
        s = [1 for _ in range(len(primes))]
        candidates = [(dp[s[j]] * primes[j], j) for j in range(len(primes))]
        heapq.heapify(candidates)
        for i in range(2, n+1):
            dp[i], index = heapq.heappop(candidates)
            while True:
                s[index] += 1
                heapq.heappush(candidates, (dp[s[index]] * primes[index], index))
                if candidates[0][0] == dp[i]:
                    _, index = heapq.heappop(candidates)
                else:
                    break
        return dp[n]

if __name__ == "__main__":
    primes = [2,7,13,19]
    n = 12
    r = Solution().nthSuperUglyNumber(n, primes)
    print(r)
