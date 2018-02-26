def MergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2
    leftArr = MergeSort(arr[:mid])
    rightArr = MergeSort(arr[mid:])

    lPointer, rPointer = 0, 0
    result = []

    while lPointer < len(leftArr) and rPointer < len(rightArr):
        if leftArr[lPointer] < rightArr[rPointer]:
            result.append(leftArr[lPointer])
            lPointer += 1
        else:
            result.append(rightArr[rPointer])
            rPointer += 1

    result += leftArr[lPointer:]
    result += rightArr[rPointer:]

    return result


if __name__ == '__main__':
    arr = [123, 312, 12, 3, 122, 313, 2, 21313, 00, 566, 435, 23]
    arr = MergeSort(arr)
    print(arr)