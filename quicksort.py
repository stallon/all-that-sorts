__author__ = 'NHNEnt'

def partition_easy(arr, start, end):
    # decide pivot - median of first, middle, and last element
    arr_len = end - start + 1
    mid_idx = start + int(arr_len / 2)

    first = arr[start]
    last = arr[end]
    middle = arr[mid_idx]

    pivot_idx = -1

    if first <= middle:
        if middle <= last:
            pivot_idx = mid_idx
        elif first <= last:
            pivot_idx = end
        else:
            pivot_idx = start
    elif middle >= last:
        pivot_idx = mid_idx
    elif first >= last:
        pivot_idx = end
    else:
        pivot_idx = start

    # do partition according to the pivot
    
    swap(arr, end, pivot_idx)       # move pivot to the end of the partial array for clarity
    pivot = arr[end]

    left = start
    right = end - 1

    while True:
        for elem in arr[left:right + 1]:
            if elem >= pivot:
                break
            else:
                left += 1

        for idx in range(right, left-1, -1):
            if arr[idx] < pivot:
                break
            else:
                right -= 1

        # condition for partition stop
        if left == end:
            return left
        elif right == start-1:
            swap(arr, start, end)
            return start
        elif left > right:
            swap(arr, left, end)
            return left
        else:
            swap(arr, left, right)
            left += 1
            right -= 1


def quick_sort(arr, start, end):
    #initial condition for recursive calls
    length = end - start +1
    if length <= 1:
        return
    elif length == 2:
        if arr[0] > arr[1]:
            swap(arr, 0, 1)
        return

    pivot_index = partition_easy(arr, start, end)

    quick_sort(arr, start, pivot_index -1)
    quick_sort(arr, pivot_index + 1, end)


def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def main():

    Int_squence = input('Type a sequence of integers: ')
    arrstr = Int_squence.split()
    arr = []

    for intstr in arrstr:
        arr.append(int(intstr))

    print('Input array is : ')
    print(arr)

    quick_sort(arr, 0, len(arr)-1)
#    ascend = True if input('Choose Ascend (0) or Descend(1) : ') == '0' else False
#    selection_sort(arr, ascend)

    print('Sorted array is : ')
    print(arr)


if __name__ == '__main__':
    main()



