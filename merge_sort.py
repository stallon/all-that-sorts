__author__ = 'stallon'

def merge_sorted_sublists(arr, start, mid, end):

    result = []

    idx1 = start
    idx2 = mid

    while True:

        if idx1 < mid and idx2 < end:
            if arr[idx1] <= arr[idx2]:
                result.append(arr[idx1])
                idx1 += 1
            else:
                result.append(arr[idx2])
                idx2 += 1
        elif idx1 == mid:
            result.extend(arr[idx2:end])
            break
        else:   # idx2 == end
            result.extend(arr[idx1:mid])
            break

    return result


def split_and_merge(arr, start, end):

    if (end - start) < 2:
        return

    mid = int((start + end) / 2)
    split_and_merge(arr, start, mid)
    split_and_merge(arr, mid, end)
    arr[start:end] = merge_sorted_sublists(arr, start, mid, end)


def merge_sort(arr):
    split_and_merge(arr, 0, len(arr))


def main():

    arr_str = input('integer array values : ').split()
    arr = [int(x) for x in arr_str]

    merge_sort(arr)
    print('sorted ==> ', arr)


if __name__ == '__main__':
    main()
