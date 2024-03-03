from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        r = []

        def backtrack(combination=[], start=0, target=0):
            if target == 0: r.append(combination[:])
            for i in range(start, len(candidates)):
                target_next = target-candidates[i]
                if target_next < 0:
                    break
                combination.append(candidates[i])
                backtrack(combination, i, target_next)
                combination.pop()
        backtrack([], 0, target)
        print(r)
        return r


if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    r = Solution().combinationSum(candidates, target)
    print(r)