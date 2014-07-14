__author__ = 'NHNEnt'


def insertion_sort(arr):
    print('hey this is insertion sort')


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

    insertion_sort(arr)

    print('Sorted array is : ')
    print(arr)


if __name__ == '__main__':
    main()
