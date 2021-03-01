input_data = input("Enter the String: ")

if input_data.isnumeric():
    print("NUMBER")
elif input_data.isalpha():
    print("WORD")
else:
    print("MIXED")