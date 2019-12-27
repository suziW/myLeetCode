from typing import List
class Solution:
    def grayCode(self, n: int) -> List[int]:
        r = [0]
        for i in range(1, n+1):
            r += [n + 2**(i-1) for n in r[::-1]]
            print(r)
        return r


if __name__ == "__main__":
    n = 3
    r = Solution().grayCode(n)
    print(r)