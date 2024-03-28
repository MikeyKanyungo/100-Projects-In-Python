seq = [20, 1, -11, 15, 0, -20, 2, -3, 3, 17, -15, -13, -19, 4, 5, -7]

def quickSort(seq):
    length = len(seq)
    if length <= 1:
        return seq
    else:
        pivot = seq.pop()
    
    greater = []
    lower = []

    for i in seq:
        if i > pivot:
            greater.append(i)
        else:
            lower.append(i)
    return quickSort(lower) + [pivot] + quickSort(greater)

print(quickSort(seq))