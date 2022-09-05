def generateDocument(characters, document):
    dicti ={}
    for i in characters:
        if i not in dicti:
            dicti[i] = 1
        else:
            dicti[i] += 1
    # print(dicti)
    for j in document:
        # print(j,'y')
        if j not in dicti or dicti[j]==0:
            return False
        elif j in dicti:
            dicti[j] -= 1

    
    return True
    
