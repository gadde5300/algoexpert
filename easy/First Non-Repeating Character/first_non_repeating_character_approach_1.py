def firstNonRepeatingCharacter(string):
	dicti = {}
	for i in string:
		if i in dicti:
			dicti[i] += 1
		else:
			dicti[i]=1
	# print(dicti)
	for j in range(len(string)):
		if dicti[string[j]]==1:
			return j
		else:
			continue
	return -1