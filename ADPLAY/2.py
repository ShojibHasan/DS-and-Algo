def TypeCheck(str):
    try:
        val = int(str)
        print("number")
    except ValueError:
        print("string")

value = input()
TypeCheck(value)