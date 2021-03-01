def too_good():
    str1= input("Enter the String : ")
    snot = str1.find('too')
    spoor = str1.find('good')
  

    if spoor > snot and snot>0 and spoor>0:
        str1 = str1.replace(str1[snot:(spoor+4)], 'excellent')
        return str1
    else:
        return str1
print(too_good())
print(too_good())
