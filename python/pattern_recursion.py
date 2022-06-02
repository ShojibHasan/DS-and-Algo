def pattern(n,row=0,result=''):
    if n==row:
        return
    if n==len(result):
        print(result)
        return pattern(n,row+1)
    if len(result) <= row:
        result += '*'
    else:
        result += ' '
    pattern(n,row,result)