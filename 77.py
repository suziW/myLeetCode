from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        r = []
        def backtrack(combination, n, k):
            if k == 0:
                r.append(combination[:])
                return
            for i in range(k, n+1):
                combination.append(i)
                backtrack(combination, i-1, k-1)
                combination.pop()
        backtrack([], n, k)
        return r

if __name__ == "__main__":
    n = 4
    k = 2
    r = Solution().combine(n, k)
    print(r)