def quick_sort(arr, start, end):

    if start >= end:
        return
    low = start
    high = end
    mid = arr[low]

    while low < high:
        while low < high and arr[high] > mid:
            high -= 1
        arr[low] = arr[high]

        while low < high and arr[low] < mid:
            low += 1
        arr[high] = arr[low]

    arr[low] = mid

    quick_sort(arr, start, low-1)
    quick_sort(arr, low+1, end)


if __name__ == '__main__':
    arr = [123, 312, 12, 3, 122, 313, 2, 21313, 00, 566, 435, 23]
    quick_sort(arr, 0, len(arr)-1 )
    print(arr)