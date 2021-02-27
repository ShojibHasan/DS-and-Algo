def isPalindrome(string):
	return string == string[::-1]


string = "MOM"
# string = input("Enter the Word")
ans = isPalindrome(string)

if ans:
	print("Palindrome")
else:
	print("Not Palindrome")
