def isPalindrome(string):
	left_index = 0
	right_index = len(string)-1
	
	while left_index < right_index:
		if string[left_index] != string [right_index]:
			return False
		left_index +=1
		right_index -= 1
	return True