from re import T


def isMonotonic(array):
    # Write your code here.
    # OR table says that if both of the values are False then it is False or else it is True.
    #  T  T  T
    #  T  F  T
    #  F  T  T
    #  F  F  F

    
    is_increasing = True
    is_decreasing = True

    if len(array) <= 2:
        return True
    for i in range(1,len(array)):
        if array[i]>array[i-1]:
            is_decreasing = False
        elif array[i]<array[i-1]:
            is_increasing = False
            
            
    return is_decreasing or is_increasing