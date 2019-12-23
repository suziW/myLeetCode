class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        pal = True
        for i in range(len(x)//2):
            print(i, x[i], x[-i-1])
            if x[i] != x[-i-1]:
                pal = False
        return pal

if __name__ == "__main__":
    x = 1001
    r = Solution().isPalindrome(x)
    print(r)