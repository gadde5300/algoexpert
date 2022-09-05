def caesarCipherEncryptor(string, key):
    # Write your code here.
    ans= ''
    key = key%26
    for i in string:
        v1 = ord(i)+key
        if v1>122:
            value = v1%122
            # print(value)
            ans += chr(96+value)
        else:
            ans += chr(v1)
    return ans
            
