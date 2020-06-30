def maxProfit(prices):
    buy = 0
    profit = 0
    if len(prices) <= 1: return 0
    for i in range(len(prices)):
        if i == 0:
            #ignore previous
            if prices[i+1] > prices[i]:
                buy += prices[i]
        elif i == len(prices)-1:
            #ignore next
            if prices[i-1] < prices[i]:
                profit += (prices[i] - buy)
                buy = 0
        else:
            #ignore nothing
            if(prices[i] < prices[i-1] and prices[i] < prices[i+1]):
                buy += prices[i]
            if(prices[i] > prices[i-1] and prices[i] >= prices[i+1]):
                profit += (prices[i] - buy)
                buy = 0
        #print(f"Stock rate {prices[i]}. Bought {buy}. profit {profit}")
    return profit

#prices = [7,6,4,3,1]
#prices = [1,2,3,4,5]
prices = [5,2,3,2,6,6,2,9,1,0,7,4,5,0]
print(maxProfit(prices))