from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        r = []

        def backtrack(s, cur, count):
            if count == 4:
                if not s:
                    r.append(cur[:-1])
                return

            if len(s) > 0:
                backtrack(s[1:], cur + s[:1] + ".", count + 1)
            if len(s) > 1 and s[0] != "0":
                backtrack(s[2:], cur + s[:2] + ".", count + 1)
            if len(s) > 2 and int(s[:3]) < 256 and s[0] != "0":
                backtrack(s[3:], cur + s[:3] + ".", count + 1)

        backtrack(s, "", 0)
        return r


if __name__ == "__main__":
    s = "101023"
    r = Solution().restoreIpAddresses(s)
    print(r)
