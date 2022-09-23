def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    ans,value,negative = 0,0,0
    for index in range(1,len(distances)):
        value = (value+(fuel[index-1]*mpg)) - distances[index-1]
        if negative > value:
            negative = value
            ans = index
        # print(value,fuel[index],distances[index])
            
    return ans
    