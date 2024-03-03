from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        r = ''
        index = 0
        count = 0
        for c in chars:
            if c == r:
                count += 1
            else:
                if count > 1:
                    count = list(str(count))
                    for num in count:
                        chars[index] = num
                        index += 1
                r = c
                count = 1
                chars[index] = r
                index += 1
        if count > 1:
            count = list(str(count))
            for num in count:
                chars[index] = num
                index += 1
        return index

if __name__ == "__main__":
    s = ["a","a","b","b","c","c","c"]
    r = Solution().compress(s)
    print(r)