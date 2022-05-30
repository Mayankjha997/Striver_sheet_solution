def aggressiveCows(stalls, k):
    stalls.sort()
    lb = 0
    up = stalls[-1] - stalls[0]
    ans = 0
    
    while lb <= up:
        mid = (lb + up) // 2
        cows = 1
        curr = stalls[0]
        
        for i in range(1,len(stalls)):
            if stalls[i] - curr >= mid:
                cows+=1
                curr = stalls[i]
                if k == cows:
                    break
        if cows == k:
            ans = mid
            lb = mid + 1
        else :
            up = mid -1
    return ans


stalls = list(map(int, input("enter the positions of the cows ").strip().split()))
k = int(input("Enter the minimum cows "))
v = aggressiveCows(stalls,k)
print(v)
            