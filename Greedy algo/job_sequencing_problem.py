import atexit
import io
import sys

class Job:

    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        info = list(map(int,input().strip().split()))
        Jobs = [Job() for i in range(n)]
        for i in range(n):
            Jobs[i].id = info[3*i]
            Jobs[i].deadline = info[3 * i + 1]
            Jobs[i].profit=info[3*i+2]
        ob = solution()
        res = ob.JobScheduling(Jobs,n)
        print (res[0], end=" ")
        print (res[1])


class solution:
    def JobScheduling(self,Jobs,n):
        Jobs.sort(key = lambda i:i.profit)
        Jobs = Jobs[::-1]
        count = 0
        result = [False] * 100
        profit = 0
        
        for i in range(n):
            for j in range(Jobs[i].deadline-1,-1,-1):
                if result[j] == False:
                    result[j] = True
                    count+=1
                    profit+=Jobs[i].profit
                    break
        return [count ,profit]
        
