
def check(num) :
	start=0
	digitSum = 0
	while num[start] > 0 :
		rem = num[start] % 10
		digitSum = digitSum + rem
		num[start] = num / 10
		
	return (digitSum % 3 == 0)
	
n = int(input())
a = list(map(int,input().split()[:n]))
if(check(a)) :
	print ("Yes")
else :
	print ("No")

