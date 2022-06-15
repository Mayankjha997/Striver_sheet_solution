import sys
def minimum_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])
    helper(0,0,rows,cols)
    
def  helper(r,c,rows,cols):
    if r == rows-1 and c == cols-1:
        return grid[r][c]
    if r >= rows or c >= cols:
        return sys.maxsize
        
    ans1 = helper(r+1,c,rows,cols)
    ans2 = helper(r,c+1,rows,cols)
        
    ans = grid[r][c] + min(ans1,ans2)
        
    return ans
    
  
r = int(input("enter the number of rows "))
c = int(input("enter the number of columns "))    
grid = []
for i in range(r):
    l = []
    for j in range(c):
        v = int(input("enter the element of the matrix "))
        l.append(v)
    grid.append(l)
print(grid)
v = minimum_path_sum(grid)
print(v)
