def twoNumberSum(array, targetSum):
    # Write your code here.

    # Here we are going through each value inside a list and checking if the (targsetSum - value at position i) exists in the list or not, Also we are checking if the index is different from the index that we are on to avoid adding the same number itself.
    answer = []
    for i,j in enumerate(array):
        required = targetSum - j
        if required in array and array.index(required) != i:
            return [j,required]
    if len(answer)==0:
        return []