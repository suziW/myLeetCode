# 你面前有一栋100层的建筑，以及两个相同的鸡蛋。如果一个鸡蛋从第 N 层或以上的楼层落下，它会碎；
# 从第 N 层以下的楼层落下，它则不会碎。这里的 N 是一个未知的固定值。
# 你的目标是找出 N，并确保你的方法在最坏情况下尝试的次数尽可能少。请问，你应该如何计划你的尝试次数？

# 满足 1 + 2 + ... + k > 100 最小的k就是第一次小球抛的高度，所以最快的情况就是k次
# k == 100 时:
# 1 + 2 + ... + 14 = 105 > 100
# 1 + 2 + ... + 13 = 91 < 100
# 所以最优解是 14