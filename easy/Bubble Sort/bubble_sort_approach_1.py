def bubbleSort(array):
    for i in range(len(array)):
        for j in range(1,len(array)-i):
            if array[j-1]>array[j]:
                swap(j-1,j,array)
    return array

def swap(i,j,array):
    array[i],array[j] = array[j],array[i]
    return array