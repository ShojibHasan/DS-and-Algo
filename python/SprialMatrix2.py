def printdata(arr, i, j, row, column):

	# If i or j lies outside the matrix
	if (i >= row or j >= column):
		return

	# Print First Row
	for p in range(i, column):
		print(arr[i][p], end=" ")

	# Print Last Column
	for p in range(i + 1, row): 
		print(arr[p][column - 1], end=" ")

	# Print Last Row, if Last and
	# First Row are not same
	if ((row - 1) != i):
		for p in range(column - 2, j - 1, -1):
			print(arr[row - 1][p], end=" ")

	# Print First Column, if Last and
	# First Column are not same
	if ((column - 1) != j):
		for p in range(row - 2, i, -1):
			print(arr[p][j], end=" ")

	printdata(arr, i + 1, j + 1, row - 1, column - 1)


# Driver code
Row = 4
Column = 4
arr = [
    [1, 2, 3, 4],
	[5, 6, 7, 8],
	[9, 10, 11, 12],
	[13, 14, 15, 16]]

# Function Call
printdata(arr, 0, 0, Row, Column)
