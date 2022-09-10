def threeNumberSum(array, targetSum):
    array.sort()
    answer = []
    for i in range(len(array)):
        left,right = i+1,len(array)-1
        while left<right:
            if (array[i]+array[left]+array[right])>targetSum:
                right -= 1
            elif (array[i]+array[left]+array[right])<targetSum:
                left += 1
            elif (array[i]+array[left]+array[right])==targetSum:
                answer.append([array[i],array[left],array[right]])
                left += 1
                right -= 1
    return answer