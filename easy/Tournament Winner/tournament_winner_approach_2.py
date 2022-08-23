def tournamentWinner(competitions, results):
	dicti = {}
    pts = 0
    winner = "#"
	for i in range(len(competitions)):
		if results[i]==1:
			if competitions[i][0] in dicti:
				dicti[competitions[i][0]] += 1
			else:
				dicti[competitions[i][0]] = 1
            if pts < dicti[competitions[i][0]]:
                pts = dicti[competitions[i][0]]
                winner = competitions[i][0]
		else:
			if competitions[i][1] in dicti:
				dicti[competitions[i][1]] += 1
			else:
				dicti[competitions[i][1]] = 1
            if pts < dicti[competitions[i][1]]:
                pts = dicti[competitions[i][1]]
                winner = competitions[i][1]					
	return winner
				
    
