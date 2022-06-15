from numpy import zeros


def ones_and_zeros(strs,m,n):          # m = 0's and n = 1's
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    
    for s in strs:
        ones = s.count('1')
        zeros = s.count('0')
        
        for i in range(n,ones-1,-1):
            for j in range(m,zeros-1,-1):
                dp[i][j] = max(dp[i][j],dp[i-ones][j-zeros] + 1)
                
    return dp[n][m]
    
    
strs = list(map(str,input("enter the inputs ").strip().split()))
m = int(input("enter the number of zeros"))
n = int(input("enter the number of ones"))
v = ones_and_zeros(strs,m,n)
print(v)