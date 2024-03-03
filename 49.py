from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        p = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        r = defaultdict(list)
        for s in strs:
            k = 1
            for c in s:
                k *= p[ord(c) - ord('a')]
            r[k].append(s)
        return r.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    r = Solution().groupAnagrams(strs)
    print(r)