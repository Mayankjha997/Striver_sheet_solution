def findPages(A, N, M):
    l = max(A)
    r = sum(A)
    res = -1
    while l <= r:
        mid = (r+l) // 2
        if allocation(mid,A,M,N) :
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res
    
def allocation(mid,A,M,N):
    allocated_student = 1
    pages = 0
    for i in range(N):
        if A[i] > mid:
            return False
        if pages+A[i] > mid:
            allocated_student += 1
            pages = A[i]
        else:
            pages+=A[i] 
    if allocated_student <= M:
        return True
    return False

A = list(map(int,input("enter the pages ").strip().split()))
M = int(input("enter the number of students "))
N = int(input())
v = findPages(A,M,N)
print(v) 