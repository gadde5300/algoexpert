def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    redShirtHeights.sort()
    blueShirtHeights.sort()

    if blueShirtHeights[0]>=redShirtHeights[0]:
        for i in range(len(blueShirtHeights)):
            if blueShirtHeights[i]<=redShirtHeights[i]:
                return False
    else:
        for i in range(len(blueShirtHeights)):
            if blueShirtHeights[i]>=redShirtHeights[i]:
                return False
    # print(redShirtHeights,'\n',blueShirtHeights)
    return True