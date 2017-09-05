def insertion_sort(array):

    for i in range(1, len(array)):

        currentElement = array[i]
        pos = i

        while pos > 0 and array[pos-1] > currentElement:
            array[pos] = array[pos-1]
            pos -= 1

        array[pos] = currentElement
        
    return array

array = [2, 33, 12, 89, 1, 30]
print(insertion_sort(array))