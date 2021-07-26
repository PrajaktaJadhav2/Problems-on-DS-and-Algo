def FindMaxSum(arr,n):
    if n==1:
        return arr[0]
    if n==2:
        return max(arr[0],arr[1])
    
    x = arr[0]
    y = max(arr[0],arr[1])

    for i in range(2,n):
        z = max(arr[i]+x,y)
        x=y
        y=z
    return max(x,y)

arr = [6,7,1,3,8,2,4]
n=len(arr)
print(FindMaxSum(arr,n))


