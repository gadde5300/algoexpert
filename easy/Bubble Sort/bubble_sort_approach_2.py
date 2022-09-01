def bubbleSort(array):
	counter = 0
	issort=False
	while not issort:
		issort=True
		for i in range(1,len(array)-counter):
			if array[i-1]>array[i]:
                array[i-1],array[i] = array[i],array[i-1]
				issort=False
		counter += 1
	return array
			
