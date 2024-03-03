from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        def partition(l, r, p):
            nums[r], nums[p] = nums[p], nums[r]
            index = l
            for i in range(l, r):
                if nums[i] < nums[r]:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1
            nums[index], nums[r] = nums[r], nums[index]
            return index

        def ksmall(l, r, k):
            print(l, r, k, nums)
            if l == r:
                print(l, r, k)
                return nums[l]
            p = random.randint(l, r)
            print('p select', p)
            p = partition(l, r, p)
            print('p after', p)
            if p == k - 1:
                return nums[p]
            elif p < k - 1:
                return ksmall(p+1, r, k)
            else:
                return ksmall(l, p-1, k)

        return ksmall(0, len(nums)-1, len(nums)+1-k)
        

if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6]
    nums= [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14][::-1]
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    r = Solution().findKthLargest(nums, k)
    print(r)