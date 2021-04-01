# Python3 program to print
# given matrix in spiral form


def spiralPrint(row, column, array):
	row_index = 0
	column_index = 0

	''' k - starting row index
		m - ending row index
		l - starting column index
		n - ending column index
		i - iterator '''

	while (row_index < row and column_index < column):

		# Print the first row from
		# the remaining rows
		for i in range(column_index, column):
			print(array[row_index][i], end=" ")

		row_index += 1

		# Print the last column from
		# the remaining columns
		for i in range(row_index, row):
			print(array[i][column - 1], end=" ")

		column -= 1

		# Print the last row from
		# the remaining rows
		if (row_index < row):

			for i in range(column - 1, (column_index - 1), -1):
				print(array[row - 1][i], end=" ")

			row -= 1

		# Print the first column from
		# the remaining columns
		if (column_index < column):
			for i in range(row - 1, row_index - 1, -1):
				print(array[i][column_index], end=" ")

			column_index += 1


# Driver Code
array = [[1, 2, 3, 4, 5, 6],
	[7, 8, 9, 10, 11, 12],
	[13, 14, 15, 16, 17, 18]]

row = 3
column = 6

# Function Call
spiralPrint(row, column, array)


