# Shell Sort
# O(n(log(n))^2) for worst and average case

def shell_sort(array):

    # length of the sublist of array
    sublistCount = int(len(array)/2)

    print(array)

    # loop till the sublist's length becomes 1
    while sublistCount > 0:
        # perform insertion sort to every sublist
        for start in range(sublistCount):
            array = gap_insertion_sort(array, start, sublistCount)

        print("After gaps of ", sublistCount)
        print(array)

        sublistCount = int(sublistCount/2)

    print("\nSorted Array")
    return array

# Logic for insertion sort
def gap_insertion_sort(array, start, gap):

    for i in range(start + gap, len(array), gap):

        currentValue = array[i]
        pos = i

        while pos >= gap and array[pos-gap] > currentValue:
            array[pos] = array[pos-gap]
            pos = pos - gap

        array[pos] = currentValue

    return array

array = [190, 2, 42, 8, 21, 11, 200, 13, 19]
print(shell_sort(array))