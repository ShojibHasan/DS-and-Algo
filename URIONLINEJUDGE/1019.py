seconds = int(input())
hour = seconds//3600
time = seconds//60
second = seconds%60
print("%i:"%hour,"%i:"%time,"%i"%second)
