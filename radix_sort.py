def radix_sort(arr1, d):
    li = []
    for i in range(d):
        s = [[] for o in range(10)]
        temp = []
        for j in arr1:
            s[int((j/(10**i))%10)].append(j)

        # list = [n for m in s for n in m ]

        count = 0
        while count < 10:
            for m in s[count]:
                temp.append(m)
            count += 1
        arr1 = temp

        if i == d-1:
            li = temp

    return li
    # s = [[] for i in range(10)]
    # s[3].append(333)
    # s[7].append(567)
    # s[7].append(37)
    # list = [n for m in s for n in m]
    # return list
    # s = [[] for o in range(10)]
    # temp = []
    # for j in arr:
    #     s[int((j / (1)) % 10)].append(j)
    #
    # # list = [n for m in s for n in m ]
    # i = 0
    # while i < 10:
    #     for m in s[i]:
    #         temp.append(m)
    #     i += 1
    # return temp

if __name__ == '__main__':
    arr = [123, 312, 12, 3, 122, 313, 2, 00, 566, 435, 23]
    arr = radix_sort(arr, 3)

    print(arr)

    # for i in range(3):
    #     print(i)

