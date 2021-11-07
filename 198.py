import numpy as np
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        r, nr = 0, 0  # rob previous and norob previous
        for n in nums:
            r, nr = max(r, nr + n), max(r, nr)
        return max(r, nr)


if __name__ == "__main__":
    l = [1]
    r = Solution().rob(l)
    print(r)
