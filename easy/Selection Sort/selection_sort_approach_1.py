def selectionSort(array):
    # Write your code here.
    for i in range(len(array)):
        minimum = i
        for j in range(i+1,len(array)):
            if array[minimum]>array[j]:
                minimum = j
        # print(minimum)
        array[i],array[minimum] = array[minimum],array[i]
    return array