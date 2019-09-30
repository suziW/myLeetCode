class SolutionMine:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subString = {}
        longestInfo = [0, 0, 0]
        for i, c in enumerate(s):
            print('================================================================', i, c, longestInfo)
            if i==0: 
                subString[c] = i
                longestInfo[0] = 1
                longestInfo[1] = i
                longestInfo[2] = subString
            elif c in subString:
                repeatPosition = subString[c]
                if len(subString) > longestInfo[0]:
                    longestInfo[0] = len(subString)
                    longestInfo[1] = repeatPosition
                    longestInfo[2] = subString
                subString = {}
                for j in range(repeatPosition + 1, i + 1):
                    print(s[j], j)
                    subString[s[j]] = j
            elif i == len(s) -1:
                subString[c] = i
                if len(subString) > longestInfo[0]:
                    longestInfo[0] = len(subString)
                    longestInfo[1] = subString[c]
                    longestInfo[2] = subString
            else:
                subString[c] = i

            print(subString)
        return longestInfo[0]

# 别人的答案很强。不用舍弃掉重复的字符串前面部分，直接对起始指针i取max(st[s[j]], i)
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            print('============================', j, s[j])
            if s[j] in st:
                print(st, i)
                i = max(st[s[j]], i)
            ans = max(ans, j - i +1)
            st[s[j]] = j + 1
        return ans



if __name__ == "__main__":
    s = "jbpnbdlaishjfoiwqjejeswgfjetfoihjewjrfoiewhjewqewojjewojqjaewrfjiewjfoiwwd"
    r = Solution().lengthOfLongestSubstring(s)
    print(r)