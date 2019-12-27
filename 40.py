from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []
        candidates.sort()
        def backtrack(combination, index, target):
            if target == 0:
                r.append(combination[:])
            temp = -1
            for i in range(index, len(candidates)):
                if target - candidates[i] < 0:
                    return
                if candidates[i] == temp:
                    continue
                combination.append(candidates[i])
                backtrack(combination, i + 1, target-candidates[i])
                combination.pop()
                temp = candidates[i]
        backtrack([], 0, target)
        return r



if __name__ == "__main__":
    candidates = [2,5,2,1,2]
    target = 5
    r = Solution().combinationSum2(candidates, target)
    print(r)