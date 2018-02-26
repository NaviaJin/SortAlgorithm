def bubble_sort(arr):

    n = len(arr)

    for i in range(0, n):
        for j in range(0, n-i-1):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

if __name__ == '__main__':
    arr = [123, 312, 12, 3, 122, 313, 2, 21313, 00, 566, 435, 23]
    bubble_sort(arr)
    print(arr)


