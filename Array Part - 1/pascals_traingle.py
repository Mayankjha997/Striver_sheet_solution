def pascals_traingle(numrows):
    traingle = [[1]]
    
    for i in range(numrows - 1):
        temp_traingle = [0] + traingle[-1] + [0]
        res = []
        for j in range(len(traingle[-1]) + 1):
            res.append(temp_traingle[j] + temp_traingle[j+1])
        traingle.append(res)    
    return traingle



numrows = int(input("number of rows : "))
print(pascals_traingle(numrows))

            
        