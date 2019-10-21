# 14
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ''
        for i, c in enumerate(strs[0]):
            print('================', i, c)
            flag = True
            for s in strs[1:]:
                if i >= len(s) or s[i] != c:
                    flag = False
                    break
            print(flag)
            if flag:
                common += c
            else:
                break
        return common


if __name__ == "__main__":
    s = ["aca", "cba"]
    r = Solution().longestCommonPrefix(s)
    print(r)