# '''
#     当前节点为k，
#     父节点为（k-1)/2
#     左子树为2k+1
#     右子树为2k+2
# '''
def adjust_heap(arr,i):
    l_child = 2*i+1
    r_child = 2*i+2
    n = len(arr)
    min = i
    if i < int(n/2):
        if l_child < n and arr[min] > arr[l_child]:
            min = l_child
        if r_child < n and arr[min] > arr[r_child]:
            min = r_child
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
            adjust_heap(arr,min)

def get_min(arr):
    n = len(arr)

    no_leaf =int(n/2)

    for i in range(0, no_leaf)[::-1]:
        adjust_heap(arr, i)

    if arr:
        min = arr[0]
        temp = arr.pop(n-1)
        if arr:
            arr[0] = temp
    # print(arr)

    return min, arr

def heap_sort(arr,result):
    min, arr = get_min(arr)
    result.append(min)
    while arr:
        heap_sort(arr,result)

if __name__ == '__main__':
    arr = [123, 312, 12, 3, 122, 313, 2, 566, 435, 23]
    result = []
    heap_sort(arr, result)


    print(result)
    # temp = arr.pop(4)
    # print(temp)
    # print(arr)


#
#
#
#list要处理的数组，i是第几个元素，size是lists的长度
# def adjust_heap(lists, i, size):
#     lchild = 2 * i + 1
#     rchild = 2 * i + 2
#     max = i
#     if i < int(size / 2):
#         if lchild < size and lists[lchild] > lists[max]:
#             max = lchild
#         if rchild < size and lists[rchild] > lists[max]:
#             max = rchild
#         if max != i:
#             lists[max], lists[i] = lists[i], lists[max]
#             adjust_heap(lists, max, size)
#
#
# def build_heap(lists, size):
#     for i in range(0, (int(size / 2)))[::-1]:
#         adjust_heap(lists, i, size)
#
#
# def heap_sort(lists):
#     size = len(lists)
#     build_heap(lists, size)
#     for i in range(0, size)[::-1]:
#         lists[0], lists[i] = lists[i], lists[0]
#         adjust_heap(lists, 0, i)
#
#