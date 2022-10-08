def minimumCharactersForWords(words):
    dicti = {}
    if len(words) == 0:
        return[]
    for i in words[0]:
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1

    for j in range(1,len(words)):
        dicti_1 ={}
        for k in words[j]:
            if k in dicti_1:
                dicti_1[k] += 1
            else:
                dicti_1[k] = 1

        for l,m in dicti_1.items():
            if l in dicti:
                if dicti[l] < m:
                    dicti[l] = m
            else:
                dicti[l]=m
    ans = []
    for n,o in dicti.items():
        while o != 0:
            ans.append(n)
            o-=1
       
    return ans