#perfectly Division Program

def division(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("Can't Division")

division(10,5)