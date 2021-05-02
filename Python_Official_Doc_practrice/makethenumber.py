
# Python program to find if there are
# two elements wtih given sum
 
# function to check for the given sum
# in the array
# This code is contributed by __Devesh Agrawal__

def printPairs(arr, arr_size, sum):
	s = set()
	
	for i in range(0, arr_size):
		temp = sum-arr[i]
		if (temp in s):
			print ("Pair with given sum "+ str(sum) +" is (" + str(arr[i]) + ", " + str(temp) + ")")
		s.add(arr[i])

A = [0,-1,2,-3,1]
n = -2
printPairs(A, len(A), n)


