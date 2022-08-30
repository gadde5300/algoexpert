def productSum(array,multiplier=1):
    sum1 = 0
    for i in array:
        if type(i) is list:
            sum1 += productSum(i,multiplier + 1)
        else:
            sum1 += i
    return sum1*multiplier