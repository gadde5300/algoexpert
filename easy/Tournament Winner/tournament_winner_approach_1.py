def tournamentWinner(competitions, results):
    # Write your code here.
	dicti = {}
    
	for i in range(len(competitions)):
		if results[i]==1:
			if competitions[i][0] in dicti:
				dicti[competitions[i][0]] += 1
			else:
				dicti[competitions[i][0]] = 1
		else:
			if competitions[i][1] in dicti:
				dicti[competitions[i][1]] += 1
			else:
				dicti[competitions[i][1]] = 1
				
	max_key = max(dicti, key=dicti.get)				
	return max_key
				
    
