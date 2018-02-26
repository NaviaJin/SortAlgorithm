def select_sort(arr):
    n = len(arr)


    for i in range(0,n):
        min = i
        for j in range(i+1,n):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

if __name__ == '__main__':
    arr = [123, 312, 12, 3, 122, 313, 2, 21313, 00, 566, 435, 23]
    select_sort(arr)
    print(arr)