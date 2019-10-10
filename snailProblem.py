# 题目描述，蜗牛往下爬杆子，第一天爬一半加3米，第二天爬一半加3米，第n天爬一半加（n-1 天多爬的 + n-2 天多爬的）米
# 如果蜗牛 第n 天落地， 求杆子最大长度


class Solution:
    def maxPole(self, day: int) -> int:
        self.day = day
        self.extraDict = [3, 3]
        return self.poleLeft(0)

    def poleLeft(self, day):
        if day == self.day:
            return 0

        return 2 * (self.poleLeft(day + 1) + self.extra(day))

    def extra(self, day):
        if day < 3:
            return self.extraDict[day - 1]
        else:
            self.extraDict = [self.extraDict[1], sum(self.extraDict)]
            return self.extraDict[1]


if __name__ == "__main__":
    day = 31
    l = Solution().maxPole(day)
    print(l)