def bubble_sort(array):

    for i in range(len(array)-1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

array = [14, 143, 53, 37, 453]
print(bubble_sort(array))
