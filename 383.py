import re
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        p = re.findall('[' + ransomNote + ']', magazine)
        print(p)
        dic = {}
        for c in ransomNote:
            if not dic.get(c):
                dic[c] = 1
            else:
                dic[c] += 1
        for c in magazine:
            if dic.get(c):
                dic[c] -= 1
        for _, val in dic.items():
            if val > 0:
                return False
        return True


if __name__ == "__main__":
    ransomNote = 'dollar'
    magazine = 'do it and ill let you go ight now'
    r = Solution().canConstruct(ransomNote,magazine)
    print(r)