def sequential_search_unordered_list(array, element):

    pos = 0
    found = False

    while pos < len(array) and not found:

        if array[pos] == element:
            found = True
        else:
            pos += 1

    return found

unordered_list = [1, 65, 37, 49, 52]
print(sequential_search_unordered_list(unordered_list, 6))

def sequential_search_ordered_list(array, element):

    pos = 0
    found = False
    stopped = False

    while pos < len(array) and not found and not stopped:

        if array[pos] == element:
            found = True
        else:
            if array[pos] > element:
                stopped = True
            else:
                pos += 1

    return found

ordered_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(sequential_search_ordered_list(ordered_list, 8))
