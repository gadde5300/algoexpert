def getNthFib(n):
    # Write your code here.
    if n == 1:
        return 0
    if n == 2:
        return 1
    n1 = 0
    n2 = 1
    for i in range(2,n):
        answer = n1+n2
        n1 = n2
        n2 = answer
    return answer