def romanToInt(s):
    roman = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    ans =0
    i=0
    for i in range(len(s)-1):
        if roman[s[i]]<roman[s[i+1]]:
            ans = ans - roman[s[i]]
            
        else:
            ans = ans + roman[s[i]]
    return ans+roman[s[-1]]       

a = romanToInt("MCMXCIV")
print(a)