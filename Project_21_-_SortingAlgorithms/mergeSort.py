def mergeSort(list):
    if len (list) > 1:
        mid = len(list)//2
        L = list[:mid]
        R = list[mid:]

        mergeSort(L)
        mergeSort(R)
        i =j = k = 0


        while i < len (L) and j < len (R):
            if L[i] <= R[j]:
                list[k] = L[i]
                i += 1
            else: 
                list[k] = R[i]
                i += 1
                k += 1
            while j < len(R):
                list[k] = R[j]
                j += 1
                k += 1
def printList(list):
    for i in range (len(list)):
        print(list[i], end=" ")
    print()

if __name__ == '__main__':
    list = [10,1,4,7,8,2,6,3,5,9]
    print ("Given list is, ", list)
    mergeSort(list)
    print("\nSorted list is ", list)