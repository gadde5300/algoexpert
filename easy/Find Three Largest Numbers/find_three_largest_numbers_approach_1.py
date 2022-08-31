def findThreeLargestNumbers(array):
    # Write your code here.
    first,second,third = array[0],float('-inf'),float('-inf')
    for i in range(1,len(array)):
        if array[i] > first:
            third = second
            second = first
            first = array[i]
        elif second<array[i]:
            third = second
            second = array[i]
        elif third<array[i]:
            third = array[i]
    return [third,second,first]
