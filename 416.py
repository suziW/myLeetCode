from typing import List
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        halfsum = sum(nums) >> 1
        if sum(nums) != halfsum << 1: return False
        print(halfsum)

        dp = set((0,))
        for n in nums:
            if n > halfsum: return False
            for s in list(dp):
                if n + s < halfsum: dp.add(n+s)
                elif n + s == halfsum: return True
            # print('============================ n:', n)
            # print(dp)
        return False

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        halfsum = sum(nums) >> 1
        if sum(nums) != halfsum << 1: return False
        print(halfsum)

        dp = [False for _ in range(halfsum+1)]
        dp[0] = True

        for n in nums:
            for s in range(halfsum, 0, -1):
                if s-n >= 0:
                    dp[s] = dp[s-n] or dp[s]
                else:
                    break
            if dp[-1]: break
        return dp[-1]     

if __name__ == "__main__":
    import time
    start = time.time()
    nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
    r = Solution().canPartition(nums)
    print(r)
    print(time.time() - start)