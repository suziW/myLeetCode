from typing import List
class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        if N > 1:
            odds = self.beautifulArray(N + 1 >> 1)
            evens = self.beautifulArray(N >> 1)
            return [i * 2 - 1 for i in odds] + [i * 2 for i in evens]
        else:
            return [1]


if __name__ == "__main__":
    N = 5
    r = Solution().beautifulArray(N)
    print(r)