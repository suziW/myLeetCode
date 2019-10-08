import numpy as np
from typing import List


class Solution:
    def mergeSort(self, l: List[int]):
        if len(l) < 2:
            return l
        left = l[:len(l) // 2]
        right = l[len(l) // 2:]
        return self.merge(self.mergeSort(left), self.mergeSort(right))

    def merge(self, l, r):
        # print('============================')
        # print(l, r)
        temp = []
        li, ri = 0, 0
        while len(temp) < len(l) + len(r):
            if li == len(l):
                temp += r[ri:]
                break
            if ri == len(r):
                temp += l[li:]
                break
            if l[li] <= r[ri]:
                temp.append(l[li])
                li += 1
            else:
                temp.append(r[ri])
                ri += 1
        #     print(temp)
        # print(temp)
        return temp


if __name__ == "__main__":
    l = list(np.random.randint(0, 100, 20))
    # print(type(l))
    # l = [62, 9, 94, 5, 96, 55, 67, 20, 0, 4, 86, 55, 83, 71, 84, 25, 95, 68]
    print(l)
    r = Solution().mergeSort(l)
    print('result is:', r)