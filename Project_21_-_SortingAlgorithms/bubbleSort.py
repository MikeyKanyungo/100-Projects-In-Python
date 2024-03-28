def bubbleSort(self):
    for n in range(len(list)-1, 0, -1):
        swapped = False
        for i in range(n):
            if list[i] > list[i + 1]:
                swapped = True
                list[i], list[i + 1] = list[i + 1], list[i]
                if not swapped:
                    return 

list = [10,1,4,7,8,2,6,3,5,9]
print("Unsorted list is, ", list)
bubbleSort(list)
print("Sorted list is, ", list)