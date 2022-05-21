def unique_path(m,n):   #here m and n are the row and column numbers
    row = [1] * n
    for i in range(m-1):
        newrow = [1] * n
        for j in range(n-2,-1,-1):
            newrow[j] = newrow[j + 1] + row[j]
        row = newrow
    return row[0]