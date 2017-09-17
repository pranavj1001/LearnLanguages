# Bubble Sort
# O(n^2) for worst and average case
# a lot of swapping takes place here

def bubble_sort(array):

    # for(int i = array.length - 1; i <= 0; i--)
    for i in range(len(array)-1, 0, -1):
        # for(int j = 0; j < i; j++)
        for j in range(i):
            # swap whenever a larger element is found
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

array = [14, 143, 53, 37, 453]
print(bubble_sort(array))
