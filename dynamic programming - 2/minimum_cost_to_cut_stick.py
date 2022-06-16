import re


def minimum_cost_to_cut_stick(cuts,n):
    cuts.sort()
    dp = [[-1 for i in range(len(cuts)+1)] for j in range(len(cuts)+1)]
    a = [0] + cuts + [n]
    def helper(i,j,a,dp):
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        mini = float("inf")
        for k in range(i,j+1):
            cost = a[j+1] - a[i-1] + helper(i,k-1,a,dp) + helper(k+1,j,a,dp)
            mini = min(mini,cost)
        
        dp[i][j] = mini
        
        return mini
    
    res = helper(1,len(cuts),a,dp)
    return res



cuts = list(map(int,input("enter the cuts point ").strip().split()))
n = int(input("enter the length of rod "))           
v = minimum_cost_to_cut_stick(cuts,n)
print(v)            