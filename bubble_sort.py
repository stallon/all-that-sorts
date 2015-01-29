__author__ = '홍성봉'


def bubble_sort(arr):
    length = len(arr)
    swapped = False

    for end in range(length-1, -1, -1):

        for idx in range(end):
            if arr[idx] > arr[idx+1]:
                swap(arr, idx, idx + 1)
                swapped = True

        if not swapped:
            break


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

    bubble_sort(arr)

    print('Sorted array is : ')
    print(arr)


if __name__ == '__main__':
    main()