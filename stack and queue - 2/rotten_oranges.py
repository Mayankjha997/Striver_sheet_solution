def rotten_oranges(grid):
    def rotting(rotten):
        temp = []
    
        for i,j in rotten:
            if i> 0 and grid[i - 1][j] == 1:
                temp.append((i -1,j))
                grid[i-1][j] = 2
        
            if i < len(grid) - 1  and grid[i+1][j] == 1:
                temp.append((i+1,j))
                grid[i+1][j] = 2
            
            if j > 0 and grid[i][j-1] == 1:
                temp.append((i,j-1))
                grid[i][j-1] = 2
        
            if j < len(grid[0])-1 and grid[i][j+1] == 1:
                temp.append((i,j+1))
                grid[i][j+1] = 2
            
        return temp
    
    rows = len(grid)
    cols = len(grid[0])
    rotten = [(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 2]
    time = 0
    
    while rotten:
        rotten = rotting(rotten)
        if len(rotten) == 0:
            break
        time+=1
        
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                return -1
        
    return time

    


rows = int(input("enter the number of rows "))
cols = int(input("enter the number of columns "))
grid = []
for i in range(rows):
    l = []
    for j in range(cols):
        z = int(input("enter the value "))
        l.append(z)
    grid.append(l)
print(grid)
v = rotten_oranges(grid)
print(v)
    