def twoNumberSum(array, targetSum):
    # Write your code here.

# Here we are iterating through each value inside a list and checking if the (targetSum - value at i) exists in the dictionary or not(By checking if the value at dicti[i] is True or not), 
# If it does not exist then we mark it as True(saying that we have already seen this number before). 
	dicti = {}
	for i in array:
		diff = targetSum - i
		if diff in dicti.keys():
			return [i,diff]
		dicti[i]=True
	return []