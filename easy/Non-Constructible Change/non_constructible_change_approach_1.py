def nonConstructibleChange(coins):
    coins.sort()
    min_sum = 0
    for coin in coins:
        if coin > min_sum+1:
            return min_sum+1
        min_sum += coin
    return min_sum+1