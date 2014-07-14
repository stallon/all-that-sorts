__author__ = 'Stallon'


def selection_sort(arr, ascend = True):

    outindex = -1
    innerindex = 0
    cp = 1 if ascend else -1

    for outer_elem in arr:
        outindex += 1
        innerindex = outindex + 1

        for inner_elem in arr[innerindex:]:

            if outer_elem*cp > inner_elem*cp :
                swap(arr, outindex, innerindex)
                outer_elem = inner_elem

            innerindex += 1


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

    ascend = True if input('Choose Ascend (0) or Descend(1) : ') == '0' else False
    selection_sort(arr, ascend)

    print('Sorted array is : ')
    print(arr)


if __name__ == '__main__':
    main()
