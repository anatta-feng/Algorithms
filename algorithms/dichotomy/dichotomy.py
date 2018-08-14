array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def binary_search(array, item):
    low_index = 0
    heigh_index = len(array) - 1

    while low_index <= heigh_index:
        mid_index = (low_index + heigh_index) / 2
        mid_index = int(mid_index)
        guess_value = array[mid_index]
        if item == guess_value:
            return mid_index
        if item < guess_value:
            heigh_index = mid_index - 1
        else:
            low_index = mid_index + 1
    return None

result = binary_search(array, 3)
print(array[result])
