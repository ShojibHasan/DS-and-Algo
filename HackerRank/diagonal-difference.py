def diagonalDifference(arr):
    first_dia=0
    second_dia=0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if(i==j):
                first_dia +=arr[i][j]
                
            if (i==len(arr)-j-1):
                second_dia +=arr[i][j]
    result = abs(first_dia - second_dia)
    return result




arr = [[1,2,3],[4,5,6],[9,8,9]]


result = diagonalDifference(arr)
print(result)