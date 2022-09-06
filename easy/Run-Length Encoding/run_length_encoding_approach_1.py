def runLengthEncoding(string):
    temp_arr = []
    count = 1

    for i in range(1,len(string)):
        if string[i]!=string[i-1] or count == 9:
            temp_arr.append(str(count))
            temp_arr.append(string[i-1])
            count = 0
        count += 1
    #For the last value
    temp_arr.append(str(count))
    temp_arr.append(string[-1])
    return "".join(temp_arr)