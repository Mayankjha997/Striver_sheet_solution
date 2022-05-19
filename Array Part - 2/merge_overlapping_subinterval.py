def merge_overlapping_subinterval(intervals):
    if intervals == []:
        return []
    
    intervals.sort()
    result = []
    for interval in intervals:
        if result == [] or result[-1][1] < interval[0]:
            result.append(interval)
        else:
            result[-1][1] = max(result[-1][1], interval[1])
    return result
            


intervals = []
no_of_intervals = int(input("enter the number of intervals "))
l = []
for i in range(no_of_intervals):
    l.append(int(input("enter the first range ")))
    l.append(int(input("enter the second range ")))
    intervals.append(l)
    l = []
print(intervals)
print(merge_overlapping_subinterval(intervals))

