def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    if fastest:
        redShirtSpeeds.sort(), blueShirtSpeeds.sort(reverse=True)
        answer = 0
        for i in range(len(redShirtSpeeds)):
            answer += max(redShirtSpeeds[i],blueShirtSpeeds[i])
        return answer
    else:
        redShirtSpeeds.sort(), blueShirtSpeeds.sort()
        answer = 0
        for i in range(len(redShirtSpeeds)):
            answer += max(redShirtSpeeds[i],blueShirtSpeeds[i])
        return answer


# Sample
# 5,5,3,9,2
# 3,6,7,2,1

# Fastest           
# 2,3,5,5,9
# 7,6,3,2,1
# 7 6 5 5 9

# Slowest
# 2,3,5,9,9
# 1,2,3,6,7
# 2 3 5 9 9