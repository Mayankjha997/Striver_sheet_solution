import atexit
import io
import sys

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        Items = [Item(0,0) for i in range(n)]
        for i in range(n):
            Items[i].value = info[2*i]
            Items[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.2f" %ob.fractionalknapsack(W,Items,n))

class Solution:    
    def fractionalknapsack(self, W,Items,n):
        arr = []
        s = 0
        total = 0
        for i in range(n):
            x = Items[i].value/Items[i].weight
            arr.append([x,i])
        
        arr.sort(reverse = True)
        
        for i in range(n):
            if s+Items[arr[i][1]].weight < W:
                total += Items[arr[i][1]].value
                s += Items[arr[i][1]].weight
            else:
                total += (W-s) * arr[i][0]
                break
            
        return total
