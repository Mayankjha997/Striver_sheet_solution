def minDistance(word1, word2):
    dp = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
    
    for i in range(len(word1)+1):
        for j in range(len(word2)+1):
            if i == 0:
                dp[0][j] = j
            elif j == 0:
                dp[i][0] = i
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j]) + 1
    return dp[-1][-1]

word1 = input("enter the first word ")
word2 = input("enter the second word ")
v = minDistance(word1,word2)
print(v)    