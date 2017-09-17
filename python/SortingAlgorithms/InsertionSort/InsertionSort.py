# Insertion Sort
# O(n^2) for worst and average case

def insertion_sort(array):

    # for(int i = 1; i < array.length; i++)
    for i in range(1, len(array)):

        # at each instance take one element except the one at 0th position
        currentElement = array[i]
        pos = i

        # print(currentElement)
        # print(array)

        # logic to move larger elements to the right side
        # and smaller elements to the left side wrt current element's position
        while pos > 0 and array[pos-1] > currentElement:
            array[pos] = array[pos-1]
            pos -= 1
        array[pos] = currentElement
        
    return array

array = [2, 33, 12, 89, 1, 30]
print(insertion_sort(array))