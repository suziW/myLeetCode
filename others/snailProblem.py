# 题目描述，蜗牛往下爬杆子，第一天爬一半加3米，第二天爬一半加3米，第n天爬一半加（n-1 天多爬的 + n-2 天多爬的）米
# 如果蜗牛 第n 天落地， 求杆子最大长度, 即求第一天还没爬的时候杆子剩余的长度


class Solution:
    # T(1) = [T(2) + f1] * 2
    # T(N - 1) = [T(N) + f(N - 1)] * 2
    # T(N + 1) = 0

    def poleLeftByBeginingOfDay(self, day):
        if day == (self.n + 1):
            poleleft = 0
        else:
            poleleft = (self.poleLeftByBeginingOfDay(day + 1) + self.fibonacci[day]) * 2

        print("pole left by beginning of day {} is {}".format(day, poleleft))
        return poleleft

    def maxPole(self, n: int) -> int:
        self.n = n
        self.fibonacci = [0, 3, 3]
        for i in range(3, n + 1):
            self.fibonacci.append(self.fibonacci[i - 1] + self.fibonacci[i - 2])

        return self.poleLeftByBeginingOfDay(1)


if __name__ == "__main__":
    day = 3
    l = Solution().maxPole(day)
    print(l)
