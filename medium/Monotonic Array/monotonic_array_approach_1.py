def isMonotonic(array):
    # Write your code here.
    if len(array)<=2:
        return True
        
    if array[-1]>array[0]:
        for i in range(1,len(array)):
            if array[i] < array[i-1]:
                return False
    else: 
        for i in range(1,len(array)):
            if array[i] > array[i-1]:
                return False
    return True