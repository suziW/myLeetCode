from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)-1):
            left, right = i+1, len(numbers)-1
            while left < right:
                mid = left + right >> 1
                if numbers[mid] < target - numbers[i]:
                    left = mid + 1
                else:
                    right = mid
            print(i, left, right)
            if numbers[i] + numbers[left] == target:
                return i + 1, left+1

if __name__ == "__main__":
    numbers = [5, 25, 75]
    target = 100
    r = Solution().twoSum(numbers, target)
    print(r)