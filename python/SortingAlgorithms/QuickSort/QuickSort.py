def quick_sort(array):

    quick_sort_help(array, 0, len(array) - 1)

    return array

def quick_sort_help(array, first, last):

    if first < last:
        splitPoint = partition(array, first, last)

        quick_sort_help(array, first, splitPoint-1)
        quick_sort_help(array, splitPoint+1, last)

    return array

def partition(array, first, last):

    pivotValue = array[first]

    leftMark = first+1
    rightMark = last

    done = False

    while not done:

        while leftMark <= rightMark and array[leftMark] <= pivotValue:
            leftMark += 1

        while rightMark >= leftMark and array[rightMark] >= pivotValue:
            rightMark -= 1

        if rightMark < leftMark:
            done = True

        else:
            array[leftMark], array[rightMark] = array[rightMark], array[leftMark]

    array[first], array[rightMark] = array[rightMark], array[first]

    return rightMark

array = [23, 1, 90, 11, 9, 999, 12]
print(quick_sort(array))