def binarySearch(array, target):
    # Write your code here.
    left,right = 0,len(array)-1
    

    while left <= right:
        mid = (left+right)//2
        if array[mid]<target:
            left = mid+1
        elif array[mid]>target:
            right = mid-1
        elif array[mid] == target:
            return mid
    return -1
