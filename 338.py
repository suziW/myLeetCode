import math
from typing import List
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0 for _ in range(num+1)]
        for i in range(1, num+1):
            dp[i] = dp[i>>1] + (i & 1)
        return dp

if __name__ == "__main__":
    num = 5
    r = Solution().countBits(num)
    print(r)