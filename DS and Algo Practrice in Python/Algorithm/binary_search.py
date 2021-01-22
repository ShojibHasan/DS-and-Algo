def binary_search(arr,left,right,number):
	while left <=right :
		mid_index= (left+right)//2
		if arr[mid_index] == number:
			return mid_index
		elif arr[mid_index] < number:
			left = mid_index+1
		else:
			right = mid_index-1
	return -1

arr = [10,20,34,55,66,67,87,90]
left = 0
right= len(arr)-1
number =66
result = binary_search(arr,left,right,number)

if result !=-1:
	print("Found index ",result)
else:
	print("Not found")
