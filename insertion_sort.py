__author__ = 'NHNEnt'


def insertion_sort(arr, n):
    """ for the first elements,
    if arr[0] > arr[1]:
        temp = arr[1]
        arr[1] = arr[0]
        arr[0] = temp

    # for the remaining elements
    for i in range(1, len(arr)):
        insert_into_sorted_sublist(arr, i)
    """

    if n == 2 and arr[0] > arr[1]:
        temp = arr[1]
        arr[1] = arr[0]
        arr[0] = temp
    elif n <= 1:
        pass
    else:
        insertion_sort(arr, n-1)
        insert_into_sorted_sublist(arr, n)




def insert_into_sorted_sublist(arr, index):

    temp = arr[index]
    j = index - 1

    while j >= 0 and arr[j] > temp:
        arr[j+1] = arr[j]
        j -= 1

    arr[j+1] = temp

"""
def swap(arr, index1, index2):
    temp = arr[index1]
    arr[index1] = arr[index2]
    arr[index2] = temp
"""

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
