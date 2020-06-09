def hourglassSum(arr):
    result = 0
    for y in range(1,len(arr)-1):
        for x in range(1,len(arr[y])-1):
            current = arr[y][x]+ arr[y-1][x]+arr[y-1][x-1]+arr[y-1][x+1]+arr[y+1][x]+arr[y+1][x-1]+arr[y+1][x+1]
            if current > result:
                result = current
    return result