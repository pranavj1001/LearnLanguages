# method to search for an element using binary search
def binary_search(array, element):

    first = 0
    last = len(array) - 1

    found = False

    while first <= last and not found:

        mid = int((first + last) / 2)

        if array[mid] == element:
            found = True
        else:

            # consider the first half of the array
            if element < array[mid]:
                last = mid - 1

            # consider the second half of the array
            else:
                first = mid + 1

    return found

array = [11, 23, 45, 55, 67, 88, 99]
print(binary_search(array, 67))