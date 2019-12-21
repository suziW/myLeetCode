def triangles():
    j = 1
    while j >= 0:
        if j == 1:
            L = [1]
            j = 2
        else:
            L2 = []
            L.insert(0, 0)  #给L两头插入0
            L.append(0)
            for i in range(len(L) - 1):  #循环生成L2
                L2.append(L[i] + L[i + 1])
            # print('L2：', L2)
            L = L2
        # print('L: ', L, L[:])
        yield L  #为什么最后一行写成 yield L结果就不对呢？


if __name__ == "__main__":
    n = 0
    results = []
    for t in triangles():
        print('t:', t)
        results.append(t)
        print('results:', results)
        n = n + 1
        if n == 10:
            break
    print('-------------------------------------')
    for t in results:
        print('t1:', t)