# Selection Sort
# O(n^2) for worst and average case

def selection_slot(array):

    # for(int i = array.length - 1; i <= 0; i--)
    for i in range(len(array)-1, 0, -1):
        maxPosition = 0

        # for(int j = 1; j < i+1; j++)
        # logic to move the max element in the last position
        for j in range(1, i+1):
            if array[j] > array[maxPosition]:
                maxPosition = j
        array[i], array[maxPosition] = array[maxPosition], array[i]

    return array

array = [23, 1, 90, 12, 56]
print(selection_slot(array))