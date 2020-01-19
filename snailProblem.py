# 题目描述，蜗牛往下爬杆子，第一天爬一半加3米，第二天爬一半加3米，第n天爬一半加（n-1 天多爬的 + n-2 天多爬的）米
# 如果蜗牛 第n 天落地， 求杆子最大长度, 即求第一天还没爬的时候杆子剩余的长度 


class Solution:
    def maxPole(self, day: int) -> int:
        self.day = day
        self.extraDict = [3, 3]
        return self.poleLeft(1)

    def poleLeft(self, day):
        if day == self.day+1:
            return 0
        next_day = 2 * (self.extra(day) + self.poleLeft(day + 1))
        print(day, next_day)
        return next_day

    def extra(self, day):
        print('extra', day)
        if day < 3:
            return self.extraDict[day - 1]
        else:
            self.extraDict = [self.extraDict[1], sum(self.extraDict)]
            return self.extraDict[1]


if __name__ == "__main__":
    day = 3
    l = Solution().maxPole(day)
    print(l)