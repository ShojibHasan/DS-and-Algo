from math import *
def boardGrames(n, a) :
 
    count0, ccount5 = 0, 0
 
    for i in range(n) :
 
        if a[i] == 0 :
            count0 += 1
        else :
            ccount5 += 1

    ccount5 = floor(ccount5 / 9) * 9
 
    if count0 == 0 : 
        print(-1,end = "") 
    elif ccount5 == 0 : 
        print(0,end = "") 
 
    else :
 
        for i in range(ccount5) :
            print(5,end = "")
        for i in range(count0) :
            print(0, end = "")

n = int(input())
a = list(map(int,input().split()[:n]))
boardGrames(n,a)