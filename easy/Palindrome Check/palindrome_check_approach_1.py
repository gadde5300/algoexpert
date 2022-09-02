def isPalindrome(string):
    # Write your code here.
    for i in range(len(string)//2):
        if string[i] == string[len(string)-1-i]:
            pass
        else:
            return False
    return True
