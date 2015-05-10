__author__ = 'stallon'

import math


def swap(arr, i, j):

    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

    print('swapping ... ' + str(arr))


def compare_and_change_with_children(arr, start, end, index):

    left_child_index = start + 2 * index + 1
    right_child_index = start + 2 * index + 2
    index += start

    # index node is a leaf
    if left_child_index >= end:
        return

    # index node has only one child in the left leaf
    if right_child_index == end:
        if arr[index] < arr[left_child_index]:
            swap(arr, index, left_child_index)
        return

    # index node has two children
    next_index = left_child_index

    if arr[index] < arr[left_child_index]:
        if arr[left_child_index] < arr[right_child_index]:  # right child is the biggest one
            swap(arr, index, right_child_index)
            next_index = right_child_index
        else:
            swap(arr, index, left_child_index)
    elif arr[index] < arr[right_child_index]:
        swap(arr, index, right_child_index)
        next_index = right_child_index
    else:   # index, left/right children are balanced
        return

    # repeat above procedures till it reaches a leaf
    compare_and_change_with_children(arr, start, end, next_index - start)


def make_max_heap(arr, start, end):

#   determine start index of heap building
#     - first element of the second deepest level

    length = end - start
    depth = math.floor(math.log2(length))

    for cur_depth in range(depth - 1, -1, -1):

        start_index = 2 ** cur_depth - 1
        end_index = 2 ** (cur_depth + 1) - 1

        for index in range(start_index, end_index):
            compare_and_change_with_children(arr, start, end, index)

    print('[MAX HEAP: start = %d] %s' % (start, str(arr)))


def heap_sort(arr):

    length = len(arr)

    for i in range(0, length - 2):
        make_max_heap(arr, i, len(arr))


def main():

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    heap_sort(arr)

    print('[FINAL SORTED] ' + len(arr))


if __name__ == '__main__':
    main()

