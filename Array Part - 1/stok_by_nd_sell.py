def buy_and_sell(prices):
    if not prices:
        return 0
    
    ans = 0
    mini = prices[0]
    
    for i in range(1,len(prices)) :
        if prices[i] < mini:
            mini = prices[i]
        else:
            ans = max(ans, prices[i]-mini)
    
    return ans 

l = int(input("enter number of stocks "))
prices = []
for i in range(l):
    v = int(input("enter prices on each day  "))
    prices.append(v)

print(prices)
print(buy_and_sell(prices))


 