def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
    sth = 0
	ans = 0
	for i in range(1,len(queries)):
		sth += queries[i-1]
		ans = ans + sth

	return ans
