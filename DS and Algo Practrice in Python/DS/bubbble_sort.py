def bubbleSort(arr):
	n = len(arr)
	for i in range(n-1):

		for j in range(0, n-i-1):


			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

arrar = []
array = open("/home/emptymind/Documents/Python/Algo/DS-and-Algo/DS and Algo Practrice in Python/DS/int.txt")
arrar.sort()
bubbleSort(array)

print ("Sorted array is:")
for i in range(len(array)):
	print ("%d" %array[i]),
