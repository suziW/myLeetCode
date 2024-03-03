import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]

if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    r = Solution().isPalindrome(s)
    print(r)