def caesarCipherEncryptor(string, key):
	alpha =list("abcdefghijklmnopqrstuvwxyz")
	
	ans = ""
	for i in string:
		print(alpha.index(i))
		new_alpha = (alpha.index(i)+key)%26
		ans += alpha[new_alpha]
	return ans
		