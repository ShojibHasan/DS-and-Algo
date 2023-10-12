def timeConversion(s):
    hour = int(s[:2])
    minute = int(s[3:5])
    second = int(s[6:8])
    
    if s[-2]=='P' and hour != 12:
        
        hour+=12
    elif s[-2]=='A' and hour == 12:
        hour =0
    
    return '{:02d}:{:02d}:{:02d}'.format(hour,minute,second)
    
s = input()

result = timeConversion(s)
print(result)