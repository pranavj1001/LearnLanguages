def selection_slot(array):

    for i in range(len(array)-1, 0, -1):
        maxPosition = 0
        for j in range(1, i+1):
            if array[j] > array[maxPosition]:
                maxPosition = j

        array[i], array[maxPosition] = array[maxPosition], array[i]

    return array

array = [23, 1, 90, 12, 56]
print(selection_slot(array))