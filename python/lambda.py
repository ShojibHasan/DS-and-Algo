def myfunc(n,m):
  return lambda b : b * n + m

mydoubler = myfunc(11,2)
print(mydoubler(2))
