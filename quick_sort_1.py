arr = [8,5,9,34,1]
lbound = 0
ubound = len(arr)-1

def arrPartition(arr, lbound, ubound):
    pivot = arr[lbound]
    start = lbound
    end = ubound
    while(start < end):
        while(  arr[start] <= pivot):
            start = start+1
        while( arr[end] > pivot):
            end = end-1
        if(start < end):
            arr[start], arr[end] = arr[end], arr[start]
        
    arr[lbound], arr[end] = arr[end], arr[lbound]
    print(arr)
    return end

# ub = arrPartition(arr, lbound, ubound)
# print(ub)
print(arr)

def quickSort(arr, lbound, ubound):
    print(arr)
    if(lbound < ubound):
        loc = arrPartition(arr, lbound, ubound)
        quickSort(arr, lbound, loc-1)
        quickSort(arr, loc+1, ubound)

quickSort(arr, lbound, ubound)
print(arr)