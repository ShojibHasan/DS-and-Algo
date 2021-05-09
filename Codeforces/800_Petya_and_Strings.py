def compared(char_input1,char_input2):
    if char_input1 < char_input2:
        print("-1")
    elif char_input2< char_input1:
        print("1")
    elif char_input1==char_input2:
        print("0")

char_input1 = input()
char_input2 = input()

compared(char_input1.lower(),char_input2.lower())