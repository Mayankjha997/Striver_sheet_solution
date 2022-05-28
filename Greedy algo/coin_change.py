def coin_change(coins,amount):
    dp = [amount+1] * (amount+1)
    dp[0] = 0
    for i in range(1,amount+1):
        for c in coins:
            if i-c >= 0:
                dp[i] = min(dp[i], 1+dp[i-c])   
    return dp[amount] if dp[amount] != amount+1 else -1
                
                
                
test_cases = int(input())
amount = int(input("enter the amount "))
for i in range(test_cases):
    coins = list(map(int,input("enter the coins ").strip().split())) 
print(coins)     
v = coin_change(coins,amount)
print(v)