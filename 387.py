class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for i, c in enumerate(s):
            if not dic.get(c):
                dic[c] = [True, i]
            else:
                dic[c][0] = False
        print(dic)
        r = float('inf')
        for _, v in dic.items():
            if v[0]:
                r = min(r, v[1])
        return -1 if r == float('inf') else r

if __name__ == "__main__":
    s = 'loveleetcode'
    r = Solution().firstUniqChar(s)
    print(r)