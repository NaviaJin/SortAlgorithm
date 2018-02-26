def insert_sort(arr):
    n = len(arr)

    i = 1
    while i < n:
        target = arr[i]
        j = i
        while j > 0 and target < arr[j-1]:
            arr[j] = arr[j-1]
            j -= 1
        arr[j] = target
        i += 1

def insert_sort2(arr):

    n = len(arr)

    for i in range(1,n):
        j = i
        while j > 0 :
            if arr[j-1] > arr[j] :
                arr[j-1], arr[j] = arr[j], arr[j-1]
                j -= 1

            else:
                break



if __name__ == '__main__':
    arr = [123, 312, 12, 3, 122, 313, 2, 21313, 00, 566, 435, 23]
    # insert_sort(arr)
    # print(arr)
    insert_sort2(arr)
    print(arr)