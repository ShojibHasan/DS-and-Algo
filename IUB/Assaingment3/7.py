n = input()

if ord(n) >=65 and ord(n) <=90:
    print("Uppercase Latter")
elif ord(n) >=97 and ord(n) <= 122:
    print("Lowercase latter")
elif ord(n) >= 48 and ord(n) <= 57:
    print("Digit")
elif ord(n) >=33 and ord(n) <=47:
    print("Symbol")
