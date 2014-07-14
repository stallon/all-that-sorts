__author__ = 'NHNEnt'


def quicksort(arr, first, last):

    if first < last:
        (lower, higher) = partition(arr, first, last)
        quicksort(arr, first, lower)
        quicksort(arr, higher, last)


def partition(arr, first, last):

    pivot = get_pivot_index(arr, first, last)
    p_value = arr[pivot]

    while first <= last:
        while arr[first] < p_value:
            first += 1
        while arr[last] > p_value:
            last -= 1

        if first <= last:
            swap(arr, first, last)
            first += 1
            last -= 1

    return (last, first)


def get_pivot_index(arr, f, l):
    """
    This function returns a median among first,last, and middle elements of the array.
    It is known to give more optimized pivot value.
    """

    # in case of no median,
    if l - f <= 1:
        return f

    first = arr[f]
    last = arr[l]

    idx_mid = int((l - f) / 2)
    middle = arr[idx_mid]

    if first <= middle and middle <= last:
        return idx_mid
    elif middle <= first and first <= last:
        return f
    else:
        return l


def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp


def main():

    str = input('Type a sequence of integers: ')
    arrstr = str.split()
    arr = []

    for intstr in arrstr:
        arr.append(int(intstr))

    print('Input array is : ')
    print(arr)

    quicksort(arr, 0, len(arr)-1)
#    ascend = True if input('Choose Ascend (0) or Descend(1) : ') == '0' else False
#    selection_sort(arr, ascend)

    print('Sorted array is : ')
    print(arr)


if __name__ == '__main__':
    main()



