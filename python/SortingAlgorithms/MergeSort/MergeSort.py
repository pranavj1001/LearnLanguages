def merge_sort(array):

    if len(array) > 1:

        mid = int(len(array)/2)
        leftHalf = array[:mid]
        rightHalf = array[mid:]

        print("<>",leftHalf)
        print("<>",rightHalf)

        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i = 0
        j = 0
        k = 0

        print(leftHalf)
        print(rightHalf)

        while i < len(leftHalf) and j < len(rightHalf):

            if leftHalf[i] < rightHalf[j]:
                array[k] = leftHalf[i]
                i += 1
            else:
                array[k] = rightHalf[j]
                j += 1

            k += 1

        while i < len(leftHalf):
            array[k] = leftHalf[i]
            i += 1
            k += 1

        while j < len(rightHalf):
            array[k] = rightHalf[j]
            j += 1
            k += 1

    print("Merged", array)

    return array

array = [12, 56, 1, 90, 23, 15, 19, 1000, 3]
print(merge_sort(array))