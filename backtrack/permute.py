from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        r = []
        def backtrack(l: List, traced_index: List):
            if len(traced_index) == len(nums):
                r.append(l[:])
                return

            for i, n in enumerate(nums):
                if i in traced_index:
                    continue
                l.append(n)
                traced_index.append(i)
                backtrack(l, traced_index)
                traced_index.pop()
                l.pop()

        backtrack([], [])
        return r


if __name__ == "__main__":
    nums = [1, 2, 3]
    r = Solution().permute(nums)
    print(r)
