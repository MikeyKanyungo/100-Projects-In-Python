list = [20, 1, -11, 15, 0, -20, 2, -3, 3, 17, -15, -13, -19, 4, 5, -7]

def selectionSort(self):
    for index in range(size):
        minimum_index = index
        for j in range (index + 1, size):
            if list[j] < list[minimum_index]:
                minimum_index = j
        (list[index], list[minimum_index]) = (list[minimum_index], list[index])

size = len(list)
selectionSort(list)
print("The sorted list after selectionSort is, ", list)