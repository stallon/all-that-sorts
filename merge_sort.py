__author__ = 'stallon'

def merge_sorted_sublists(arr, start, mid, end):

    result = []

    left = start
    right = mid

    while True:
        if arr[left] < arr[right]:
            result.append(arr[left])
            left += 1
        else:
            result.append(arr[right])
            right += 1

        if left == mid:
            result.extend(arr[right:])
            break
        elif right == end + 1:
            result.extend(arr[left:mid])
            break

    for idx in range(start, end + 1):
        arr[idx] = result[idx - start]



def merge_sort(arr, start, end):

    if start == end:
        return

    mid_idx = int((end + start)/2)
    merge_sort(arr, start, mid_idx)
    merge_sort(arr, mid_idx + 1, end)

    merge_sorted_sublists(arr, start, mid_idx + 1, end)


def main():

    arr_str = input('integer array values : ').split()
    arr = [int(x) for x in arr_str]

    merge_sort(arr, 0, len(arr)-1)
    print('sorted ==> ', arr)


if __name__ == '__main__':
    main()
