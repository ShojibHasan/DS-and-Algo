cities={0:"Dhaka", 1:"Cumilla", 2:"Chittagong", 3:"Khulna", 4:"Sylhet", 5:"Barishal", 6:"Jamalpur"}  # Dictionary 

graph={0:[1,2], 1:[0,2,3], 2:[0,1,3,4,5], 3:[1,2,4], 4:[2,3,5], 5:[2,4], 6:[]}  # Dictionary 



colors=["Red", "Green", "Blue"] # List

n=0  #  variable 

i=0 #  variable 

col_graph={} # empty dictionary  

def check(city, colour):  # 0,0
	global graph
	global col_graph
	for i in graph[city]:  # [1,2]
		if i in col_graph and col_graph[i]==colour:  # 
			return False
	return True

def assign(city, colour): # 0,0
	global col_graph
	col_graph[city]=colour


while n<7:
	assigned=0
	for i in range(3):
		if check(n,i)==True:
			assign(n,i)  #0-0
			n+=1
			assigned=1
			break
	if assigned==0:
		prevas=0
		for x in range(3):
			if check(n-1, (col_graph[n-1]+1)%3)==True:
				assign(n,(col_graph[n-1]+1)%3)
				prevas=1
				break
		if prevas==0:
			n-=1

for key, value in col_graph.items():
	print(cities[key] + " : " + colors[value])