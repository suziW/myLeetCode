class Solution:
    def mergeSort(self, l):
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


while True:
    try:
        l = input().split(',')
        r = Solution().mergeSort(l)
        print(l)
        l.sort(),
        print(l)
        print(','.join(r))
    except Exception as e:
        print(e)
        break
