def taskAssignment(k, tasks):
    dicti = get_indices(tasks)
          
    tasks.sort()
    start,end = 0,len(tasks)-1
    ans = []
    
    while start < end:
        ans.append([dicti[tasks[start]][-1],dicti[tasks[end]][-1]])
        dicti[tasks[start]].pop()
        dicti[tasks[end]].pop()
        start += 1
        end -= 1
    return ans

def get_indices(tasks):
    dicti = {}
    for i,j in enumerate(tasks):
      if j not in dicti:
        dicti[j] = [i]
      else:
        dicti[j].append(i)
    return dicti
