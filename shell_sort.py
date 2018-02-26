def shell_sort(arr):
    n = len(arr)

    gap = n//2

    while gap > 0:
        for i in range(gap, n):
            j = i
            while j > 0:
                if arr[j-gap] > arr[j]:
                    arr[j-gap], arr[j] = arr[j], arr[j-gap]
                    j -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    arr = [123, 312, 12, 3, 122, 313, 2, 21313, 00, 566, 435, 23]
    shell_sort(arr)
    print(arr)